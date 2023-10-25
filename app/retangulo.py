class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    
    def definirDimensoes(self, ):
        if self.altura and self.largura > 0:
            return f"A altura do do retangulo é {self.altura} M"
          
        else:
            return False

    def calcularArea(self, ):
        return f"A área do retangulo é {self.largura} + {self.altura} = {self.largura + self.altura}"

    def calcularPerimetro(self,):
        return f"O perímetro é {2*(self.altura + self.largura)}"