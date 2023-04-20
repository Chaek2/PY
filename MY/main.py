import BD as bd
from flask import Flask,request
from flask_restful import Api, Resource,reqparse

app = Flask(__name__)
api = Api()

class Main(Resource):
    def get(self,id):
        return bd.Sel_Post(id),200
    def delete(self,id):
        return 200
    def post(self,id):
        args = request.args
        title = args['title']  
        print(title)
        return bd.Ins_Post(title), 201
    def put(self,id):
        return 200

api.add_resource(Main,"/api/main/<int:id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True,port=3000,host="127.0.0.1")