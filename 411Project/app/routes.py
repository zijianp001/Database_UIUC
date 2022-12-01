""" Specifies routing for the application"""
from flask import render_template, request, jsonify, g, redirect, url_for
from app import app
from app import database as db_helper

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items, keys = db_helper.fetch_product()
    return render_template("index.html", items=items, keys=keys)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/check", methods=['POST'])
def checklogin():
    data = request.get_json()
    state = db_helper.check_login(data)
    if state == 2:
        return redirect('/')


@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/createid", methods=['POST'])
def createid():
    data = request.get_json()
    db_helper.register_account(data)
    return render_template('register.html')

@app.route("/delete/<float:product_id>", methods=['POST'])
def delete(product_id):
    try:
        ptype = db_helper.remove_task_by_id(product_id)
        if ptype == 'CPU':
            items, keys = db_helper.fetch_cpu()
        elif ptype == 'GPU':
            items, keys = db_helper.fetch_gpu()
        elif ptype == 'RAM':
            items, keys = db_helper.fetch_ram()
        elif ptype == 'MOTHERBOARD' or ptype == 'MOTHER BOARD':
            items, keys = db_helper.fetch_mob()
        else:
            items, keys = db_helper.fetch_product()
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return render_template("index.html", items=items, keys=keys)


@app.route("/edit", methods=['POST'])
def update():
    data = request.get_json()
    ptype = db_helper.update_attributes(data)
    print(ptype)
    if ptype == 'CPU':
        items, keys = db_helper.fetch_cpu()
    elif ptype == 'GPU':
        items, keys = db_helper.fetch_gpu()
    elif ptype == 'RAM':
        items, keys = db_helper.fetch_ram()
    else:
        items, keys = db_helper.fetch_mob()

    return render_template("index.html", items=items, keys=keys)


@app.route("/create", methods=['POST'])
def create():
    data = request.get_json()
    ptype = db_helper.insert_new_task(data)

    if ptype == 'CPU':
        items, keys = db_helper.fetch_cpu()
    elif ptype == 'GPU':
        items, keys = db_helper.fetch_gpu()
    elif ptype == 'RAM':
        items, keys = db_helper.fetch_ram()
    else:
        items, keys = db_helper.fetch_mob()

    # result = {'success': True, 'response': 'Done'}
    return render_template("index.html", items=items, keys=keys)


@app.route("/search", methods=['GET','POST'])
def search():
    print(request.url)
    data = request.get_json()
    print(data)
    items, keys = db_helper.search_task_by_ProductName(data['input'], data['current'])
    return render_template("index.html", items=items, keys=keys)


@app.route("/cpu", methods=['GET','POST'])
def cpu():
    items, keys = db_helper.fetch_cpu()
    return render_template("index.html", items=items, keys=keys)


@app.route("/gpu", methods=['GET','POST'])
def gpu():
    items, keys = db_helper.fetch_gpu()
    return render_template("index.html", items=items, keys=keys)

@app.route("/mob", methods=['GET','POST'])
def mob():
    print(g.get('name',None))
    items, keys = db_helper.fetch_mob()
    return render_template("index.html", items=items, keys=keys)

@app.route("/ram", methods=['GET','POST'])
def ram():
    print(g.get('name',None))
    items, keys = db_helper.fetch_ram()
    return render_template("index.html", items=items, keys=keys)


@app.route("/ADquery", methods=['POST'])
def ADquery():
    data = request.get_json()
    # print(data)
    items, keys = db_helper.search_adquery(data['input'])
    return render_template("index.html", items=items, keys=keys)

@app.route("/ADquerysp", methods=['POST'])
def ADquerysp():
    data = request.get_json()
    # print(data)
    items, keys = db_helper.search_adquery_sp(data['input'])
    return render_template("index.html", items=items, keys=keys)

@app.route("/ADquery2sp", methods=['POST'])
def ADquery2sp():
    data = request.get_json()
    # print(data)
    items, keys = db_helper.search_adquery2_sp(data['input'])
    return render_template("index.html", items=items, keys=keys)

@app.route("/ADquery2", methods=['POST'])
def ADquery2():
    data = request.get_json()
    print(data)
    items, keys = db_helper.search_adquery2(data['input'])
    return render_template("index.html", items=items, keys=keys)