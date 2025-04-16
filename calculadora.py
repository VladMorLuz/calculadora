def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    else:
        return "Essa opção não existe"

while True:
    print("\nEscolha a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    
    try:
        operacao = int(input("Digite a opção: "))
    except ValueError:
        print("Entrada inválida. Digite um número.")
        continue

    if operacao == 0:
        print("Saindo da calculadora. Até mais.")
        break
    elif operacao not in [1, 2, 3, 4]:
        print("Essa opção não existe")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Digite números válidos.")
        continue

    resultado = calculadora(num1, num2, operacao)
    print(f"Resultado: {resultado}")
