continuar = "S"
while continuar == "S":
    # entrada dos números e operação
    numero1 = float(input("Insira o primeiro número: "))
    operacao = input("Insira a operação (+, -, *, /): ")
    numero2 = float(input("Insira o segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2
        print(f"{numero1} + {numero2} = {resultado}")

    elif operacao == "-":
        resultado = numero1 - numero2
        print(f"{numero1} - {numero2} = {resultado}")

    elif operacao == "*":
        resultado = numero1 * numero2
        print(f"{numero1} * {numero2} = {resultado}")

    elif operacao == "/":
        if numero2 == 0:
            print("Divisão por zero não é permitida!")
            continue
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")

    else:
        print("Digite uma operação válida!")


    continuar = input("Deseja continuar? Digite S para sim e N para não: ").upper()

    while continuar != "S" and continuar != "N":
        print("Resposta inválida.")
        continuar = input("Digite S para sim ou N para não: ").upper()