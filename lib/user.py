class User():
    def __init__ (self,id,name,email,username,password):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def create(self,id,name,email,username,password):
        self._connection.execute('INSERT INTO cheeps (content,time_posted,poster_id) VALUES (%s,%s,%s)', [content,time_posted,poster_id])
    
    
    def __repr__(self):
        return f"User Profile - {self.id}, {self.name}, {self.email} {self.username} {self.password}"



