import pytest

from .application import TestMe

def test_server():
    assert TestNe().take_five() == 5

def test_port():
    assert TestMe().port() == 8000
