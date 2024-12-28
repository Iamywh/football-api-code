import requests

def fetch_matches(api_key):
    url = "https://api.football-data.org/v4/competitions/PL/matches"
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        matches = [
            ["Data", "Casa", "Ospite", "Risultato Casa", "Risultato Ospite"]
        ]
        for match in data.get("matches", []):
            matches.append([
                match["utcDate"],
                match["homeTeam"]["name"],
                match["awayTeam"]["name"],
                match["score"]["fullTime"]["homeTeam"],
                match["score"]["fullTime"]["awayTeam"]
            ])
        return matches
    else:
        return f"Errore API: {response.status_code}"

fetch_matches(arg1)
