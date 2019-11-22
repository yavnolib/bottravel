import os, dotenv
dotenv.load_dotenv()
token = os.environ['TOKEN']
print(token)