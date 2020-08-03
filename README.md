# SimpleRestApi
The goal of this project is to write a simple Django Rest Application for the cataloging of books. 
The project comprises of two parts:

(I) Server - written in Django, implementing REST functionality. The application has four endpoints:
(a) for a 'GET' call  ('/' address),  the server responds with serialized json version of all the books from the database; 
(b) for a 'POST' call ('/' address), the server saves a new book in the database with the sent json data;
(c) for a 'GET' call ('/book/id'), the server responds with a complete json information of the specified item;
(d) for a 'DELETE' call ('/book/id'), the server deletes the relevant item from the database.

The 'tests.py' file contains suitable tests ensuring that the views classes for specific endpoints work as desired.
The file 'Api/populate_db.py' is a simple python script for populating database with some mock data.

(II) Client - written in HTML and JavaScript, interacting with the Server by the use of AJAX. 
The Server implements a class Book which has its identifier ISBN, title and author. 
The client implements only home page. The website presents all books created in the system - the (a) endpoint. 
The data are read in from the address '/' using AJAX (the (a) endpoint). 
There is a form for creating new books at the top of the website sending data by AJAX (POST method) - 
the (b) endpoint. 
When a user clicks the title of a book, a div with data concerning the book slides down underneath - 
the (c) endpoint. 
Next to the title of a book there is a button to delete the book - the (d) endpoint.

