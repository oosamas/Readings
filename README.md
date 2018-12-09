#### Name: Osama Saddique
#### Online Demo:  https://youtu.be/ipVblBPnBJw
#### Project Title: Readings- a book review database
#### Class: CCPS 530
####  Instructor: Ghassem Tofighi

When you begin my web app, you will be redirected to the login page where you can sign up.
The password has to be 8 characters long and must be re-typed. A JavaScript function checks that the passwords match during the registration period.

This webapp builds on the API of Goodreads.com. I have incorporated a database of 5000 books (Note: The books.csv file has been taken from Harvard's CS50 Web development using Python and Javasript course on Edx.org). If a user searches for a book that is within the database he/she can review the book, see the average rating, and number of reviews. The ratings information is essentially the API doing its job.

Searching and choosing a book takes you to books.html, wherein layout.html is extended and author, year, ISBN are loaded.
You may review a book, only once, if you try to do it again, you will be told otherwise. Below the review is a link to API that, once clicked, will generate and redirect you to a json file with all data from this app--for the books that you individually have reviewed, etc.
The log out button is at the top right corner, which will end session and take you back.

Workings:

application.py is the main file for this app. It is built in Flask, Python. It uses sessions, sqlalchemy, and markup, among other things. It contains all the routes to different html files, and queries to databases, etc. The database could be locally hosted using DATABASE_URL, but this app uses heroku to host the database.

helpers.py is essentially a one function file, that checks for data in session, if there is
no data found in session, user is re-directed to login.

import.py creates and fills up the database (hosted on heroku) with 5000 books, that were imported from the internet as a csv file.

While all images are held in Static, all html files are held in templates, as is the norm with Flask.
All html files, use a combination of jinja2, CSS, Javascript, and of course bootstrap.
Most of the layout is done using bootstrap (including the login forms, buttons, etc), however, tiny snippets, where a color of text, or different size was required, I have used individual styling using CSS or even HTML.
While I did use jinja, I think the app could have been more optimized had I relieved more heavily on it, instead of using other tools.

![index.html greets the user](https://github.com/oosamas/Readings/blob/master/screenshots/image1.png "index.html")

When the user makes a login, if the passwords dont match, the in-forms warning color light up. The passwords have to be 8 chars long.

![index.html greets the user](https://github.com/oosamas/Readings/blob/master/screenshots/image2.png "index.html with information")

When the user logs in to, he may search for a book by Title, ISBN, author, or a word within the title.
![index.html greets the user](https://github.com/oosamas/Readings/blob/master/screenshots/image4.png "index.html")
The list of all books within the database are presented with the word train. Once you click on the search result
THe website then uses the API to collect information about the book through goodreads.org to showcase the number of ratings on the website and the average number of ratings it has recieved.

You many now give your own rating and review. But if you come back and try to review it again, it wont't let you redo it.
![index.html greets the user](https://github.com/oosamas/Readings/blob/master/screenshots/image3.png "index.html")

