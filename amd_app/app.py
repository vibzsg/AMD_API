from flask import Flask,request,Response,make_response,jsonify
import requests

app = Flask(__name__)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return http 500 status code"""
    return make_response(jsonify({'error' : 'Internal Server Error'}),500)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return http 404 status code"""
    return make_response(jsonify({'error' : 'The requested URL was not found on the server'}),404)

@app.route('/executeshellscript')
def callshellscript():
    try:
        data = request.get_json()
        print(data)

        responce = requests.get(url= "http://127.0.0.1:5500/index-shellscript", params=data )
        print(responce.json())
        return Response(status=200)
    except Exception as e:
        return e




@app.route('/listfolderstructure')
def listfolder():

    responce = requests.get(url="http://127.0.0.1:5500/index-listfolder")
    print(responce.json())

    return responce.json()



@app.route('/getresult')
def res():

    responce = requests.get(url="http://127.0.0.1:5500/index-results")


    return responce.json()


app.run(host='0.0.0.0',port=4000)