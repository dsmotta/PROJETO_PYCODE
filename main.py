# Variaveis para segurança das informações e valores
# Linux -  export MINHA_VAR=valor
# windows - set MINHA_VAR=valor
# usar  a importação do OS

import os
import api

ambiente = os.environ.get('AMBIENTE')
# usu = os.environ.get('USUARIO_API')
# sen = os.environ.get('SENHASENHA_API')

# api.login(usu, sen)

if ambiente == 'dev':
    print(api.envia_email_log())



