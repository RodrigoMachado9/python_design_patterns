# -*- coding: UTF-8 -*-
class Orcamento(object):

    def __init__(self):
        #:.todo >> lista contendo determinandos itens
        self.__itens = []


    #:.todo python_get.:
    #:.dentro de uma property não é obrigatório utilizar uma variável explicita no construtor python ou global,
    #:.a propriedade python encapsula o processo retornando apenas o resultset da operação.Igual ao caso da propriedade valor.
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total

    @property
    def nome_item(self):
        nome = []
        for item in self.__itens:
            nome.append({'nome_item':item.nome,
                         'valor_item':item.valor})
        return nome

    #:.todo valor em tupla = value resultset imutable.
    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)


    def adiciona_item(self, item):
        self.__itens.append(item)





#:.todo ( class Item ) do orçamento
class Item(object):

    def __init__(self, nome, valor):
        #:.todo >> atributos referente a determinado orçamento
        self.__nome =  nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome