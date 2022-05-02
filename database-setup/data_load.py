import boto3 # type: ignore
from csv import DictReader
from decimal import Decimal

def load_footballers(csv, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="eu-west-2")

    table = dynamodb.Table("Footballers")
    for footballer in csv:
        item = {
        "rank": Decimal(footballer["Rank"]),
        "player": footballer["PLAYER"],
        "team": footballer["TEAM"],
        "games_played": footballer["GP"],    
        "games_started": footballer["GS"],   
        "mins": footballer["MIN"],    
        "goals": footballer["G"],   
        "assists": footballer["ASST"],   
        "shots": footballer["SHOTS"],    
        "shots_on_goal": footballer["SOG"]
        }    
        table.put_item(Item=item)

if __name__ == '__main__':
    with open("player_stats.csv", encoding="utf-8") as csv:
        csv_reader = DictReader(csv)
        load_footballers(csv_reader)
