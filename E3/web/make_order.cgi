#!/usr/bin/python3
import cgi
import psycopg2
import login

def print_error(message):
    print("<h1>Error: {}</h1>".format(message))
    print("<form action='make_order.html'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def print_success(message):
    print("<h1>Success: {}</h1>".format(message))
    print("<form action='make_order.html'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def check_customer_existence(c, customer_id):
    c.execute("SELECT * FROM customer WHERE cust_no = %(cust_no)s", {'cust_no': customer_id})
    customer = c.fetchone()
    return customer is not None

def check_product_existence(c, product_sku):
    c.execute("SELECT * FROM product WHERE SKU = %(product_sku)s", {'product_sku': product_sku})
    product = c.fetchone()
    return product is not None

def check_order_uniqueness(c, order_id):
    c.execute("SELECT * FROM orders WHERE order_id = %(order_id)s", {'order_id': order_id})
    order = c.fetchone()
    return order is None

def check_positive_quantity(quantity):
    return int(quantity) > 0

def make_order(form, c, connection):
    order_id = form.getvalue('order_id')
    order_date = form.getvalue('order_date')
 

    if not check_order_uniqueness(c, order_id):
        print_error("Order with ID {} already exists.".format(order_id))
        return

    customer_id = form.getvalue('customer_id')
    if not check_customer_existence(c, customer_id):
        print_error("Customer with ID {} does not exist.".format(customer_id))
        return

    product_sku = form.getvalue('product_sku')
    if not check_product_existence(c, product_sku):
        print_error("Product with SKU {} does not exist.".format(product_sku))
        return

    quantity = form.getvalue('quantity')
    if not check_positive_quantity(quantity):
        print_error("Quantity must be a positive number.")
        return

    try:
        c.execute("INSERT INTO orders VALUES (%(order_id)s, %(customer_id)s, %(product_sku)s, %(order_date)s, %(quantity)s)",
                       {'order_id': order_id, 'customer_id': customer_id, 'product_sku': product_sku, 'order_date': order_date, 'quantity': quantity})

        connection.commit()
        print_success("Order added successfully.")
    except Exception as e:
        print_error("An error occurred: {}".format(str(e)))

# Main program
conn = None

print("Content-type: text/html\n\n")

print('''
<html>
<head>
<title>Request Answer</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div class="container">
''')

try:
    # Estabelecendo conexão
    conn = psycopg2.connect(login.credentials)
    conn.autocommit = False
    c = conn.cursor()

    form = cgi.FieldStorage()
    form_keys = form.keys()

    make_order(form, c, conn)

    c.close()

except Exception as e:
    print('<h1>Unexpexted Error.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if conn is not None:
        conn.close()

print("</div>")
print('</body>')
print('</html>')

