Tableau Visualization

Purpose: Visualize network traffic and anomalies for enhanced monitoring and analysis.

Components:

Anomaly Detection Metrics: Highlights metrics like wrong fragments and failed logins.
Protocol and Service Analysis: Shows distribution of Protocol_type and Service.
Connection Status Overview: Overview of connection health.
Host-based Traffic Features: Insights on targeted or unusual host behavior.
Interactive Filters: Filters for time periods, Protocol_type, Service, etc.
Correlation Analysis: Relationships between numerical features.
Alerts and Anomalies Log: Lists recent detected anomalies.
Note: View the Tableau dashboard link  https://public.tableau.com/views/NetworkAnamoly/Dashboard1_1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link.

Exploratory Data Analysis (EDA) and Hypothesis Testing

File Name: Network_anomaly_detection_EDA.ipynb
Points Covered:
Time Series Analysis: Monitored time-dependent patterns in network traffic.
Influence of Urgent Packets: Evaluated if connections with urgent packets were more likely to be anomalous.

Model Selection and Evaluation

File Name: NetworkAnomalyDetectionMLModeling.ipynb
Points Covered:
Model Selection: Used supervised models (Decision Trees, Random Forest, Gradient Boosting) and unsupervised models (K-means, DBSCAN) for anomaly detection.
Feature Engineering: Created new features and combined existing ones to improve model performance.
Encoding: Applied CatBoostEncoder for categorical features and label encoding for the target variable.
SMOTE: Used to handle class imbalance.
Model Evaluation: Employed cross-validation and performance metrics like Accuracy, Precision, Recall, F1-score, ROC-AUC for supervised models, and Silhouette score, Davies-Bouldin index for unsupervised models.

Deployment via Flask API

File Name: app.py , model.ipynb and its pickel file 

Points Covered:

Flask API Setup: Configured the Flask environment and application structure.
Model Integration: Serialized and loaded the trained model.
API Endpoints: Created routes for prediction and data preprocessing.
Model Used: Bagging model.
Screenshot: View the final deployment and prediction using JSON input in the screenshot FinalModelDeployedScreenshot.png.


