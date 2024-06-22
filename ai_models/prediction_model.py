import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar datos
ventas = pd.read_csv('data/sales_data.csv')
inventario = pd.read_csv('data/inventory_data.csv')

# Preprocesamiento
datos = ventas.merge(inventario, left_on='id_producto', right_on='id')
X = datos[['cantidad', 'precio']]
y = datos['cantidad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de predicción
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones
predicciones = modelo.predict(X_test)
print(predicciones)
