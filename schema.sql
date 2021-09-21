DROP TABLE IF EXISTS posts;
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        name TEXT NOT NULL,
        content TEXT NOT NULL
    );