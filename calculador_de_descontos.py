from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):
    def calcula(self, orcamento):
        #:todo:. pattern projeto -  Chain of Responsibility_ sequencia de nós encadeados,
        #:todo:. onde cada nó possui uma determinada responsabilidade.
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto()
                                                  )
        ).calcula(orcamento)

        print(desconto)


if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 70))
    orcamento.adiciona_item(Item('ITEM - 2', 500))
    orcamento.adiciona_item(Item('ITEM - 3', 80))

    #orcamento.adiciona_item(Item('ITEM - 4', 10))
    #orcamento.adiciona_item(Item('ITEM - 5', 20))
    #orcamento.adiciona_item(Item('ITEM - 6', 10))
    #orcamento.adiciona_item(Item('ITEM - 7', 150))

    calculador = Calculador_de_descontos()
    desconto_calculado = calculador.calcula(orcamento)



    print('\n')
    for var in range(len(orcamento.nome_item)):
        print(var)

    print('\n\n', orcamento.nome_item[0]['nome_item'])





"""
:.deverá saber o proximo nó da cadeia.:

    O padrão Chain of Responsibility 
cai como uma luva quando temos uma lista de comandos a 
serem executados de acordo com algum cenário em específico, 
e sabemos também qual o próximo cenário que deve ser validado, 
caso o anterior não satisfaça a condição.
    Nesses casos, o Chain of Responsibility 
nos possibilita a separação de responsabilidades 
em classes pequenas e enxutas, e ainda provê uma maneira 
flexível e desacoplada de juntar esses comportamentos novamente.


"""