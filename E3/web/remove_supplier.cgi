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

def dostuff(tin, c, conn):

    c.execute("SELECT * FROM supplier WHERE TIN = %s", (tin,))
    sup = c.fetchone()

    if sup is None:
        printm("<h1>Suplier to be deleted " + str(tin) + " doesn't exist.</h1>")
        return
    else:
        cursor.execute("DELETE FROM delivery WHERE TIN = %s", (tin,))
        cursor.execute("DELETE FROM suplier WHERE TIN = %s", (tin,))
        conn.commit()
        printm("<h1>Product " + str(tin) + " removed successfully.</h1>")
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

    tin = form.getvalue('reg_supplier_tin')
    dostuff(tin, c, conn)

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

