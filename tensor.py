import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import pandas as pd

# Load the dataset
def load_data(filename):
    data = pd.read_csv(filename)
    return data

# Preprocess the data
def preprocess_data(data):
    X = data[['density', 'time', 'weather']]
    y = data['congestion_level']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Create a TensorFlow model
def create_model():
    model = Sequential([
        Dense(64, activation='relu', input_shape=(3,)),  # 3 features: density, time, weather
        Dense(64, activation='relu'),
        Dense(1)  # Output layer for congestion level
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def main():
    data = load_data('traffic_data.csv')
    X_train, X_test, y_train, y_test = preprocess_data(data)

    model = create_model()
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    model.evaluate(X_test, y_test, verbose=2)

if __name__ == "__main__":
    main()
