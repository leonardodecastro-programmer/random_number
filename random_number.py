import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def gerar_numero():
    numero1 = random.randint(100, 999)
    numero2 = random.randint(100, 999)
    numero3 = random.randint(100, 999)

    resultado = f"{numero1}-{numero2}-{numero3}"
    return jsonify({"numero": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Porta 10000 é a padrão no Render
