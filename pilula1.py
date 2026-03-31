def validarsenha(senha):
    if len(senha) < 8:
        return 'Senha inválida, muito curta'
    
    temNumero = False
    temMaiusculo = False

    for c in senha:
        if c == ' ':
            return 'Senha inválida, não pode conter espaço'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiusculo = True

    if not temNumero:
     return 'Senha inválida, não tem número'
    
    if not temMaiusculo:
     return 'Senha inválida, não tem leta maiúscula'
    
    return 'Senha válida'

#main
senha = input("Digite sua senha: ")
print(validarsenha(senha))