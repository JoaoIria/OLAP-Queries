#!/usr/bin/python3
import cgi
import psycopg2
import re
import login


def printm(message):
    print(message)
    print("<form action='remove_client.html'>")
    print("    <div class=""secondary-menu"">")
    print("    <input type='submit' value='Go Back'>")
    print("    </div>")
    print("</form>")

def dostuff(ordn, cusn, c, conn):

    c.execute("SELECT * FROM orders WHERE order_no = %s", (ordn,))
    order = c.fetchone()

    if order is None:
        printm("<h1>Order to be paid " + str(ordn) + " doesn't exist.</h1>")
        return
    
    if cusn != order[1]:  # check if the customer that's paying is the same as the one that made the order
        printm("<h1>Order to be paid " + str(ordn) + " isn't associated with the client " + str(cusn) + ".</h1>")
        return
    c.execute("SELECT * FROM pay WHERE order_no = %s", (ordn,))
    pays = c.fetchone()
    if pays == ():
        printm("<h1>Order to be payed " + str(ordn) + " has already been payed.</h1>")
        return
    c.execute(
        "INSERT INTO pay VALUES(%(order_no)s, %(customer_no)s",
        {
            'order_no': ordn,
            'customer_no': cusn
        }
    )
    conn.commit()
    printm("<h1>Order " + str(ordn) + " payed successfully.</h1>")
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

    ordn = form.getvalue('order_id')
    cusn = form.getvalue('customer_id')
    dostuff(ordn, cusn, c, conn)

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

