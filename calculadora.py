import os

class Calculadora:

    def getOperators(self):
        return {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
            '**': lambda a, b: a ** b,
            '%': lambda a, b: a % b
        }

    def validOperation(self, operation):
        operators = self.getOperators()
        return operation in list(operators.keys())

    def display(self):
        while True:
            operation = input('''
            Calculadora:

                
                Escolha a opção:

                + para adição
                - subtração
                * multiplicação
                / divisão
                ** exponenciação
                % módulo
            ''')
            if not self.validOperation(operation):
                self.clearDisplay()
                print('\nOPERAÇÃO INVÁLIDA!\n')
                continue
            number1 = int(input('Entre com o primeiro número: '))
            number2 = int(input('Entre com o segundo número: '))
            print("\n{} {} {} = {}\n\n".format(
                number1,
                operation,
                number2,
                self.calc(operation, number1, number2)
            ))
            if input('Aperte "Enter" para continuar ou digite "Q" para sair: ') == 'Q':
                break
            self.clearDisplay()
            

    def clearDisplay(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def calc(self, operation, number1, number2):
        operators = self.getOperators()  
        return operators[operation](number1, number2)

    def start(self):
        self.display()  

calc = Calculadora()
calc.start()