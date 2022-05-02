from flask import Flask, json # type: ignore
from flask import jsonify
from flask_restful import Resource, Api, reqparse # type: ignore
import boto3 # type: ignore
import os

app = Flask(__name__)

FOOTBALLERS_TABLE = os.environ["FOOTBALLERS_TABLE"]
client = boto3.client("dynamodb", region_name="eu-west-2") 


@app.route("/players/<player>") 
def get(player):
    resp = client.get_item(
        TableName=FOOTBALLERS_TABLE,
        Key={
            "player": {"S": player}
        }
    )
    item = resp.get("Item")
    if item:
        return jsonify({
            "rank": item.get("rank").get("N"),
            "player": item.get("player").get("S"),
            "team": item.get("team").get("S"),
            "games_played": item.get("games_played").get("S"), 
            "games_started": item.get("games_started").get("S"), 
            "mins": item.get("mins").get("S"),  
            "goals": item.get("goals").get("S"),
            "assists": item.get("assists").get("S"),   
            "shots": item.get("shots").get("S"),       
            "shots_on_goal": item.get("shots_on_goal").get("S")
        }), 200
    else:
        return jsonify({"error": f"{player} does not exist or is misspelt"}), 404


if __name__ == "__main__":
    app.run()
