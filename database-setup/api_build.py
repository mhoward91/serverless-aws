from flask import Flask # type:ignore
from flask_restful import Resource, Api, reqparse # type: ignore
import pandas as pd # type: ignore

app = Flask(__name__)
api = Api(app)


class Players(Resource):
    
    def get(self):
        data = pd.read_csv("./database-setup/player_stats.csv")
        data = data.to_dict()
        return {"data": data}, 200

    def post(self):
        parser = reqparse.RequestParser()   # initialise parser
        
        parser.add_argument("Rank", required=False)
        parser.add_argument("PLAYER", required=True)
        parser.add_argument("TEAM", required=True)
        parser.add_argument("GP", required=False)
        parser.add_argument("GS", required=False)

        args = parser.parse_args()  # parse args to dict

        data = pd.read_csv("./database-setup/player_stats.csv")
        if args["PLAYER"] in list(data["PLAYER"]):
            return {"message": f"""'{args["PLAYER"]}' already exists"""}, 401
        else:
            # create new df with new values
            new_player = pd.DataFrame({
                "Rank": args["Rank"],
                "PLAYER": args["PLAYER"],
                "TEAM": args["TEAM"],
                "GP": args["GP"],
                "GS": args["GS"]
            }, index=[0])

            data = pd.read_csv("./database-setup/player_stats.csv")
            data = data.append(new_player, ignore_index=True)
            data.to_csv("./database-setup/player_stats.csv", index=False)
            return {"data": data.to_dict()}, 200
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("PLAYER", required=True)
        args = parser.parse_args()

        data = pd.read_csv("./database-setup/player_stats.csv")

        if args["PLAYER"] in list(data["PLAYER"]):
            data = data[data["PLAYER"] != args["PLAYER"]] 
            data.to_csv("./database-setup/player_stats.csv", index=False)
            return {"data": data.to_dict()}, 200
        else:
            return {"message": f"{args['PLAYER']} player not found."}, 404


api.add_resource(Players, "/players")

if __name__ == "__main__":
    app.run()
