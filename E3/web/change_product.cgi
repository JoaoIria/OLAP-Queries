#!/usr/bin/python3
import cgi
import psycopg2
import re
import login

def printm(message):
    print(message)
    print("<form action='change_product.html'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def dostuff(sku, price, descr, c, conn):

    c.execute("SELECT * FROM product WHERE {} = %(sku)s", {'sku': sku})
    prod = c.fetchone()

    if prod is None:
        printm("<h1>Product to be changed " + str(sku) + " doesn't exist.</h1>")
        return
    else:
        cursor.execute("UPDATE product SET price = %(price)s, description = %(descr)s WHERE SKU = %(sku)s", {'price': price, 'descr': descr, 'sku': sku})
        printm("<h1>Product " + str(sku) + " removed successfully.</h1>")
        conn.commit()x
    return



conn = None
dsn = f'host={db_host} port={db_port} user={data_base} password={db_password} dbname={data_base}'

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

    sku = form.getvalue('change_product_sku')
    price = form.getvalue('change_product_price')
    descr = form.getvalue('change_product_description')
    dostuff(sku, price, descr, c, conn)

    c.close()

except Exception as e:
    print('<h1>An error occurred.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if conn is not None:
        conn.close()

print("</div>")
print('</body>')
print('</html>')

