# Discord Bot
## Como funciona o bot
- Basicamente usando google cloud eu criei uma vm(virtual machine), usando recurso compute engine. Com isso eu criei uma vm ubuntu 18.04LTS e dentro da vm eu clonei o repositório do projeto, instalei dependencias para criar um abiente virtual do python, configurei uma rotina no crontab para executar comandos bash no arquivo runscript.sh

## virtualenv
- virtualenv é basicamente para você poder rodar seu python e dependencias de forma isolada, assim se corromper ou algo assim não tem problema, pois está apenas no ambiente.

### Como criar um virtualenv?

- Install **pip** first

    sudo apt-get install python3-pip

- Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

- Now create a virtual environment 

    virtualenv venv 

>you can use any name insted of **venv**

- You can also use a Python interpreter of your choice

    virtualenv -p /usr/bin/python2.7 venv
  
- Active your virtual environment:    
    
    source venv/bin/activate
    

- To deactivate:

    deactivate

- Create virtualenv using Python3
    virtualenv -p python3 myenv

- Instead of using virtualenv you can use this command in Python3
    python3 -m venv myenv 

## Rotina
- Para que o bot possa executar todo dia no mesmo horário foi usado uma ferramenta do próprio SO chamado crontab que executa um script a momento predefinido.
- Para determinar o momento foi usado um site que nos auxilia, o "https://crontab.guru/"
- crontab funcionar basta editar o arquivo usando comando "$ crontab -e", com isso adicionamos uma linha informando o periodo e comando, no nosso caso será o nosso arquivo bash, ou seja "*/01 * * * * bash /home/dininhociano/twitter_bot/runscript.sh"
- Temos sempre que lembrar que no crontab temos que adicionar os diretórios completos paras os arquivos

## Dependences
 - Tweepy
 - python-dotenv