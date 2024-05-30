import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mahasiswa'
)

cursor = conn.cursor()

cursor.execute(
    """
create trigger before_insert
before insert on mahasiswa
for each row
begin
    set new.grade = case
    when new.nilai >= 90 then 'A'
    when new.nilai >= 85 then 'A-'
    when new.nilai >= 70 then 'B+'
    when new.nilai >= 75 then 'B'
    when new.nilai >= 70 then 'B-'
    when new.nilai >= 60 then 'C'
    when new.nilai >= 55 then 'C-'
    when new.nilai >= 45 then 'D'
    else 'E'
    end;
end
"""
)

cursor.execute(
    """
create trigger before_update
before update on mahasiswa
for each row
begin
    set new.grade = case
    when new.nilai >= 90 then 'A'
    when new.nilai >= 85 then 'A-'
    when new.nilai >= 70 then 'B+'
    when new.nilai >= 75 then 'B'
    when new.nilai >= 70 then 'B-'
    when new.nilai >= 60 then 'C'
    when new.nilai >= 55 then 'C-'
    when new.nilai >= 45 then 'D'
    else 'E'
    end;
end
"""
)

cursor.execute("insert into mahasiswa (nim, nama, nilai) values (1, 'Aaron Jevon', 89)")
conn.commit()