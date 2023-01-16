import sqlite3

# connecting to the database
connection = sqlite3.connect('mastermind_game.db')

# creating a cursor object to insert the new data and fetch the data
c = connection.cursor()

# create a table for the result
# c.execute("""CREATE TABLE result (
#     name text,
#     secret_code text,
#     round integer
#     )""")

def insert_result(result):
    with connection:
        c.execute("INSERT INTO result VALUES (:name, :secret_code, :round)", {"name": result.name, "secret_code":convert_list_to_string(result.secret_code), "round":result.round})

# the secret code is a list so convert it to a string
def convert_list_to_string(data):
    return f"[{', '.join(str(num) for num in data)}]"

# show the top 10 results in the ascending order of the round they took to figure out a secret code
def get_result():
    c.execute("SELECT * FROM result ORDER BY round ASC LIMIT 10")
    return c.fetchall()

# commit the change
# connection.commit()
# end the connection
# connection.close()