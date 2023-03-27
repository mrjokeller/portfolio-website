from flask import Flask, render_template, request, redirect, url_for


COLORS = [
    "#EFFFFB",
    "#50D890",
    "#4F98CA",
    "#272727"
]
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Jonathan Keller', content=COLORS)


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
    app.run(port=8000, debug=True)