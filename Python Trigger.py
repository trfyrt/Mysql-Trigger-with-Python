import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',   # Database host address, usually 'localhost' for local server
    user='root',        # Database username
    password='',        # Database password
    database='mahasiswa' # Name of the database
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a BEFORE INSERT trigger
cursor.execute(
    """
    CREATE TRIGGER before_insert
    BEFORE INSERT ON mahasiswa
    FOR EACH ROW
    BEGIN
        -- Set the grade before inserting a new row based on the value of 'nilai'
        SET NEW.grade = CASE
            WHEN NEW.nilai >= 90 THEN 'A'
            WHEN NEW.nilai >= 85 THEN 'A-'
            WHEN NEW.nilai >= 70 THEN 'B+'
            WHEN NEW.nilai >= 75 THEN 'B'
            WHEN NEW.nilai >= 70 THEN 'B-'
            WHEN NEW.nilai >= 60 THEN 'C'
            WHEN NEW.nilai >= 55 THEN 'C-'
            WHEN NEW.nilai >= 45 THEN 'D'
            ELSE 'E'
        END;
    END
    """
)

# Create a BEFORE UPDATE trigger
cursor.execute(
    """
    CREATE TRIGGER before_update
    BEFORE UPDATE ON mahasiswa
    FOR EACH ROW
    BEGIN
        -- Update the grade before updating a row based on the new value of 'nilai'
        SET NEW.grade = CASE
            WHEN NEW.nilai >= 90 THEN 'A'
            WHEN NEW.nilai >= 85 THEN 'A-'
            WHEN NEW.nilai >= 70 THEN 'B+'
            WHEN NEW.nilai >= 75 THEN 'B'
            WHEN NEW.nilai >= 70 THEN 'B-'
            WHEN NEW.nilai >= 60 THEN 'C'
            WHEN NEW.nilai >= 55 THEN 'C-'
            WHEN NEW.nilai >= 45 THEN 'D'
            ELSE 'E'
        END;
    END
    """
)

# Insert a new record into the 'mahasiswa' table
cursor.execute(
    "INSERT INTO mahasiswa (nim, nama, nilai) VALUES (1, 'Aaron Jevon', 89)"
)
# Commit the transaction to make the changes persistent in the database
conn.commit()

# Close the cursor and the database connection
cursor.close()
conn.close()
