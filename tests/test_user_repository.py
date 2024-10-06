from unittest.mock import MagicMock, patch

import pytest

from src.api.repository import user_repository


def test_get_db_connection():
    with patch("psycopg2.connect") as mock_connect:
        connection = user_repository.get_db_connection()

        assert connection == mock_connect.return_value
        mock_connect.assert_called_once_with(user_repository.settings.DATABASE_URL)


def test_check_db_connection_success():
    with patch("src.api.repository.user_repository.get_db_connection") as mock_get_conn:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        result = user_repository.check_db_connection()

        assert result == "Connected"
        mock_cursor.execute.assert_called_once_with("SELECT 1")


def test_check_db_connection_failure():
    with patch("src.api.repository.user_repository.get_db_connection") as mock_get_conn:
        mock_get_conn.side_effect = Exception("Test exception")

        result = user_repository.check_db_connection()

        assert result == "Failed to connect to database: Test exception"
