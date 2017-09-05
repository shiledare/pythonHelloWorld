from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
	return "Hello World!"

@app.route("/About")
def about():	
	return "My name is Damilare" 

@app.route("/Contact")
def contact():
	return "07038706480" 
	
if __name__ == "__main__":
    app.run()

#print ("Hello World!")    