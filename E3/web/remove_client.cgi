#!/usr/bin/python3
import cgi
import psycopg2
import re
import login

def printm(message):
    print(message)
    print("<form action='remove_client.html'>")
    print("    <div class=""secondary-menu"">")
    print("    <input type='submit' value='Go Back'>")
    print("    </div>")
    print("</form>")

def dostuff(c, conn, cosn):

    c.execute("SELECT cust_no FROM customer WHERE cust_no = %s", (cosn,))
    cust = c.fetchall()

    if len(cust) == 0:
        printm("<h1>Customer to be deleted " + str(cosn) + " doesn't exist.</h1>")
        return
    else:
        c.execute("DELETE FROM orders WHERE cust_no = %s", (cosn,))
        c.execute("DELETE FROM customer WHERE cust_no = %s", (cosn,))
        
        conn.commit()
        printm("<h1>Customer " + str(cosn) + " removed successfully.</h1>")
    return

conn = None

print("Content-type: text/html\n\n")

print('<html>')
print('<head>')
print('<title>Request Answer</title>')
print('<link rel="stylesheet" type="text/css" href="style.css">')
print('<head>')
print('<body>')
print('<div class="container">')

try:
    #Estabelecendo conexão
    conn = psycopg2.connect(login.credentials)
    conn.autocommit = False
    c = conn.cursor()
    form = cgi.FieldStorage()
    form_keys = form.keys()
    
    cosn = form.getvalue('customer_id')
    dostuff(c, conn, cosn)

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