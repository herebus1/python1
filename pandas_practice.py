import pandas as pd
import numpy as np
import random
from faker import Faker

# Configuración
fake = Faker('es_MX')  # Datos en español
np.random.seed(42)     # Para resultados reproducibles
random.seed(42)

# Generar datos
data = {
    'id': range(1, 1001),
    'direccion': [fake.address().replace('\n', ', ') for _ in range(1000)],
    'nombre_sucursal': [f"Tienda {fake.city()}" for _ in range(1000)],
    'nombre_gerente': [fake.name() for _ in range(1000)],
    'ventas_anuales': np.round(np.random.uniform(-50000, 500000, 1000), 2)
}

# Asegurar que algunos valores sean exactamente 0
for i in random.sample(range(1000), 50):
    data['ventas_anuales'][i] = 0

# Crear DataFrame
df = pd.DataFrame(data)

# Guardar en Excel
nombre_archivo = 'datos_tiendas.xlsx'
df.to_excel(nombre_archivo, index=False, engine='openpyxl')

print(f"Archivo '{nombre_archivo}' generado exitosamente con 1000 registros.")
print("Las primeras filas son:")
print(df.head())