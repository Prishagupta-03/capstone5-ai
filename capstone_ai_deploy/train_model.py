import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("traffic.csv")

# Input features
X = df[['CarCount', 'BikeCount', 'BusCount', 'TruckCount']]

# Encode string labels ('low', 'medium', 'high') to numbers
le = LabelEncoder()
y = le.fit_transform(df['Traffic'])  # e.g. 'low' -> 0, 'medium' -> 1, 'high' -> 2

# Train model
model = LinearRegression()
model.fit(X, y)

# Save both model and label encoder
joblib.dump(model, 'traffic_model.pkl')
joblib.dump(le, 'label_encoder.pkl')

print("✅ Model and label encoder saved!")
