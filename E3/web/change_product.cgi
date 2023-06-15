import cgi
import psycopg2
import re
import login

def dostuff(form, c, conn):

    sku = form.getvalue('get_product_sku')
    price = form.getvalue('get_product_price')
    descr = form.getvalue('get_product_description')

    c.execute("SELECT * FROM product WHERE {} = %(sku)s", {'sku': sku})
    prod = c.fetchone()

    if prod is None:
        print("<h1>Product to be changed %(sku)s doesn't exist.</h1>", {'sku': sku})
        print("<form action='index.HTML'>")
        print("    <input type='submit' value='Go Back'>")
        print("</form>")
        return
    else:
        cursor.execute("UPDATE product SET price = {price}, description = {descr} WHERE SKU = {sku}")
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

    if 'product_id_price' in form_keys:
        modify_product_price(form, c, conn)
    elif 'product_id_description' in form_keys:
        modify_product_description(form, c, conn)
    else:
        print('<h1> Unexpected behaviour </h1>')

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

