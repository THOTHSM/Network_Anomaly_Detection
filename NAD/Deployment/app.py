from flask import Flask, request, jsonify
import pickle
import pandas as pd
import numpy as np
import category_encoders as ce

app = Flask(__name__)

# Loading the trained model and encoders
with open('network_anomaly_detection_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('label_encoder.pkl', 'rb') as le_file:
    label_encoder = pickle.load(le_file)

with open('catboost_encoder.pkl', 'rb') as cbe_file:
    catboost_encoder = pickle.load(cbe_file)

# Defining the input features for preprocessing
categorical_columns = ['protocoltype', 'service', 'flag']

# Features used during training
training_features = ['duration', 'protocoltype', 'service', 'flag', 'land', 'hot',
                     'numfailedlogins', 'loggedin', 'numcompromised', 'rootshell',
                     'suattempted', 'numroot', 'numfilecreations', 'numshells',
                     'numaccessfiles', 'numoutboundcmds', 'ishostlogin', 'isguestlogin',
                     'count', 'srvcount', 'dsthostcount', 'dsthostsrvcount',
                     'dsthostsamesrvrate', 'dsthostdiffsrvrate', 'dsthostsamesrcportrate',
                     'dsthostsrvdiffhostrate', 'lastflag', 'total_bytes', 'byte_ratio',
                     'combined_serror_rerror_rate', 'combined_srv_serror_rerror_rate',
                     'ratio_samesrvrate_diffsrvrate', 'service_host_distribution_ratio',
                     'combined_dsthostserrorrate_dsthostrerrorrate',
                     'combined_dsthostsrvserrorrate_dsthostsrvrerrorrate']

@app.route('/')
def index():
    return "Welcome to the Network Anomaly Detection API!"

@app.route('/predict', methods=['POST'])
def predict():
    # Geting the JSON data from the request
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    # Converting the input data into a DataFrame
    input_df = pd.DataFrame(data, index=[0])

    # Applying feature engineering similar to model
    if 'srcbytes' in input_df.columns and 'dstbytes' in input_df.columns:
        input_df['total_bytes'] = input_df['srcbytes'] + input_df['dstbytes']
        input_df['byte_ratio'] = input_df['srcbytes'] / (input_df['dstbytes'] + 1e-6)
        input_df.drop(columns=['srcbytes', 'dstbytes'], inplace=True)

    if 'serrorrate' in input_df.columns and 'rerrorrate' in input_df.columns:
        input_df['combined_serror_rerror_rate'] = (input_df['serrorrate'] + input_df['rerrorrate']) / 2
        input_df.drop(columns=['serrorrate', 'rerrorrate'], inplace=True)

    if 'srvserrorrate' in input_df.columns and 'srvrerrorrate' in input_df.columns:
        input_df['combined_srv_serror_rerror_rate'] = (input_df['srvserrorrate'] + input_df['srvrerrorrate']) / 2
        input_df.drop(columns=['srvserrorrate', 'srvrerrorrate'], inplace=True)

    if 'samesrvrate' in input_df.columns and 'diffsrvrate' in input_df.columns:
        input_df['ratio_samesrvrate_diffsrvrate'] = input_df['samesrvrate'] / (input_df['diffsrvrate'] + 1e-6)
        input_df.drop(columns=['samesrvrate', 'diffsrvrate'], inplace=True)

    if 'srvdiffhostrate' in input_df.columns and 'samesrvrate' in input_df.columns:
        input_df['service_host_distribution_ratio'] = input_df['samesrvrate'] / (input_df['srvdiffhostrate'] + 1e-6)
        input_df.drop(columns=['srvdiffhostrate'], inplace=True)

    if 'dsthostserrorrate' in input_df.columns and 'dsthostrerrorrate' in input_df.columns:
        input_df['combined_dsthostserrorrate_dsthostrerrorrate'] = input_df['dsthostserrorrate'] + (input_df['dsthostrerrorrate'] + 1e-6)
        input_df.drop(columns=['dsthostserrorrate', 'dsthostrerrorrate'], inplace=True)

    if 'dsthostsrvserrorrate' in input_df.columns and 'dsthostsrvrerrorrate' in input_df.columns:
        input_df['combined_dsthostsrvserrorrate_dsthostsrvrerrorrate'] = input_df['dsthostsrvserrorrate'] + (input_df['dsthostsrvrerrorrate'] + 1e-6)
        input_df.drop(columns=['dsthostsrvserrorrate', 'dsthostsrvrerrorrate'], inplace=True)

    # Ensures the input DataFrame matches the model's expected feature set
    for feature in training_features:
        if feature not in input_df.columns:
            input_df[feature] = 0  # Or could use  imputation strategy

    # Droping any unexpected features
    input_df = input_df[training_features]

    # Applying the CatBoost encoding for categorical features
    input_encoded = catboost_encoder.transform(input_df[categorical_columns])
    input_df[categorical_columns] = input_encoded

    # Making predictions
    prediction = model.predict(input_df)

    # Converting the prediction back to the original labels
    predicted_label = label_encoder.inverse_transform(prediction)

    # Returning the prediction as JSON
    return jsonify({'prediction': predicted_label[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5001)