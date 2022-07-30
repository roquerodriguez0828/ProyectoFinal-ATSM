from flask import Flask,request,jsonify
import extractiveSummary as ext
import Summarizer as summ

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def test():
	if request.method == "GET":
		return jsonify({"response":"Bienvenido a ATSM"})
	elif request.method == "POST":
		req_Json = request.json
		text = req_Json['text']
		lang = req_Json['lang']
		max_length = 150
		min_length = 50
		summary = summ.summarize(lang,text,max_length,min_length)
		return jsonify({"response":summary})

if __name__ == '__main__':
	app.run(debug=True)


#print(summ.summarize('ENG',text_example,20,15))