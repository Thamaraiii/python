from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
API_KEY=os.getenv("API_KEY")

print(f'SECRETKEY:{SECRET_KEY}')
print(f'API_KEY:{API_KEY}')
