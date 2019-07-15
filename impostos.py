#:.todo pattern python strategy + ( ducktyping - porque utiliza-se classes com metodos e nomes iguais )
#:.todo ( aplicando uma generalização a estrutura  utilizando a (class Template_de_imposto_condicional) )

from abc import ABCMeta, abstractmethod

#:. as classes filhas de template, serão responsáveis por implementar os métodos abstratos da classe.
class Template_de_imposto_condicional(object):

    #:.todo propriedade mágica
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    #:.todo  @abstractmethod ( magic method )
    #:.todo  Obriga as classes que herdarem template a utilizar as funções da mesma.
    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass





class ISS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06



class ICPP(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500


    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07


    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05



class IKCV(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1


    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06


    #:.todo metodo privado, auxiliar para verificar se existe pelo meno um elemento maior que 100.
    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False



