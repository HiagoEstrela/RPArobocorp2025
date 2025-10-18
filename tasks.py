from robocorp.tasks import task
from robocorp.log import log

@task
def minimal_task():
    message = "Hello"
    message = message + " World!"
    print (message)
    return message

@task
def saudacao_personalizada():
    print("Iniciando tarefa de saudação...")
    nome_usuario = input("Por favor, digite seu nome: ")
    print(f"Olá, {nome_usuario}!Bem vindo ao mundo Robocorp.")
    print("Tarefa de saudação finalizada com sucesso")

@task
def main()
    minimal_task()
    saudacao_personalizada()