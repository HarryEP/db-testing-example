import pytest
from unittest.mock import MagicMock

from database import get_all_messages, get_all_messages_no_with, insert_message


def test_get_all_messages_returns_list():

    fake_connection = MagicMock()

    fake_connection.cursor().__enter__().fetchall.return_value = []

    result = get_all_messages(fake_connection)

    assert isinstance(result, list)


def test_get_all_messages_no_with_returns_list():
    """If my function gets specific things, does it behave in expected ways"""

    fake_connection = MagicMock()

    fake_execute = fake_connection.cursor().execute
    fake_fetch = fake_connection.cursor().fetchall
    fake_fetch.return_value = []

    result = get_all_messages_no_with(fake_connection)

    assert isinstance(result, list)
    assert fake_fetch.call_count == 1
    assert fake_execute.call_count == 1
    assert fake_execute.call_args[0] == ("SELECT * FROM message;",)


"""test insert returns tuple
test error raised if input not str
test .execute() called
test correct sql executed
"""


def test_insert_returns_tuple():

    fake_connection = MagicMock()

    fake_connection.cursor().__enter__().fetchone.return_value = 123, "test"

    result = insert_message(fake_connection, "Hello there!")

    assert isinstance(result, tuple)


def test_insert_raises_error():

    fake_connection = MagicMock
    with pytest.raises(TypeError) as e_info:
        insert_message(fake_connection, 12)


def test_insert_called_once():

    fake_connection = MagicMock()
    insert_message(fake_connection, "hi")
    assert fake_connection.cursor().__enter__.execute().call_count == 1
    # incomplete
