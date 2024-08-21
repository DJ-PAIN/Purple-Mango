#exit()
from flask import Flask, request, jsonify, send_file, redirect, make_response, url_for, render_template, Response, session
import json
from flask.sessions import NullSession
import requests
import random
import os
import Config
import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import json


from OldRecRoom_API import Player_API, avatar_API


app = Flask("december 23rd 2016")

def index():
    return render_template("main.html"), 200


@app.route("/api/presence/v1/list", methods=["POST"])
def presence_list():
    response_data2 = {
      "Id": 2,
      "PlayerID": 1,
      "RelationshipType": 3,
      "Favorited": 1,
      "Muted": 0,
      "Ignored": 0
    }
    return jsonify(response_data2), 200




@app.route("/api/platformlogin/v1", methods=["POST"])
def platform_login_v2():
    # Assuming login logic goes here (e.g., handle POST data)

    # Create the response data dictionary
    response_data = {
        "Token": "base64EncodedString",
        "PlayerId": "userid",
        "Error": ""
    }

    return response_data




@app.route("/api/versioncheck/v1", methods=["GET"])
def versioncheck_V1():
    # Always return {"ValidVersion": true}
    return jsonify({"ValidVersion": True}), 200



@app.route("/launcher/startup", methods=["GET"])
def launcher_startup():
  return "[Yep that shit went]", 200

@app.route("/img/launcher/<img>", methods=["GET"])
def images_prrfgvrofile_ID(img):
    if os.path.exists(F"images/Launcher/{img}"):
        return send_file(F"images/Launcher/{img}"), 200
    else:
        pfp = requests.get(f"{Config.Data_URL}pfp.png").content
        return Response(pfp, 200, content_type="image/png")



@app.route("/api/config/v2", methods=["GET"])
def config():
    # Placeholder message since the external URL is down
    MessageOfTheDay = "Hi"

    # If you still want to handle errors gracefully for future cases, you can keep the try-except block
    # but just return the placeholder message for now.
    # try:
    #     MessageOfTheDay = requests.get(f"{Config.Data_URL}mesgoftheday.txt").text
    # except RequestException as e:
    #     app.logger.error(f"Failed to fetch MessageOfTheDay: {e}")
    #     MessageOfTheDay = "Hi"

    response = {
        "MessageOfTheDay": MessageOfTheDay,
        "CdnBaseUri": "http://localhost:20182/",
        "LevelProgressionMaps": [{"Level": i, "RequiredXp": i + 1} for i in range(21)],
        "MatchmakingParams": {"PreferFullRoomsFrequency": 1.0, "PreferEmptyRoomsFrequency": 0.0},
        "DailyObjectives": [
            [{"type": 20, "score": 1}, {"type": 21, "score": 1}, {"type": 22, "score": 1}] * 7
        ],
        "ConfigTable": [{"Key": "Gift.DropChance", "Value": "0.5"}, {"Key": "Gift.XP", "Value": "0.5"}],
        "PhotonConfig": {"CloudRegion": "us", "CrcCheckEnabled": False, "EnableServerTracingAfterDisconnect": False}
    }

    return jsonify(response)



@app.route("/api/avatar/v2/gifts/consume/", methods=["POST"])
def consume_gifts():
    return jsonify({'Id': 2, 'UnlockedLevel': 0}), 200



@app.route("/api/avatar/v2", methods=["GET"])
def avatar_V2():
    id = request.headers["X-Rec-Room-Profile"]
    with open("avatars.json", "r") as f:
        avatars = json.load(f)
    for x in avatars:
        if x["id"] == int(id):
            return jsonify(x["avatarData"]), 200
    return "", 200


@app.route("/api/avatar/v2/set", methods=["POST"])
def avatar_V2_SET():
    avatarFile = request.get_json()
    if "id" not in avatarFile:
        return "KeyError: 'id'", 500

    avatar_API.SaveAvatar(
        OutfitSelections=avatarFile["OutfitSelections"],
        HairColor=avatarFile["HairColor"],
        SkinColor=avatarFile["SkinColor"],
        FaceFeatures="",
        avatarFile=avatarFile,
        id=avatarFile["id"]
    )

    avatars = json.load(open("avatars.json", "r"))  # Load avatars from file
    for x in avatars:
        if x["id"] == int(avatarFile["id"]):
            x["avatarData"] = avatarFile["avatarData"]

    with open("avatars.json", "w") as f:
        json.dump(avatars, f)

    return "", 200
  

@app.route("/api/settings/v2/", methods=["GET"])
def settings_V2():
  id = request.headers["X-Rec-Room-Profile"]
  with open("settings.json", "r") as f:
    settings = json.load(f)
  for x in settings:
    if x["id"] == int(id):
      return jsonify(x["settingsData"]), 200
  return "", 200

@app.route("/api/settings/v2/set", methods=["POST"])
def settings_V2_set():
  return ""

@app.route("/api/avatar/v3/items", methods=["GET"])
def avatar_V3_items():
    url = "https://raw.githubusercontent.com/RealMCoded/Rec.js/master/user-info/avataritems.txt"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()  # Parse the JSON response
    except RequestException as e:
        # Log the error and return a friendly message
        app.logger.error(f"Failed to fetch avatar items: {e}")
        data = {"error": "Unable to fetch avatar items."}

    return jsonify(data)

