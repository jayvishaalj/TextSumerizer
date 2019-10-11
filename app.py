from flask import Flask ,jsonify,request
app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/api/getAdventurePlaces', methods=['POST'])
def hello():
    req = request.get_json()
    userId = req['userId']
    userType = req['userType']
    print('User Id  =  '+userId +'   User Type =  ' + userType )
    result=[]
    
    places = [
	    {   
		    'locationNames': ['Place1','Place2','Place3']
		
	    }
    ]
    return jsonify({'places': places})


	


if __name__ == '__main__':
    app.run()
