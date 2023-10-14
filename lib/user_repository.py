from lib.user import User

class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all user information
    def all(self):
        Users = []
        rows = self._connection.execute('Select * from users')   
        return rows
        
    # Checks that email and username are not already registered
    def Registration_Errors(self, email, username ):
        errors=[]
        all_registered_users = self._connection.execute('Select username,email from users ') 
        all_usernames = [user['username'] for user in all_registered_users]
        all_emails = [user['email'] for user in all_registered_users]
        
        if username in all_usernames:
            errors.append ('Username already taken - Please choose another name')
        if email in all_emails:
            errors.append ('Account already regsitered to that email address!')
        if errors ==[]:
            return None
        else:
            return errors


# Find a user by their Username
    def find(self, username):
        DictResponse = self._connection.execute('SELECT * from users WHERE username = %s', [username])
        if DictResponse ==[]:
            return None
        else:
            user_account= User(DictResponse[0]['id'],DictResponse[0]['name'],DictResponse[0]['email'],DictResponse[0]['username'],DictResponse[0]['password'])
            return user_account
    # Create a User
    def create(self,name, email, username, password):
        self._connection.execute('INSERT INTO users (name,email,username,password) VALUES (%s,%s,%s,%s)', [name,email,username,password])
        return (f'{name} registered!')



    # # Delete a book by its id
    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None