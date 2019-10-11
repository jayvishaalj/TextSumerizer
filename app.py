from flask import Flask ,jsonify,request
app = Flask(__name__)

@app.route('/api/getAdventurePlaces', methods=['POST'])
def hello():
    req = request.get_json()
    userId = req['userId']
    userType = req['userType']
    print('User Id  =  '+userId +'   User Type =  ' + userType )
    result=[]
    
    places = [
	    {   
		    'locationNames': ['Place1','Place2','Place3'],
            'locationDescription' : ['Description1','Description2','Description3']		
	    }
    ]
    return jsonify({'places': places})


	


if __name__ == '__main__':
    app.run()
