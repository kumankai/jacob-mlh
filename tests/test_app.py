"""
integration testing between db and api endpoints
"""

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app 

class AppTestCase(unittest.TestCase):
  def setUp(self):
    # creates a test client for flask app
    self.client = app.test_client()
  
  def test_home(self):
    # make a get request to client at base url
    response = self.client.get("/")
    # ensure status code is OK
    assert response.status_code == 200
    # also check the html content
    html = response.get_data(as_text=True)
    assert "<title>Jacob Angga</title>" in html
  
  def test_timeline(self):
    # a get request to api endpoint should return json list of posts
    response = self.client.get("/api/timeline_post")
    assert response.status_code == 200
    assert response.is_json
    json = response.get_json()
    assert "timeline_posts" in json
    assert len(json["timeline_posts"]) == 0 # should be empty

  def test_malformed_timeline_post(self):
    # MISSING name field
    response = self.client.post("/api/timeline_post", data={
      "email": "samin@gmail.com",
      "content": "samin was here"
    })
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid name" in html


    # EMPTY CONTENT FIELD
    response = self.client.post("/api/timeline_post", data={
      "name": "samin",
      "email": "samin@gmail.com",
      "content": ""
    })
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid content" in html


    # MALFORMED EMAIL
    response = self.client.post("/api/timeline_post", data={
      "name": "samin",
      "email": "not a email",
      "content": "samin was here"
    })
    assert response.status_code == 400
    html = response.get_data(as_text=True)
    assert "Invalid email" in html