import json
import random
from flask import request, jsonify

import json
import random
from flask import request, jsonify

@app.route("/api/avatar/v2/gifts", methods=["GET"])
def avatar_V2_gifts():
    try:
        with open("Gifts.json", "r") as f:
            gifts_data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading Gifts.json: {e}")
        gifts_data = {}

    try:
        with open("Players.json", "r") as f:
            players_data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print(f"Error loading Players.json: {e}")
        players_data = {}

    headers = request.headers.get("X-Rec-Room-Profile")

    if headers in gifts_data:
        # User has already received their daily XP
        return "[]", 200
    else:
        # User hasn't received their daily XP, add it
        xp_amount = random.randint(10, 100)
        gifts_data[headers] = xp_amount
        with open("Gifts.json", "w") as f:
            json.dump(gifts_data, f)

        # Update user's XP in Players.json
        if headers in players_data:
            players_data[headers]["XP"] += xp_amount
            with open("Players.json", "w") as f:
                json.dump(players_data, f)
        else:
            print(f"User {headers} not found in Players.json")

        return jsonify([
            {
                "Id": 2,
                "AvatarItemDesc": "274cb9b2-2f59-47ea-9a8d-a5b656d148c6",
                "Xp": xp_amount
            }
        ]), 200


@app.route("/api/images/v1/profile/<id>", methods=["GET"])
def images_profile_ID(id):
    if os.path.exists(F"images/{id}.png"):
        return send_file(F"images/{id}.png"), 200
    else:
        pfp = requests.get(f"{Config.Data_URL}pfp.png").content
        return Response(pfp, 200, content_type="image/png")

@app.route("/api/images/v2/profile", methods=["POST"])
def images_v2_profile():
    id = request.headers["X-Rec-Room-Profile"]
    with open("Players.json", "r") as f:
      players = json.load(f)
    for x in players:
      if x["Id"] == int(id):
          if not os.path.exists("images"):
              pass
          image = request.files["image"]
          image.save(f"images/{id}.png")

          Username = x["Username"]
          data = {
            "content": None,
            "embeds": [
              {
                "title": "Account PFP Changed",
                "thumbnail": {
                  "url": f"{Config.URL}api/images/v1/profile/{id}?data={random.randint(1, 999999999999)}"
                }, 
                "timestamp": f"{datetime.datetime.utcnow()}",
                "description": f"@{Username} changed their pfp",
                "color": 16742912,
                }
            ]
          }

          requests.post(Config.console_WebHook, json=data)
          return "", 200

    return "", 401

#Players

@app.route("/api/players/v1/getorcreate", methods=["POST"])
def players_getorcreate():
  PlayName = request.form["Name"]
  with open("Players.json", "r") as f:
    players = json.load(f)
  for x in players:
    if x["steam"] == PlayName:
      return jsonify(x), 200
  return jsonify(Player_API.CreatePlayer(PlayName)), 200

@app.route("/api/players/v1/list", methods=["POST"])
def players_list():
  PlayerData = Player_API.GetPlayerDecember_23rd_2016()
  if PlayerData == "err":
    return jsonify({"error": "the server failed to decode the json file requested."}), 500
  else:
    return jsonify(PlayerData), 200

#GameSession

@app.route("/api/gamesessions/v1/", methods=["GET"])
def gamesessions_V1():
  return "", 403

@app.route("/api/presence/v2", methods=["POST"])
def presence_V2():
  print(request.get_json())
  return "[]", 200




@app.route("/api/config/v1/amplitude", methods=["POST"])
def amplitude():
  return "BrahMan", 200





@app.route("/api/objectives/v1/myprogress", methods=["GET"])
def myprogress():
    # Handle request data if needed (currently not used)
    # request_data = request.get_json()

    # Prepare the response data (replace with actual data retrieval)
    response_data = {
        "Objectives": [
            {"Index": 2, "Group": 0, "Progress": 0.0, "VisualProgress": 0.0, "IsCompleted": True, "IsRewarded": True},
            {"Index": 1, "Group": 0, "Progress": 0.0, "VisualProgress": 0.0, "IsCompleted": True, "IsRewarded": True},
            {"Index": 0, "Group": 0, "Progress": 0.0, "VisualProgress": 0.0, "IsCompleted": True, "IsRewarded": True}
        ],
        "ObjectiveGroups": [
            {"Group": 0, "IsCompleted": False, "ClearedAt": "2021-04-18T01:59:14.8642558"}
        ]
    }

    return jsonify(response_data), 200  # Return JSON response with status code 200


@app.route("/api/activities/charades/v1/words", methods=["POST"])
def charades():
    response_data = {"EN_US": "Free me", "Difficulty": 0}
    return jsonify(response_data), 200



#Admin 

@app.route("/admin", methods=["GET"])
def Admin():
  return render_template("admin/main.html")

@app.route("/admin/login", methods=["GET"])
def Admin_login():
  return render_template("admin/Login.html")


print("nigger")

def run():
    print(f"Running on {Config.URL}")
    app.run(host=Config.ip, port=Config.port)
