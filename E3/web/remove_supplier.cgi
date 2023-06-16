#!/usr/bin/python3
import cgi
import psycopg2
import re
import login


def printm(message):
    print(message)
    print("<form action='remove_supplier.html'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def dostuff(form, c, conn):
    tin = form.getvalue('reg_supplier_tin')

    c.execute("SELECT * FROM supplier WHERE TIN = %(tin)s", {'tin': tin})
    sup = c.fetchone()

    if sup is None:
        printm("<h1>Suplier to be deleted "+str(tin)+" doesn't exist.</h1>")
        return
    else:
        cursor.execute("DELETE FROM delivery WHERE TIN = %(tin)s", {'tin': tin})
        cursor.execute("DELETE FROM suplier WHERE TIN = %(tin)s", {'tin': tin})
        conn.commit()
        printm("<h1>Product "+str(tin)+" removed successfully.</h1>")
        conn.commit()
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

