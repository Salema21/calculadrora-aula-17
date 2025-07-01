class Calculadora:

    def soma(self,valor1,valor2):
        return valor1 + valor2

    def subtrair(self,valor1,valor2):
        return  valor1 - valor2

    def multiplicar(self,valor1,valor2):
        return  valor1 * valor2

    def dividir(self,valor1,valor2):
        if valor2 == 0:
            return "erro de divisao por zero"
        return valor1 / valor2

    def exponenciacao(self,valor1,valor2):
            return int(valor1) ** (valor2)


def livro():
    return None