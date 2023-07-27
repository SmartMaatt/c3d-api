import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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

# Inicjalizacja i trening klasyfikatora k-NN
k = 5  # Liczba sąsiadów do rozważenia
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Klasyfikacja danych testowych
y_pred = knn.predict(X_test)
print(y_pred)

# Obliczenie dokładności klasyfikacji
accuracy = accuracy_score(y_test, y_pred)
print("Dokładność klasyfikacji: {:.2f}%".format(accuracy * 100))