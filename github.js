/*
**CURSO DE GIIHUB CONTINUACION DE GIT**
    Se va a utilizar las claves SSH, van a estar
    guardadas en /home/usuario/.ssh/, el comando
    para crear la clave es:
        ssh-keygen -t ed25519 -C "youremail@example.com"
        ssh -T git@github.com
# Attempts to ssh to GitHub
    **COMANDO REMOTE
        Comando que sirve para vincular el repositorio
        local con el de github con el comando:
            git remote add origin 
            https://github.com/ramirezjoserain-beep/hello_git.git
    **COMANDO PUSH
        Se utiliza para llevar el contenido del 
        repositorio local al de github.
            git push -u origin (nombre de la rama)"main"
    **COMANDO FETCH
        Permite descargar el historial de cambios
        sin descargar los cambios con el comando:
            git fetch
    **COMANDO PULL
        Permite descargar el historial de cambios 
        descargando tambien los cambios ejecutados
        con el comando:
            git pull origin main
        ****NOTA****
            Es importante al comento de realizar el
            pull utilizar el merge para evitar problemas
            dado que de haber alguno, al hacer el merge
            git nos mostraria si hay o no conflicto.
            Con el comando:
                git config pull.rebase false #merge




https://www.youtube.com/watch?v=3GymExBkKjE
min 3:00:00
*/ 