class CheepRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('Select * from cheeps join users on cheeps.poster_id= users.id')   
        return rows

    # # Find a single book by its id
    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return Book(row["id"], row["title"], row["author_name"])

    # Create a Cheep
    def create(self, content,time_posted,poster_id):
        self._connection.execute('INSERT INTO cheeps (content,time_posted,poster_id) VALUES (%s,%s,%s)', [content,time_posted,poster_id])
    

    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None
