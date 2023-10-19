class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    
    def definirDimensoes(self, ):
        if self.altura and self.largura > 0:
            print(f'A altura do do retangulo é {self.altura}M')
            print(f'A largura do retangulo é {self.largura}M')
            return True
        else:
            return False