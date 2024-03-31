import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open('C:/Users/hp/Desktop/Recent/trained_model.sav', 'rb'))

# Generate a new set of 11 random values for prediction
input_data = np.random.randint(1, 101, size=(1, 11))

# Reshape input_data for prediction
input_data_reshaped = input_data.reshape(1, -1)  # Reshape to (1, 11)

# Make predictions using the trained model
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
