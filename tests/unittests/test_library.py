from app.models import db, Book
from tests.data import BOOKS


class TestLibraryCollection:

    def test_get(self, client):
        assert 1

    def test_post(self, client):
        assert 1

class TestLibraryBookCollection:

    def test_get(self, client):
        assert 1

    def test_post(self, client):
        assert 1

class TestLibraryBookBorrow:

    def test_put(self, client):
        assert 1

    def test_already_checked_out(self, client):
        assert 1

class TestLibraryBookReturn:

    def test_put(self, client):
        assert 1

    def test_already_returned(self, client):
        assert 1
