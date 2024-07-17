"""
writing a mini database for testing with peewee framework
"""

# import frameworks
import unittest
from peewee import *

from app import TimelinePost
MODELS = [TimelinePost] # specify tables for testing

# creates a temporary db stored in memory and not disk
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
  # called before each test method
  # connects to db and creates tables
  def setUp(self):
    test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
    test_db.connect()
    test_db.create_tables(MODELS)
  
  # called after each test method
  # removes all data in tables and closes connection
  def tearDown(self):
    test_db.drop_tables(MODELS)
    test_db.close()
  
  def test_timeline_post(self):
    first_post = TimelinePost.create(name="John Doe", email="john@exmaple.com", content="Hello world")
    assert first_post.id == 1 # should be first row of table
    second_post = TimelinePost.create(name="Samin Sarker", email="samin@gmail.com", content="samin was here")
    assert second_post.id == 2 # should be second row of table
    get_first = TimelinePost.get_by_id(1)
    assert get_first.name == "John Doe"
    get_second = TimelinePost.get_by_id(2)
    assert get_second.name == "Samin Sarker"
