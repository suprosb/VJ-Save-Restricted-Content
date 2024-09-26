import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN","7885103214:AAEd-Q-gBYDvE1NpXuszuTlprRqomPAtCYc")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID","22920744"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "31cb93c017f265e4fa6d0ba91236b826")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://starastar230:<password>@cluster0.5mhoa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
