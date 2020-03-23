# Discord Bot

## Rotina
- Para que o bot possa executar todo dia no mesmo horário foi usado uma ferramenta do próprio SO chamado crontab que executa um script a momento predefinido.
- Para determinar o momento foi usado um site que nos auxilia, o "https://crontab.guru/"
- crontab funcionar basta editar o arquivo usando comando "$ crontab -e", com isso adicionamos uma linha informando o periodo e comando, no nosso caso será o nosso arquivo bash, ou seja "*/01 * * * * bash /home/dininhociano/twitter_bot/runscript.sh"
- Temos sempre que lembrar que no crontab temos que adicionar os diretórios completos paras os arquivos

## Dependences
 - Tweepy
 - python-dotenv