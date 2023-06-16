#!/usr/bin/python3
import cgi
import psycopg2
import re
import login

def printm(message):
    print(message)
    print("<form action='remove_product.html'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def dostuff(sku, c, conn):

    c.execute("SELECT * FROM product WHERE SKU = %s", (sku,))
    prod = c.fetchone()

    if prod is None:
        printm("<h1>Product to be deleted " + str(sku) + " doesn't exist.</h1>")
        return
    else:
        c.execute("DELETE FROM delivery WHERE SKU = %s", (sku,))
        c.execute("DELETE FROM suplier WHERE SKU = %s", (sku,))
        c.execute("DELETE FROM contains WHERE SKU = %s", (sku,))
        c.execute("DELETE FROM product WHERE SKU = %s", (sku,))
        printm("<h1>Product " + str(sku) + " removed successfully.</h1>")
        conn.commit()
    return


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

    sku = form.getvalue('remove_product_sku')
    dostuff(sku, c, conn)

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

