from flask import Flask, render_template
from flask_socketio import SocketIO, send 

app = Flask(__name__) 
app.config["SECRET"] = "asdkkasjdjwej8oifefAaS44"
app.config["DEBUG"] = True
soketio = SocketIO(app, cors_allowed_origins="*")

@soketio.on("message")
def gerenciar_mensagem(mensagem):
    print(f"Mensagem: {mensagem}")
    send(mensagem, broadcast =True)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    soketio.run(app, host='localhost')
