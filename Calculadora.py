print("\nCalculadora")
def somar(a,b):
    resultado = a + b
    return (f"A soma de {a} + {b} é igual a {resultado}")

def subtracao(a,b):
    resultado = a - b
    return (f"A subtração de {a} - {b} é igual a {resultado}")

def multiplicacao(a,b):
    resultado = a * b
    return (f"A multiplcação de {a} * {b} é igual a {resultado}")

def divisao(a,b):
    resultado = a / b
    return (f"A divisão de {a} / {b} é igual a {resultado}")

while True:
    a = int(input("Digite o primeiro número:"))
    b = int(input("Digite o segundo número:"))
    print("\n[1] SOMA" \
    "\n[2] SUBTRAÇÃO" \
    "\n[3] MULTIPLICAÇÃO" \
    "\n[4] DIVISÃO")
    operacao = input("Digite qual das operações quer? ")
    if operacao == "1":
        print(somar(a,b))
    elif operacao == "2":
        print(subtracao(a,b))
    elif operacao == "3":
        print(multiplicacao(a,b))
    elif operacao == "4":
        print(divisao(a,b))
    else:
        print()
    
    
    
    
    