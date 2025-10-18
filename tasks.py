from robocorp.tasks import task
from robocorp import log

@task
def minimal_task():
    message = "Hello"
    message = message + " World!"
    senha_secreta = "12345"

    log.hide_from_output(senha_secreta)
    log.info("Senha secreta" + senha_secreta)
    log.info(message)

    print (message)
    return message

