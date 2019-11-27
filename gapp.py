from flask import Flask, request
import os, sys, io, subprocess
from google.cloud import texttospeech
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from cStringIO import StringIO

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Gapp!'

@app.route('/generate', methods=['POST']) 
def generate():
    if not request.json:
        abort(400)

    #os.chmod("/var/www/html/gapp/mycreds.txt", 777) 
    #os.chmod("/var/www/html/gapp/", 777)       

    result = "SUCCESS"

    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("/var/www/html/gapp/mycreds.txt")
    if gauth.credentials is None:
        print ("NEED FIRST OAUTH LOGIN CODE - gauth.CommandLineAuth()")
        result = "NEED FIRST OAUTH LOGIN CODE - gauth.CommandLineAuth()"
        #gauth.CommandLineAuth()
        #gauth.SaveCredentialsFile("/var/www/html/gapp/mycreds.txt")
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    
    drive = GoogleDrive(gauth)

    for item in request.get_json():
       res = subprocess.check_output(['python', '/var/www/html/gapp/generate.py',item['cell'], item['name']])
       file = drive.CreateFile({'title': item['name']})
       file.content = StringIO(res)
       file.Upload()


    #res = subprocess.call(['python', '/var/www/html/gapp/generate.py', request.get_json()[0]['cell'], request.get_json()[0]['name']])
    
    
    return result#str(res) #request.get_json()['cell'] #'{"success":"true '+request.get_json()['name']+'"}'

if __name__ == '__main__':
  app.run()

