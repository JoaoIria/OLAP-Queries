import cgi
import psycopg2
import re
import login


def check_product_ean(product_ean):
    if product_ean is None:
        return None
    elif not product_ean.isdigit():
        return "Error: EAN is not a numeric sequence"
    elif int(product_ean) < 0:
        return "Error: EAN is negative"
    else:
        return None
    
def check_existing_product(cursor, product_sku, product_ean):
    c.execute("SELECT * FROM product WHERE SKU = %(product_sku)s", {'product_sku': product_sku})
    product = cursor.fetchone()

    if product is not None:
        return "Error: Product already exists"

    if product_ean is not None:
        cursor.execute("SELECT * FROM product WHERE ean = %(product_ean)s", {'product_ean': product_ean})
        product = cursor.fetchone()

        if product is not None:
            return "Error: Product already exists"

    return None

def print_error(message):
    print("<h1>{}</h1>".format(message))
    print("<form action='index.HTML'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")


def print_success(message):
    print("<h1>{}</h1>".format(message))
    print("<form action='index.HTML'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")


def reg_product(form, c, conn):
    product_sku = form.getvalue('get_product_sku')
    product_name = form.getvalue('get_product_name')
    product_description = form.getvalue('get_product_description')
    product_price = form.getvalue('get_product_price')
    product_ean = form.getvalue('get_product_ean')

    if check_product_ean(product_ean) is not None:
        print_error(check_product_ean(product_ean))
        return
    
    if check_existing_product(c, product_sku, product_ean) is not None:
        print_error(check_existing_product(c, product_sku, product_ean))
        return
    c.execute(
        "INSERT INTO customer VALUES(%(product_sku)s, %(product_name)s, %(product_description)s, %(product_price)s, %(product_ean)s)",
        {
            'product_sku': product_sku,
            'product_name': product_name,
            'product_description': product_description,
            'product_price': product_price,
            'product_ean': product_ean
        }
    )
    conn.commit()
    print_success("Customer registered successfully")

    

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

    reg_product(form, c, conn)

    c.close()

except Exception as e:
    print('<h1>Unexpexted Error.</h1>')
    print('<p>{}</p>'.format(e))

finally:
    if conn is not None:
        conn.close()

print("</div>")
print('</body>')
print('</html>')

