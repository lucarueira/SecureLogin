# Dicionário contendo os usuários e senhas válidos
usuarios_senhas = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
    'usuario3': 'senha3'
}

def fazer_login():
    tentativas = 3
    while tentativas > 0:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        # Verifica se o usuário e senha correspondem aos registrados
        if usuario in usuarios_senhas and usuarios_senhas[usuario] == senha:
            print("Login bem-sucedido!")
            return
        else:
            tentativas -= 1
            print("Usuário ou senha inválidos. Tente novamente.")
            print("Tentativas restantes:", tentativas)
    
    print("Você excedeu o número máximo de tentativas.")

# Função principal
def main():
    print("Bem-vindo ao programa de login!")
    fazer_login()

if __name__ == "__main__":
    main()
