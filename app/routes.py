from flask import Flask, render_template
import time
import cotizaciones

app = Flask(__name__)


@app.route('/')
def home():
    cambios = []
    cambios.append(cotizaciones.dolarBrou())
    cambios.append(cotizaciones.dolarSir())
    cambios.append(cotizaciones.dolarMatriz())
    fechahoy = time.strftime("%H:%M:%S %d/%m/%Y")
    return render_template('home.html', cambios=cambios, fechahoy=fechahoy)


if __name__ == '__main__':
    app.run(debug=True)
