import sqlite3
from xml.dom.minidom import CharacterData
from flask import Flask, redirect, render_template,request
app= Flask(_name_)

digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

character = ['@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

@app.route("/")
def index():
    """Show portfolio of stocks"""
    return render_template("index.html")


@app.route('/login' , methods=['GET','POST'])

def login():
   if request.method=='POST':

       connection = sqlite3.connect("user.db")
       cursor = connection.cursor()

       name=request.form("username")

       password=request.form("password")

       query ="SELECT * FROM users WHERE (Name,Password)  VALUES(?,?)", (name, password)

       cursor.execute(query)

       result = cursor.fetchall()

       if len(result)==0:
            print("somthing went wrong")

       else:
            return render_template('/')

   else:
          return redirect('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "GET":

        # Ensure username was submitted
        return render_template("register.html")

    else:
         connection = sqlite3.connect("user.db")
         cursor = connection.cursor()

         username= request.form.get("username")
         password= request.form.get("password")
         reenter = request.form.get("reenter")

         if not username:
             return ("Enter Username")
         if not len(password)==8:
             return ("Enter 8 digit")
         if not reenter:
             return("retype password")
         if password  == reenter :
             try:
                  if not password(len(uppercase))>1:
                    return ("Enter at least 1uppercase")
                  if  not password(len(lowercase))>1:
                    return ("Enter at least 1lowercase")
                  if  not password(len(character))>1:
                    return ("Enter at least 1 specialcharacter")
                  if  not password(len(digit))>1:
                    return ("Enter at least 1digit")
             except:
              return("Passwords did not match")
    new_user= "INSERT INTO users (Name,Password) VALUES (?,?)" , (username, password)
    cursor.execute(new_user)
    connection.cursor()
    cursor.commit()
    return render_template("login.html")