from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', page='home')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', page='dashboard')


@app.route('/story')
def story():
    return render_template('story.html', page='story')


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', page='portfolio')


if __name__ == '__main__':
    app.run(debug=True)
