from flask import Flask, render_template, redirect, request


app = Flask(__name__)

# lista, amelyben tároljuk a pizzákat
pizzak = [
    {"név": "Margaréta", "feltétek": ["sajt", "paradicsom"], "ár": 1000},
    {"név": "Sonkás", "feltétek": ["sajt", "sonka", "paradicsom"], "ár": 1200},
    {"név": "Gombás", "feltétek": ["sajt", "gomba", "paradicsom"], "ár": 1300},
    {"név": "Hawaii", "feltétek": ["sajt", "sonka", "ananász", "paradicsom"], "ár": 1400},
    {"név": "Magyaros", "feltétek": ["sajt", "kolbász", "paradicsom", "paprika", "hagyma"], "ár": 1500}
]

# lista, amelyben tároljuk a kosár tartalmát
kosaram = []

@app.route("/")
def kezdolap():
    # megjelenítjük a pizzákat egy ciklus segítségével
    return render_template("index.html", pizzak=pizzak)

@app.route("/kosarhoz_ad", methods=["POST"])
def kosarhoz_ad():
    # hozzáadjuk a kiválasztott pizzának az adatait a kosár listához
    pizza_neve = request.form["nev"]
    pizza_ara = int(request.form["ara"])
    kosaram.append({"név": pizza_neve, "ár": pizza_ara})
    # átirányítjuk a felhasználót a kosár oldalra
    return redirect("/kosar")

@app.route("/kosar")
def kosar():
    # megjelenítjük a kosár tartalmát
    osszeg = 0
    for pizza in kosaram:
        osszeg += pizza["ár"]
    return render_template("kosar.html", kosaram=kosaram, osszeg=osszeg)

if __name__ == "__main__":
    app.run(debug=True)
