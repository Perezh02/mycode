from flask import Flask, redirect, request, render_template

app = Flask(__name__)

# Landing page with trivia question form
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route to handle form submission
@app.route("/", methods=["POST"])
def check_answer():
    answer = request.form.get("answer")
    if answer == "42":
        return redirect("/correct")
    else:
        return render_template("index.html", incorrect=True)

# Route for correct answer
@app.route("/correct")
def correct():
    return "Congratulations! You answered correctly!"

if __name__ == "__main__":
    app.run(debug=True)
