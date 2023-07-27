import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
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

# Standaryzacja danych (opcjonalne, ale może poprawić wyniki klasyfikacji)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicjalizacja klasyfikatora SVM
svm_classifier = SVC()

# Trenowanie klasyfikatora na danych uczących
svm_classifier.fit(X_train, y_train)

# Predykcja klas na danych testowych
y_pred = svm_classifier.predict(X_test)
print(y_pred)

# Obliczenie dokładności klasyfikacji
accuracy = accuracy_score(y_test, y_pred)
print("Dokładność klasyfikacji: {:.2f}%".format(accuracy * 100))