from database.connection import get_db_connection
class Magazine:
    def __init__(self, id, name, category= "General"):
        self.id = id
        self.name = name
        self.category = category
       
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?);", (self._name, self._category))
        self._id = cursor.lastrowid
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        self._id = id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name
        if len(name)< 2 or len(name) > 16: 
            raise ValueError("name must be between 2 and 16 characters")
        self._name = name
        
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE magazines SET name = ? WHERE id = ?;", (self._name, self._id))
        connection.commit()
        connection.close()
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        self._category = category
        if len(category) < 0:
            raise ValueError("category must be longer than 0 characters")
        self._category = category
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE magazines SET category = ? WHERE id = ?;", (self._category, self._id))
        connection.commit()
        connection.close()
    def articles(self):
         connection = get_db_connection()
         cursor = connection.cursor()
         cursor.execute('''
         SELECT title FROM articles WHERE magazine_id = ?;
         ''', (self._id,))
         articles = cursor.fetchall()
         connection.close()
         return [article[0] for article in articles]
 
    def contributors(self):
         connection = get_db_connection()
         cursor = connection.cursor()
         cursor.execute('''
         SELECT DISTINCT a.name FROM authors a
         INNER JOIN articles ar ON a.id = ar.author_id
         WHERE ar.magazine_id = ?;
         ''', (self._id,))
         contributors = cursor.fetchall()
         connection.close()
         return [contributor[0] for contributor in contributors]
    
    def article_titles(self):
        articles = self.articles()
        return articles if articles else None
    
    def contributing_authors(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
        SELECT a.name FROM authors a
        INNER JOIN articles ar ON a.id = ar.author_id
        WHERE ar.magazine_id = ?
        GROUP BY a.id
        HAVING COUNT(ar.id) > 2;
        ''', (self._id,))
        authors = cursor.fetchall()
        connection.close()
        return [author[0] for author in authors] if authors else None
    
    def __repr__(self):
        return f'<Magazine {self.name}>'