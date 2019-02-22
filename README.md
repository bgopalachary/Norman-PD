Project 0: Norman PD
The aim of the project is to scrape data from the Norman Police Department website, take data from the pdfs available there and push all the data into a database we create with the help of SQLite. On opening the website, we see pdfs for various things such as daily activity, incidents and arrests. Our job is to take just the arrests and perform the specified operations on it.

Function 1: fetchincidents()
In the first function by making use of the urllib.request package, I downloaded the pdf files from the Norman Police Department website.
An example url is http://normanpd.normanok.gov/filebrowser_download/657/2019-02-18%20Daily%20Arrest%20Summary.pdf
I have obtained the urls from the page and downloaded the files using the urllib.request.urlopen() funtion by passing these urls in to the function.

Function 2: extractincidents()
In this function, I extracted data from the pdfs. In each pdf there were 12 columns . To extract the data I made use of the PyPDF2.PdfFileReader package. This page helps us in extracting the data from the pdfs and returns it in the form of a string.
After we get the string, there is still a lot of work to be done. As the returned string has a lot of extra spaces or commas or other unwanted data in addition to be badly structured.
This is the part where I faced quite a few problems. Firstly, the cleaning of the data consumed a lot of time because each pdf file is different in some ways to the others. By making use of the .replace() function, I replaced and cleaned the data wherever necessary. An example of the .replace() function from my code is-   page1 = page1.replace(" \n"," ")
In some cases, instead of replacing, there was a need to remove things. For this purpose I made use of the strip() function. I made use of a for loop to iterate through all the rows in the pdf whenever there was a nee while striping and replacing.
Even after all this cleaning, there were still some issues in my code when it came to the missing values in the address column. My first thought was to delete those columns in whichever row was necessary but that turned out to be too complicated and did not yield the required results. After some research on the internet, I came across the idea of joining when I saw the join() function. Then, by making use of the join() function, I combined the needed columns and removed the empty elements by making use of the pop() function.
But even after this my code did not work for all the pdfs. This is when I went through all the pdfs again and created a case for each of type of rows. Some rows had a length of 12, some had 11, some had 10 and others less. I use the same join() and pop() functions and wrote the code for each of the mentioned cases. After this when I ran the code it worked.

Function 3: created()
In this function, the objective was to create a database. To do this I made use of the sqlite3 package. I first established a connection. Then I created a cursor object and then by making use of the cursor object I created a database and created a table called arrests in the database. The name of my database is normanpd.db . 
The command I used to create the tables in the database was- 
cursor.execute("CREATE TABLE arrests (arrest_time TEXT,case_number TEXT,arrest_location TEXT,offense TEXT,arrestee_name TEXT,arrestee_birthday TEXT,arrestee_address TEXT,status TEXT,officer TEXT)") 
And finally I used the commit() and close() functions to commit and close the connection.

Function 4: populated()
After the second function, we get the data in a somewhat structured format. This data is pushed in to the tables created in the database in this function. The function I used to create the table was the same function I used to insert elements in to the tables. The only difference was the query I used. Here is the command I used to insert elements into the tables-
c.execute('INSERT INTO arrests VALUES (?,?,?,?,?,?,?,?,?)',page2[i]) 

Function 5: status()
The job of this function is to fetch a random row from the populated database table. The only extra thing to be added is to print this row with the thorn character ( þ ). This extra addition is done by again making use of the join() function and making the thorn character the separator. For the join() function to work right, I created an empty list L[] and joined the already existing list in to in and returning the random row as Random.

Assumptions:
One major assumption i made is the written code will not throw any error for pdfs that are of the same format as that of the pdfs existing in the Norman Police Department website. Any other format might create minor issues. 
My test cases are based on the assumptions that the given url will be avalilable for a while as my test cases are taking data from the url.It is hard coded.

Test Cases:

Test 1: 
In the first test case, i'm checking to see if the downloaded data has been downloaded or not by using the not None command.

Test 2:
In the second test case, the checking is done with regards to the extracted data . I'm checking againg by using the not None command, if any data has been extracted or not.

Test 3:
In the third test case,by using an sql query i'm checking to see if the database table has been created or not. I'm using a variable x into which i'm pushing the return value of the sql query and checking the variable x with the not None command.

Test 4:
In the fourth test, I'm using an sql query to return the values of the table arrests in the form of a variable values. This values is put inside a variable z and i'm checking to see if the value z is not None.

Test 5:
In the last and final test, i'm checking to see if the returned value by the function status is a string or not by using the type()==str condition.

Packages:
urllib.request
PyPDF2
sqlite3

Version:
Python 3.7.2
Sqlite 2.8.17 
