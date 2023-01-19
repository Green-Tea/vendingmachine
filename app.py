from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# https://pypi.org/project/Flask-MySQLdb/
app.config['MYSQL_HOST'] = "host"
app.config["MYSQL_USER"] = "user"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "database"
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Display Index page
@app.route('/')
def index():  
    return render_template('index.html')

# Listings with machines and products
@app.route('/api/list')
def listing():
    cursor = mysql.connection.cursor()
    
    query = "SELECT * FROM listing"
    rows = cursor.exectue(query)
    machines = cursor.fetchall()
    
    cursor.close()
    
    if rows == 0:
        return jsonify(None)
    
    return jsonify(machines)

@app.route('/api/list/add', methods=['GET', 'POST'])
def list_add():
    cursor = mysql.connection.cursor()
    
    machine_id = request.form['machine_id']
    product_id = request.form['product_id']
    amount = request.form['amount']
    query = f"INSERT INTO listing(product_id, machine_id, amount) VALUES({product_id}, {machine_id}, {amount})"
    
    cursor.execute(query)
    mysql.connection.commit()
    
    cursor.close()
    
    return listing()

@app.route('/api/list/edit', methods=['POST'])
def list_edit():
    cursor = mysql.connection.cursor()
    
    id = request.form['id']
    machine_id = request.form['machine_id']
    product_id = request.form['product_id']
    amount = request.form['amount']
    query = f"UPDATE listing SET product_id = {product_id}, machine_id = {machine_id}, amount = {amount} WHERE listing_id = {id}"
    rows = cursor.execute(query)
    
    cursor.close()
    
    if rows == 0:
        return jsonify(None)

    return listing()

@app.route('/api/list/delete')
def list_delete():
    cursor = mysql.connection.cursor()
    
    id = request.form['id']
    query = f"DELETE FROM listing WHERE listing_id = {id}"
    
    cursor.execute(query)
    mysql.connection.commit()
    
    cursor.close()
    
    return listing()

# Machines
@app.route("/api/machine")
def machine():
    cursor = mysql.connection.cursor()
    
    query = "SELECT * FROM machine"
    rows = cursor.execute(query)
    machines = cursor.fetchall()
    
    cursor.close()
    
    if rows == 0:
        return jsonify(None)
    
    return jsonify(machines)

@app.route("/api/machine/add", methods=['GET', 'POST'])
def machine_add():
    cursor = mysql.connection.cursor()
    
    location = request.form['location']
    query = f"INSERT INTO machine(location) VALUES('{location}')"
    
    cursor.execute(query)
    mysql.connection.commit()
    
    cursor.close()
    
    return machine()

@app.route("api/machine/edit", methods=['POST'])
def machine_edit():
    cursor = mysql.connection.cursor()
    
    id = request.form['id']
    location = request.form['location']
    query = f"UPDATE machine SET location = '{location}' WHERE machine_id = {id}"
    rows = cursor.execute(query)
    
    cursor.close()
    
    if rows == 0:
        return jsonify(None)
    
    return machine()

@app.route("api/machine/delete")
def machine_delete():
    cursor = mysql.connection.cursor()
    
    id = request.form['id']
    query = f"DELETE FROM machine WHERE machine_id = {id}"
    
    cursor.execute(query)
    mysql.connection.commit()
    
    cursor.close()
    
    return machine()

# Products
@app.route("api/product")
def product():
    cursor = mysql.connection.cursor()
    
    query = f"SELECT * FROM product"
    rows = cursor.execute(query)
    products = cursor.fetchall()
    
    cursor.close()
    
    if rows == 0:
        return jsonify(None)
    
    return jsonify(products)

@app.route("/api/product/add", methods=['GET', 'POST'])
def product_add():
    cursor = mysql.connection.cursor()
    
    product = request.form['product']
    price = request.form['price']
    query = f"INSERT INTO product(product_name, price) VALUES('{product}', {price})"
    
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    
    return product()

@app.route("api/product/edit", methods=['POST'])
def product_edit():
    cursor = mysql.connection.cursor()
    
    id = request.form['id']
    product = request.form['product']
    price = request.form['price']
    query = f"UPDATE product SET product_name = '{product}', price = {price} WHERE product_id = {id}"
    rows = cursor.execute(query)
    
    cursor.close()
    
    if rows == 0:
        return jsonify(None)
    return product()

@app.route("api/product/delete")
def product_delete():
    cursor = mysql.connection.cursor()
    
    id = request.form['id']
    query = f"DELETE FROM product WHERE product_id = {id}"
    
    cursor.execute(query)
    mysql.connection.commit()
    cursor.close()
    
    return product()

if __name__ == '__main__':
    app.run(debug=True)