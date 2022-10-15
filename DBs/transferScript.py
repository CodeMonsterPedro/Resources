import sqlite3


f = open('data', 'r')
data = f.readlines()

conn = sqlite3.connect('main.db')