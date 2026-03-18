from flask import Flask
from model import db
from route.primedata import primedata
from controller import data_service


class Config:
   SECRET_KEY="hello"
   SQLALCHEMY_DATABASE_URI="postgresql://postgres:XXXXX@localhost:5432/bello"
   SQLALCHEMY_TRACK_MODIFICATIONS=False


def create_app():
   app=Falsk(__name__)
   app.config.from_object(Config)
   db.init_app(app)
   with app.app_context():
      db.create_all()
   app.register_blueprint(primedata)
   return app

if __name__=="__main__":
   app=create_app()
   app.run(debug=True)
   
   
