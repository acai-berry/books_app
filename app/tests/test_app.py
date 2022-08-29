from http import HTTPStatus


def test_should_create_a_book(client):
    # given
    payload = {"title": "test_title1", "author": "test_author1", "price": 9.99}
    # when
    response = client.post("/books/", json=payload)
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value, response.text
    payload.update({"id": 1})
    expected_data = payload
    assert data == expected_data


def test_should_get_all_books(client):
    # when
    response = client.get("/books/")
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value
    assert len(data) == 1


def test_should_get_a_book(client):
    # given
    payload = {"title": "test_title1", "author": "test_author1", "price": 9.99, "id": 1}
    # when
    response = client.get("books/1")
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value, response.text
    assert data == payload


def test_should_get_404_error_no_such_book(client):
    # when
    response = client.get("books/2")
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value


def test_should_update_a_book_entry(client):
    # given
    payload = {"title": "test_title1_updated", "author": "test_author1", "price": 9.99}
    # when
    response = client.put("books/1", json=payload)
    response = client.get("books/1")
    # then
    assert response.status_code == HTTPStatus.OK.value
    data = response.json()
    payload.update({"id": 1})
    expected_data = payload
    assert data == expected_data


def test_should_successfully_delete_a_book(client):
    # when
    response = client.delete("books/1")
    # then
    assert response.status_code == HTTPStatus.OK.value


def test_should_get_404_error_attempt_to_delete_nonexisting_book(client):
    # when
    response = client.delete("books/2")
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value
