# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
# Load dataset
data = pd.read_csv('C:/Users/sunil/Downloads/KDDTrain+.txt/KDDTrain+.txt')

# Select only the columns present in the original column list
original_columns = (['duration'
,'protocol_type'
,'service'
,'flag'
,'src_bytes'
,'dst_bytes'
,'land'
,'wrong_fragment'
,'urgent'
,'hot'
,'num_failed_logins'
,'logged_in'
,'num_compromised'
,'root_shell'
,'su_attempted'
,'num_root'
,'num_file_creations'
,'num_shells'
,'num_access_files'
,'num_outbound_cmds'
,'is_host_login'
,'is_guest_login'
,'count'
,'srv_count'
,'serror_rate'
,'srv_serror_rate'
,'rerror_rate'
,'srv_rerror_rate'
,'same_srv_rate'
,'diff_srv_rate'
,'srv_diff_host_rate'
,'dst_host_count'
,'dst_host_srv_count'
,'dst_host_same_srv_rate'
,'dst_host_diff_srv_rate'
,'dst_host_same_src_port_rate'
,'dst_host_srv_diff_host_rate'
,'dst_host_serror_rate'
,'dst_host_srv_serror_rate'
,'dst_host_rerror_rate'
,'dst_host_srv_rerror_rate'
,'attack'
,'level'])
data.columns=original_columns
data = data[original_columns]

# Convert categorical variables to numerical using label encoding
from sklearn.preprocessing import LabelEncoder

categorical_columns = ['protocol_type', 'service', 'flag']
label_encoders = {}

for col in categorical_columns:
    label_encoders[col] = LabelEncoder()
    data[col] = label_encoders[col].fit_transform(data[col])

# Proceed with your remaining code

# Perform feature selection/reduction (example: using all features)
#selected_features = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'attack']

# Select relevant columns
#data = data[selected_features]

# Convert categorical variables to dummy variables
#data = pd.get_dummies(data)

# Print column names to check if 'attack' column exists
print(data)
print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

# Drop the 'attack' column
X = data.drop('attack', axis=1)
print(X)
y = data['attack']
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
print(clf)
# Predict on test set
y_pred = clf.predict(X_test)
print(y_pred)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#Save the trained model
import joblib
joblib.dump(clf, 'random_forest_model.pkl')
#joblib.memo.clear()
# Load the pickled model
model = joblib.load('random_forest_model.pkl')

# Inspect the model attributes
print(model)

# import pickle

# # Save the trained model
# with open('random_forest_model.pkl', 'wb') as f:
#     pickle.dump(clf, f)

#pickle.dump(clf, open('model.pkl','wb'))
# model = pickle.load(open('random_forest_model.pkl','rb'))