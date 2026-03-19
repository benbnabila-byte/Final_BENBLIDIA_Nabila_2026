from flask import Flask

app = Flask(__name__)

@app.route('/exercice')
def exercice():
    return "Nom: BENBLIDIA Prénom: NABILA"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)