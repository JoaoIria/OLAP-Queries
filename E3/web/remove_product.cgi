import cgi
import psycopg2
import re

def remove_product(sku):
    cursor.execute("DELETE FROM delivery WHERE SKU = %(sku)s
                    DELETE FROM suplier WHERE SKU = %(sku)s
                    DELETE FROM contains WHERE SKU = %(sku)s
                    DELETE FROM product WHERE SKU = %(sku)s", {'sku': sku})
    #refresh page
    print ("<meta http-equiv=\"refresh\" content=\"0")


data_base = 'ist1103557'
db_host = 'db.tecnico.ulisboa.pt'
db_port = 5432
db_password = 'aaaa1111'
db_connection_str = "host=%s port=%d user=%s password=%s dbname=%s" % (db_host, db_port, data_base, db_password, data_base)

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
    conn = psycopg2.connect(dsn)
    conn.autocommit = False
    c = conn.cursor()

    form = cgi.FieldStorage()
    form_keys = form.keys()

    #print the product table
    products = c.execute("SELECT sku, name FROM product")

    print('<table border="0" cellspacing="5">')
    for row in products:
        print('<tr>')
        for value in row:
            print('<td>{}</td>'.format(value))
        #this bellow should be the delete button
        print('<td><input type="hidden" name="id" value="1"><a onClick="remove_product(1)" href="">1</a>'.format(row[0]))
        print('</tr>')
    print('</table>')

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

