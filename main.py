from flask import Flask,redirect,url_for,render_template,request
from valasztek import pizzak,hamburgerek,etelek
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length

app=Flask(__name__)

kosaram=[]

@app.route("/")
@app.route("/kezdolap")
def kezdolap():
    return render_template("kezdolap.html")

@app.route("/elerhetoseg")
def elerhetoseg():
    return render_template("elerhetoseg.html")

@app.route("/kepek")
def kepek():
    return render_template("kepek.html")

@app.route("/rolunk")
def rolunk():
    return render_template("rolunk.html")

@app.route('/rendeles')
def rendeles():
    return render_template("rendeles.html",etelek=etelek)

@app.route("/hamburger")
def hamburger():
    return render_template("hamburgerek.html",hamburgerek=hamburgerek)

@app.route("/pizza")
def pizza():
    return render_template("pizzak.html",pizzak=pizzak)


@app.route("/ürlap",methods=["GET","POST"])
def ürlap():
    szamlalo=0
    szallitasi_cim=[]
    for kosar in kosaram:
        szamlalo+= int(kosar["ár"])
    if request.method== "POST":
       email=request.form.get('email')
       vnev=request.form.get('vnev') 
       knev=request.form.get('knev')
       tel=request.form.get('tel') 
       irszam=request.form.get('irszam') 
       varos=request.form.get('varos')
       utca=request.form.get('utca')
       hszam=request.form.get('hszam')
       szallitasi_cim.append({"email":email,"vnev":vnev,"knev":knev,"telefonszam":tel,"irszam":irszam ,"varos":varos,"utca":utca,"hszam":hszam,"kosár":kosaram})
       print (szallitasi_cim)
    return render_template("rendeles_ürlap.html",kosaram=kosaram,szamlalo=szamlalo)


@app.route("/kosarhoz_ad", methods=["POST"])
def kosarhoz_ad():
    pizza_neve = request.form["nev"]
    pizza_ara = int(request.form["ara"])
    kosaram.append({"név": pizza_neve, "ár": pizza_ara})
    return redirect("/kosar")

@app.route("/kosar")
def kosar():
    osszeg=0
    for pizza in kosaram:
        osszeg += pizza["ár"]
        
    return render_template("kosar.html", kosaram=kosaram, osszeg=osszeg,hamburgerek=hamburgerek)

@app.route("/kosar_2")
def kosar_2():
    osszeg=0
    for pizza in kosaram:
        osszeg -= pizza["ár"]
        return redirect("/kosar")
    return render_template("kosar.html", kosaram=kosaram, osszeg=osszeg)


@app.route("/kosar_torles", methods=["POST"])
def kosar_ürites():
    for _ in kosaram:
        kosaram.clear() 
        return redirect("/kosar")
    return render_template("kosar.html",kosaram=kosaram)

if __name__== "__main__":
    app.run(debug=True)