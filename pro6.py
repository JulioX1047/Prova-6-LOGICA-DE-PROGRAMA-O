
ucorreto = "cara"
scorreta = "chato"


tmaximas = 3


for tentativa in range(tmaximas):
    
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    
    if usuario == ucorreto and senha == scorreta:
        print("Bem-vindo! Você está logado.")
        break  
    else:
        trestantes = tmaximas - (tentativa + 1)
        if trestantes > 0:
            print(f"Credenciais incorretas. Você tem {trestantes} tentativas restantes.")
        else:
            
            for _ in range(3):
                print("Acesso bloqueado.")
