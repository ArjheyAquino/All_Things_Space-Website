from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/stars')
def home():
    return render_template('stars.html')

@app.route('/asteroids')
def about():
    return render_template('asteroids.html')

@app.route('/galaxies')
def solid():
    return render_template('galaxy.html')

@app.route('/aboutus')
def liquid():
    return render_template('aboutus.html')
    
if __name__ == "__main__":
   app.run(debug=True)
