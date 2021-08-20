from flask import Flask, jsonify, render_template, request
import requests


app = Flask(__name__)

app.config.from_pyfile('settings.py')

server_address = app.config.get("SERVER")


@app.route('/')
def index():
    return "Welcome To UPL"


@app.route('/league', methods=['GET'])
def league():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/leagues?season={parameters.get('season')}"

        querystring = {"country":"Uganda"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])

@app.route('/standing', methods=['GET'])
def standing():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/standings?season={parameters.get('season')}"

        querystring = {"league":"585"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])

@app.route('/teams', methods=['GET'])
def teams():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/teams?season={parameters.get('season')}"

        querystring = {"country":"Uganda" , "league":"585"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])

@app.route('/lineups', methods=['GET'])
def lineups():
  
    url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures/lineups"

    querystring = { "fixture":"215662","team":"12452"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    return res


@app.route('/fixtures', methods=['GET'])
def fixtures():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures?season={parameters.get('season')}"

        querystring = {"league":"585"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])
@app.route('/team-fixtures', methods=['GET'])
def Tfixtures():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures?season={parameters.get('season')}"

        querystring = {"team":"12452"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])
@app.route('/headtohead', methods=['GET'])
def Hfixtures():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead?season={parameters.get('season')}"

        querystring = {"h2h":"33-34"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])

@app.route('/top-scorers', methods=['GET'])
def topscorers():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/players/topscorers?season={parameters.get('season')}"

        querystring = {"league":"39"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])
@app.route('/top-assists', methods=['GET'])
def topassists():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/players/topassists?season={parameters.get('season')}"

        querystring = {"league":"39"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])
@app.route('/top-redcards', methods=['GET'])
def topredcards():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/players/topredcards?season={parameters.get('season')}"

        querystring = {"league":"39"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])
@app.route('/top-yellowcards', methods=['GET'])
def topyellowcards():
    parameters = request.args
  
    if parameters.get('season'):
        url = f"https://api-football-v1.p.rapidapi.com/v3/players/topyellowcards?season={parameters.get('season')}"

        querystring = {"league":"39"}

        headers = {
            'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
            'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()
        return res
    else:  
        return jsonify(['Provide The season year'])

@app.route('/team-info', methods=['GET'])
def teamInfo():
    parameters = request.args
  
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"

    querystring = {"id":"12452"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    return res

@app.route('/venues', methods=['GET'])
def venues():
    parameters = request.args
  
    url = "https://api-football-v1.p.rapidapi.com/v3/venues"

    querystring = {"country":"Uganda"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    return res

@app.route('/transfers', methods=['GET'])
def transfers():
    parameters = request.args
  
    url = "https://api-football-v1.p.rapidapi.com/v3/transfers"

    querystring = {"team":"12452"}

    headers = {
        'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
        'x-rapidapi-key': "2721a1c4f7msheeb20bef5e17d1dp12a29ajsn5696a067e9bd"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    return res




if __name__ == 'main':
    app.run()
