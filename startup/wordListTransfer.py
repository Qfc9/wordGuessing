import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=postgres user=postgres password=password")
# Open a cursor to perform database operations
cur = conn.cursor()

try:
    # To add our table to the DB
    cur.execute("""
        CREATE TABLE public.words (
            id serial NOT NULL,
            word varchar NOT NULL
        );
    """)

    cur.execute("""
        ALTER TABLE public.words ADD CONSTRAINT words_pk PRIMARY KEY (id);
    """)

    # Push our changes to the table
    conn.commit()

# If it was a duplicate table error
except psycopg2.errors.DuplicateTable as e:
    print("Table already exsists, ignoring and adding words")
    conn.rollback()

# If it was any other type of error
except Exception as e:
    print("Oh no, something bad happened!")
    print(e)
    exit()

# Read from the file
file = open("wordlist", "r")
allTheLinesIfTheFile = file.readlines()
file.close()

for word in allTheLinesIfTheFile:
    temp = word.strip()
    cur.execute("INSERT INTO public.words (word) VALUES(%s);", [temp])
    conn.commit()

conn.close()
