from re import fullmatch
from sympy import sympify
from time import sleep

class Calculadora:

    @staticmethod
    def operar_basico():
        while True:
            operacao = input('''Essa categoria permite:
    - Adição (+)
    - Subtração (-)
    - Multiplicação (*)
    - Divisão (/)
    - Potência (**)
    - Uso de colchetes [ ] e chaves { } para organização.
Digite a operação ou "sair" para retornar ao menu.\n''')

            if operacao.lower() == 'sair':
                Calculadora.menu()
                break
            elif fullmatch(r"[0-9.+\-*/()\[\]{} ]+", operacao):
                resultado = sympify(operacao)
                print(f'O resultado é {resultado}')
                sleep(1)
            else:
                print('ERRO: Digite uma operação válida ou "sair".')
                sleep(1)

    @staticmethod
    def menu():
        while True:
            selecao = input('''Os tipos de operação disponíveis são:
[1] Operações Básicas
[2] Operações Avançadas
[3] Conversões
[4] Estatística
[5] Geometria
[6] Finanças
Digite o número correspondente à opção desejada ou "sair" para encerrar o programa.\n''')

            match selecao.lower():
                case 'sair':
                    exit()
                case '1':
                    Calculadora.operar_basico()
                    break
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    pass
                case '6':
                    pass
                case _:
                    print('ERRO: Digite uma opção válida ou "sair".')
                    sleep(1)