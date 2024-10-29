# Configuration for pytest
import pytest
from fastapi.testclient import TestClient
from src.api import app

@pytest.fixture
def sample_fixture():
    return "sample data"

@pytest.fixture
def client():
    return TestClient(app) 