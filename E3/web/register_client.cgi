#!/usr/bin/python3
import cgi
import psycopg2
import re
import login

def is_valid_name(name):
    return bool(re.match("^[a-zA-Z]+$", name))

def check_existing_customer(c, column, value):
    c.execute("SELECT * FROM customer WHERE {} = %({})s".format(column, column), {column: value})
    customer = c.fetchone()
    return customer is not None
    
def print_error(message):
    print("<h1>{}</h1>".format(message))
    print("<form action='register_client.html'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def print_success(message):
    print("<h1>{}</h1>".format(message))
    print("<form action='index.HTML'>")
    print("    <input type='submit' value='Go Back'>")
    print("</form>")

def reg_customer(form, c, conn):
    customer_id = form.getvalue('customer_id')
    customer_name = form.getvalue('reg_name')
    
    if not is_valid_name(customer_name):
        print_error("Invalid customer name")
        return

    # Verificar se um cliente com o ID fornecido já existe
    if check_existing_customer(c, "cust_no", customer_id):
        print_error("Error: Customer already exists")
        return

    # Verificar se um cliente com o e-mail fornecido já existe
    customer_email = form.getvalue('reg_email')
    if check_existing_customer(c, "email", customer_email):
        print_error("Error: Email already exists")
        return
    
    customer_phone = form.getvalue('reg_phone')
    customer_address = form.getvalue('reg_address')

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

    reg_customer(form, c, conn)

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

