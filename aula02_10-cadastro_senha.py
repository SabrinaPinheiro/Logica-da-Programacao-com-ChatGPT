# Neste módulo você construirá um simulador de cadastro de senha e inicialização de celular.
# Vamos supor que o usuário acabou de comprar um celular na loja e após a primeira carga, ele liga o celular pela primeira vez.
# Ao iniciar o celular, a primeira coisa que aparece na tela é o pedido para cadastrar a senha e, logo após, confirmar a senha.
# Essa é a sua primeira tarefa.
# Construa o pedido de senha e confirmação.
# Se a senha confirmada estiver correta, exiba a mensagem: Senha correta. Bem-vindo.
# Senão, exiba a mensagem: Senha incorreta. Tente novamente

# Solicita ao usuário que digite uma senha
senha = float(input("Digite uma senha: "))

senha_conf = float(input("Digite a senha novamente: "))

# Verifica se as senhas são iguais e imprimi a mensagem correspondente
resultado = "Senha correta. Bem-vindo." if senha == senha_conf else 'Senha incorreta. Tente novamente'

# Imprime a mensagem com o resultado
print (resultado)