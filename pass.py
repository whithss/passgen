import string
import random
import os
import time
import getpass  # Importar o módulo getpass

# Funções para adicionar cores no terminal
def print_green(text):
    print("\033[92m{}\033[0m".format(text))

def print_yellow(text):
    print("\033[93m{}\033[0m".format(text))

os.system('cls' if os.name == 'nt' else 'clear')  # Limpar o terminal

def generate_password(length, upper_case, lower_case, special_chars, numbers):
    all_chars = string.ascii_letters + string.digits

    if upper_case:
        all_chars += string.ascii_uppercase

    if lower_case:
        all_chars += string.ascii_lowercase

    if special_chars:
        all_chars += string.punctuation

    if numbers:
        all_chars += string.digits

    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

# Obter entrada de senha de forma segura
password_length = int(input("Adicione o tamanho da senha ex:(8): "))
upper_case = input("Deseja Letras Maiúsculas? (Sim/Não): ").lower() == 'sim'
lower_case = input("Deseja Letras Minúsculas? (Sim/Não): ").lower() == 'sim'
special_chars = input("Deseja Caracteres Especiais? (Sim/Não): ").lower() == 'sim'
numbers = input("Deseja Números? (Sim/Não): ").lower() == 'sim'

os.system('cls' if os.name == 'nt' else 'clear')  # Limpar o terminal

time.sleep(0)  # Adicionar um tempo de espera de 3 segundos

# Gerar senha e imprimir em verde
generated_password = generate_password(password_length, upper_case, lower_case, special_chars, numbers)
print_green(generated_password)

# Adicionar uma pausa e impedir entrada após a exibição da senha
print_yellow("Pressione enter para sair.")
input()