from sympy import sympify
from re import fullmatch
from time import sleep
import math

class Calculadora:

    @staticmethod
    def operar_simples():
        while True:
            operacao = input('Digite uma operação ou "sair" para retornar ao menu:\n')
            if operacao.lower() == 'sair':
                Calculadora.menu()
                break
            elif fullmatch(r'[0-9.+\-*/()\[\]{}% ]+', operacao):
                # O símbolo de adição fora dos colchetes permite que a função verifique múltiplos caracteres
                resultado = sympify(operacao)
                if resultado.is_Integer:
                    print(f'RESULTADO: {int(resultado)}')
                elif resultado.is_rational:
                    print(f'RESULTADO: {float(resultado)}')
                else:
                    print(f'RESULTADO: {resultado.evalf()}')
                    # Converte o resultado simbólico para numérico (ex: 2*sqrt(6))
            else:
                print('ERRO: Entrada inválida.')
                sleep(1)

    @staticmethod
    def calcular_logaritmo():
        while True:
            numero = input('Digite o número do qual você deseja o logaritmo ou "sair" para voltar ao menu anterior:\n')
            base = input('Digite a base do logaritmo ou "sair" para voltar ao menu anterior:\n')
            if numero.lower() or base.lower() == 'sair':
                Calculadora.operar_especifico()
                break
            elif numero.isnumeric() and base.isnumeric():
                numero = int(numero)
                base = int(base)
                print(f'O logaritmo de {numero} na base {base} é {math.log(numero, base)}.')
                sleep(1)
            else:
                print('ERRO: Entrada inválida.')
                sleep(1)

    @staticmethod
    def calcular_fatorial():
        while True:
            entrada = input('Digite o número do qual você deseja o fatorial ou "sair" para retornar ao menu anterior.\n')
            if entrada.lower() == 'sair':
                Calculadora.operar_especifico()
                break
            elif entrada.isnumeric():
                entrada = int(entrada)
                print(f'O fatorial de {entrada} é {math.factorial(entrada)}')
                sleep(1)
            else:
                print('ERRO: Entrada inválida')
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
                case '1':
                    Calculadora.calcular_logaritmo()
                case '2':
                    Calculadora.calcular_fatorial()
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