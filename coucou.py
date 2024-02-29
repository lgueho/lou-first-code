from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def send_root():
    return send_file("./index.html")

@app.route('/level1')
def send_level1():
    return send_file("./level1.html")

if __name__ =="__main__":
    app.run()
