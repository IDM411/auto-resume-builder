import sqlite3

def setup_database():
    # This creates a file called resume_memory.db right inside your project folder
    conn = sqlite3.connect('resume_memory.db')
    cursor = conn.cursor()

    # Create the table for your Master Resume
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS MasterResume (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')

    # Create the table for your generated resumes (The Learning Engine)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Generations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_description TEXT NOT NULL,
            generated_json TEXT NOT NULL,
            is_winner BOOLEAN DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()
    print("Success! Database 'resume_memory.db' created and ready to go.")

if __name__ == "__main__":
    setup_database()