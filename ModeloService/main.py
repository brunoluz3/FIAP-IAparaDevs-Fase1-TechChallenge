import pickle
import uvicorn
import json
import pandas as pd
from fastapi import FastAPI, status, HTTPException
from model.perfil import PerfilSegurado

app = FastAPI()

@app.get("/ml/previsao")
def fazerPrevisao(
    idade, genero,
    fumante, regiao
):    
    try:   
        modelo = carregarModelo()
        previsao = modelo.predict(montarPerfil(idade=idade, 
                                           genero=genero, 
                                           fumante=fumante, 
                                           regiao=regiao))
     
        return previsao[0]
    except:
         raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                             detail=f"Ocorreu um erro ao executar a previsão de custo")    
                       
def carregarModelo():
     return pickle.load(open("modelo_regressaoLinearMultipla.pkl", "rb"))

def montarPerfil(idade, genero, fumante, regiao):   
        '''
        conversao dos campos string para numeros
        campos: 
            genero: {"feminino": "0" , "masculino": "1"}
            fumante: {"sim": "1" e "nao": "0"}
            regiao: {"centro-oeste": "0", "nordeste": "1", "norte": "2", "sudeste": "3", "sul": "4"}

        '''
        try:
            _idade = int(idade)
            _genero = str(genero)
            _fumante = str(fumante)
            _regiao = str(regiao)
        except:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  detail=f"Ocorreu um erro durante o tratamento dos dados, forneça os dados com o seguinte formato: \n idade = int \n genero = masculino/feminino \n fumante = sim/não \n regiao = norte/nordeste/centro-oeste/sudeste/sul")
              
        try:
            perfil = PerfilSegurado()
            entrada = [[_idade, 
                        perfil.tratarGenero(_genero), 
                        perfil.tratarFumante(_fumante), 
                        perfil.tratarRegiao(_regiao)]]
            
            return entrada
        except:
             raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR,
                                  detail=f"Ocorreu um erro durante a montagem do perfil do segurado")

if __name__ == "__main__":
    uvicorn.run(app, port=8000)