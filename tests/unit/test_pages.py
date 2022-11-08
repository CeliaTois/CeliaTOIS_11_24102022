from flask import request

class TestIndex:
    def test_get_index_page(self, client):
        response = client.get("/")
        assert response.status_code == 200


class TestShowSummary:
    def test_login_with_existing_user(self, client):
        response = client.post("/showSummary", data={"email": "john@simplylift.co"})
        assert response.status_code == 200
    
    def test_login_with_non_existing_user(self, client):
        response = client.post("/showSummary", data={"email": "user@simplylift.co"}, follow_redirects=True)
        assert b"<li>Sorry, that email wasn&#39;t found.</li>" in response.data


class TestBook:
    def test_get_book_page(self, client):
        response = client.get("/book/Fall Classic/Simply Lift")
        assert response.status_code == 200

    def test_get_book_page_with_passed_event(self, client):
        response = client.get("/book/Spring Festival/Simply Lift")
        assert b"<li>Something went wrong-please try again</li>" in response.data

    def test_get_book_page_with_inexisting_event(self, client):
        response = client.get("/book/Fake Event/Simply Lift", follow_redirects=True)
        assert response.status_code == 500


class TestPurchasePlaces:
    def test_purchase_places(self, client):
        response = client.post("/purchasePlaces", data={"places": 3, "competition": "Fall Classic", "club": "Simply Lift"})
        assert response.status_code == 200
        assert b"<li>Great-booking complete!</li>" in response.data

    
    def test_purchase_more_places_than_allowed(self, client):
        response = client.post("/purchasePlaces", data={"places": 13, "competition": "Fall Classic", "club": "Simply Lift"})
        assert b"<li>Please, select a number lower or equal to" in response.data


class TestPointsDisplya:
    def test_get_points_display(self, client):
        response = client.get("/pointsDisplay")
        assert response.status_code == 200


class TestLogout:
    def test_logout_redirect(self, client):
        response = client.get("/logout", follow_redirects=True)
        assert response.status_code == 200
        assert request.path == "/"
