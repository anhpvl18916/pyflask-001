from flask import  (
    Flask,
    render_template,
    request
)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import math

app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

@app.route('/')
def  index():
    return "<h1> Flask DB 001 - Connecting !!! </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")

@app.route('/params', methods=['GET'])
def api_filter():
    query_parameters = request.args
    return jsonify(query_parameters)
@app.route('/giaiptb1', methods=['GET'])
def giaiptb1():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")

    a = int(a)
    b = int(b)

    str = "khong co nghiem"
    
    kq = { "tt" : str }

    if a == 0 and b == 0:
        str = "VSN"
        kq = { "tt" : str }
    elif a != 0:
        x =  -b/a
        str = "co 1 nghiem"
        kq = { "tt" : str , "x" : x}
    else:
        str = "KoCoN"
        kq = { "tt" : str }
    return jsonify(kq)
@app.route('/giaiptb2', methods=['GET'])
def giaiptb2():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")

    a = int(a)
    b = int(b)
    c = int(c)

    str = "khong co nghiem"
    
    kq = { "tt" : str }
   
    if(a==0):
        if(b==0):
            if(c==0):
                str = "Vo So NG"
                kq = { "tt" : str }
            else:
                str = "VN"
                kq = { "tt" : str }
        elif(c!=0):
            x = (-c)/b
            str = "co 1 nghiem"
            kq = { "tt" : str, "x" : x }
    else:
        Delta = (b*b - 4*a*c)
        if(Delta <0):
            str = "VN"
            kq = { "tt" : str }
        elif(Delta ==0):
            x = (-b)/(2*a)
            str = "co nghiem kep"
            kq = { "tt" : str, "x" : x }
        elif(Delta >0):
            x =(-b + math.sqrt(Delta))/(2*a) 
            y =(-b - math.sqrt(Delta))/(2*a) 
            str = "co 2 nghiem"
            kq = { "tt" : str, "x1" : x, "x2":y}
    return jsonify(kq)
@app.route('/loaiTamGiac', methods=['GET'])
def loaiTamGiac():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")

    a = int(a)
    b = int(b)
    c = int(c)

    str = "Day là Tam giac"
    
    kq = { "tt" : str }
    if (a+b)>c and (a+c)>b and (b+c)>a:
        if a==b or b==c or a==c :
            str = "Day la Tam giac CAN"
            kq = { "tt" : str }
            if a==b==c :
                str = "Day là Tam giac DEU"
                kq = { "tt" : str }
        elif a*a == (b*b + c*c) or b*b==(a*a+c*c) or c*c ==(a*a+b*b):
            str ="Day là Tam giac VUONG"
            kq = { "tt" : str }
        else :
            str = "Day là Tam giac THUONG"
            kq = { "tt" : str }
      else:
        str ="Day la khong phai la Tam giac"
        kq = { "tt" : str }
      return jsonify(kq)

class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam

api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1
