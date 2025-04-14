import joblib
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response

# Load model and encoder once at top level
model = joblib.load('traffic_model.pkl')
encoder = joblib.load('label_encoder.pkl')

class PredictTraffic(APIView):
    def post(self, request):
        try:
            # Get feature values from request
            data = request.data
            input_data = np.array([
                data['CarCount'],
                data['BikeCount'],
                data['BusCount'],
                data['TruckCount']
            ]).reshape(1, -1)

            # Predict
            prediction_numeric = model.predict(input_data)[0]
            prediction_label = encoder.inverse_transform([round(prediction_numeric)])[0]

            return Response({'prediction': prediction_label})
        except Exception as e:
            return Response({'error': str(e)}, status=400)
