from lib.user import User

class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        Users = []
        rows = self._connection.execute('Select * from users')   
        return rows

    # # Find a single book by its id
    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return Book(row["id"], row["title"], row["author_name"])

    # Create a User
    def create(self,name, email, username, password):
        self._connection.execute('INSERT INTO users (name,email,username,password) VALUES (%s,%s,%s,%s)', [name,email,username,password])
        return (f'{name} registered!')



    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None