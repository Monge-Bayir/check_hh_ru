from unittest.mock import patch
import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.extract import extract_data


@pytest.fixture
def mock_api_response():
    """Фикстура с мок-ответом от API HH"""
    return {
        "items": [
            {"id": "1", "name": "Data Engineer", "salary": None},
            {"id": "2", "name": "Junior Data Engineer", "salary": {"from": 100000}}
        ]
    }



def test_extract_data_error_handling():
    """Проверяем обработку ошибок запроса"""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("API error")

        with pytest.raises(Exception, match="API error"):
            extract_data()