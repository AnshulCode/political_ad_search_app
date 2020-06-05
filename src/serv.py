from flask import Flask,request
import crud_functs

serv = Flask(__name__)




@serv.route('/',methods=['POST','GET','PUT','DELETE'])
def entry():
    req = {}
    if request.method == 'POST':
        req = request.json
        crud_functs.create(req["message"])
        return req
    if request.method == 'GET':
        req = request.json
        if req == None:
            return "null"
        ret = crud_functs.find(req["message"])
        return ret
    if request.method == 'PUT':
        req = request.json
        update = crud_functs.update(req["_id"],req["message"])
        return update
    if request.method == 'DELETE':
        req = request.json
        crud_functs.delete(req["message"])
        return req
    return req

if __name__ == '__main__':
  serv.run(host = '127.0.0.1', port = 1500)