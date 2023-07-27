from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from load import ImageAnalysis, userAnalysis
import json
from PIL import Image
import base64
import io
import os
import shutil
import time

app = Flask(__name__)
#api = Api(app)
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

@app.route('/api', methods=['POST', 'GET'])
def api():
    data = request.get_json()
    returnValue = "2"
    #directory = os.path.join(os.getcwd(), '/Content/analyze/picture.jpg')
    if data:
        try:
            result = data['data']
            b = bytes(result, 'utf-8')
            image = b[b.find(b'/9'):]
            im = Image.open(io.BytesIO(base64.b64decode(image)))
            im.save('./Content/analyze/userImage.jpg')
            
            if (userAnalysis.analyzeImage() == 0):
                returnValue = "0"
            elif (userAnalysis.analyzeImage() == 1): 
                returnValue = "1"
        except:
            pass        
    return returnValue
    
#def main():
    #return("helloworld")

#class HelloWorld(Resource):
    #def get(self, name):
        #return {"name": name}


#api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == ("__main__"):
    app.run(port=5000)
