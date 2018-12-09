import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

engine= create_engine('postgres://lsaucmpqckmbeg:5db265b207265c44d1b62a78e0f2c26e120d6d9d767443834e514db7b83cf3c0@ec2-54-235-193-0.compute-1.amazonaws.com:5432/dc76rsns7imnl4')
db =scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL, rating INTEGER NOT NULL,username VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    f=open("books.csv")
    reader =csv.reader(f)
    for isbn,title,author,year in reader:
        if year == "year":
            print('skipped first line')
        else:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)",{"a":isbn,"b":title,"c":author,"d":year})

    print("done")
    db.commit()







if __name__ == "__main__":
    main()
