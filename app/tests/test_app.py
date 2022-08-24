def test_create_book(client):
    response = client.post(
        "/",
        json={"title": "test_title1", "author": "test_author1", "price": 9.99},
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert "id" in data
    book_id = data["id"]

    response = client.get(f"/{book_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == book_id


def test_get_all_books(client):
    response = client.get("/")
    events = response.json()
    assert response.status_code == 200
    assert len(events) == 1


def test_get_a_book_happy_path(client):
    response = client.get("/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == 1


def test_get_a_book_no_book(client):
    response = client.get("/2")
    assert response.status_code == 404


def test_update_a_book(client):
    response = client.put(
        f"/{1}",
        json={"title": "test_title1_updated", "author": "test_author1", "price": 9.99},
    )
    assert response.status_code == 200

    response = client.get("/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1_updated"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == 1


def test_delete_a_book(client):
    response = client.delete("/1")
    assert response.status_code == 200

    response = client.get("/1")
    assert response.status_code == 404


def test_delete_no_book(client):
    response = client.delete("/2")
    assert response.status_code == 404
