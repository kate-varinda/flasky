def test_get_all_bikes_with_empty_db_returns_empty_list(client):
    response = client.get("/bike")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_bike_with_empty_db_returns_404(client):
    response = client.get("/bike/3")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "message" in response_body

def test_get_one_bike_with_populated_db_returns_bike_json(client, two_bikes):
    response = client.get("/bike/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Speedy",
        "price": 1,
        "size": 6,
        "type": "racing"
    }

def test_post_one_bike_creates_bike_in_db(client, two_bikes):
    response = client.post("/bike", json={
            "name":"shiny", 
            "price":10, 
            "size":3, 
            "type":"gift"
            })
    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["id"] == 3

def test_post_one_bike_to_empty_db_creates_bike_in_db_with_id_1(client):
    response = client.post("/bike", json={
            "name":"shiny", 
            "price":10, 
            "size":3, 
            "type":"gift"
            })
    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["id"] == 1