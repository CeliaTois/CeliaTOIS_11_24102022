from server import app

# def test_get_request(client, live_server):
#     @live_server.app.route('/')
#     def get_endpoint():
#         return url_for('name.index', _external=True)

#     live_server.start()

#     res = client.get(get_endpoint())

#     assert res.status_code == 200


# def test_get_max_number_of_places(competitions, clubs):
#     assert get_max_number_of_places(int(competitions[0]['numberOfPlaces']), int(clubs[0]['points'])) == 13