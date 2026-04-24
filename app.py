from flask import Flask

app = Flask(_name_)

@app.route('7')
def home():
    return "Hello, DevOps World! V1"


if __name__ == '_main_':
    app.run(host='0.0.0.0' , port=5000)