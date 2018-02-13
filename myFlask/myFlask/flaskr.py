import os
import mysql
from flask import Flask, request, session, g, redirect, url_for, aborrender_template, flash

app = Flask(__name__) #create the application instance
app.config.from_object(__name__) #load config from this file, flask

#Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flasker.db'), #/User/.../MyTest/MyTest/flasker.db
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='defalut'
))

#config값을 외부에서 가져올려면 아래처럼...
app.config.from_envvar('FLASKR_SETTINGS', silent=True) #FLASKR_SETTINGS라는 환경변수의 경로에 있는 파일 값가져옴. silent=True는 환경변수 없어도 오류안나게
#FLASKR_SETTINGS=/Users/outsider/flaskr/config.cfg 하고 config.cfg파일에 설정값 넣으면됨
#json 설정파일 사용시는 app.config.from_json(os.environ['FLASKR_SETTINGS'], silent=True)

def connect_db():
    rv = mysql.connet(app.config['DATABASE'])
    rv.row_factory
    return rv