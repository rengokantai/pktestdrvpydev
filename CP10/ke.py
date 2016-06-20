__author__ = 'Hernan Y.Ke'
import pytest
from .stock import K
@pytest.fixture
def ke():
    return K("k")

def test_k(k):
    assert ke.price is None