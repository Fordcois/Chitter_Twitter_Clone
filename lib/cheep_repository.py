class CheepRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all cheeps
    def all(self):
        rows = self._connection.execute('Select * from cheeps join users on cheeps.poster_id= users.id')   
        return rows
    
    # Return all Cheeps By user
    def all_by(self,username):
        rows = self._connection.execute('Select * from cheeps join users on cheeps.poster_id= users.id where username =(%s)',[username])   
        return rows

    # Create a Cheep
    def create(self, content,time_posted,poster_id):
        self._connection.execute('INSERT INTO cheeps (content,time_posted,poster_id) VALUES (%s,%s,%s)', [content,time_posted,poster_id])
    
    # Create and return Cheep id:
    def CreateAndReturnID(self, content,time_posted,poster_id):
        NewPost=self._connection.execute('INSERT INTO cheeps (content,time_posted,poster_id) VALUES (%s,%s,%s) RETURNING id;', [content,time_posted,poster_id])
        print (type(NewPost))
        return (NewPost[0]['id'])
    
    #Find all Cheeps by Hashtag:
    def all_by_hashtag(self,hashtag):
        rows = self._connection.execute('SELECT cheeps.id, cheeps.content, cheeps.time_posted, users.username FROM hashtag_post_join_table JOIN cheeps ON cheeps.id = hashtag_post_join_table.post_id JOIN hashtags ON hashtags.id = hashtag_post_join_table.hashtag_id JOIN users on users.id = hashtag_post_join_table.poster_id WHERE hashtags.hashtag ILIKE (%s)',[hashtag])   
        return rows
 
    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None
