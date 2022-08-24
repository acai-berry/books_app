def test_create_book(client):
    # when
    response = client.post(
        "/",
        json={"title": "test_title1", "author": "test_author1", "price": 9.99},
    )
    # then
    data = response.json()
    assert response.status_code == 200, response.text
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert "id" in data
    assert data["id"] == 1


def test_get_all_books(client):
    # when
    response = client.get("/")
    # then
    events = response.json()
    assert response.status_code == 200
    assert len(events) == 1


def test_get_a_book_happy_path(client):
    # when
    response = client.get("/1")
    # then
    data = response.json()
    assert response.status_code == 200, response.text
    assert data["title"] == "test_title1"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == 1


def test_get_a_book_no_book(client):
    # when
    response = client.get("/2")
    # then
    assert response.status_code == 404


def test_update_a_book(client):
    # when
    response = client.put(
        f"/{1}",
        json={"title": "test_title1_updated", "author": "test_author1", "price": 9.99},
    )
    # then
    assert response.status_code == 200
    # when
    response = client.get("/1")
    # then
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "test_title1_updated"
    assert data["author"] == "test_author1"
    assert data["price"] == 9.99
    assert data["id"] == 1


def test_delete_a_book(client):
    # when
    response = client.delete("/1")
    # then
    assert response.status_code == 200
    # when
    response = client.get("/1")
    # then
    assert response.status_code == 404


def test_delete_no_book(client):
    # when
    response = client.delete("/2")
    # then
    assert response.status_code == 404
