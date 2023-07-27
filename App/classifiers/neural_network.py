import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

TRAIN_DIR = r"C:\Repos\Mgr\data\hundred_frames\csv_complete\csv_train.csv"
TEST_DIR = r"C:\Repos\Mgr\data\hundred_frames\csv_complete\csv_test.csv"

# Wczytanie danych treningowych
training_data = pd.read_csv(TRAIN_DIR, header=None)

# Podział danych treningowych na cechy (X) i etykiety klas (y)
X_train = training_data.iloc[:, 1:].values  # Pozycje markerów, bez pierwszej kolumny (etykieta klasy)
y_train = training_data.iloc[:, 0].values   # Numer klatki (etykieta klasy)

# Wczytanie danych testowych
test_data = pd.read_csv(TEST_DIR, header=None)

# Podział danych testowych na cechy (X) i etykiety klas (y)
X_test = test_data.iloc[:, 1:].values
y_test = test_data.iloc[:, 0].values

# Standaryzacja danych (opcjonalne, ale może poprawić wyniki klasyfikacji)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicjalizacja prostego modelu sieci neuronowej
model = Sequential()
model.add(Dense(64, activation='relu', input_dim=X_train_scaled.shape[1]))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Kompilacja modelu
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Trenowanie modelu na danych uczących
model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Ocena modelu na danych testowych
_, accuracy = model.evaluate(X_test_scaled, y_test)
print("Dokładność klasyfikacji: {:.2f}%".format(accuracy * 100))