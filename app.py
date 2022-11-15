from flask import Flask,make_response
from mongoengine import connect
from datetime import timedelta
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from module.respons_str import respons_str



from router.identity import user
from router.upload_files import upload_file

db_connection=connect('archive_zng')
app = Flask(__name__)



jwt=JWTManager(app)
app.config["JWT_SECRET_KEY"] = "@PZ-#22"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=8)
app.config['MONGO_DBNAME'] = 'archive_zng'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/archive_zng'
app.config['AllOWED_EXTENSIONS_PDF'] = []
app.config['AllOWED_EXTENSIONS_FILE'] = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'svg', 'webp', 'ico','pdf','docx','doc','xlsx','xls','pptx','ppt','txt','rar','tar','zip','JPG']
app.config['AllOWED_EXTENSIONS_DOC'] = []
app.config['AllOWED_EXTENSIONS_ZIP'] = []



mongo=PyMongo(app)

app.register_blueprint(user)
app.register_blueprint(upload_file)



@app.route('/api/connection')
def root():
    return make_response(respons_str('connect', None), 200)




if __name__ == '__main__':
   # app.run(debug=True,port=3000)
    app.run(debug=True,host='0.0.0.0',port=3000)

