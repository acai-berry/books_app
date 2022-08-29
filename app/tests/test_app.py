from http import HTTPStatus


def test_create_book(client):
    # given
    payload = {"title": "test_title1", "author": "test_author1", "price": 9.99}
    # when
    response = client.post("/", json=payload)
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value, response.text
    payload.update({"id": 1})
    expected_data = payload
    assert data == expected_data


def test_get_all_books(client):
    # when
    response = client.get("/")
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value
    assert len(data) == 1


def test_get_a_book_happy_path(client):
    # given
    payload = {"title": "test_title1", "author": "test_author1", "price": 9.99, "id": 1}
    # when
    response = client.get("/1")
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value, response.text
    assert data == payload


def test_get_a_book_no_book(client):
    # when
    response = client.get("/2")
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value


def test_update_a_book(client):
    # given
    payload = {"title": "test_title1_updated", "author": "test_author1", "price": 9.99}
    # when
    response = client.put(
        f"/{1}",
        json=payload,
    )
    response = client.get("/1")
    # then
    assert response.status_code == HTTPStatus.OK.value
    data = response.json()
    payload.update({"id": 1})
    expected_data = payload
    assert data == expected_data


def test_delete_a_book(client):
    # when
    response = client.delete("/1")
    # then
    assert response.status_code == HTTPStatus.OK.value
    # when
    response = client.get("/1")
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value


def test_delete_no_book(client):
    # when
    response = client.delete("/2")
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value
