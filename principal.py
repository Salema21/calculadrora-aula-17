'''from calculadora import Calculadora
from livro import livro

if __name__ == "__main__":
    calculadora = Calculadora()
livro1 = livro("Pedro", "27")
print(livro1)

while True:
        print("\nOperacao disponiveis:\nsoma, + , subtrair , - , multiplicar, * , dividir , / ,exponenciacao ,** ")
        operacao = input("Escolha a operção para continuar ou digite 'sair' para encerrar: ")

        if operacao == "sair":
            break

        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))


        if operacao == "soma" or operacao == "+":
            resultado = calculadora.soma(valor1,valor2)
        elif operacao == "subtrair" or operacao == "-":
            resultado = calculadora.subtrair(valor1,valor2)
        elif operacao == "multiplicar" or operacao == "*":
            resultado = calculadora.multiplicar(valor1,valor2)
        elif operacao == "dividir" or operacao == "/":
            resultado = calculadora.dividir(valor1,valor2)
        elif  operacao == "exponenciacao" or operacao == "**":
            resultado = calculadora.exponenciacao(valor1,valor2)
        else:
            print("opercao invalida")
            continue # ele volta para o inicio de do programa

        print(f"Resultado:  {resultado}")'''
from calculadora import Calculadora
from livro import livro

if __name__ == "__main__":
    calculadora = Calculadora()
    livro1 = livro("Pedro", "27")
    print(livro1)

    while True:
        # print("\nOperações disponíveis: soma,+,subtrair,-, multiplicar,*,dividir, /,exponenciacao,**")
        print("Operações disponíveis:soma (+)  subtrair (-)  multiplicar (*)  dividir (/)  exponenciacao (**)""")

        operacao = input("Escolha a operação ou digite 'sair' para encerrar: ")

        if operacao == "sair":
            break

        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))

        if operacao in ["soma", "+"]:
            resultado = calculadora.soma(valor1, valor2)
        elif operacao in ["subtrair", "-"]:
            resultado = calculadora.subtrair(valor1, valor2)
        elif operacao in ["multiplicar", "*"]:
            resultado = calculadora.multiplicar(valor1, valor2)
        elif operacao in ["dividir", "/"]:
            resultado = calculadora.dividir(valor1, valor2)
        elif operacao in ["exponenciacao", "**"]:
            resultado = calculadora.exponenciacao(valor1, valor2)
        else:
            print("Operação inválida.")
            continue

        print(f"Resultado: {resultado}")



