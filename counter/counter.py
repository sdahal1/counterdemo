from flask import Flask, render_template, session, redirect, request 
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def home():
    if 'visitcount' not in session:
        session['visitcount'] = 1
    else:
        session['visitcount'] += 1
    return render_template("counter.html")

@app.route("/plus2")
def plustwo():
    session['visitcount'] +=1 
    return redirect("/")

@app.route("/custom", methods=['POST'])
def custom():
    print(request.form)
    print(request.form['howmuch'])
    session['visitcount'] += int(request.form['howmuch']) -1
    return redirect("/")
@app.route("/destroy_session")
def destroysession():
    session.clear()
    return redirect("/")
if __name__ == '__main__':
    app.run(debug = True)