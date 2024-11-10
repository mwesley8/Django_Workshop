from sqlite3 import Date
from selenium import webdriver
import datetime

# Opens the browser
browser = webdriver.Firefox()

# Navigates to the page passed to the getter
browser.get("http://localhost:8000")

assert "Affinity Trucking" in browser.title
print("ok")





























testQuerySet = [
  {
    'id': 1,
    'firstname': 'Maurice',
    'lastname': 'Wesley',
    'phone': 8887755,
    'joined_date': datetime.date(2017, 10, 25)
  },
  {
    'id': 2,
    'firstname': 'Carl',
    'lastname': 'Lewis',
    'phone': 5557777,
    'joined_date': datetime.date(2010, 4, 1)
  },
  {
    'id': 3,
    'firstname': 'Andrew',
    'lastname': 'Henderson',
    'phone': 8889965,
    'joined_date': datetime.date(2015, 12, 24)
  },
  {
    'id': 4,
    'firstname': 'John',
    'lastname': 'Stamos',
    'phone': 8887741,
    'joined_date': datetime.date(2019, 5, 1)
  },
  {
    'id': 5,
    'firstname': 'Tom',
    'lastname': 'Simson',
    'phone': 8886654,
    'joined_date': datetime.date(2022, 9, 29)
  }
]

