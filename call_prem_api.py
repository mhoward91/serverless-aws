import requests # type: ignore

print()
player = input("Type a player: ").strip()
req1 = requests.get(f"https://7gie9bueak.execute-api.eu-west-2.amazonaws.com/dev/players/{player}")

req = req1.json()                   
if req1.ok:
    print()
    print(f"{req['player']} - 2019/2020 Premier League Season Statistics playing for {req['team']}:")
    print()
    print(f"Games Played: {req['games_played']}")
    print(f"Games Started: {req['games_started']}")
    print(f"Minutes Played: {req['mins']}")
    print(f"Goals Scored: {req['goals']}")
    print(f"Shots Taken: {req['shots']}")
    print(f"Shots On Target: {req['shots_on_goal']}")
    print(f"Assists: {req['assists']}")
    print()
    print(f"{req['player']}'s Premier League player ranking is {req['rank']}.")
else:
    print("Check your spelling and try again...")
