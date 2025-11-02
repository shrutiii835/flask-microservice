from app import app

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

#This is a small comment added to show the change made