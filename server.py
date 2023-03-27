from flask import Flask, render_template, request, redirect, url_for


COLORS = [
    "#E4F9F5",
    "#30E3CA",
    "#11999E",
    "#40514E"
]
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Jonathan Keller')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', title='Portfolio')


@app.route('/content')
def content():
    return render_template('content.html', title='Content')


@app.route('/about')
def about():
    return render_template('about.html', title='About me')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact me')


if __name__ == '__main__':
    app.run(debug=True)