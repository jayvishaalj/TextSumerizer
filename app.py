from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)
    
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
    app.run(debug=True, use_reloader=True)

