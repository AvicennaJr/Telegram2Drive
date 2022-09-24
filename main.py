from pyrogram import Client, filters
from pyrogram.types import Message
from utils import upload_to_my_drive

app = Client("mybot", api_id, api_hash, bot_token)

MY_USER_ID = Your-telegram-user-id


@app.on_message(filters.document & filters.user(MY_USER_ID))
def document_downloader(client: Client, message: Message):

    FILE_NAME = message.document.file_name

    message.download(f"{FILE_NAME}")
    upload_to_my_drive(f"downloads/{FILE_NAME}")

    message.reply("Uploaded Successfully")


@app.on_message(filters.video & filters.user(MY_USER_ID))
def video_downloader(client: Client, message: Message):

    FILE_NAME = "Video-" + message.video.file_unique_id

    message.download(f"{FILE_NAME}")
    upload_to_my_drive(f"downloads/{FILE_NAME}")

    message.reply("Uploaded Successfully")


@app.on_message(filters.photo & filters.user(MY_USER_ID))
def photo_downloader(client: Client, message: Message):

    FILE_NAME = "Image-" + message.photo.file_unique_id

    message.download(f"{FILE_NAME}")
    upload_to_my_drive(f"downloads/{FILE_NAME}")

    message.reply("Uploaded Successfully")


@app.on_message(filters.audio & filters.user(MY_USER_ID))
def audio_downloader(client: Client, message: Message):

    FILE_NAME = message.audio.title

    message.download(f"{FILE_NAME}")
    upload_to_my_drive(f"downloads/{FILE_NAME}")

    message.reply("Uploaded Successfully")


app.run()
