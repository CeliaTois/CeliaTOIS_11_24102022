from server import competitions
import re


class TestBookPlaces:
    def test_book_places(self, client):
        get_response_before_book = client.get("/book/Fall Classic/Simply Lift")

        assert get_response_before_book.status_code == 200

        number_of_places_available_before_book = re.search(
            "Places available: (.*)\n",
            get_response_before_book.data.decode("utf-8")).group(1)

        assert number_of_places_available_before_book == "13"

        post_response = client.post(
            "/purchasePlaces",
            data={
                "places": 3,
                "competition": "Fall Classic",
                "club": "Simply Lift"
                })

        assert post_response.status_code == 200

        get_response_after_book = client.get("/book/Fall Classic/Simply Lift")

        assert get_response_after_book.status_code == 200

        number_of_places_available_after_book = re.search(
            "Places available: (.*)\n",
            get_response_after_book.data.decode("utf-8")).group(1)

        assert number_of_places_available_after_book == "10"
