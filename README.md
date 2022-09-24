# TELEGRAM TO GOOGLE DRIVE BOT

I needed to store some files from Telegram to my google drive. I tried looking for a bot to do this, but all of them didn't work. So I decided to create my own.

This is useful if you have a server where by the bot can download large telegram files and send them to google drive without you using any bandwidth. Pretty neat.

# Setup

 - Get a [Telegram API KEY](https://my.telegram.org/apps) and a bot token from [Bot Father](https://t.me/botfather). You can get more information [here](https://docs.pyrogram.org/start/auth.html).
 - Follow this [Guide](https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf) to get a detailed explanation on how to get authentication for Google Service API.
 - On the 5th page of the guide above, you will download a json file. **Rename it to `client_secrets.json`**
 - Fill in your `client id` and `client secret` from the `client_secrets.json` file to the `settings.yaml` file.
 - Fil in your Telegram user-id on the `main.py` file. This is so the bot saves files only from you.

# How to use
Clone the repository:
```bash
git clone https://github.com/AvicennaJr/Telegram2Drive
```

Install the requirements:
```bash
cd Telegram2Drive
pip install -r requirements.txt
```

Then run the bot with:
```python
python main.py
```

Send any file to your bot and you will find it on your google drive.

**Note:** If you are using a server you can make a simple `Systemd` script to let the bot run in the background.

# License

[MIT](https://choosealicense.com/licenses/mit/)
