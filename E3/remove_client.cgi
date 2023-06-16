#!/usr/bin/env python
import cgi
import psycopg2
import re
import login

def dostuff(c, conn, cosn):

    c.execute("SELECT cust_no FROM customer WHERE cust_no = %s", (cosn,))
    cust = c.fetchall()

    if cust is None:
        print("<h1>Customer to be deleted %(cosn)s doesn't exist.</h1>", {'cosn': cosn})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
        return
    else:

        cursor.execute("DELETE FROM orders WHERE cost_no = %s", (cosn,))
        cursor.execute("DELETE FROM customer WHERE cost_no = %s", (cosn,))
        
        conn.commit()
        print("<h1>Customer %(cosn)s removed successfully.</h1>", {'cosn': cosn})
        print("<form action='website.html'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
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
    #Estabelecendo conexão
    conn = psycopg2.connect(login.credentials)
    conn.autocommit = False
    c = conn.cursor()
    form = cgi.FieldStorage()
    form_keys = form.keys()
    cosn = form.getvalue('customer_id')
    dostuff(c, conn, cosn)
    print('<h1>IT CAME.</h1>')

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