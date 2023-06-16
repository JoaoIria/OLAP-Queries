import cgi
import psycopg2
import re
import login


def do_stuff(form, c, conn):

    sku = form.getvalue('product_sku')

    c.execute("SELECT * FROM product WHERE {} = %(sku)s", {'sku': sku})
    prod = c.fetchone()

    if prod is None:
        print("<h1>Product to be deleted %(sku)s doesn't exist.</h1>", {'sku': sku})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
        return
    else:
        cursor.execute("DELETE FROM delivery WHERE SKU = %(sku)s
            DELETE FROM suplier WHERE SKU = %(sku)s
            DELETE FROM contains WHERE SKU = %(sku)s
            DELETE FROM product WHERE SKU = %(sku)s", {'sku': sku})
        print("<h1>Product %(sku)s removed successfully.</h1>", {'sku': sku})
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

