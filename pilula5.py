def calcularnotas(valor):
    for nota in (100,50,20,10,5,2):
        qnt = valor // nota
        valor = valor % nota
        if qnt > 0:
            print(f'{qnt} notas de R$ {nota}')

valor = int(input('Digite seu valor: '))
calcularnotas(valor)