#!/usr/bin/python3
import cgi
import psycopg2
import re
import login


def check_supplier_exists(cursor, tin):
    cursor.execute("SELECT * FROM supplier WHERE TIN = %(tin)s", {'tin': tin})
    supplier = cursor.fetchone()
    return supplier is not None

def check_product_ean(product_ean):
    if product_ean is None:
        return None
    elif not product_ean.isdigit():
        return "Error: EAN is not a numeric sequence"
    elif int(product_ean) < 0:
        return "Error: EAN is negative"
    else:
        return None


def check_product_exists(cursor, sku):
    cursor.execute("SELECT * FROM product WHERE SKU = %(product_sku)s", {'product_sku': sku})
    product = cursor.fetchone()
    return product is not None

def print_error(message):
    print("<h1>{}</h1>".format(message))
    print("<form action='index.HTML'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")


def print_success(message):
    print("<h1>{}</h1>".format(message))
    print("<form action='index.HTML'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")


def reg_supplier(form, c, conn):
    supplier_name = form.getvalue('get_supplier_name')
    supplier_address = form.getvalue('get_supplier_address')
    date = form.getvalue('date')

    # Check if a supplier with the given TIN already exists
    
    c.execute("SELECT * FROM supplier WHERE TIN = %(tin)s", {'tin': supplier_tin})
    supplier = c.fetchone()

    product_sku = form.getvalue('get_product_sku')
    if not check_product_exists(c, product_sku):
        print_error("Error: SKU does not exist")
        return

    supplier_tin = form.getvalue('get_supplier_tin')
    if check_supplier_exists(c, supplier_tin):
        print_error("Error: Supplier already exists")
        return
    

    # Create the supplier
    c.execute(
        "INSERT INTO supplier VALUES (%(tin)s, %(supplier_name)s, %(supplier_address)s, %(product_sku)s), %(date)s)",
        {'tin': supplier_tin, 'supplier_name': supplier_name,
         'supplier_address': supplier_address, 'product_sku': product_sku, 'date': date})

    conn.commit()
    print_success("Supplier registered successfully")
    

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

    reg_supplier(form, c, conn)

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

