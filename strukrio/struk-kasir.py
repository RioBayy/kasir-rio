from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
items = []

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/tambah", methods=["POST"])
def tambah_item():
    nama = request.form["nama"]
    harga = float(request.form["harga"])
    items.append({"nama":nama, "harga":harga})
    return redirect(url_for("index"))

@app.route("/checkout")
def checkout():
    total = sum(item["harga"] for item in items)
    return render_template("checkout.html", items=items, total=total)

def format_rupiah(value):
    return "Rp{:,.2f}".format(value).replace(",", "X").replace(".", ",").replace("X", ".")
app.jinja_env.filters["rupiah"] = format_rupiah

if __name__ == "__main__":
    app.run(debug=True)