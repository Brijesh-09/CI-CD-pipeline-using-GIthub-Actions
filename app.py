from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

@app.route("/")
def hello():
    #return "Flask inside Docker!!"
    return f'Hello my name is, {os.getenv("SECRET_NAME")},this is my secret number  {os.getenv("SECRET_NO")}'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
