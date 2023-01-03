"""a intenção do código é uma demonstração básica do flask e do Jinja (que já vem instalado com o FLASK).
O código vai lidar com duas API's simples que 'advinham' o gênero e a idade através do nome. Primeiro,
se importam as bibliotecas, atentar que é requests e não request no singular"""

import random
import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


"""abaixo foi criada uma função do Python e depois foi passado como argumento no render_template, pois no código 
html foi passado o seguinte argumento  <h3>Random Number: {{num}}</h3>, assim, a função aqui executada
vai ser mostrada no HTML, também criou-se uma função para pegar o ano e assim, atualizar o footer do site. Essa
função não tem a ver com o objetivo final do exercício, foi para mostrar como passar funções do Python"""
@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)
"""já no código abaixo foi criada uma nova rota, nessa rota, ao se colocar o nome após a / o sistema 
entende como uma variável e a passa para as API's que retornam a informação em um formato json, depois,
 a informação retornada em um dicionário é passada nas variáveis gender e age que estão dentro de [] pois,
 como já explicado, é a chave correspondente dentro do dicionário json. Já no return render_template
 são passados o novo código html criado para essa rota, assim como as variáveis que são o nome da variável aqui
 criada = o nome da variável criada no html."""
@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response=requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)