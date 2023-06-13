# Envio-automatico-de-mensagens-por-email
Usando PyAutoGUI, coleta algumas informações pelo terminal e envia um email. O programa abre o Chrome pelo menu iniciar do Windows, abre o Gmail e envia um email com uma mensagem personalizada, além da data de envio (usando a biblioteca datetime) e um printscreen do terminal.

Atenção: por usar as coordenadas da tela para clicar nos botões, o código precisa ser atualizado de máquina em máquina usando a função pyautogui.position() (ou pg.position, depende de como foi importada a bilbioteca). A função retorna as coordenadas atuais do mouse, que devem ser inseridas nas linhas 29 e 47, dentro do argumento da função pg.click().

Além disso, é importante o usuário já estar logado no email, e se certificar que a conexão com a internet é boa, pois o código executa independente do que estiver na tela.
