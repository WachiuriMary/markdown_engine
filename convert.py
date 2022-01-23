import sqlite3
import markdown

# database function
def get_data():
    # connecting to the database and creating a cursor
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    
    # retrieving records
    c.execute("SELECT * FROM customers")
    items = c.fetchall()
    
    conn.commit()
    conn.close()
    
    return items

# Markdown to html
def conversion():
    customers = get_data()

    with open('customer.md', 'bw+') as f:
        f.write('| Name    | Email           |\n| :------- | :---------------: |\n'.encode('utf-8'))
        for name, email in customers:
            f.write('| {}\t'.format(name).encode('utf-8'))
            f.write('| {} |\n'.format(email).encode('utf-8'))
        f.seek(0)
        markdown.markdownFromFile(input=f, output='customer.html', extensions=['markdown.extensions.tables'])
    
    print("Execution complete")

conversion()