from flask import Flask, render_template, redirect, url_for, request
import wed

app = Flask(__name__, template_folder='template')


@app.route("/")
def home():
    return(render_template("home.html"))


@app.route("/form", methods=["POST", "GET"])
def form():
    return(render_template("form.html"))


@app.route("/about", methods=["POST", "GET"])
def about():
    return(render_template("about.html"))

# @app.route("/success")
# def success(data):
#	return(render_template("success.html",data=data))


@app.route("/weather", methods=["GET", "POST"])
def weather():
    if(request.method == "POST"):
        city = request.form["nm"]
        app1 = wed.wea(str(city))
        data = app1.find_data()
        return render_template("success.html", data=data)
        
if __name__ == "__main__":
    app.run(debug=True)

"""app1=wea(str(city))
		data = app1.find_data()
	return render_template("success.html",data=data)"""
