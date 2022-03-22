class Estados:
    def __init__(self, nome, sigla, regiao, populacao, area, cod_area):
        """Construtor do objeto estado

        Args:
            nome (string): nome do estado
            sigla (string)): sigla do estado
            regiao (string): regiao onde o estado esta localizado
            populacao (int): populacao
            area (float): area territorial (em km^2)
            cod_area (string): codigo de area
        """
        
        try:
            self.nome = nome
            self.sigla = sigla
            self.regiao = regiao
            self.populacao = populacao
            self.area = area
            self.cod_area = cod_area
        except Exception as e:
            print(str(e))
            
    def set_nome(self, nome):

        try:
            self.nome = nome
        except Exception as e:
            print(str(e))
          
    def get_nome(self):
        try:
            return self.nome
        except Exception as e:
            print(str(e))

    def set_sigla(self, sigla):
        try:
            self.sigla = sigla
        except Exception as e:
            print(str(e))
             
    def get_sigla(self):
        try:
            return self.sigla
        except Exception as e:
            print(str(e))
    
    def set_regiao(self, regiao):
        try:
            self.regiao = regiao
        except Exception as e:
            print(str(e))
    
    def get_regiao(self):
        try:
            return self.regiao
        except Exception as e:
            print(str(e))
                    
    def set_populacao(self, populacao):
        try:
            self.populacao = str(populacao)
        except Exception as e:
            print(str(e))
    
    def get_populacao(self):
        try:
            return self.populacao
        except Exception as e:
            print(str(e))
    
    def set_area(self, area):
        try:
            self.area = str(area)
        except Exception as e:
            print(str(e))
    
    def get_area(self):
        try:
            return self.area
        except Exception as e:
            print(str(e))
            
    def set_cod_area(self, cod_area):
        try:
            self.area = cod_area
        except Exception as e:
            print(str(e))
    
    def get_cod_area(self):
        try:
            return self.cod_area
        except Exception as e:
            print(str(e))