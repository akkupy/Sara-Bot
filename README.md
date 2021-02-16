<p align="center"><a href="https://t.me/Akku_Legend"><img src="https://github.com/AkkuPY/Sara-Bot/blob/main/Assets/Sara_Bot.jpg" width="5000"></a></p> 
<h1 align="center"><b>SARA-BOT  🇮🇳 </b></h1>
<h4 align="center">A Powerful, Smart And Simple Telegram Bot By Akku</h4>




# KeyFeatures

* Wiki Searching
* YT Mp3 Converter
* Multiple Client Support.
* Smart & Powerful Tools.
* Customizable.
* Much Cleaner And Stable.
* Daily Maintained.







# Deploying To Heroku

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AkkuPY/Sara-Bot)

# Steps To Follow On Heroku

 * Click Deploy To Heroku
 * Fill up the App name
 * Create a Bot with Botfather on telegram(https://t.me/BotFather)
 * Retreive The Api ID and Bot User Name From BotFather
 * Config vars(refer [mandatory configs](https://github.com/AkkuPY/Sara-Bot#mandatory-configs)) Based On this Data
 * Deploy
 * Run https://app-name.herokuapp.com/set_webhook on a browser tab (change app-name to the name of heroku app)
 * If it shows webhook setup ok ! You are good to Go... Else Try Refreshing after 10 sec+
 * Check if your telegram bot works!


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
[+] If You Running Sara On A Deploy Services With Config Env Support Like Heroku, Zeet.co, Please Set "ENV" To True , Else For Self Host Services Like Digital Ocean Just Make A Credentials File And Put Vars Given Below.
    [-] bt_token:   Telegram Bot Token 
    [-] bot_user_name :   Telegram Bot UserName
    [-] URL : For WebHook(https://<app-name>.herokuapp.com/)
 
[+] The Sara will not work without setting the mandatory vars.
```


## An Example Of "credentials.py" File
```

bot_token = "sd78g6add897s8d7f875adad768d"
bot_user_name = "akkubot"
URL = "https://akkubot45646.herokuapp.com"
```


# Contact Me
 [![telegram](https://img.shields.io/badge/Akku-000000?style=for-the-badge&logo=telegram)](https://t.me/Akku_Legend)


# License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

SaraBot is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

 
