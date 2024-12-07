import pickle

idade = 34
genero = 0
fumante = 0
regiao = 4


dados=[[idade, genero, fumante, regiao]]
modelo = pickle.load(open("modelo_regressaoLinearMultipla.pkl", "rb"))

previsao = modelo.predict(dados)
print(previsao[0:1])