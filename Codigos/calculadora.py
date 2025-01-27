from sympy import sympify
from re import fullmatch
from time import sleep
import math

class Calculadora:
    @staticmethod
    def operar_simples():
        while True:
            operacao = input('Digite uma operação ou "sair" para retornar ao menu:\n').strip()
            if operacao.lower() == 'sair':
                Calculadora.menu()
            elif fullmatch(r'[0-9.+\-*/()\[\]{}% ]+', operacao):
                # O símbolo de adição fora dos colchetes permite que a função verifique múltiplos caracteres
                resultado = sympify(operacao)
                if resultado.is_Integer:
                    print(f'RESULTADO: {int(resultado)}')
                    sleep(1)
                elif resultado.is_rational:
                    print(f'RESULTADO: {float(resultado)}')
                    sleep(1)
                else:
                    print(f'RESULTADO DECIMAL: {resultado.evalf()}')
                    print(f'RESULTADO COM RADICAL: {resultado}')
                    # Converte o resultado simbólico para numérico (ex: 2*sqrt(6))
                    sleep(1)
            else:
                print('Por favor, digite uma entrada válida.\n')
                sleep(1)

    @staticmethod
    def calcular_logaritmo():
        while True:
            numero = input('Digite o número do qual você deseja o logaritmo ou "sair" para voltar ao menu anterior:\n').strip()
            base = input('Digite a base do logaritmo ou "sair" para voltar ao menu anterior:\n')
            if numero.lower() or base.lower() == 'sair':
                Calculadora.operar_especifico()
            elif numero.isnumeric() and base.isnumeric():
                numero = int(numero)
                base = int(base)
                print(f'O logaritmo de {numero} na base {base} é {math.log(numero, base)}.')
                sleep(1)
            else:
                print('Por favor, digite uma entrada válida.\n')
                sleep(1)

    @staticmethod
    def calcular_fatorial():
        while True:
            entrada = input('Digite o número do qual você deseja o fatorial ou "sair" para retornar ao menu anterior.\n').strip()
            if entrada.lower() == 'sair':
                Calculadora.operar_especifico()
            elif entrada.isnumeric():
                entrada = int(entrada)
                print(f'O fatorial de {entrada} é {math.factorial(entrada)}')
                sleep(1)
            else:
                print('Por favor, digite uma entrada válida.\n')
                sleep(1)

    @staticmethod
    def calcular_radiciacao():
        while True:
            entrada = input('Digite um número para ver suas raízes (quadrada, cúbica e quinta) ou "sair" para retorna ao menu anterior:\n').strip()

            if entrada.lower() == 'sair':
                Calculadora.operar_especifico()
            elif entrada.isdigit():
                raiz_quadrada = sympify(f'{entrada} ** (1/2)')
                raiz_cubica = sympify(f'{entrada} ** (1/3)')
                raiz_quinta = sympify(f'{entrada} ** (1/5)')
                # Se não usar o sympify numa string ou numa variável originalmente string, ele não interpretará do jeito certo

                if raiz_quadrada.is_Integer:
                    print(f'RAIZ QUADRADA: {int(raiz_quadrada)}\n')
                elif raiz_quadrada.is_rational:
                    print(f'RAIZ QUADRADA: {float(raiz_quadrada)}')
                else:
                    print(f'RAIZ QUADRADA (Forma Decimal): {raiz_quadrada.evalf()}')
                    print(f'RAIZ QUADRADA (Representação Simbólica): {raiz_quadrada}\n')

                if raiz_cubica.is_Integer:
                    print(f'RAIZ CÚBICA: {int(raiz_cubica)}\n')
                elif raiz_cubica.is_rational:
                    print(f'RAIZ CÚBICA: {float(raiz_cubica)}')
                else:
                    print(f'RAIZ CÚBICA (Forma Decimal): {raiz_cubica.evalf()}')
                    print(f'RAIZ CÚBICA (Representação Simbólica): {raiz_cubica}\n')

                if raiz_quinta.is_Integer:
                    print(f'RAIZ QUINTA: {int(raiz_quinta)}\n')
                elif raiz_quinta.is_Float:
                    print(f'RAIZ QUINTA: {float(raiz_quinta)}\n')
                else:
                    print(f'RAIZ QUINTA (Forma Decimal): {raiz_quinta.evalf()}')
                    print(f'RAIZ QUINTA (Representação Simbólica): {raiz_quinta}\n')

                sleep(1)

            else:
                print('Por favor, digite uma entrada válida.\n')
                sleep(1)

    @staticmethod
    def operar_especifico():
        while True:
            selecao = input('''As operações disponíveis são:
[1] Logaritmo
[2] Fatoração
[3] Radiciação (automática)
[4] Porcentagem (automática)
Digite o número correspondente à opção desejada ou "sair" para retornar ao menu.\n''').strip()

            match selecao.lower():
                case 'sair':
                    Calculadora.menu()
                case '1':
                    Calculadora.calcular_logaritmo()
                case '2':
                    Calculadora.calcular_fatorial()
                case '3':
                    Calculadora.calcular_radiciacao()
                case '4':
                    pass
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
Digite o número correspondente à opção desejada ou "sair" para encerrar o programa.\n''').strip()

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