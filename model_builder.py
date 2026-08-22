import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

print("Step 1: Generating Financial Transaction Data...")
# Hum 2000 transactions ka ek dummy data bana rahe hain training ke liye
np.random.seed(42)
n_samples = 2000

data = {
    'txn_amount': np.random.uniform(50, 10000, n_samples), # Transaction Amount in Rs
    'distance_from_home': np.random.uniform(1, 1000, n_samples), # Kms away from home
    'time_since_last_txn': np.random.uniform(1, 240, n_samples) # Minutes since last transaction
}
df = pd.DataFrame(data)

# Risk Logic: Agar amount bada hai aur ghar se door hai, toh fraud (1) ka chance zyada hai, warna normal (0)
df['is_fraud'] = np.where((df['txn_amount'] > 5000) & (df['distance_from_home'] > 500), 1, 0)

# Thoda 'noise' add kar rahe hain taaki AI real-world ki tarah thoda confuse bhi ho
noise_idx = np.random.choice(n_samples, 100, replace=False)
df.loc[noise_idx, 'is_fraud'] = 1 - df.loc[noise_idx, 'is_fraud']

print("Step 2: Training the AI Risk Manager Model...")
# Features (X) aur Target (y) alag karna
X = df[['txn_amount', 'distance_from_home', 'time_since_last_txn']]
y = df['is_fraud']

# Data ko train aur test me split karna
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# AI Model (Random Forest) banake train karna
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy check (Terminal me dikhegi)
accuracy = model.score(X_test, y_test)
print(f"Model Training Complete! Accuracy: {accuracy * 100:.2f}%")

print("Step 3: Saving the Model as 'risk_model.pkl'...")
# Model ko save karna taaki hum isko website me use kar sakein
joblib.dump(model, 'risk_model.pkl')
print("✅ Success! 'risk_model.pkl' is ready for the dashboard.")