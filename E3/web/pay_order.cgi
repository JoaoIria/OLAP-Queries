#!/usr/bin/env python
import cgi
import psycopg2
import re
import login

def dostuff(form, c, conn):
    ordn = tin = form.getvalue('order_id')
    cusn = tin = form.getvalue('customer_id')

    c.execute("SELECT * FROM orders WHERE order_no = %s", (ordn,))
    order = c.fetchone()
    if cusn NOT order[1]: #check if the customer that's paying is the same as the one that made the order
        print("<h1>Order to be payed %(ordn)s isn't associated with the client %(cusn)s.</h1>", {'ordn': ordn, 'cusn': cusn})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
        return
    c.execute("SELECT * FROM pay WHERE order_no = %s", (ordn,))
    pays = c.fetchone()
    if pays is Not None:
        print("<h1>Order to be payed %(ordn)s has already been payed.</h1>", {'ordn': ordn})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
        return
    c.execute(
        "INSERT INTO pay VALUES(%(order_no)s, %(customer_no)s",
        {
            'order_no': ordn,
            'customer_no': cusn
        }
    )
    conn.commit()
    print("<h1>Order %(ordn)s payed successfully.</h1>", {'ordn': ordn})
    print("<form action='index.HTML'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")
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

    dostuff(form, c, conn)

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

