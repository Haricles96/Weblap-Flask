from flask import Flask,redirect,url_for,render_template,request,flash
from valasztek import pizzak,hamburgerek,etelek
from form import Rendeles_ürlap_

app=Flask(__name__)

app.config['SECRET_KEY']="28caf2c60b3e26676be6dec167e2f70f"

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
    form = Rendeles_ürlap_()
    szamlalo=0
    szallitasi_adatok=[]
    for kosar in kosaram:
        szamlalo+= int(kosar["ár"])
    if request.method== "POST":
        if form.validate_on_submit():
            szallitasi_adatok.append({"email":form.email.data,"vnev":form.vnev.data,"knev":form.knev.data,"telefonszam":form.tel.data,"irszam":form.irsz.data,"varos":form.varos.data,"utca":form.utca.data,"hszam":form.hszam.data,"kosár":kosaram})
            print (szallitasi_adatok)
            flash("Sikeres rendelés!","success")
            kosar_ürites()
            szamlalo=0
            return redirect(url_for("ürlap"))   
    return render_template("rendeles_ürlap.html",kosaram=kosaram,szamlalo=szamlalo,form=form)


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