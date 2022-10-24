import json
from flask import Flask,render_template,request,redirect,flash,url_for
from datetime import datetime


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def get_max_number_of_places(club_points, number_of_competition_places):
    max_places = 12
    if number_of_competition_places < club_points and number_of_competition_places < 12:
        max_places = number_of_competition_places
    elif club_points < 12:
        max_places = club_points
    return max_places


def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions,
            current_datetime=get_current_datetime()
            )
    except IndexError:
        flash("Sorry, that email wasn't found.")
        return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    current_datetime = get_current_datetime()
    if foundClub and foundCompetition and foundCompetition['date'] > current_datetime:
        max_places = get_max_number_of_places(int(foundClub['points']), int(foundCompetition['numberOfPlaces']))
        return render_template('booking.html',club=foundClub,competition=foundCompetition,max_places=max_places)
    else:
        flash("Something went wrong-please try again")
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions,
            current_datetime=current_datetime
            )


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    max_places = get_max_number_of_places(int(club['points']), int(competition['numberOfPlaces']))
    if placesRequired > max_places:
        flash(f'Please, select a number lower or equal to {max_places}')
        return render_template('booking.html',club=club,competition=competition,max_places=max_places)
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
        flash('Great-booking complete!')
        return render_template(
            'welcome.html',
            club=club,
            competitions=competitions,
            current_datetime=get_current_datetime()
            )


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))