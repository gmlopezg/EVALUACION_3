from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/notas', methods=['GET', 'POST'])
def notas():
    if request.method == 'POST':
        nota1 = request.form['nota1']
        nota2 = request.form['nota2']
        nota3 = request.form['nota3']
        asistencia = request.form['asistencia']

        prom = (int(nota1)+int(nota2)+int(nota3))/3
        asis = int(asistencia)

        if prom >= 40 and asis >= 75:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'

        return render_template('notas.html', resultado=prom, mensaje=estado)

    return render_template('notas.html')



@app.route('/nombres', methods=['GET', 'POST'])
def nombres():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        def nombre_mas_largo(lista_nombres):
            nombre_mas_largo = ""
            for nombre in lista_nombres:
                if len(nombre) > len(nombre_mas_largo):
                    nombre_mas_largo = nombre
            return nombre_mas_largo

        lista_nombres = [nombre1, nombre2, nombre3]
        nombre_mas_grande = nombre_mas_largo(lista_nombres)
        cantidad_caracteres = len(nombre_mas_grande)

        return render_template('nombres.html', resultado=nombre_mas_grande, mensaje=cantidad_caracteres)

    return render_template('nombres.html')


if __name__ == '__main__':
    app.run()
