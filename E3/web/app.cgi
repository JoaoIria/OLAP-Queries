import cgi
import psycopg2
import re

def is_valid_name(name):
    return bool(re.match("^[a-zA-Z]+$", name))


def check_existing_customer(c, column, value):
    c.execute("SELECT * FROM customer WHERE {} = %({})s".format(column, column), {column: value})
    customer = c.fetchone()
    return customer is not None

def check_product_exists(cursor, sku):
    cursor.execute("SELECT * FROM product WHERE SKU = %(product_sku)s", {'product_sku': sku})
    product = cursor.fetchone()
    return product is not None


def check_supplier_exists(cursor, tin):
    cursor.execute("SELECT * FROM supplier WHERE TIN = %(tin)s", {'tin': tin})
    supplier = cursor.fetchone()
    return supplier is not None


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

def reg_customer(form, c, conn):
    customer_id = form.getvalue('get_customer_id')
    customer_name = form.getvalue('get_name_register')

    
    if not is_valid_name(customer_name):
        print_error("Invalid customer name")
        return

    # Verificar se um cliente com o ID fornecido já existe
    if check_existing_customer(c, "cust_no", customer_id):
        print_error("Error: Customer already exists")
        return

    # Verificar se um cliente com o e-mail fornecido já existe
    customer_email = form.getvalue('get_customer_email')
    if check_existing_customer(c, "email", customer_email):
        print_error("Error: Email already exists")
        return
    
    customer_phone = form.getvalue('get_customer_phone')
    customer_address = form.getvalue('get_customer_adress')

    # Criar o cliente
    c.execute(
        "INSERT INTO customer VALUES(%(customer_id)s, %(customer_name)s, %(customer_email)s, %(customer_phone)s, %(customer_address)s)",
        {
            'customer_id': customer_id,
            'customer_name': customer_name,
            'customer_email': customer_email,
            'customer_phone': customer_phone,
            'customer_address': customer_address
        }
    )

    conn.commit()
    print_success("Customer registered successfully")

def reg_supplier(form, c, conn):
    supplier_name = form.getvalue('get_supplier_name')
    supplier_address = form.getvalue('get_supplier_address')

    # Check if a supplier with the given TIN already exists
    
    c.execute("SELECT * FROM supplier WHERE TIN = %(tin)s", {'tin': supplier_tin})
    supplier = c.fetchone()

    product_sku = form.getvalue('get_product_sku')
    if not check_product_exists(c, product_sku):
        print_error("Error: SKU does not exist")
        return

    supplier_tin = form.getvalue('get_supplier_tin')
    if check_supplier_exists(c, supplier_tin):
        print_error("Error: Supplier already exists")
        return
    

    # Create the supplier
    c.execute(
        "INSERT INTO supplier VALUES (%(tin)s, %(supplier_name)s, %(supplier_address)s, %(product_sku)s)",
        {'tin': supplier_tin, 'supplier_name': supplier_name,
         'supplier_address': supplier_address, 'product_sku': product_sku})

    conn.commit()
    print_success("Supplier registered successfully")


def reg_product(form, c, conn):
    product_sku = form.getvalue('get_product_sku')
    product_name = form.getvalue('get_product_name')
    product_descr = form.getvalue('get_product_description')
    product_price = form.getvalue('get_product_price')
    product_ean = form.getvalue('get_product_ean')


    return


data_base = 'ist198954'
db_host = 'db.tecnico.ulisboa.pt'
db_port = 5432
db_password = 'ujar9764'
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

    if 'get_customer_id' in form_keys:
        reg_customer(form, c, conn)
    elif 'get_supplier_tin' in form_keys:
        reg_supplier(form, c, conn) 
    elif 'reg_product_sku' in form_keys:
        reg_product(form, c, conn)
    elif 'product_remove_sku' in form_keys:
        remove_product(form, c, conn)
    elif 'supplier_tin_remove' in form_keys:
        remove_supplier(form, c, conn)
    elif 'product_id_price' in form_keys:
        modify_product_price(form, c, conn)
    elif 'product_id_description' in form_keys:
        modify_product_description(form, c, conn)
    elif 'customer_remove_id' in form_keys:
        remove_customer(form, c, conn)
    elif 'make_order_no' in form_keys:
        make_an_order(form, c, conn)
    elif 'pay_order_no' in form_keys:
        pay_an_order(form, c, conn)
    else:
        print('<h1>Unknown Operation</h1>')

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
