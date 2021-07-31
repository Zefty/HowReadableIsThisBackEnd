from flask import Flask, json, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET'])
def bert():
  uri = "http://d449ac5c-5942-4da0-a42b-41e46814b152.australiaeast.azurecontainer.io/score"
  headers = {"Content-Type": "application/json"}
  if request.method == 'GET':
    data = {
        "data": "My hope lay in Jack's promise that he would keep a bright light burning in the upper story to guide me on my course.",
    }
  if request.method == 'POST':
    print(request.json)
    data = json.loads(request.json)
  data = json.dumps(data)
  response = requests.post(uri, data = data, headers = headers)
  return json.dumps(response.json())

if __name__ == '__main__':
  app.run() 