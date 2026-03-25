from .. import User

print("Ola, Crie seu usuario:")
print("----------------------")

email = input("Insira o seu email: ")
username = input("Insira o seu username: ")
password = input("Insira sua senha: ")

newUser = User.User(email, username, password)

print(f"\n{newUser}")