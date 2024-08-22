CONSTANT_BONUS = 1000

# 1. Solicite que o usuário digite o seu nome
nome_usuario = input("Digite o seu nome: ")

# 2. Solicite que o usuário digite o seu salário
salario = float(input("Digite o seu salário: "))

# 3. Solicite que o usuário digite o seu bônus
bonus = float(input("Digite o seu bônus (em percentual, por exemplo, 0.10 para 10%): "))

# 4. Calcule o valor do bônus
valor_bonus = CONSTANT_BONUS + (salario * bonus)

# 5. Exiba o resultado na tela do usuário
print(f"O funcionário {nome_usuario} tem {valor_bonus:.2f} de bônus para receber.")
print("Obrigado!")








