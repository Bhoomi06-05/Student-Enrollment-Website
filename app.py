from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/fees', strict_slashes=False)
def fees():
    return render_template('fees.html')

@app.route('/contact', strict_slashes=False)
def contact():
    return render_template('contact.html')

@app.route('/enroll', strict_slashes=False)
def enroll():
    return render_template('enroll.html')

if __name__ == '__main__':
    app.run(debug=True)