from flask import Flask

app = Flask(__name__)

@app.route("/")
df hello():
   return "Container rodando na AWS!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=80)
