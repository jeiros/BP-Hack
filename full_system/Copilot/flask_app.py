from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def run():
    return render_template('playmp3.xml')


if __name__ == "__main__":
    app.run(debug=True, host='localhost')
