from flask import Flask, render_template

app = Flask(__name__, template_folder="../frontend")

@app.route('/', methods=['GET', 'POST'])
def tracker():
    return render_template('tracker.html')


if __name__ == "__main__":
    app.run(debug=True)