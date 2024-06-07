from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def _init_(self,nome,preco,tamanho):
        super()._init_(nome,preco)
        self.tamanho = tamanho
    
    def _str_(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)