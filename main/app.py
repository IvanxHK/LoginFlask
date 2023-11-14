from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Cambia esto a una clave segura

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return f'¡Hola, {username}! <a href="/logout">Cerrar sesión</a>'
    return '¡Hola! <a href="/login">Iniciar sesión</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Aquí puedes realizar la lógica de autenticación (por ahora, simplemente compara con valores fijos)
        if username == 'usuario' and password == 'contraseña':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Error de inicio de sesión. Inténtalo de nuevo.')
    return render_template('login.html', error=None)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
