from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if name and email:
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('name', name)
            response.set_cookie('email', email)
            return response
        else:
            return render_template('index.html', error="Пожалуйста, заполните все поля")
    return render_template('index.html', error=None)


@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')

    if not name:
        return redirect(url_for('index'))

    return render_template('welcome.html', name=name)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
