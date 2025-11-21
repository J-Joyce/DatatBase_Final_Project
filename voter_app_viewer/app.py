from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL connection config
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '!Leo-pard',
    'database': 'Voter_app'
}

def fetch_table_data(table_name):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return columns, rows

@app.route('/')
def index():
    tables = ['counties', 'congress', 'house']
    data = {}
    for table in tables:
        cols, rows = fetch_table_data(table)
        data[table] = {'columns': cols, 'rows': rows}
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)