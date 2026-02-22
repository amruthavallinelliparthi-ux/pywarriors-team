from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    try:
        with open("data.txt", "r") as file:
            content = file.read()
    except:
        content = "No records yet."
    return render_template("index.html", data=content)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]

    with open("data.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}\n")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)