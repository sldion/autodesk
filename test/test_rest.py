import pytest
import responses
import requests

from requests_mock_flask import add_flask_app_to_mock

from autodesk.app import app


@responses.activate
def test_responses_no_header() -> None:
    """
    It is possible to use the helper with a ``responses`` decorator.
    """
    add_flask_app_to_mock(
        mock_obj=responses,
        flask_app=app,
        base_url="http://localhost:5000",
    )

    response = requests.get("http://localhost:5000")

    assert response.status_code == 200
    assert response.text == "<p>Hello, World!</p>"


@responses.activate
def test_responses_with_header() -> None:
    add_flask_app_to_mock(
        mock_obj=responses,
        flask_app=app,
        base_url="http://localhost:5000",
    )

    response = requests.get(
        "http://localhost:5000", headers={"Accept": "application/json"}
    )

    assert response.status_code == 200
    assert response.text == '{"message":"Hello, World!"}\n'
