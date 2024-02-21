from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Witaj, świecie! Pozdrawiam Pana Michała!'

if __name__ == '__main__':
    app.run(debug=True)
