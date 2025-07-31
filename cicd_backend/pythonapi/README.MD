# Descomplica

Projetos de exemplo para as aulas da faculdade Descomplica

## Módulo de back-end - Python API

Neste respositório você encontrará um projeto já pronto! Você só terá que fazer algumas adaptações caso você altere alguma informação como o nome de usuário, senha, porta de comunicação com o banco de dados e nomes de tabelas, se você seguiu todo o passo-a-passo para subir o banco de dados MySQL da forma como está neste repositório, então provavelmente você não precisará alterar nada!

Teremos os seguintes passos:

1) Download do pacote de desenvolvimento em Python
2) Importação do projeto de API em Python deste repositório
3) Como criar uma imagem do Docker à partir do projeto em Python
4) Como subir um container para nossa API em Python no nosso Docker

## Download do Python

Bom, a primeira coisa é fazer o download do Python, neste caso é um pacote de desenvolvimento que nos permite programar e compilar aplicações escritas em Python.

[https://www.python.org/downloads/release/python-368/](https://www.python.org/downloads/release/python-368/)

Eu sei, há outras versões inclusive mais recentes, mas esta aplicação de exemplo foi feito no Python 3.6 e o instalador para Windows se encontra especificamente na versão 3.6.8 que é a do link acima, então para facilitar as coisas baixe e instale este pacote.

Após instalar, você terá que fazer o download de outra ferramenta (feita em Python inclusive) que é o PIP. Esta ferramenta é um gerenciador de pacotes e será necessário para baixar todas as dependências da aplicação. Para isto baixe o seguinte arquivo:

[https://bootstrap.pypa.io/pip/3.6/get-pip.py](https://bootstrap.pypa.io/pip/3.6/get-pip.py)

A versão do PIP também tem que casar com a versão do Python, por isso o link acima mostra um "3.6" no meio do endereço. Ao acessar este link, é provável que você veja o conteúdo do arquivo no próprio browser, neste caso clique com o botão direito do mouse e salve o arquivo em seu computador, abaixo está um exemplo feito com o Google Chrome:

A exemplo:

Acesso ao arquivo:
![get-pip.py](./imagens/imagem55.png "imagem55")

Clicar com o botão direito do mouse no Chrome e depois no item "Salvar como..."
![Salvar como](./imagens/imagem56.png "imagem56")

Eu escolhi salvar em D:\Temp\Downloads, o importante não é a pasta em si, mas você terá que lembrar onde deixou o arquivo
![Salvar como pasta](./imagens/imagem57.png "imagem57")

Uma vez que o arquivo tenha sido baixado, vá na pasta onde o arquivo foi baixado. No Windows, a pasta possui uma "barra de endereço" que mostra o caminho completo da pasta, clique nesta barra de endereços, digite "cmd" (sem as aspas duplas) e depois pressione a tecla ENTER.

A exemplo:

![Prompt de Comando do Windows](./imagens/imagem58.png "imagem58")

Digite o comando abaixo, isso fará com que o Python execute o script recém baixado, que basicamente instala o PIP.

`python get-pip.py`

O PIP começará a ser instalado, é só aguardar até o final da instalação.

A exemplo:

![Python install pip](./imagens/imagem59.png "imagem59")

## Importar o projeto API Python

Aqui na real não é necessário baixar uma ferramenta específica para olhar código Python, poderíamos usar o Visual Studio Code que é bem simples, você pode baixá-lo no link abaixo:

[https://code.visualstudio.com/](https://code.visualstudio.com/)

Depois de instalar, você poderá abrir o Visual Studio Code e dentro dele abrir a pasta onde está o código-fonte da API Python.

A exemplo:

![Visual Studio Code](./imagens/imagem60.png "imagem60")

Selecione a pasta "pythonapi".

A exemplo:

![Visual Studio Code pasta](./imagens/imagem61.png "imagem61")

Será aberta a pasta inteira do projeto em Python, com os arquivos visíveis no menu à esquerda.

A exemplo:

![Visual Studio Code itens](./imagens/imagem62.png "imagem62")

Para ajudar, é importante instalar a extensão para Python, isso habilita o "IntelliSense" por exemplo entre outras funcionalidades que ajudarão no desenvolvimento de código Python.

A exemplo:

![Visual Studio Code extension](./imagens/imagem63.png "imagem63")

Depois de abrir a pasta do projeto e instalar a extensão (que ajudará e muito!), vamos baixar as depências do projeto, que estão descriminadas no arquivo "requirements.txt", para isto abra um terminal.

A exemplo:

![Visual Studio Code terminal](./imagens/imagem64.png "imagem64")

No terminal aberto, execute o seguinte comando:

`pip install -r requirements.txt`

A exemplo:

![Visual Studio Code terminal pip install](./imagens/imagem65.png "imagem65")

Este projeto usa o uvicorn como uma espécie de Web Server para servir a aplicação API, então será necessário instalar o uvicorn através do Terminal do Visual Studio Code.

No terminal, execute o comando à seguir:

`pip install uvicorn`

A exemplo:

![Visual Studio Code terminal pip install uvicorn](./imagens/imagem92.png "imagem92")

Pronto! Seu projeto em Python está preparado para você brincar!

Se quiser executar o projeto, no terminal digite o seguinte comando:

`.\run.sh`

Isso abrirá uma tela do Git Bash (pois tem que ser um terminal preparado para executar comandos do Linux) para executar o script do arquivo "run.sh", você pode abrir o arquivo para ver o que ele faz, basicamente ele executa o "univcorn" que é como se fosse um web server indicando para rodar localmente, além disso ele atribui a porta de comunicação 8000 para que possam ser feitas chamadas na aplicação através desta porta e indica qual módulo do projeto Python executar, no caso "app.main:app"

A exemplo:

![Visual Studio Code terminal run.sh](./imagens/imagem68.png "imagem68")

Porém se você prefere uma ferramenta mais robusta e que habilite debug entre outras funções interessantes, você poderia baixar o PyCharm versão Community que é gratuito no link abaixo:

[https://www.jetbrains.com/pycharm/download/#section=windows](https://www.jetbrains.com/pycharm/download/#section=windows)

Quando você abrir o PyCharm, você terá que abrir o projeto deste repositório, clique no botão "Open".

A exemplo:

![PyCharm](./imagens/imagem69.png "imagem69")

Selecione a pasta onde estão os arquivos do projeto em API Python.

A exemplo:

![PyCharm pasta](./imagens/imagem70.png "imagem70")

Uma vez feito isso, o PyCharm já irá abrir o projeto mostrando todos os arquivos do projeto no menu à esquerda.

A exemplo:

![PyCharm projeto](./imagens/imagem71.png "imagem71")

Bom, diferente do Visual Studio Code em que usamos um script "run.sh" no terminal para executar a aplicação, no PyCharm executaremos diretamente pela ferramenta de desenvolvimento, porém lembrem-se que estávamos usando o uvicorn como web server por conta da estrutura do código que usa FastApi como biblioteca para que a aplicação funcione como uma API.

Como estamos com um projeto feito em Python 3.6, vamos criar um ambiente com um interpretador que possui uma cópia das aplicações do Python 3.6, para isto abriremos o Prompt de Comando do Windows e rodaremos um comando para criar este ambiente.

Para abrir o Prompt de Comando do Windows, vá na barra de pesquisa do Windows e digite cmd. É só abrir o aplicativo que aparecer.

![cmd](./imagens/imagem72.png "imagem72")

Depois rodar o seguinte comando:

`python3 -m venv FastEnv`

A exemplo:

![cmd FastEnv](./imagens/imagem73.png "imagem73")

Este projeto usa o uvicorn como uma espécie de Web Server para servir a aplicação API, então será necessário instalar o uvicorn através do seguinte comando:

`pip install uvicorn`

A exemplo:

![cmd uvicorn](./imagens/imagem74.png "imagem74")
![cmd uvicorn instalado](./imagens/imagem75.png "imagem75")

Para uso do ambiente recém criado, no PyCharm clique no canto inferior direito em cima do ambiente do Python atual e depois clique no item "Add interpreter..."

A exemplo:

![PyCharm add interpreter](./imagens/imagem76.png "imagem76")

Na tela que surgir, clique na opção "Existing environment" e clique no botão com os 3 pontinhos.

A exemplo:

![PyCharm add interpreter tree dots](./imagens/imagem77.png "imagem77")

Escolha o "python.exe" da pasta do FastEnv recém criado.

A exemplo:

![PyCharm add interpreter tree dots python](./imagens/imagem78.png "imagem78")

Após selecionar, clique no botão OK.

A exemplo:

![PyCharm add interpreter OK](./imagens/imagem79.png "imagem79")

Aguarde até o ambiente ser carregado.

A exemplo:

![PyCharm add interpreter updating](./imagens/imagem80.png "imagem80")

Quando estiver tudo pronto, o novo ambiente estará selecionado, é possível ver isso no canto inferior direito do PyCharm.

A exemplo:

![PyCharm FastEnv](./imagens/imagem81.png "imagem81")

Outra coisa a ser feita é incluir uma configuração para uso do uvicorn recém instalado quando a aplicação for executada, para isto clique na configuração na parte superior ao lado do botão "play", depois clique em "Edit Configurations...".

A exemplo:

![PyCharm Configurations](./imagens/imagem82.png "imagem82")

Na tela que se abrir, clique no botão de "mais" e depois clique no item "Python".

A exemplo:

![PyCharm Configurations Python](./imagens/imagem83.png "imagem83")

Configure conforme à seguir:

A exemplo:

![PyCharm Configurations Python Add](./imagens/imagem84.png "imagem84")

Sendo:

- Name: insira um nome amigável para este tipo de configuração, no exemplo eu deixei como "uvicorn"
- Aba Configuration: mude de "Script Path:" para "Module name:" e indique à frente no campo texto o valor "uvicorn"
- Parameters: indique o valor "--reload --host 0.0.0.0 --port 8000 app.main:app"
- Python interpreter: selecione a opção do ambiente FastEnv que criamos
- Working directory: selecione a pasta completa do projeto da API Python

Antes de executar o projeto, é necessário fazer o download de todas as dependências do projeto. Para isto clique no menu "Tools" e depois no item "Sync Python Requirements..."

A exemplo:

![PyCharm Tools Requirements](./imagens/imagem85.png "imagem85")

Na tela que se seguir, mantenha os seguintes parâmetros:

- Package requirements file: mantenha o valor "requirements.txt"
- Version in requirements: mantenha selecionada a opção "Strong equality (==x.y.z)

E depois clique no botão OK.

A exemplo:

![PyCharm Tools Requirements OK](./imagens/imagem86.png "imagem86")

Na tela que surgir, serão exibidas todas as bibliotecas presentes no arquivo "requirements.txt", na parte superior direito, clique no link "install requirements".

A exemplo:

![PyCharm install requirements](./imagens/imagem87.png "imagem87")

Na tela de confirmação de todos os pacotes a serem instalados, confirme clicando no botão OK.

A exemplo:

![PyCharm install requirements OK](./imagens/imagem88.png "imagem88")

Aguarde a instalação, demora um pouco.

A exemplo:

![PyCharm install requirements updating](./imagens/imagem89.png "imagem89")

O PyCharm mostrará que a instalação de todos os pacotes foi concluída, visto no canto inferior direito. Agora podemos executar a aplicação!!! Selecione o item "uvicorn" ao lado do botão "play" e depois clique no botão "play".

A exemplo:

![PyCharm executar](./imagens/imagem90.png "imagem90")

Aparecerá o terminal, quando aparecer a mensagem "Application startup complete", a API Python estará pronta para ser utilizada.

A exemplo:

![PyCharm executar terminal](./imagens/imagem91.png "imagem91")

## Criar uma imagem do Docker

Depois que você deu uma olhada no projeto e deu uma brincada nele, é hora de criarmos uma imagem do Docker à partir desse projeto para podermos subir um container no Docker, mas antes precisamos tomar alguns cuidados:

Você deve ter notado que há um arquivo chamado "databaseurlprod.py" solto na pasta do projeto, este arquivo é diferente do "databaseurl.py" dentro da pasta "data" do projeto, esse arquivo "databaseurlprod.py" vai substituir o arquivo "databaseurl.py" na hora de montarmos nossa imagem Docker, vamos olhar ele com calma.

A exemplo:

![O arquivo databaseurl.py](./imagens/imagem93.png "imagem93")

Note que há uma linha diferente entre os arquivos:

DATABASE_URL = "mysql+mysqlconnector://MeuUsuario:MinhaSenha@localhost:3306/MeuDatabase"

Porque trocamos o "localhost" pelo "MeuMySQL"?

- Quando executamos a aplicação Python, conseguimos chamar o banco de dados apontando para o "localhost" pois quando subimos o container do MySQL indicamos uma porta de entrada onde a "escuta" se dará como "localhost" na porta 3306. Isso funciona pois para nós que estamos no computador usando o Windows, localhost é o ambiente do Windows como um todo.
- Precisamos mudar para "MeuMySQL" que no meu caso é o nome do container em que eu subi o MySQL, se você subiu o container com outro nome, utilize o nome que você indicou para o container. Pensa assim: um container tentando acessar o outro é dentro do ambiente do Docker, e não o ambiente do Windows, então para que um container enxergue o outro não dá para usar o "localhost". Ao subirmos um container para a API Python, estaremos subindo como se fosse um sistema operacional só pra ele, então "localhost" é tudo que estiver dentro do próprio container da API Python, como o MySQL está em outro container, está "fora" do "localhost" do container da API Python e é por isso que não tem como usar o "localhost" pra subir no container.

Por esta questão de um container precisar "enxergar" o outro, assim como um computador precisasse enxergar outro computador, é que indicamos no comando de criação do container o --network, é como se no final do dia você tivesse o ComputadorA com o MySQL, o ComputadorB com o Python e conectássemos ele a um roteador (nosso --network), assim um conseguirá "enxergar" e "falar" com o outro.

Veja também que temos um outro arquivo na pasta do projeto, chamado "Dockerfile", ele contém as instruções de como criar essa imagem Docker, vamos olhar com calma:

A exemplo:

![O arquivo Dockerfile](./imagens/imagem94.png "imagem94")

Vocês verão que esse arquivo tem várias instruções, vamos ver a estrutura dessas instruções:

- FROM python:3.6-slim: esta instrução diz a imagem do Docker que será baixada e utilizada para fazer a execução da aplicação. Como estamos usando um projeto Python, usamos uma imagem que tenha o Python para execução dos arquivos do projeto

- WORKDIR /code: indica a pasta principal para execução da aplicação Python, como se fosse uma pasta num ambiente Linux
- COPY ./requirements.txt /code/requirements.txt: aqui que copio o arquivo "requirements.txt" que estava fora da pasta "app", é através dele que o baixaremos as dependências do projeto

- RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt: executa a aplicação pip no ambiente do Python para instalar todas as dependências contidas no arquivo requirements.txt

- COPY ./app /code/app: o código-fonte do Python está na pasta "app", então o que é feito aqui é a cópia de tudo que está na pasta "app" pra dentro da imagem do Python (que tem um "mini sistema operacional" próprio e a aplicação do Python já pré-instalada), a cópia ficará numa estrutura de pastas do Linux chamada "/code/app"
- RUN rm -rf /code/app/data/databaseurl.py: aqui nós removemos o arquivo "databaseurl.py" que está apontando para "localhost"
- COPY ./databaseurlprod.py /code/app/data/databaseurl.py: aqui eu copio aquele "databaseurlprod.py" que está apontando para o nome do container do MySQL renomeando o arquivo para "databaseurl.py", assim eu substituo o arquivo de propriedades de conexão original

- CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]: e finalmente esta é a instrução que será executada sempre que subir um container, neste caso ele usa o módulo "uvicorn", indica que é para executar a aplicação "app,main:app", que usará o localhost como hospedagem da aplicação Python (dentro do container) e a exposição pela porta 8000, assim será possível acessar a API do seu computador pela porta 8000

Agora precisamos abrir o Terminal do Git Bash ou o Promt de Comandos do Windows e executar a seguinte instrução:

`docker build --label pythonapi --no-cache -t pythonapi:latest .`

O "docker build" é o comando utilizado para criar uma imagem do Docker à partir das instruções do arquivo Dockerfile.
Seus parâmetros são:

--label pythonapi: é uma informação que vai como metadado dentro da imagem, neste caso indica-se uma "etiqueta" chamada "pythonapi", você pode mudar esta etiqueta para o que você preferir
--no-cache: indica que não haverá uso de conteúdo em cache para montar o build, o ponto ruim é que sempre serão feitos os downloads de tudo durante o build, porém isso também força o resultado final não ter o risco de alguma versão antiga em cache
-t pythonapi:latest: é a tag referente à esta versão de imagem, então toda vez que for criado um container à partir desta imagem, é necessário indicar esta tag "pythonapi:latest", você pode mudar esta tag para o que você preferir
.: este ponto ao final indica que o conteúdo para o build está presente na pasta atual, se estivesse em outra pasta é só trocar este . pelo caminho completo da pasta onde está o Dockerfile

A exemplo:

![docker build via terminal do Visual Studio Code](./imagens/imagem95.png "imagem95")

Assim que o build é feito (às vezes demora um pouquinho dependendo do que tem que ser baixado e por conta do build e si), você verá a imagem na lista de imagens em seu Docker Desktop.

A exemplo:

![imagens do Docker](./imagens/imagem96.png "imagem96")

## Subir um container do nosso API Python

Agora é só subir um container à partir desta imagem, através do comando:

`docker run --name MeuPythonAPI --network MinhaRede -p 8000:8000 -d pythonapi:latest`

Sendo:

- --name MeuPythonAPI: é o nome/apelido do container, é importante indicar um nome amigável para gerenciar seus vários containers, você pode indicar outro nome se preferir.
- --network [nome do Docker network]: Esse parâmetro faz com que o container fique dentro de uma "subrede" dentro do Docker. Se você quiser subir esta API Python para brincar conectando diretamente a ele do seu computador, não precisa deste parâmetro, agora se você quiser acessar partindo de outros containers ou acessar outros containers (como o do MySQL), isso é necessário!
- -p 8000:8000: É a configuração da porta de entrada para comunicações com esta API Python, sem isso você não consegue conectar na aplicação através do seu computador.
- -d: Indica que o container irá subir em modo "desatachado", ou seja, sem necessidade de abrir um terminal interativo para você estar dentro do container assim que subir. Necessário para que a API Python já suba rodando em background
- pythonapi:latest: É a imagem que será usada como base para subir o container, neste caso é a imagem que acabamos de criar! Se você criou a imagem com outro nome de tag, ajuste neste parâmetro

Assim que o container subir, você o verá no Docker Desktop.

A exemplo:

![Container da API Python](./imagens/imagem97.png "imagem97")

Você pode testar essa API! Há uma ferramenta que permite isso facilmente, ainda mais pois este repositório possui um arquivo de collection com todas as requisições de API já salvas e prontas para você usar!

Primeiramente baixe a ferramenta Postman no link abaixo:

https://www.postman.com/downloads/?utm_source=postman-home

Depois de instalar, ao abrir a ferramenta você verá que poderá criar coleções ou salvar as requisições.

A exemplo:

![Postman](./imagens/imagem98.png "imagem98")

Clique no botão "Import" para subir a coleção presente no arquivo "Descomplica.postman_collection.json", presente na pasta "cicd_backend" deste repositório.

A exemplo:

![Postman Import](./imagens/imagem99.png "imagem99")

Selecione o arquivo "Descomplica.postman_collection.json".

A exemplo:

![Postman Import arquivo](./imagens/imagem100.png "imagem100")

Você verá que deu certo quando a collection aparecer na tela de importação, após esta confirmação clique no botão "Import".

A exemplo:

![Postman Import Confirmar](./imagens/imagem101.png "imagem101")

A collection aparecerá no menu à esquerda, expandindo ela você conseguirá ver todas as requisições já salvas e prontas para uso.

A exemplo:

![Postman Requests](./imagens/imagem102.png "imagem102")

Você pode clicar em qualquer uma das requisições, no exemplo aqui eu cliquei na primeira requisição que é um POST, para chamada da API Python que cadastra uma playlist nova no banco de dados MySQL.

A exemplo:

![Postman Requests POST](./imagens/imagem103.png "imagem103")

No caso do POST, você precisará incluir um conteúdo no corpo da requisição, a aba "Body" já tem um exemplo que você pode alterar. Você pode checar no código-fonte da API Python as funcionalidades que a API oferece.

A exemplo:

![Postman Requests POST body](./imagens/imagem104.png "imagem104")

Ao clicar no botão "POST" é feita uma chamada à API Python que responderá à requisição.

Pronto! Você já tem uma API no Docker chamando o banco de dados MySQL!
