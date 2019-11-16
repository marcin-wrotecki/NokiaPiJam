from flask import Flask, render_template, request

app = Flask(__name__)


name = ""

@app.route('/')
def index():
    return render_template('index.html')

# implement endpoint for handling POST request from script for face recognition, save name from request
@app.route('/',methods=['POST'])
def parse_request():
    request.get_data()
    global name
    name=request.data
    print(name)
    return ""
# implement endpoint for handling get request from frontend and return saved earlier name

@app.route('/landing',methods=['GET'])
def landing():
    global name
    print(name)
    return name
# implement endpoint for handling get request from frontend and return saved earlier name

if __name__ == '__main__':
    app.run(debug=True)
