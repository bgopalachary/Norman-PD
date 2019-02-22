import pytest
import sqlite3
from sqlite3 import Error
import project0
from project0 import main

url= "http://normanpd.normanok.gov/filebrowser_download/657/2019-02-18%20Daily%20Arrest%20Summary.pdf"

def test_download_sanity():
    
    assert main.fetchincidents(url) is not None

def test_extractincidents():
    
    result=main.fetchincidents(url)
    incidents = main.extractincidents(result)
    assert main.extractincidents(result) is not None

def test_createdb():
      
    result=main.fetchincidents(url)
    incidents = main.extractincidents(result)
    conn = sqlite3.connect('normanpd.db')
    db = main.createdb()
    main.populatedb(db, incidents)
    cursor = conn.cursor()
    x=cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{arrests}';")
    assert x is not None

def test_populatedb():
    result=main.fetchincidents(url)
    incidents = main.extractincidents(result)
    conn = sqlite3.connect('normanpd.db')
    db = main.createdb()
    z=main.populatedb(db,incidents)
    assert z is not None

def test_status():
    result=main.fetchincidents(url)
    incidents = main.extractincidents(result)
    db = main.createdb()
    main.populatedb(db,incidents)
    y=main.status(db)
    assert type(y) == str
    

