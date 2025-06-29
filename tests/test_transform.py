import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.transform import clean_data


@pytest.fixture
def sample_data():
    return [
        {
            "name": "Python Developer",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "employer": {"name": "Company A"}
        },
        {
            "name": "Data Scientist",
            "salary": {"from": 120000, "to": 180000, "currency": "USD"},
            "employer": {"name": "Company B"}
        },
        {
            "name": "Python Developer",
            "salary": {"from": 90000, "to": 120000, "currency": "EUR"},
            "employer": {"name": "Company C"}
        }
    ]


def test_clean_data_structure(sample_data):
    """Проверяем структуру выходного DataFrame"""
    result = clean_data(sample_data)

    expected_columns = ["name", "salary_from", "salary_to", "salary_currency", "employer_name"]
    assert list(result.columns) == expected_columns


def test_salary_normalization(sample_data):
    """Проверяем нормализацию salary"""
    result = clean_data(sample_data)

    assert result.iloc[0]["salary_from"] == 100000
    assert result.iloc[0]["salary_to"] == 150000
    assert result.iloc[0]["salary_currency"] == "RUR"


def test_employer_normalization(sample_data):
    """Проверяем нормализацию employer"""
    result = clean_data(sample_data)

    assert result.iloc[1]["employer_name"] == "Company B"


def test_duplicates_removal(sample_data):
    """Проверяем удаление дубликатов по полю name"""
    result = clean_data(sample_data)

    assert len(result) == 2
    assert result.iloc[0]["name"] == "Python Developer"
    assert result.iloc[0]["salary_from"] == 100000

