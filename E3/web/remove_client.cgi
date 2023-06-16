import cgi
import psycopg2
import re
import login

def dostuff(form, c, conn):
    cosn = form.getvalue('customer_id')

    c.execute("SELECT * FROM customer WHERE cost_no = %(cosn)s", {'cosn': cosn})
    cost = c.fetchone()

    if cost is None:
        print("<h1>Customer to be deleted %(cosn)s doesn't exist.</h1>", {'cosn': cosn})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
        return
    else:
        cursor.execute("DELETE FROM orders WHERE cost_no = %(cosn)s
            DELETE FROM customer WHERE cost_no = %(cosn)s", {'cosn': cosn})
        conn.commit()
        print("<h1>Customer %(cosn)s removed successfully.</h1>", {'cosn': cosn})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
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

