import qrcode
import pandas as pd

# cambiar por la ruta de cada quien
data = pd.read_csv("C:/Users/reaxa/OneDrive/Escritorio/QRCode/Components/BaseDatos.csv")
print(data.head())

for i in range(len(data)):
    cod_supplier = data.iloc[i, 0]
    name_supplier = data.iloc[i, 1]

    img = qrcode.make(cod_supplier)
    img.save(f"img/{name_supplier}.png")
