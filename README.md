# Serverless-AWS

A serverless deployment of a Flask REST API on AWS. I challenged myself to see code through to deployment, and learn about some common serverless infrastructure.   

## Description

The API endpoint retrieves player data for a selected player, based on their statistics from the 2019/20 English Premier League season. An Amazon DynamoDB NoSQL database serves as the backend database for the project, which I created from a publicly available csv file.

The Flask app (api.dynamo.py) is deployed as an AWS Lambda function, using an API Gateway to expose its endpoint. Calling the endpoint will fetch data from the DynamoDB and respond back with player data. The architecture is totally serverless.

## Getting Started

### URL

https<nolink>://7gie9bueak.execute-api.eu-west-2.amazonaws.com/dev/players/\<player\>

- **URL Parameters** `GET`

    `player=[str]` (required) 
  
### Available methods

| Method   | Description                              |
| -------- | ---------------------------------------- |
| `GET`    | Returns a `dict` of data for a single player, identified by the \<player\> parameter|

### Available data
- team 
- games_played
- games_started
- mins
- goals
- shots
- shots_on_goal
- assists
- rank

## Sample calls (from Python)

In order to call the API endpoint from a python program, install the `requests` module from PyPI:

```python
$ pip install requests
```

### Executing a request
  
#### Example 1 - request all data for Marcus Rashford:
  
``` python
import requests

stats = requests.get("https://7gie9bueak.execute-api.eu-west-2.amazonaws.com/dev/players/Marcus%20Rashford").json()
print("Marcus Rashford statistics:", stats, sep="\n\n")
```

#### Response

```python
'Marcus Rashford statistics:'

{'assists': '7.0', 'games_played': '31', 'games_started': '31', 'goals': '17.0', 'mins': '2653.0', 'player': 'Marcus Rashford', 'rank': '9', 'shots': '77.0', 'shots_on_goal': '44.0', 'team': 'Manchester United'}
```
#### Example 2 - request team & goal data for Harry Kane:

``` python
import requests
  
req = requests.get("https://7gie9bueak.execute-api.eu-west-2.amazonaws.com/dev/players/Harry%20Kane").json()
print(f"{req['player']} played for {req['team']}, and scored {req['goals']} goals.")
```

#### Response

```python
"Harry Kane played for Tottenham Hotspur, and scored 18 goals."
```

## Repository file guide


| File   | Description                              |
| -------- | ---------------------------------------- |
| [api_dynamo.py](https://github.com/mhoward91/serverless-aws/blob/master/api_dynamo.py) | The primary Flask API |
| [call_prem_api.py](https://github.com/mhoward91/serverless-aws/blob/master/call_prem_api.py) | Takes user input to select a player, and calls the API to return cleanly structured data |
| [data_load.py](https://github.com/mhoward91/serverless-aws/blob/master/database-setup/data_load.py) | Loading of player data from the original csv file to the DynamoDB database |
| [api_build.py](https://github.com/mhoward91/serverless-aws/blob/master/database-setup/api_build.py) | Flask RESTful API with `GET`, `POST` and `DELETE` requests to modify the csv data file. Not deployed |

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Final word
For more API development, including authentication elements, please refer to my [REST-APIs-Flask repository.](https://github.com/mhoward91/REST-APIs-Flask)
