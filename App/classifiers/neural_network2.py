import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

TRAIN_DIR = r"C:\Repos\Mgr\data\hundred_frames\csv_complete\csv_train.csv"
TEST_DIR = r"C:\Repos\Mgr\data\hundred_frames\csv_complete\csv_test.csv"

# Wczytanie danych treningowych
training_data = pd.read_csv(TRAIN_DIR, header=None)

# Podział danych treningowych na cechy (X) i etykiety klas (y)
X_train = training_data.iloc[:, 1:].values  # Pozycje markerów, bez pierwszej kolumny (etykieta klasy)
y_train = training_data.iloc[:, 0].values   # Numer klatki (etykieta klasy)

# Konwersja danych na tensory PyTorch
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)  # Dostosowanie kształtu etykiet dla późniejszej propagacji

# Wczytanie danych testowych
test_data = pd.read_csv(TEST_DIR, header=None)

# Podział danych testowych na cechy (X) i etykiety klas (y)
X_test = test_data.iloc[:, 1:].values
y_test = test_data.iloc[:, 0].values

X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).view(-1, 1)  # Dostosowanie kształtu etykiet dla późniejszej propagacji

# Definicja prostego modelu sieci neuronowej
class SimpleNet(nn.Module):
    def __init__(self, input_size):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x

# Inicjalizacja modelu
input_size = X_train.shape[1]
model = SimpleNet(input_size)

# Definicja funkcji straty i optymalizatora
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Trenowanie modelu na danych uczących
num_epochs = 10
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Ocena modelu na danych testowych
with torch.no_grad():
    y_pred = model(X_test)
    y_pred = (y_pred >= 0.5).float()  # Konwersja wyników na etykiety binarne (0 lub 1)
    accuracy = (y_pred == y_test).float().mean()
    print("Dokładność klasyfikacji: {:.2f}%".format(accuracy.item() * 100))