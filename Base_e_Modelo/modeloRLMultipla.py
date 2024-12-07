import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def normalizarBase(dataset):
    '''
    Normalizacao dos dodos

        conversao dos campos string para numeros
        campos: 
            genero: {"feminino": "0" , "masculino": "1"}
            fumante: {"sim": "1" e "nao": "0"}
            regiao: {"centro-oeste": "0", "nordeste": "1", "norte": "2", "sudeste": "3", "sul": "4"}

    '''
    encoder = OrdinalEncoder()
    dataset[["genero"]] = encoder.fit_transform(dataset[["genero"]])
    dataset[["fumante"]] = encoder.fit_transform(dataset[["fumante"]])
    dataset[["regiao"]] = encoder.fit_transform(dataset[["regiao"]])
    # print(dataset.describe())
    # print(dataset.info())
    # print(dataset.head())

    # #Histograma dos dados
    # dataset.hist(figsize=(12,12))
    # plt.show()

    # plt.figure(figsize=(6,4))
    # sns.heatmap(dataset[["idade", "genero", "encargos", "fumante", "regiao"]].corr(method = 'pearson'), annot=True, fmt=".1f")
    # plt.show()

    # sns.pairplot(dataset, hue="idade")
    # sns.histplot(dataset, x="encargos")
    # plt.show()

    return dataset

def treinarModelo(x_train, y_train):
    '''
    Iniciando o treinamento do modelo
        X: serao utilizados os campos: idade, genero, fumante e regiao para a criacao dos dados de referencia do modelo, analisando a correlacao,
            esses campos apresentaram um comportamento que gera uma influencia direta na definicao dos encargos
        Y: Nosso target de pesquisa será o campo encargos, ele armazenos os custo do seguro saude de cada um dos registros da base

    '''
    modelo = LinearRegression()
    modelo.fit(x_train, y_train)

    return modelo

def salvarModelo(modelo):
    '''
    salvando o modelo treinado

    '''
    filename = "modelo_regressaoLinearMultipla.pkl"
    pickle.dump(modelo, open(filename, "wb"))
    

def testarModelo(modelo, x_test, y_test):
    previsao = modelo.predict(x_test)
    # print(x_test[0:1])
    # print(previsao[0:1])
    
    # Avaliando o desempenho do modelo
    mse = mean_squared_error(y_test, previsao)
    erro_medio_quadratico = np.sqrt(mse)
    erro_absoluto_medio = mean_absolute_error(y_test, previsao)
    r_quadrado = r2_score(y_test, previsao)

    print(f"Erro Médio Quadrático: {erro_medio_quadratico}")
    print(f"Erro Absoluto Médio: {erro_absoluto_medio}")
    print(f"R² (coeficiente de determinação): {r_quadrado}")


#avaliacao da estrutura da base
base = pd.read_csv("baseSeguroSaude.csv", sep=",")
# print(base.head())
# print(base.describe())
# print(base.info())
# print(base.isnull().sum())

base = normalizarBase(base)

'''
Separacao dos dados para treinamento e testes

'''
x = base.drop(columns=["encargos", "imc", "filhos"])
y = base["encargos"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = treinarModelo(x_train, y_train)
salvarModelo(modelo)
testarModelo(modelo, x_test, y_test)