# Hacking Cookie Game

Este projeto é uma automação do famoso [Jogo do cookie](), jogo no estilo clicker onde o jogador tem que ficar clicando na tela para conseguir mais pontos ou evoluir no jogo.

## Como rodar?

### Baixando o ambiente

Antes de tudo, garanta que o python está instalado na máquina para ser possível rodar o projeto. Caso não tenha, [neste link](https://www.python.org/downloads/) é possível baixá-lo.
Para baixar é muito simples, ou se usa `git clone https://github.com/AHVG/hacking-cookie-game.git` ou `git clone git@github.com:AHVG/hacking-cookie-game.git` ou baixa diretamente o zip do projeto. Independete do modo é necessário saber onde foi instalado para ser possível fazer o próximo passo.

### Criando um ambiente virtual

Para uma melhorar experiência, é interessante usar um ambiente virtual do python ([documentação](https://docs.python.org/pt-br/3/tutorial/venv.html)), principalmente para futuramente não dar conflito com as bibliotecas já instalados do python. No link dado, está como é feito isso. Essencialmente é precisso apenas entrar dentro da pasta do projeto, usando `cd ./path/da/pasta/Game-of-Life/`, por exemplo, e criar um ambiente virtual e em seguida ativá-lo com `source nome-do-ambiente-virtual/bin/activate` (esse comando pode variar de SO, veja a documentação para saber qual é o seu).

### Instalando as dependências

Depois de criado e ativado o ambiente virtual, basta executar o pip na raiz do projeto para instalar o requirements.txt. Para isso, use o seguinte comando `pip3 install -r requirements.txt`, para o linux, e `pip install -r requirements.txt`, para o Windows.

### Executando o programa

Finalmente, após ter feito todos passos anteriores, execute os seguintes comandos na raiz do projeto para executá-lo: `cd src/` e, em seguida, `python3 main.py`, para linux, ou `python main.py`, para Windows.

## Como funciona

Ao abrir, um driver do chrome ou do firefox irá iniciar e o programa automaticamente entrará no jogo do cookie e o jogará. Sem precisar fazer mais nada, você verá seus cookies crscendo e se tornando cada vez mais rico. A seguir estão algumas imagens do programa em execução.

![image](https://github.com/AHVG/hacking-cookie-game/assets/97568599/b01ef884-d840-473c-93eb-4c9bfbc3b3fa)

![image](https://github.com/AHVG/hacking-cookie-game/assets/97568599/c86dee50-8245-4cb3-abd7-c169fc53bcc0)

