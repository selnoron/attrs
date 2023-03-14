# Flask
import flask


app: flask.app.Flask = flask.Flask(__name__)
users: list[dict] = [{"login": "Fofo", "password": "12345"}]

@app.route('/')
def main_page():
    if flask.request.method == "GET":
        a: str = flask.request.args.get('a')
        b: str = flask.request.args.get('b')
        c: str = ''
        if a != None and b != None:
            c = int(a) + int(b)
        return flask.render_template(
            'main.html',
            c=c
        )

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if flask.request.method == "GET":
        login: str = flask.request.args.get('login')
        password: str = flask.request.args.get('password')
        for user in users:
            if user.get('login') == login:
                if user.get('password') == password:
                    return "Hello"
                else:
                    raise ValueError(
                        "password is not correct"
                    )
        return flask.render_template(
            'login.html'
        )
    
    
    

@app.route('/profile')
def profile_page():
    return flask.render_template(
        'profile.html'
    )

if __name__ == '__main__':
    app.run(host='localhost',
            port=8080, debug=True)