import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
def connect_db():
    return sqlite3.connect('movies.db')

# Create the movies table
def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                director TEXT,
                year INTEGER,
                genre TEXT
            )
        ''')
        conn.commit()

# Add a movie to the database
def add_movie(title, director, year, genre):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO movies (title, director, year, genre)
            VALUES (?, ?, ?, ?)
        ''', (title, director, year, genre))
        conn.commit()

# Retrieve all movies from the database
def get_all_movies():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies')
        return cursor.fetchall()

# Retrieve movies by a specific director
def get_movies_by_director(director):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM movies WHERE director = ?', (director,))
        return cursor.fetchall()

# Update movie information by ID
def update_movie(id, title=None, director=None, year=None, genre=None):
    with connect_db() as conn:
        cursor = conn.cursor()
        if title:
            cursor.execute('UPDATE movies SET title = ? WHERE id = ?', (title, id))
        if director:
            cursor.execute('UPDATE movies SET director = ? WHERE id = ?', (director, id))
        if year:
            cursor.execute('UPDATE movies SET year = ? WHERE id = ?', (year, id))
        if genre:
            cursor.execute('UPDATE movies SET genre = ? WHERE id = ?', (genre, id))
        conn.commit()

# Delete a movie by ID
def delete_movie(id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM movies WHERE id = ?', (id,))
        conn.commit()

# Print all movies for demonstration purposes
def print_all_movies():
    movies = get_all_movies()
    for movie in movies:
        print(movie)

# Main function to demonstrate the usage
def main():
    create_table()  # Ensure the table exists

    # Adding some movies
    add_movie('Inception', 'Christopher Nolan', 2010, 'Sci-Fi')
    add_movie('The Matrix', 'Wachowski Sisters', 1999, 'Action')
    
    print("All movies in the database:")
    print_all_movies()

    # Update a movie
    print("\nUpdating movie with ID 1...")
    update_movie(1, genre='Science Fiction')
    
    print("All movies in the database after update:")
    print_all_movies()

    # Retrieve movies by director
    print("\nMovies directed by 'Wachowski Sisters':")
    print(get_movies_by_director('Wachowski Sisters'))

    # Delete a movie
    print("\nDeleting movie with ID 2...")
    delete_movie(2)

    print("All movies in the database after deletion:")
    print_all_movies()

if __name__ == '__main__':
    main()
sabarish
