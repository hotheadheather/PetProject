from flask import Flask,render_template,request,redirect
from models import db,donationModel

 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petprojectdonations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':

        date = request.form['date']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        gender = request.form['gender']
        foodtype = request.form['foodtype']
        amount = request.form['amount']
        weight = request.form['weight']
       
       
        donations = donationModel(
            date=date,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender, 
            foodtype=foodtype,
            amount=amount,
            weight=weight
          
           
        )
        db.session.add(donations)
        db.session.commit()
        return redirect('/')
 
 
@app.route('/')
def RetrieveList():
    donations = donationModel.query.all()
    return render_template('datalist.html',donations = donations)
 
 
@app.route('/<int:id>')
def Retrievedonation(id):
    donations = donationModel.query.filter_by(id=id).first()
    if donations:
        return render_template('data.html', donations = donations)
    return f"Employee with id ={id} Doenst exist"
 
 
@app.route('/<int:id>/edit',methods = ['GET','POST'])
def update(id):
    donation = donationModel.query.filter_by(id=id).first()

  
    if request.method == 'POST':
        if donation:
            db.session.delete(donation)
            db.session.commit()
  
        date = request.form['date']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        gender = request.form['gender']     
        amount = request.form['amount']
        weight = request.form['weight']
        foodtype = request.form ['foodtype']  
    
    

        donation = donationModel(
            date=date,
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,           
            amount=amount,
            weight=weight,
            foodtype=foodtype
         
     
        )
        db.session.add(donation)
        db.session.commit()
        return redirect('/')
        return f"donation with id = {id} Doesnt exist"
 
    return render_template('update.html', donation = donation)
 
 
@app.route('/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    donations = donationModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if donations:
            db.session.delete(donations)
            db.session.commit()
            return redirect('/')
        abort(404)
     #return redirect('/')
    return render_template('delete.html')



 
app.run(host='localhost', port=5000)