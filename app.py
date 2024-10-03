from flask import Flask, render_template, redirect, request, g
import requests
import sqlite3
import random


lista = []


app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html', Titulo='API Patos')


@app.route('/cadastro')
def cadastro():
    url = random.randint(1, 100)
    imagemPato = (f'https://random-d.uk/api/{url}.jpg')
    return render_template('cadastro.html', Titulo='API Patos - Cadastro', imagem=imagemPato)


@app.route('/galeria')
def galeria():
    images = lista
    return render_template('galeria.html', Titulo='API Patos - Galeria', imagensbd=images)


@app.route('/criar', methods=['POST'])
def criar():
    pato = request.form['pato']
    nome = request.form['nome']
    patos = [pato, nome]
    lista.append(patos)
    return redirect('/cadastro')


if __name__ == '__main__':
    app.run()
