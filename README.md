# Network Anomaly Detection Project Summary

### Problem Statement
Network anomaly detection involves identifying unusual patterns or behaviors in network traffic that deviate from the norm. These anomalies can indicate various security threats, including malware infections and large-scale cyber-attacks. Traditional methods relying on predefined rules often fail to detect new or evolving threats, making dynamic and robust anomaly detection crucial.

### Goal
The primary goal of this project was to develop an effective network anomaly detection system capable of identifying and classifying anomalies in real-time. This system aims to enhance security measures by detecting potential threats, ensuring operational continuity, and facilitating compliance with data security regulations.

### Need for Network Anomaly Detection
- **Evolving Security Threats**: Adapts to new threats that bypass traditional security measures.
- **Increasing Network Complexity**: Handles the diverse and interconnected nature of modern networks.
- **Operational Continuity**: Ensures reliable and available network services.
- **Regulatory Compliance**: Helps meet data security and privacy regulations.

### Dataset
- **Dataset File**: `NAD.csv`

### Data Description
- **Basic Connection Features**: Duration, Protocol_type, Service, Flag, Src_bytes, Dst_bytes, Land, Wrong_fragment, Urgent.
- **Content-Related Features**: Hot, Num_failed_logins, Logged_in, Num_compromised, Root_shell, Su_attempted, Num_root, Num_file_creations, Num_shells, Num_access_files, Num_outbound_cmds, Is_hot_login, Is_guest_login.
- **Time-Related Traffic Features**: Count, Srv_count, Serror_rate, Srv_serror_rate, Rerror_rate, Srv_rerror_rate, Same_srv_rate, Diff_srv_rate, Srv_diff_host_rate.
- **Host-Based Traffic Features**: Dst_host_count, Dst_host_srv_count, Dst_host_same_srv_rate, Dst_host_diff_srv_rate, Dst_host_same_src_port_rate, Dst_host_srv_diff_host_rate, Dst_host_serror_rate, Dst_host_srv_serror_rate, Dst_host_rerror_rate, Dst_host_srv_rerror_rate.

### Project Components

1. **Tableau Visualizations**
   - **Traffic Volume Over Time**: Line graphs/area charts for inbound and outbound traffic.
   - **Anomaly Detection Metrics**: Statistical charts for wrong fragments, urgent packets, and failed login attempts.
   - **Protocol and Service Analysis**: Pie charts/bar graphs for Protocol_type and Service distributions.
   - **Connection Status Overview**: Heatmap/bar chart for Flag status.
   - **Host-Based Traffic Features**: Visualizations for Dst_host_count, Dst_host_srv_count, etc.
   - **Interactive Filters**: Filters for time periods, Protocol_type, Service.
   - **Correlation Analysis**: Scatter plots/correlation matrices for numerical features.
   - **Alerts and Anomalies Log**: Recent detected anomalies with details.
   - **Predictive Insights**: Forecasts of potential future anomalies.

2. **EDA and Hypothesis Testing**
   - **Exploratory Data Analysis (EDA)**: Feature distribution, correlation analysis, outlier detection, time series analysis, feature engineering, and missing values analysis.
   - **Hypotheses Tested**:
     - Network traffic volume and anomalies.
     - Impact of Protocol type on anomaly detection.
     - Role of Service in network security.
     - Connection status and anomalies.
     - Influence of urgent packets on anomalies.

3. **ML Modeling**
   - **Data Processing**: Cleaning, feature engineering, transformation, and splitting.
   - **Model Selection**: 
     - **Supervised**: Logistic Regression, Decision Trees, Random Forests, SVMs, Neural Networks.
     - **Ensemble techniques**: Boosting, Bagging, Stacking.
     - **Unsupervised**: K-means, DBSCAN.
     - **Dimensionality Reduction**: PCA, t-SNE.
   - **Model Evaluation**: Cross-validation, performance metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC), confusion matrix, adjustment, and tuning.

4. **Deployment**
   - **Purpose**: Integrate the model with operational systems for real-time detection, accessible from various client applications.
   - **Flask API Setup**:
     - **Environment Setup**: Python virtual environment, Flask, and necessary libraries.
     - **Model Integration**: Serialize and load the model.
     - **API Endpoints**: Define routes, preprocess data, and return prediction results.
   ## Output:
   ![FinalModelDeployedScreenshot](https://github.com/user-attachments/assets/b214feb9-bdfa-486c-9352-bf49eab66223)

   
