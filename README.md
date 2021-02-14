<h1 align="center"><b>Sara Telegram Bot</b></h1>
<h4 align="center">A Powerful, Smart And Simple Bot By Akku</h4>







# Support




# Deploying To Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AkkuPY/Sara-Bot)




# Self-hosting (For Devs)

## Simply clone the repository and run the main file:
```sh
# Install Git First // (Else You Can Download And Upload to Your Local Server)
$ git clone https://github.com/AkkuPY/Sara-Bot
# Open Git Cloned File
$ cd Sara-Bot
# Config Virtual Env (Skip is already Done.)
$ virtualenv -p /usr/bin/python3 venv
$ . ./venv/bin/activate
# Install All Requirements 
$ pip(3) install -r requirements.txt
# Create credentials.py with variables as given below
# Start Bot 
$ python(3) -m app
```

# Mandatory Configs
```
[+] If You Running Sara On A Deploy Services With Config Env Support Like Heroku, Zeet.co, Please Set "ENV" To True , Else For Self Host Services Like Digital Ocean Just Make A Local Config And Put Vars Given Below.
    [-] bt_token:   Telegram Bot Token 
    [-] bot_user_name :   Telegram Bot UserName
    [-] URL : For WebHook(https://<app-name>.herokuapp.com/)
 
[+] The Sara will not work without setting the mandatory vars.
```


## An Example Of "credentials.py" File
```
import os

bot_token = "sd78g6add897s8d7f875adad768d"
bot_user_name = "akkubot"
URL = "https://akkubot45646.herokuapp.com"
```



 
