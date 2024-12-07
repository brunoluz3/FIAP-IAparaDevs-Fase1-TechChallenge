import csv
import random

'''
Essa base se trata de uma estrutura para armazenamento de dados de cliente de uma seguradora de saude

Estrutura do arquivo:
idade,gênero,imc,filhos,fumante,região,encargos

tipo: csv

'''

caminho = "baseSeguroSaude.csv"

#Criando a estrutura do arquico de acordo com a orientacao do desafio
cabecalho = ["idade","genero","imc","filhos","fumante","regiao","encargos"]
linha1 = ["56","feminino","29.774373714007336","2","sim","sudeste","3109.889763423336"]
linha2 = ["46","masculino","25.857394655216346","1","não","nordeste","2650.702646642694"]
linha3 = ["32","masculino","23.014839993647488","0","não","sudeste","2159.03799039332"]

with open (caminho, mode="w", encoding="utf-8", newline="") as csvFile:
    write = csv.writer(csvFile)
    write.writerow(cabecalho)
    write.writerow(linha1)
    write.writerow(linha2)
    write.writerow(linha3)

    #Iniciando a criacao de novos registros para montagem da base
    novoRegistro = []
    for i in range (0, 1000):   
        idade = random.randint(1, 85)
        genero = "masculino" if random.randint(1, 2) == 1 else "feminino"   
        imc = random.uniform(20, 50)
        filho = random.randint(1, 3)
        fumante = "sim" if random.randint(1,2) == 1 else "não"
        regiaoRandom = random.randint(1, 5)
        encargos = 600
        
        #manipulacao da massa para incrementar o encargo de acordo com a idade
        if idade >= 70:
            encargos += 3000
        elif idade >= 60 and idade < 70:
            encargos += 2500
        elif idade >= 50 and idade < 60:
            encargos += 2000
        elif idade >= 40 and idade < 50:
            encargos += 1200
        elif idade >= 30 and idade < 40:
            encargos += 600
        elif idade >20 and idade <30:
            encargos += 400

        #manipulacao da massa para incrementar o encargo caso o genero seja masculino
        if genero == "masculino":
            encargos += 200

        #manipulacao da massa para incrementar o encargo caso o genero seja fumate
        if fumante == "sim":
            encargos += 500    
        
        regiao = ""
        match regiaoRandom:
            case 1:
                regiao = "norte"
                #manipulacao da massa para incrementar o encargo de acordo com a regiao
                encargos += 100 
            case 2:
                regiao = "nordeste"
                #manipulacao da massa para incrementar o encargo de acordo com a regiao
                encargos += 100 
            case 3:
                regiao = "centro-oeste"
                #manipulacao da massa para incrementar o encargo de acordo com a regiao
                encargos += 200 
            case 4:
                regiao = "sudeste"
                #manipulacao da massa para incrementar o encargo de acordo com a regiao
                encargos += 800 
            case 5:
                regiao = "sul"
                #manipulacao da massa para incrementar o encargo de acordo com a regiao
                encargos += 600
            case _:
                regiao = "não identificada"

        novoRegistro = [idade, genero, imc, filho, fumante, regiao, encargos]        
        write.writerow(novoRegistro)   