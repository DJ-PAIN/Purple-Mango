import os
import json
import random
import Config
import requests
import datetime

def CreatePlayer(steamName):
  UseSteamName = Config.UseSteamNameWhenCreate

  with open("Players.json", "r") as accountDetail:
    accountDetails = json.load(accountDetail)

  with open("NamegenOptions.json", "r") as NamegenOptions:
    NamegenOptions = json.load(NamegenOptions)

  adjectives = NamegenOptions["adjectives"]
  nouns = NamegenOptions["nouns"]

  Name = random.choice(adjectives) + random.choice(nouns) + str(random.randint(1000, 9999))

  nextAvailableId = max([account["Id"] for account in accountDetails]) + 1


  if UseSteamName:
    SteamName1 = steamName
  else:
    SteamName1 = Name



  newAccount = {
    "steam": steamName,
    "Id":int(nextAvailableId),
    "Username":str(Name),
    "DisplayName":SteamName1,
    "Verified":False,
    "Bio": None,
    "XP":0,
    "Level":10,
    "RegistrationStatus":0,
    "Reputation": 0,
    "Developer":False,
    "CanReceiveInvites":True,
    "ProfileImageName":f"{nextAvailableId}.png",
    "JuniorProfile":False,
    "ForceJuniorImages":False,
    "PendingJunior":False,
    "HasBirthday":True,
    "AvoidJuniors":False,
    "PlayerReputation":{
      "Noteriety":0,
      "CheerGeneral":0,
      "CheerHelpful":0,
      "CheerGreatHost":0,
      "CheerSportsman":0,
      "CheerCreative":0,
      "CheerCredit":0,
      "SubscriberCount":0,
      "SubscribedCount":0,
      "SelectedCheer":0
    },"PlatformIds":[
      {
        "Platform":2,
        "PlatformId":1
      }
    ],
    "AdministrativeData":{
      "LastLoginTime":638041373704901902,
      "JoinData":638041373704883267,
      "TrustFactor":0,
      "PermissionFactors":0
    }
  }

  accountDetails.append(newAccount)

  with open("Players.json", "w") as accountDetail:
    json.dump(accountDetails, accountDetail, indent=2)

  with open("avatars.json", "r") as avatarss:
    avatars = json.load(avatarss)

  with open("settings.json", "r") as settingss:
    settings = json.load(settingss)




  NewAvatars = {
    "id": nextAvailableId,
    "avatarData": {
      "OutfitSelections": "b33dbeee-5bdd-443d-aa6a-761248054e08,,,,1;6d48c545-22bb-46c1-a29d-0a38af387143,,,,2;6d48c545-22bb-46c1-a29d-0a38af387143,,,,3;d6b0a1e7-e918-43e5-8191-3a8d9d01df7c,,,,1;102c625b-b988-4bf8-a2aa-a31ad7029cdc,,,,0;abc25091-ed5f-4c72-9364-fffeef1bc239,,,,2;abc25091-ed5f-4c72-9364-fffeef1bc239,,,,3;2cb4f372-3372-4583-8b57-c4e3988e3c28,,,,0;f527ffaf-da03-4519-82ed-46a9cb981dc3,,,,0",
      "HairColor": "befcc00a-a2e6-48e4-864c-593d57bbbb5b",
      "SkinColor": "85343b16-d58a-4091-96d8-083a81fb03ae",
      "FaceFeatures": ""
    }
  }

  NewSettings = {
    "id": nextAvailableId,
    "settingsData": [
      {"Key":"MOD_BLOCKED_TIME","Value":"0"},
      {"Key":"MOD_BLOCKED_DURATION","Value":"0"},
      {"Key":"PlayerSessionCount","Value":"10"},
      {"Key":"ShowRoomCenter","Value":"1"},
      {"Key":"QualitySettings","Value":"3"},
      {"Key":"Recroom.OOBE","Value":"100"},
      {"Key":"VoiceFilter","Value":"2"},
      {"Key":"VIGNETTED_TELEPORT_ENABLED","Value":"0"},
      {"Key":"CONTINUOUS_ROTATION_MODE","Value":"0"},
      {"Key":"ROTATION_INCREMENT","Value":"0"},
      {"Key":"ROTATE_IN_PLACE_ENABLED","Value":"1"},
      {"Key":"TeleportBuffer","Value":"0"},
      {"Key":"VoiceChat","Value":"1"},
      {"Key":"PersonalBubble","Value":"0"},
      {"Key":"IgnoreBuffer","Value":"0"},
      {"Key":"ShowNames","Value":"1"},
      {"Key":"H.264 plugin","Value":"1"},
      {"Key":"USER_TRACKING","Value":"54"},
      {"Key":"google_analytics_clientid_pref_key","Value":"IRPMLQAF1caeb7f2784cd09e15a6e3ad06864ad1ea655c4b"},
      {"Key":"DAILY_LOGIN_DATE","Value":"0"},
      {"Key":"OBJECTIVE_DATE","Value":"0"},
      {"Key":"OBJECTIVE_PROGRESS0","Value":"0"},
      {"Key":"OBJECTIVE_COMPLETED0","Value":"0"},
      {"Key":"OBJECTIVE_PROGRESS1","Value":"0"},
      {"Key":"OBJECTIVE_COMPLETED1","Value":"0"},
      {"Key":"OBJECTIVE_PROGRESS2","Value":"0"},
      {"Key":"OBJECTIVE_COMPLETED2","Value":"0"}
    ]
  }


  settings.append(NewSettings)
  avatars.append(NewAvatars)

  with open("settings.json", "w") as settingss:
    json.dump(settings, settingss, indent=2)

  with open("avatars.json", "w") as accountDetail:
    json.dump(avatars, accountDetail, indent=2)

  pfp = requests.get(f"{Config.Data_URL}pfp.png").content

  with open(f"images/{nextAvailableId}.png", "wb") as f:
    f.write(pfp)

  data = {
    "content": None,
    "embeds": [
      {
        "title": "New Account Created",
        "description": f"Welcome, \"{steamName}\" to OldRecRoom",
        "color": 16742912,
        "timestamp": f"{datetime.datetime.utcnow()}",
        #"thumbnail": {
        #  "url": f"{Config.URL}api/images/v1/profile/{nextAvailableId}"
        #}
      }
    ]
  }

  requests.post(Config.console_WebHook, json=data)

  return newAccount

def GetPlayerDecember_23rd_2016():
  with open("Players.json", "r") as acccs:
    try:
      loadaccounts = json.load(acccs)
    except json.JSONDecodeError:
      return "err"

  for loadaccount in loadaccounts:
    del loadaccount["steam"]
    del loadaccount["Bio"]
    del loadaccount["RegistrationStatus"]
    del loadaccount["Developer"]
    del loadaccount["CanReceiveInvites"]
    del loadaccount["ProfileImageName"]
    del loadaccount["JuniorProfile"]
    del loadaccount["ForceJuniorImages"]
    del loadaccount["PendingJunior"]
    del loadaccount["HasBirthday"]
    del loadaccount["AvoidJuniors"]
    del loadaccount["PlayerReputation"]
    del loadaccount["PlatformIds"]
    del loadaccount["AdministrativeData"]
  return loadaccounts