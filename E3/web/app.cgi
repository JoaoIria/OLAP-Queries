import cgi
import psycopg2



def register_customer(form, cursor, connection):
    customer_id = form.getvalue('customer_register_id')
    customer_name = form.getvalue('customer_register_name')

    if not is_valid_name(customer_name):
        print_error("Customer Name should only contain letters")
        return

    # Verificar se um cliente com o ID fornecido já existe
    if check_existing_customer(cursor, "cust_no", customer_id):
        print_error("Error: Customer with this ID already exists")
        return

    # Verificar se um cliente com o e-mail fornecido já existe
    customer_email = form.getvalue('customer_register_email')
    if check_existing_customer(cursor, "email", customer_email):
        print_error("Error: Customer with this email already exists")
        return

    customer_phone = form.getvalue('customer_register_phone')
    customer_address = form.getvalue('customer_register_address')

    # Criar o cliente
    cursor.execute(
        "INSERT INTO customer VALUES(%(customer_id)s, %(customer_name)s, %(customer_email)s, %(customer_phone)s, %(customer_address)s)",
        {
            'customer_id': customer_id,
            'customer_name': customer_name,
            'customer_email': customer_email,
            'customer_phone': customer_phone,
            'customer_address': customer_address
        }
    )

    connection.commit()
    print_success("Customer registered successfully")


def is_valid_name(name):
    return bool(re.match("^[a-zA-Z]+$", name))


def check_existing_customer(cursor, column, value):
    cursor.execute("SELECT * FROM customer WHERE {} = %({})s".format(column, column), {column: value})
    customer = cursor.fetchone()
    return customer is not None


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




ist_id = 'ist198954'
db_host = 'db.tecnico.ulisboa.pt'
db_port = 5432
db_password = 'ujar9764'
data_base = 'ist198954@db.tecnico.ulisboa.pt'
db_connection_str = "host=%s port=%d user=%s password=%s dbname=%s" % (db_host, db_port, ist_id, db_password, data_base)

print("Content-type: text/html\n\n")


connection = None
