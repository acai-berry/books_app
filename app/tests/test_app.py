from http import HTTPStatus
import json
from app import main


def test_health(test_client):
    # when
    response = test_client.get(main.app.url_path_for("health"))
    # then
    assert response.status_code == HTTPStatus.OK.value
    assert response.json() == {"health": "It's working ✨"}


def test_should_create_a_book(test_client):
    # given
    test_request_payload = {
        "title": "something",
        "author": "something else",
        "price": 10.0,
    }
    test_response_payload = {
        "id": 1,
        "title": "something",
        "author": "something else",
        "price": 10.0,
    }

    # when
    response = test_client.post(
        main.app.url_path_for("add_book"),
        data=json.dumps(test_request_payload),
    )
    # then
    assert response.status_code == HTTPStatus.CREATED.value
    assert response.json() == test_response_payload


def test_should_get_a_book(test_client):
    # given
    test_data = {
        "id": 1,
        "title": "something",
        "author": "something else",
        "price": 10.0,
    }
    # when
    response = test_client.get(main.app.url_path_for("get_book", book_id=1))
    # then
    assert response.status_code == HTTPStatus.OK.value
    assert response.json() == test_data


def test_should_get_404_error_no_such_book(test_client):
    # when
    response = test_client.get(main.app.url_path_for("get_book", book_id=999))
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value
    assert response.json()["detail"] == "Book with such ID not found"


def test_should_get_all_books(test_client):
    # when
    response = test_client.get(main.app.url_path_for("get_all_books"))
    # then
    data = response.json()
    assert response.status_code == HTTPStatus.OK.value
    assert len(data) == 1


def test_should_update_a_book_entry(test_client):
    # given
    test_update_data = {
        "title": "test_title1_updated",
        "author": "test_author1",
        "price": 9.99,
    }
    expected_data = {
        "id": 1,
        "title": "test_title1_updated",
        "author": "test_author1",
        "price": 9.99,
    }

    # when
    response = test_client.put(
        main.app.url_path_for("update_book", book_id=1),
        data=json.dumps(test_update_data),
    )
    # then
    assert response.status_code == HTTPStatus.OK.value
    assert response.json() == expected_data


def test_should_successfully_delete_a_book(test_client):
    # when
    response = test_client.delete(main.app.url_path_for("delete_book", book_id=1))
    # then
    assert response.status_code == HTTPStatus.OK.value
    assert response.json()["detail"] == "Successfully deleted!"


def test_should_get_404_error_attempt_to_delete_nonexisting_book(test_client):
    # when
    response = test_client.delete(main.app.url_path_for("update_book", book_id=999))
    # then
    assert response.status_code == HTTPStatus.NOT_FOUND.value
    assert response.json()["detail"] == "Book with such ID not found"
