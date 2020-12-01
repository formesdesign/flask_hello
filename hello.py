from flask import Flask

app = Flask(__name__) #creen l'aplicació en el nom del fixer

#s'han de crear els punts d'entrada  (son les rutes)
@app.route("/hello") #es el nom d'arxiu @app.route es el decorador, 
#el route agara al hello_world, xq se comunique en el servidor
def hello_world():
    return "Hola, món"