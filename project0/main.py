import urllib.request 
import tempfile
from PyPDF2 import PdfFileReader
import sqlite3
from sqlite3 import Error


def fetchincidents(url):
    data = urllib.request.urlopen(url).read()
    return(data)

def extractincidents(b):

    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(b)

    # Set the curser of the file back to the begining
    fp.seek(0)
    # Read the PDF
    pdfReader = PdfFileReader(fp)
    pdfReader.getNumPages()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText().replace("Officer","Officer;")
    page1 = page1.replace(" \n"," ")
    page1 = page1.replace("-\n","-").replace('\nD - DUS','D - DUS')
    list1= page1.split(';')
    list1=list1[0:len(list1)-1]
    for i in range(len(list1)):
        list1[i]=list1[i].strip('\n')
        list1[i]=list1[i].replace('\n',',')
    global page2
    page2=[sub.split(',') for sub in list1]
    #print(page2)
    for i in range(1,len(page2)):
         if (len(page2[i])==12):
            page2[i][6]= ' '.join(page2[i][6:10])
            page2[i][7]= page2[i][10]
            page2[i][8]= page2[i][11]
            page2[i].pop()
            page2[i].pop()
            page2[i].pop()
     
         elif(len(page2[i])==11):
            page2[i][6]= ' '.join(page2[i][6:9])
            page2[i][7]= page2[i][9]
            page2[i][8]= page2[i][10]
            page2[i].pop()
            page2[i].pop()
         elif(len(page2[i])==10):
            page2[i][6]= ' '.join(page2[i][6:8])
            page2[i][7]= page2[i][8]
            page2[i][8]= page2[i][9]
            page2[i].pop()
         else:
            page2[i] = page2[i]
    del page2[0]
    return page2
def createdb():
    try:
     conn = sqlite3.connect('normanpd.db')
    except Error as e:
        print(e)
    db_file="normanpd.db"
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS arrests")
    try:
        cursor.execute("CREATE TABLE arrests (arrest_time TEXT,case_number TEXT,arrest_location TEXT,offense TEXT,arrestee_name TEXT,arrestee_birthday TEXT,  arrestee_address TEXT,status TEXT,officer TEXT)")
        db_file.commit()
        db_file.close()
    except:
        pass
    return 'normanpd.db'
def populatedb(db,page2):
    conn = sqlite3.connect(db)
    c=conn.cursor()
    for i in range(len(page2)):
     c.execute('INSERT INTO arrests VALUES (?,?,?,?,?,?,?,?,?)',page2[i])
    values= c.execute('SELECT * from arrests' )
    conn.commit()
    conn.close()
    return values
def status(db):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute("SELECT COUNT(*) FROM arrests")
    total_row_count=c.fetchone()[0]
    print('Random row from normanpd.db database:\n')
    c.execute("SELECT * FROM arrests ORDER BY RANDOM() LIMIT 1;")
    for row in c.fetchall():
        L=[]
        L = row
        Random='þ'.join(L)
        print(Random)
        return Random
    conn.commit()
    conn.close()

# -*- coding: utf-8 -*-
# Example main.py
import argparse
def main(url):
    # Download data
    result=fetchincidents(url)
    # Extract Data
    incidents = extractincidents(result)
    # Create Dataase
    db = createdb()
    # Insert Data
    populatedb(db, incidents)
    # Print Status
    status(db)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--arrests", type=str, required=True,
                         help="The arrest summary url.")
    args = parser.parse_args()
    if args.arrests:
        main(args.arrests)
