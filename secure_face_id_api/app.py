#curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/syoon/Desktop/<img.jpg>" http://localhost:5000/file-upload
from flask import Flask

UPLOAD_FOLDER = './images'

app = Flask(__name__)
app.secret_key = "here"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
         
if __name__ == "__main__":
    app.run()
