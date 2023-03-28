from server import get_current_datetime, get_max_number_of_places
from datetime import datetime


class TestCurrentDatetime:
    def test_get_current_datetime(self):
        assert (get_current_datetime() ==
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


class TestMaxNumberOfPlaces:
    def test_number_of_competition_places_is_max(self):
        assert get_max_number_of_places(
            club_points=14, number_of_competition_places=9) == 9

    def test_club_points_is_max(self):
        assert get_max_number_of_places(
            club_points=7, number_of_competition_places=9) == 7

    def test_max_places_is_max(self):
        assert get_max_number_of_places(
            club_points=14, number_of_competition_places=15) == 12
