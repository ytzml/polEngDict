from flask import Flask, request
import boto3
import json

app = Flask(__name__)
boto3.setup_default_session(region_name='eu-central-1')

@app.route('/<word>/', methods=['POST'])
def add_word_translation(word:str):
    dynamodb_client = boto3.client("dynamodb")
    req_body = request.data.decode('utf-8')
    req_dict = json.loads(req_body)
    translation = req_dict['translation']
    example = req_dict['example']
    dynamodb_client.put_item(TableName='polEngDict', Item = {"word": {"S": word}, "translation":{"S": translation}, "example":{"S": example}})
    return "OK"

@app.route('/<word>/', methods = ['GET'])
def get_word(word:str):
    dynamodb_client = boto3.client("dynamodb")
    response = dynamodb_client.get_item(TableName="polEngDict", Key={"word": {"S": word}})
    #return response
    translation = response["Item"]["translation"]["S"]
    example = response["Item"]["example"]["S"]
    return {"translaiton": translation, "example": example}

@app.route('/', methods = ['GET'])
def status():
    return 'OK'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
