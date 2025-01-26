from utilidades import *

class Calculadora:

    @staticmethod
    def operar_simples():
        while True:
            operacao = input('Digite uma operação ou "sair" para retornar ao menu:\n')

            if operacao.lower() == 'sair':
                Calculadora.menu()
                break
            elif fullmatch(r"[0-9.+\-*/()\[\]{}% ]+", operacao):
                resultado = sympify(operacao)
                print(f'RESULTADO: {resultado}.')
                sleep(1)
            else:
                print('ERRO: Entrada inválida.')
                sleep(1)

    @staticmethod
    def operar_especifico():
        while True:
            selecao = input('''As operações disponíveis são:
[1] Logaritmo
[2] Fatoração
Digite o número correspondente à opção desejada ou "sair" para retornar ao menu.\n''')

            match selecao.lower():
                case 'sair':
                    Calculadora.menu()
                    break
                case '1':
                    numero = input('Digite o número do qual você deseja o logaritmo:\n')
                    base =  input('Digite a base do logaritmo:\n')
                    if numero.isnumeric() and base.isnumeric():
                        numero = int(numero)
                        base = int(base)
                        print(f'O logaritmo de {numero} na base {base} é {math.log(numero, base)}.')
                        sleep(1)
                    else:
                        print('ERRO: Entrada inválida.')
                        sleep(1)
                case '2':
                    numero = input('Digite o número do qual você deseja o fatorial.\n')
                    if numero.isnumeric():
                        numero = int(numero)
                        print(f'O fatorial de {numero} é {math.factorial(numero)}')
                        sleep(1)
                    else:
                        print('ERRO: Entrada inválida')
                        sleep(1)
                case _:
                    print('ERRO: Entrada inválida')
                    sleep(1)

    @staticmethod
    def menu():
        while True:
            selecao = input('''Os tipos de operação disponíveis são:
[1] Operações simples
[2] Operações específicas
[3] Conversões
[4] Estatística
[5] Geometria
[6] Finanças
Digite o número correspondente à opção desejada ou "sair" para encerrar o programa.\n''')

            match selecao.lower():
                case 'sair':
                    exit()
                case '1':
                    print('''Essa categoria permite:
    - Adição (+)
    - Subtração (-)
    - Multiplicação (*)
    - Divisão comum (/)
    - Divisão inteira (//)
    - Resto da divisão (%)                   
    - Potenciação (**)
    - Radiciação (X ** (1/2) para raíz quadrada, X ** (1/3) para raíz cúbica e X ** (1/5) para raíz quinta)
    - Porcentagem (X * (P/100) sendo P a porcentagem de X desejada)
    - Uso de chaves, colchetes e parênteses''')
                    Calculadora.operar_simples()
                    break
                case '2':
                    Calculadora.operar_especifico()
                    break
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    pass
                case '6':
                    pass
                case _:
                    print('ERRO: Digite uma opção válida ou "sair":')
                    sleep(1)