from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    # Leer el archivo Excel
    df = pd.read_excel('Data/datos.xlsx')
    # Convertir los datos a una lista de diccionarios para pasarlos al template
    datos = df.to_dict(orient='records')
    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)