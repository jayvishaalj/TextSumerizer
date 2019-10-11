from flask import Flask
from datetime import datetime
import pickle

app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

# load model
model = pickle.load(open('Adventuretrain.pkl','rb'))


adventure ={'P001': 'Sri Chamarajendra Park',
 'P002': 'Bannerghatta Biological Park',
 'P003': 'Bugle Rock Park',
 'P004': 'Jaya Prakash Narayana Park',
 'P005': 'M.N. Krishna Rao Park',
 'P006': 'Ranadheera Kanteerava Park',
 'P007': 'Freedom Park',
 'P008': 'Butterfly Park',
 'P009': 'Cariappa Memorial Park',
 'P010': 'Jayamahal Park',
 'P011': 'Mahatma Gandhi Park',
 'P012': 'Chinnappanahalli Lake Park',
 'P013': 'Lalbagh Botanical Garden',
 'P014': 'Bangalore One HSR Park',
 'P015': 'Hanuman Park',
 'P016': 'Indira Gandhi Musical Fountain Park',
 'P017': 'Lakshmi Devi Park',
 'P018': 'Coles Park',
 'P019': 'Sir. M. Vishveshwaraiah Park',
 'P020': 'National Poet Kuvempu Park',
 'P021': 'Ulsoor Lake',
 'P022': 'Bellandur Lake',
 'P023': 'Sankey Tank',
 'P024': 'Hebbal Lake',
 'P025': 'Agara Village',
 'P026': 'Agara Lake',
 'P027': 'Hesaraghatta Lake',
 'P028': 'Puttenahalli Lake',
 'P029': 'Sarakki Lake',
 'P030': 'Vibhutipura Lake',
 'P031': 'Kanva Reservoir',
 'P084': 'Wildlife hospital',
 'P085': 'Wildlife Rescue & Rehabilitation Centre - Admin Office',
 'P086': 'Wildlife Conservation Society - India',
 'P087': 'Avian and Reptile Rehabilitation Centre',
 'P088': 'WASI',
 'P089': 'Wildlife Rescue And Rehabilitation Centre (WRRC)',
 'P090': 'Bison in Africa',
 'P091': 'Bannerghatta Safari',
 'P092': 'Wildlife Museum',
 'P093': 'Wildlife',
 'P094': 'Centre For Wildlife Studies',
 'P095': 'wildlife rescue',
 'P096': 'INDIAN WILDLIFE RESCUE TRUST',
 'P097': 'Wildlife First',
 'P098': 'Wildlife Conservation & You',
 'P099': 'World Wildlife Trust',
 'P100': 'Wildlife Rescue & Rehabilitation Centre',
 'P101': 'Nature Conservation Foundation, South Bangalore Branch',
 'P102': 'Vanamitra',
 'P103': 'Wonderla Bangalore',
 'P104': 'Fun World Amusement Park',
 'P105': 'Innovative Film City',
 'P106': 'Snow City',
 'P107': 'Lumbini Gardens',
 'P108': 'Water World',
 'P109': 'Jawahar Bal Bhavan',
 'P110': 'Greenland Amusements',
 'P111': 'Children Amusement Park',
 'P112': 'Krishna Leela Theme Park (ISKCON)',
 'P113': 'DeRoots Kids Amusement Park Bangalore',
 'P114': 'Janatha Bazaar Park',
 'P115': 'Lalbagh Lake',
 'P116': 'Sky Zone Bengaluru',
 'P117': 'cylone ride water world',
 'P118': 'The Ritz-Carlton, Bangalore',
 'P159': 'The Pride Hotel',
 'P160': 'Radisson Blu Atria Bengaluru',
 'P161': 'JW Marriott Hotel Bengaluru',
 'P162': 'Hotel Chalukya Bangalore',
 'P163': 'ITC Gardenia, A Luxury Collection Hotel, Bengaluru',
 'P164': 'Shangri-La Hotel, Bengaluru',
 'P165': 'The Leela Palace',
 'P166': 'Hotel Bangalore Gate',
 'P167': 'ITC Windsor, A Luxury Collection Hotel, Bengaluru',
 'P168': 'The LaLiT Ashok Bangalore',
 'P169': 'Sheraton Grand Bangalore Hotel at Brigade Gateway',
 'P170': 'Hotel Royal Orchid Regenta Bangalore',
 'P171': 'Holiday Inn Express & Suites Bengaluru Racecourse',
 'P172': 'The Rialto Hotel',
 'P173': 'Le Meridien Bangalore',
 'P174': 'Bengaluru Marriott Hotel Whitefield',
 'P175': 'Hilton Bangalore Embassy GolfLinks',
 'P176': 'The Chancery Hotel',
 'P177': 'Royal Orchid Central Bangalore',
 'P178': 'Oota Bangalore',
 'P179': 'Edo | Japanese Restaurant and Bar',
 'P180': 'Flechazo | Whitefield',
 'P181': 'JW Kitchen',
 'P182': 'Rim Naam',
 'P183': 'Raj Pavilion',
 'P184': 'Karavalli',
 'P185': 'Sattvam Restaurant',
 'P186': 'Citrus',
 'P187': 'Persian Terrace at Sheraton Grand Bangalore Hotel at Brigade Gateway',
 'P188': 'Jamavar',
 'P189': 'The Cubbon Pavilion',
 'P190': 'The Black Pearl',
 'P191': "The Fisherman's Wharf",
 'P192': 'La Brasserie Restaurant',
 'P193': 'Chianti, Indiranagar',
 'P194': 'Truffles',
 'P195': 'Yauatcha Bengaluru',
 'P196': 'Carrots Restaurant',
 'P197': 'Alto Vino',
 'P198': 'Gilly�s Resto Bar, Bangalore',
 'P199': 'Skyye',
 'P200': 'Monkey Bar',
 'P201': 'The 13th Floor',
 'P202': 'Toit Brewpub',
 'P203': 'High Ultra Lounge',
 'P204': 'I Bar',
 'P205': 'Church Street Social',
 'P206': 'The Black Rabbit',
 'P207': 'Prost',
 'P208': "Watson's",
 'P209': 'Windmills Craftworks',
 'P210': 'Bootlegger',
 'P211': 'Hakuna Matata',
 'P212': 'Arbor Brewing Company - Brewpub & Eatery',
 'P213': 'Loft 38',
 'P214': 'The Biere Club',
 'P215': 'Sotally Tober - Koramangala',
 'P216': 'Liquid Bar, Hyatt Centric MG Road Bangalore',
 'P217': 'Deja Vu Restaurant and Bar'}

@app.route('/api/getAdventurePlaces', methods=['POST'])
def hello():
    req = request.get_json()
    userId = req['userId']
    userType = req['userType']
    print('User Id  =  '+userId +'   User Type =  ' + userType )
    result=[]
    for key in adventure :
        result.append((model.predict(int(userId),key)).est)
    print(result[0])
    diction = {}
    i=0
    for key in adventure:
        diction[key]=result[i]
        i=i+1
    sorted(diction.values())
    i=0
    finalLocation = []
    for key in diction :
        if(i<5):
            finalLocation.append(adventure[key])
            i=i+1
        else:
            break

    locations = {
        'locations' : finalLocation,
    }
    return jsonify({'places': locations})



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

