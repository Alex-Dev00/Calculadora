print("\nCalculadora")
num1 = input("Digite um número:")
operacao = input("Digite a operação que deseja: ")
num2 = input("Digite o segundo numero: ")

def soma():
    resu = int(num1 + num2)
    
    print(f"O resultado da soma é {resu}")

print(soma)



while True:

    if operacao == "+":
        print(soma())
    
    break
    
    
    
    
    
    
    
    
    