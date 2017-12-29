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
    cambios.append(cotizaciones.dolarCambio18())
    cambios.append(cotizaciones.dolarVarlix())
    cambios.append(cotizaciones.dolarGales())
    cambios.append(cotizaciones.dolarFavorita())
    fechahoy = time.strftime("%H:%M:%S %d/%m/%Y")
    return render_template('home.html', cambios=cambios, fechahoy=fechahoy)


if __name__ == '__main__':
    app.run(debug=True)
