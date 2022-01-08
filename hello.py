from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://64.media.tumblr.com/tumblr_ly9h3l7eSW1r31cpxo1_500.gif">'


@app.route('/<name>')
def greet(name):
    return f"Hello there {name}!"


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'

    return wrapper


def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'

    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return "Bye!"


if __name__ == '__main__':
    app.run(debug=True)
