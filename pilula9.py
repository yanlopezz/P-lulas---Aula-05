def calcular_media (prod,quali,pont):
    return (prod + quali + pont) / 3

def classificar(media):
    if media >= 8:
        return 'Excelente'
    elif media >= 6:
        return 'Bom'
    else:
        return 'Crítico'
    
def avaliar_funcionarios():
    total = 0
    exc = 0
    bom = 0
    crit = 0
    melhornome = " "
    melhormedia = -1

    while True:
        nome = input('Nome: ')
        if nome == 'Fim':
         break
        prod = float(input('Produtividade: '))
        qual = float(input('Qualidade: '))
        pont = float(input('Pontualidade: '))

        media = calcular_media(prod, qual, pont)
        categoria = classificar(media)

        print(f'{nome}, média {media}, {categoria}')

        total += 1
        if categoria == "Excelente":
            exc += 1
        elif categoria == "Bom":
            bom += 1
        else:
            crit += 1

        if media > melhormedia:
            melhormedia = media
            melhornome = nome

    if total == 0:
        print('Nada para calcular')
        return
    
    print("-" * 50)
    print('Relatório')
    print("-" * 50)
    print(f'Total de func: {total}')
    print(f"Excelente: {exc}")
    print(f"Bom: {bom}")
    print(f"Crítico: {crit}")
    print(f"Melhor func: {melhornome}")
    print(f"Mlehor func média: {melhormedia}")

avaliar_funcionarios()

