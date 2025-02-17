from sympy import sympify
from re import fullmatch
from time import sleep
import math

class Calculadora:
    @classmethod
    def operar_simples(cls):
        while True:
            operacao = input('Digite uma operação ou "sair" para retornar ao menu:\n').strip()
            substituicoes = {'×': '*', '÷': '/', ',': '.', '[': '(', ']': ')', '{': '(', '}': ')'}
            for errado, certo in substituicoes.items():
                operacao = operacao.replace(errado, certo)

            if operacao.lower() == 'sair':
                cls.menu()
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
                print('Por favor, digite uma entrada válida ou "sair".\n')
                sleep(1)

    @classmethod
    def calcular_logaritmo(cls):
        while True:
            numero = input('Digite o número do qual você deseja o logaritmo ou "sair" para voltar ao menu anterior:\n').strip()
            if numero.lower() == 'sair':
                cls.operar_especifico()
            base = input('Digite a base do logaritmo ou "sair" para voltar ao menu anterior:\n')
            if base.lower() == 'sair':
                cls.operar_especifico()

            if numero.isdigit() and base.isdigit():
                numero = float(numero)
                base = float(base)
                print(f'O logaritmo de {numero} na base {base} é {math.log(numero, base)}.')
                sleep(1)
            else:
                print('Por favor, digite entradas válidas ou "sair".\n')
                sleep(1)

    @classmethod
    def calcular_fatorial(cls):
        while True:
            entrada = input('Digite o número do qual você deseja o fatorial ou "sair" para retornar ao menu anterior.\n').strip()
            if entrada.lower() == 'sair':
                cls.operar_especifico()
            elif entrada.isdigit():
                entrada = int(entrada)
                print(f'O fatorial de {entrada} é {math.factorial(entrada)}')
                sleep(1)
            else:
                print('Por favor, digite uma entrada válida ou  "sair".\n')
                sleep(1)

    @classmethod
    def calcular_radiciacao(cls):
        while True:
            entrada = input('Digite um número para ver suas raízes (quadrada, cúbica e quinta) ou "sair" para retorna ao menu anterior:\n').strip()

            if entrada.lower() == 'sair':
                cls.operar_especifico()
            elif entrada.isdigit():
                raiz_quadrada = sympify(f'{entrada} ** (1/2)')
                raiz_cubica = sympify(f'{entrada} ** (1/3)')
                raiz_quinta = sympify(f'{entrada} ** (1/5)')
                # Se não usar o sympify numa string ou numa variável originalmente string, ele não interpretará do jeito certo

                if raiz_quadrada.is_Integer:
                    print(f'RAIZ QUADRADA: {int(raiz_quadrada)}\n')
                elif raiz_quadrada.is_Float:
                    print(f'RAIZ QUADRADA: {float(raiz_quadrada)}')
                else:
                    print(f'RAIZ QUADRADA (Forma Decimal): {raiz_quadrada.evalf()}')
                    print(f'RAIZ QUADRADA (Representação Simbólica): {raiz_quadrada}\n')

                if raiz_cubica.is_Integer:
                    print(f'RAIZ CÚBICA: {int(raiz_cubica)}\n')
                elif raiz_cubica.is_Float:
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
                print('Por favor, digite uma entrada válida ou "sair".\n')
                sleep(1)

    @classmethod
    def calcular_porcentagem(cls):
        while True:
            numero = input('Digite o número do qual deseja extrair a porcentagem ou "sair" para retornar ao menu anterior:\n').strip()
            if numero.lower() == 'sair':
                cls.operar_especifico()

            porcentagem = input('Digite a porcentagem desejada (apenas números) ou "sair" para retornar ao menu anterior:\n')
            if porcentagem.lower() == 'sair':
               cls.operar_especifico()

            if fullmatch(r'[0-9. ]+', numero) and fullmatch(r'[0-9. ]+', porcentagem):
                numero = float(numero)
                if numero.is_integer():
                    numero = int(numero)

                porcentagem = float(porcentagem)
                if porcentagem.is_integer():
                    porcentagem = int(porcentagem)

                resultado = numero * (porcentagem / 100)
                if resultado.is_integer():
                    resultado = int(resultado)

                print(f'{porcentagem}% de {numero} é igual a {resultado}')
            else:
                print('Por favor, digite entradas válidas ou "sair".\n')

    @classmethod
    def operar_especifico(cls):
        while True:
            selecao = input('''As operações disponíveis são:
[1] Logaritmo
[2] Fatoração
[3] Radiciação (automática)
[4] Porcentagem (automática)
Digite o número correspondente à opção desejada ou "sair" para retornar ao menu.\n''').strip()

            match selecao.lower():
                case 'sair':
                    cls.menu()
                case '1':
                    cls.calcular_logaritmo()
                case '2':
                    cls.calcular_fatorial()
                case '3':
                    cls.calcular_radiciacao()
                case '4':
                    cls.calcular_porcentagem()
                case _:
                    print('ERRO: Entrada inválida')
                    sleep(1)

    @classmethod
    def menu(cls):
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
                    print('Até mais!')
                    sleep(1)
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
                    cls.operar_simples()
                    break
                case '2':
                    cls.operar_especifico()
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
                    print('Por favor, digite uma entrada válida ou "sair".')
                    sleep(1)