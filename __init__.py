class Author:
    def __init__(self, id, name):
        # Ensure id is an integer
        if not isinstance(id, int):
            raise TypeError("id must be of type int")
        
        # Ensure name is a string and longer than 0 characters
        if not isinstance(name, str):
            raise TypeError("name must be of type str")
        if len(name.strip()) == 0:
            raise ValueError("name must be longer than 0 characters")
        
        # Initialize properties
        self._id = id
        self._name = name

        # Simulate creating a new entry in the database
        self._create_author_in_database()

    def _create_author_in_database(self):
        """
        Simulate the creation of the author in the database.
        This is a placeholder and represents where you'd implement your database logic.
        """
        # Normally, you'd insert into a database here.
        # E.g., "INSERT INTO authors (id, name) VALUES (?, ?)"
        print(f"Author created in the database: id={self._id}, name='{self._name}'")

    # Getter for id
    @property
    def id(self):
        return self._id

    # Setter for id (not needed since id should not be changed, but included for completeness)
    @id.setter
    def id(self, value):
        raise AttributeError("id cannot be modified after initialization")

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name (disabled to ensure immutability after initialization)
    @name.setter
    def name(self, value):
        raise AttributeError("name cannot be modified after initialization")


# Example usage
try:
    author = Author(1, "John Doe")
    print(f"Author ID: {author.id}")
    print(f"Author Name: {author.name}")

    # Trying to modify name or id will raise an error
    # author.name = "Jane Doe"  # Uncommenting this will raise an AttributeError
    # author.id = 2  # Uncommenting this will raise an AttributeError
except (TypeError, ValueError, AttributeError) as e:
    print(e)

class Magazine:
    def __init__(self, id, name, category):
        # Ensure id is an integer
        if not isinstance(id, int):
            raise TypeError("id must be of type int")
        
        # Ensure name is a string and between 2 and 16 characters
        if not isinstance(name, str):
            raise TypeError("name must be of type str")
        if not (2 <= len(name.strip()) <= 16):
            raise ValueError("name must be between 2 and 16 characters")

        # Ensure category is a string and longer than 0 characters
        if not isinstance(category, str):
            raise TypeError("category must be of type str")
        if len(category.strip()) == 0:
            raise ValueError("category must be longer than 0 characters")
        
        # Initialize properties
        self._id = id
        self._name = name
        self._category = category

        # Simulate creating a new entry in the database
        self._create_magazine_in_database()

    def _create_magazine_in_database(self):
        """
        Simulate the creation of the magazine in the database.
        This is a placeholder and represents where you'd implement your database logic.
        """
        # Normally, you'd insert into a database here.
        # E.g., "INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)"
        print(f"Magazine created in the database: id={self._id}, name='{self._name}', category='{self._category}'")

    # Getter for id
    @property
    def id(self):
        return self._id

    # Setter for id (not needed since id should not be changed)
    @id.setter
    def id(self, value):
        raise AttributeError("id cannot be modified after initialization")

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name (allows change after initialization)
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be of type str")
        if not (2 <= len(value.strip()) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = value

    # Getter for category
    @property
    def category(self):
        return self._category

    # Setter for category (allows change after initialization)

class Article:
    def __init__(self, author, magazine, title):
        # Ensure author is an instance of Author
        if not hasattr(author, "id") or not isinstance(author.id, int):
            raise TypeError("author must be an instance of Author with a valid id")

        # Ensure magazine is an instance of Magazine
        if not hasattr(magazine, "id") or not isinstance(magazine.id, int):
            raise TypeError("magazine must be an instance of Magazine with a valid id")

        # Ensure title is a string and between 5 and 50 characters
        if not isinstance(title, str):
            raise TypeError("title must be of type str")
        if not (5 <= len(title.strip()) <= 50):
            raise ValueError("title must be between 5 and 50 characters")

        # Retrieve ids from author and magazine
        self._author_id = author.id
        self._magazine_id = magazine.id
        self._title = title

        # Simulate creating a new entry in the database
        self._create_article_in_database()

    def _create_article_in_database(self):
        """
        Simulate the creation of the article in the database.
        This is a placeholder and represents where you'd implement your database logic.
        """
        # Normally, you'd insert into a database here.
        # E.g., "INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)"
        print(f"Article created in the database: author_id={self._author_id}, magazine_id={self._magazine_id}, title='{self._title}'")

    # Getter for title
    @property
    def title(self):
        return self._title

    # Setter for title (disabled to ensure immutability)
    @title.setter
    def title(self, value):
        raise AttributeError("title cannot be modified after initialization")


# Example usage
try:
    # Assuming Author and Magazine classes are already implemented
    author = Author(1, "John Doe")  # Example Author instance
    magazine = Magazine(1, "Tech World", "Technology")  # Example Magazine instance

    # Create an Article
    article = Article(author, magazine, "The Future of AI")
    print(f"Article Title: {article.title}")

    # Trying to modify the title will raise an error
    # article.title = "New Title"  # Uncommenting this will raise an AttributeError
except (TypeError, ValueError, AttributeError) as e:
    print(e)