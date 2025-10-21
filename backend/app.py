from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/weather')
def get_weather ():
    return jsonify({"message": "Hello from Weather App!"})

if __name__=="__main__":
    app.run(host="0.0.0.0" , port=5000)