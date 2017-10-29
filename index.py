from flask import Flask, render_template

app = Flask("MyApp")

@app.route("/") 
def main():
    return render_template('home.html')
    
app.run(debug=True)