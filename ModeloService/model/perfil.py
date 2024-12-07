class PerfilSegurado:

    # def __init__(self, idade, genero, fumante, regiao):
    #     self._idade = idade
    #     self._genero = genero
    #     self._fumante = fumante
    #     self._regiao = regiao

    def tratarGenero(self, genero):
        '''
        genero: {"feminino": "0" , "masculino": "1"}

        '''

        if genero == "masculino":
            return 1
        else:
            return 0
        
    def tratarFumante(self, fumante):
        '''
        fumante: {"sim": "1" e "nao": "0"}

        '''

        if fumante == "sim":
            return 1
        else:
            return 0
        
    def tratarRegiao(self, regiao):
        '''
            regiao: {"centro-oeste": "0", "nordeste": "1", "norte": "2", "sudeste": "3", "sul": "4"}

        '''
        
        match regiao:
            case "centro-oeste":
                return 0
            case "nordeste":
                return 1
            case "norte":
                return 2
            case "sudeste":
                return 3
            case "sul":
                return 4    