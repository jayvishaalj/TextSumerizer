from flask import Flask
from flask import request
from docx import Document


app = Flask(__name__)

@app.route('/')
def display():
    return 'Hello World<>'

# @app.route('/api/summarize', methods=['POST']) 
# def json_example():
#     result_data =  ""
#     req_data = request.get_json()
#     file_location = req_data['file']
#     print(" FILE LOCATION : " + file_location)
#     document = Document(file_location)
#     for paragraph in document.paragraphs :
#         for run in paragraph.runs:
#             if run.bold:
#                 result_data = result_data + '\n' + paragraph.text
#                 break
            
#     print(result_data)
#     return result_data

if __name__ == '__main__':
    app.run() 