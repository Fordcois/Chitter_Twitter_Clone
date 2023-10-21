
class HashtagRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('Select * from hashtags')   
        return rows
    
    # Create a Hashtag and returns the ID of the newly created 
    def CreateAndReturnId(self,hashtag):
        HashtagID=self._connection.execute("INSERT INTO hashtags (hashtag) VALUES (%s) RETURNING id;", [hashtag])
        return HashtagID[0]['id']
    
    def AddJoin(self,hashtag_id,post_id):
        self._connection.execute("INSERT INTO hashtag_post_join_table (hashtag_id,post_id) VALUES (%s,%s)", [hashtag_id,post_id])

