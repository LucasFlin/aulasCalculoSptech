def calcular():
    txtPeso = input("Digite seu peso em kg: ")
    peso = float(txtPeso)
    while (peso <= 0):
        txtPeso = input("Peso inválido, tente novamente: ")
        peso = float(txtPeso)

    txtAltura = input("Digite sua altura em metros: ")
    altura = float(txtAltura)
    while (altura <= 0):
        txtAltura = input('Altura inválida, tente novamente: ')
        altura = float(txtAltura)
    imc = peso/(altura**2)
    msg = f"Seu IMC é {imc:.2f}"

    if (imc < 16):
        msg += ' - Baixo peso MUITO GRAVE (;_;)'
    elif (imc <= 16.9):
        msg += ' - Baixo peso grave (@_@)'
    elif (imc <= 18.4):
        msg += ' - Baixo peso :-|'
    elif (imc <= 24.9):
        msg += ' - Peso ideal <(-^,^-)=b'
    elif (imc <= 29.9):
        msg += ' - Sobrepeso :-0'
    elif (imc <= 34.9):
        msg += ' - Obesidade grau I :-|'
    elif (imc <= 39.9):
        msg += ' - Obesidade grau II (@_@)'
    else:
        msg += ' - Obesidade grau III (;_;)'

    print(msg)

    continuar = input("Deseja calcular outro IMC? (Digite S para continuar, ou aperte qualquer tecla para encerrar) ")
    if (continuar == 'S'):
        calcular()
    else:
        print("Encerrando a calculadora...")



calcular()