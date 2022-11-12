""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<float:product_id>", methods=['POST'])
def delete(product_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_task_by_id(product_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)



@app.route("/edit", methods=['POST'])
def update():
    """ recieved post requests for entry updates """
    data = request.get_json()
    db_helper.update_attributes(data['1'], data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['9'], data['10'], data['11'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_new_task(data['1'], data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['9'], data['10'], data['11'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/search", methods=['POST'])
def search():
    data = request.get_json()
    """ returns rendered homepage """
    items, keys = db_helper.search_task_by_ProductName(data['input'])
    return render_template("index.html", items=items, keys=keys)

@app.route("/")
def homepage():
    """ returns rendered homepage """
    items, keys = db_helper.fetch_todo()
    return render_template("index.html", items=items, keys=keys)


@app.route("/ADquery", methods=['POST'])
def ADquery():
    """ returns rendered homepage """
    items, keys = db_helper.search_adquery()
    return render_template("index.html", items=items, keys=keys)

@app.route("/ADquery2", methods=['POST'])
def ADquery2():
    """ returns rendered homepage """
    items, keys = db_helper.search_adquery2()
    return render_template("index.html", items=items, keys=keys)