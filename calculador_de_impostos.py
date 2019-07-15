from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):

        def realiza_calculo(self, orcamento, imposto):

                #:.metodo calcula -> graças a tipagem => duck typing
                imposto_calculado = imposto.calcula(orcamento)

                print (imposto_calculado)


if __name__ == '__main__':

        from orcamento import Orcamento, Item

        #todo:.objetos referente as classes
        orcamento = Orcamento()
        calculador = Calculador_de_impostos()


        orcamento.adiciona_item(Item('ITEM 1', 50))
        orcamento.adiciona_item(Item('ITEM 2', 200))
        orcamento.adiciona_item(Item('ITEM 3', 251))


        print('\nISS and ICMS')
        calculador.realiza_calculo(orcamento, ISS())
        calculador.realiza_calculo(orcamento, ICMS())


        print('\nICPP and IKCV')
        calculador.realiza_calculo(orcamento, ICPP())
        calculador.realiza_calculo(orcamento, IKCV())
        print('\n')
        print(orcamento.total_itens)