from flask import Flask, request, redirect, render_template, flash, session
app = Flask(__name__)
app.secret_key = "penguin"
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/result', methods=['POST'])
def results():
    print "Got Info"
    if len(request.form['firstname']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    else:
        session['name'] = request.form['firstname']
    
    if len(request.form['location']) < 1:
        flash("you must select a location")
        return redirect('/')
    else:
        session['location'] = request.form['location']
    
    if len(request.form['language']) < 1:
        flash("Theres gotta be some language you like")
        return redirect('/')
    else:
        session['language'] = request.form['language']

    if len(request.form['comments']) < 1 or len(request.form['comments']) > 120:
        flash("Your comments field cannot be empty and cannot exceed 120 characters")
        return redirect('/')
    else:
        session['comments'] = request.form['comments']
    
    return render_template('results.html')
    

app.run(debug=True)