from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
from pymongo import MongoClient
import database as dbase
from docs import User

db=dbase.dbConnection()

app=Flask(__name__)



#rutas de la aplicacion
#Metodo GET
@app.route('/users', methods=['GET'])
def index():
    users=db['users']
    usersReceived=users.find()
    return render_template('index.html', users=usersReceived)





#Metodo POST
@app.route('/users', methods=['POST','PUT'])
def addUser():
    #recibiendo datos
    users=db['users']
    name=request.form['name']
    password=request.form['password']
    number=request.form['number']

    if name and password and number:
        user=User(name, password, number)
        users.insert_one(user.toDBCollection())
        response = jsonify({
             'name':name,
             'password':password,
             'number':number
        })
        return redirect(url_for('index'))
    else:
        return notFound()
     




#Metodo Delete
@app.route('/delete/<string:user_name>', methods=['DELETE'])
def delete(user_name):
    users=db['users']
    users.delete_one({'name':user_name})
    return redirect(url_for('index'))





#Metodo PUT
@app.route('/edit/<string:user_name>', methods=['POST', 'PUT'])
def edit(user_name):
    #recibiendo datos
     users=db['users']
     name=request.form['name']
     password=request.form['password']
     number=request.form['number']

     if name and password and number:
         users.update_one({'name':user_name},
                          {'$set':{'name':name, 
                           'password':password, 
                           'number':number}
                           })
         response=jsonify({'message':'Usuario'+ user_name + 'actualizado correctamente'})
         return redirect(url_for('index'))
     else:
         return notFound()
     






@app.errorhandler(404)
def notFound(error=None):
    message={
        'message':'No encontrado'+ request.url,
        'status':'404 Not Found'
    }
    response=jsonify(message)
    response.status_code=404
    return response

     

if __name__=="__main__":
    app.run(debug=True, port=4000)