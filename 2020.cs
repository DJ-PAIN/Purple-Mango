// kutivault.APIServer
// Token: 0x0600006C RID: 108 RVA: 0x000026A8 File Offset: 0x000008A8
public static void ADListen()
{
  APIServer.server.Prefixes.Add("http://localhost:2000/");
  APIServer.server.Prefixes.Add("http://" + APIUtils.GetMyLocalIP() + ":2000/");
  try
  {
    for (;;)
    {
      APIServer.server.Start();
      Console.WriteLine("{api} listening");
      HttpListenerContext context = APIServer.server.GetContext();
      string rawurl = context.Request.RawUrl;
      string r = "[]";
      Console.WriteLine("{api} requested! url: " + rawurl + ".");
      byte[] bytepost;
      string post;
      using (MemoryStream getpost = new MemoryStream())
      {
        context.Request.InputStream.CopyTo(getpost);
        bytepost = getpost.ToArray();
        post = Encoding.ASCII.GetString(bytepost);
      }
      if (rawurl.StartsWith("/api/versioncheck/v4"))
      {
        r = "{\"VersionStatus\":0}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/versioncheck/"))
      {
        r = "{\"ValidVersion\":true}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/players/v1/list"))
      {
        Console.WriteLine(post);
        r = "[" + Login.DynPlayer() + "]";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/consumables/v1/getUnlocked"))
      {
        r = Consumables.DebugConsumeableGen();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/communityboard/v1/current"))
      {
        r = Login.notavirus.DownloadString("https://coffeeman240.github.io/CoffeeVaultRBSData/CommunityBoard.json");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/gameconfigs/v1/all"))
      {
        r = File.ReadAllText(Program.DataPath + "\\GC.txt");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/config/v2"))
      {
        r = Config.GetConfig(false);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v1/getcachedlogins"))
      {
        r = Login.GCL();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v2/getcachedlogins"))
      {
        Console.WriteLine(post);
        r = Login.GCLV2();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v3/getcachedlogins"))
      {
        Console.WriteLine(post);
        r = Login.GCLV2();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v1/logincached"))
      {
        r = Login.CLogin();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v2/logincached"))
      {
        r = Login.CLogin();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v3/logincached"))
      {
        Console.WriteLine(post);
        r = Login.CLogin();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v4/logincached"))
      {
        Console.WriteLine(post);
        r = Login.CLogin();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/platformlogin/v3/createaccount"))
      {
        Console.WriteLine(post);
        r = Login.CLogin();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/store"))
      {
        r = "{}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/PlayerReporting/v1/moderationBlockDetails"))
      {
        r = "{\"ReportCategory\":0,\"Duration\":0,\"GameSessionId\":0,\"Message\":\"\"}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/config/v1/amplitude"))
      {
        r = "{\"AmplitudeKey\":\"morbius\"}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/auth/cachedlogin/forplatformid/"))
      {
        r = AccountAuth.CachedLogins();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/accounts/account/bulk"))
      {
        r = AccountAuth.GetAccountsBulk();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/auth/connect/token"))
      {
        Console.WriteLine(post);
        foreach (object obj in context.Request.Headers.Keys)
        {
          string headers = (string)obj;
          Console.WriteLine(headers + " : " + context.Request.Headers[headers]);
        }
        r = AccountAuth.ConnectToken();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/player/login"))
      {
        r = AccountAuth.ConnectToken();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/accounts/account/me"))
      {
        r = JsonConvert.SerializeObject(JsonConvert.DeserializeObject<List<Account>>(AccountAuth.GetAccountsBulk())[0]);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/accounts/account/"))
      {
        r = JsonConvert.SerializeObject(JsonConvert.DeserializeObject<List<Account>>(AccountAuth.GetAccountsBulk())[0]);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/images/v2/named"))
      {
        r = "[{\"FriendlyImageName\":\"DormRoomBucket\",\"ImageName\":\"n/67gesMhbOkCd3-qO1cKkIg\",\"StartTime\":\"2018-09-27T18:00:00Z\",\"EndTime\":\"2222-02-22T22:22:00Z\"}]";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v2/gifts/generate"))
      {
        r = Storefront.GenerateGift();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v2/gifts/consume"))
      {
        Storefront.DisposeAndAwardGift();
        r = "[]";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v2/gifts"))
      {
        r = "[]";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/players/v1/disallowInAppPurchases"))
      {
        r = "true";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/quickPlay/v1/getandclear"))
      {
        r = "true";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/config/v1/cohortnux/"))
      {
        r = Config.CohortNux();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/announcement/v1/get"))
      {
        r = Annoncements.AnnouncementGen();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v3/items"))
      {
        r = File.ReadAllText(Program.DataPath + "\\AVItems.txt");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/rooms/v2/name/"))
      {
        string roomname = rawurl.Substring("/api/rooms/v2/name/".Length);
        r = JsonConvert.SerializeObject(GameSessionsV3.RROS[roomname].Room);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/roomserver/rooms/bulk?name=RecCenter"))
      {
        r = JsonConvert.SerializeObject(GameSessionsV3.GetRoomByName("RecCenter"));
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v4/items"))
      {
        r = File.ReadAllText(Program.DataPath + "\\AVItems.txt");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v2/set"))
      {
        AvatarAPI.SaveAvatar(post);
        r = "i'm saved dummy";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/avatar/v2"))
      {
        r = File.ReadAllText(Program.ProfilePath + "\\avatar.txt");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/players/v1/progression/"))
      {
        r = AccountAuth.GetLevel();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/playerReputation/v1/"))
      {
        r = AccountAuth.GetRep();
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/settings/v2/set"))
      {
        Settings.SaveSettings(post);
        r = "seted deez nutz";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/rooms/v2/name/RecCenter"))
      {
        JsonConvert.SerializeObject(GameSessionsV3.RROS["RecCenter"].Room);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/settings/v2"))
      {
        r = File.ReadAllText(Program.ProfilePath + "\\settings.txt");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/objectives/v1/myprogress"))
      {
        r = File.ReadAllText(Program.DataPath + "\\progress.txt");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/playerevents/v1/all"))
      {
        r = "{\"Created\":[],\"Responses\":[]}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/gamesessions/v4/joinroom"))
      {
        Console.WriteLine(post);
        r = GameSessionsV3.joinRoom(post);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/gamesessions/v2/reportjoinresult"))
      {
        r = JsonConvert.SerializeObject(GameSessionsV3.responce.GameSession);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/auth/v1"))
      {
        Console.WriteLine(post);
        foreach (object obj2 in context.Request.Headers.Keys)
        {
          string headers2 = (string)obj2;
          Console.WriteLine(headers2 + " : " + context.Request.Headers[headers2]);
        }
        r = "uhhhhhhhhhhh";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/presence/v3/heartbeat"))
      {
        Console.WriteLine(post);
        r = "{\"Error\":\"\",\"Presence\":" + JsonConvert.SerializeObject(GameSessionsV3.PresenceV3()) + "}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/rooms/v1/hot"))
      {
        GameSessionsV3.GetMenuRooms();
        r = JsonConvert.SerializeObject(GameSessionsV3.MenuRoom);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/rooms/v2/hot"))
      {
        GameSessionsV3.GetMenuRooms();
        r = JsonConvert.SerializeObject(GameSessionsV3.MenuRoom);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/match/player/statusvisibility"))
      {
        Console.WriteLine(post);
        r = "{}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/match/player/vrmovementmode"))
      {
        Console.WriteLine(post);
        r = "{}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/rooms/v4/details/"))
      {
        r = GameSessionsV3.GetDetails(rawurl.Substring(22));
        goto IL_A79;
      }
      if (rawurl.StartsWith("/roomserver/rooms/"))
      {
        r = GameSessionsV3.GetDetailsV3(rawurl.Substring("/roomserver/rooms/".Length).Replace("?include=301", ""));
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/rooms/v2/"))
      {
        r = GameSessionsV3.GetDetails(rawurl.Substring("/api/rooms/v2/".Length));
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/storefronts/v3/balance/"))
      {
        r = Storefront.GetBalence(int.Parse(rawurl.Substring(rawurl.Length - 1)));
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/images/v4/uploadsaved"))
      {
        r = Images.UplaodtoRecNet(bytepost);
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/images/v1/slideshow"))
      {
        r = Login.notavirus.DownloadString("https://coffeeman240.github.io/CoffeeVaultRBSData/Slideshow.json");
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/sanitize/v1/isPure"))
      {
        r = "{\"IsPure\":true}";
        goto IL_A79;
      }
      if (rawurl.StartsWith("/api/PlayerReporting/v1/hile"))
      {
        r = "{\"Message\":\"\",\"Type\":0}";
        if (APIServer.hileJigInt == 10 && !Program.HasHileJigCompleted)
        {
          break;
        }
        APIServer.hileJigInt++;
        goto IL_A79;
      }
      else
      {
        if (rawurl.StartsWith("/api/rooms/v1/roomRolePermissions"))
        {
          r = GameSessionsV3.GetRole();
          goto IL_A79;
        }
        if (rawurl.StartsWith("/auth/eac/challenge"))
        {
          r = "AQAAABNqojOcpiZUi5XH7cFlnT12bH0gOz+Y6HTej6I+/VCpRlw3sNHZx/wY2AxtDTrpuJmISGr8jiNbpAZ5Sc6NgauMH/Gq6EvCKc5g+o2OUVdwA1xnwTrBXrrR+P72ZWMHJ7Mu3+sdj+4zhW6vowDNzDHzXSkp7CQO9S4xaAk=";
          goto IL_A79;
        }
        if (rawurl.StartsWith("/api/sanitize/v1"))
        {
          Sanitise sans = JsonConvert.DeserializeObject<Sanitise>(post);
          r = "\"" + sans.Value + "\"";
          goto IL_A79;
        }
        if (rawurl.StartsWith("/api/objectives/v1/myprogress"))
        {
          r = Login.notavirus.DownloadString("https://coffeeman240.github.io/CoffeeVaultRBSData/Challenges/objectives.json");
          goto IL_A79;
        }
        if (rawurl.StartsWith("/api/challenge/v1/getCurrent"))
        {
          r = Login.notavirus.DownloadString("https://coffeeman240.github.io/CoffeeVaultRBSData/Challenges/challenges.json");
          goto IL_A79;
        }
        if (rawurl.StartsWith("/config/LoadingScreenTipData"))
        {
          r = File.ReadAllText(Program.DataPath + "\\load.txt");
          goto IL_A79;
        }
        if (rawurl.StartsWith("/api/checklist/v1/current"))
        {
          r = Login.notavirus.DownloadString("https://coffeeman240.github.io/CoffeeVaultRBSData/Challenges/checklist.json");
          goto IL_A79;
        }
        if (rawurl.StartsWith("//video/"))
        {
          try
          {
            byte[] bytess = Login.notavirus.DownloadData("https://coffeeman240.github.io/CoffeeVaultRBSData/Videos/" + rawurl.Substring("//video/".Length));
            context.Response.ContentLength64 = (long)bytess.Length;
            context.Response.OutputStream.Write(bytess, 0, bytess.Length);
            goto IL_AAD;
          }
          catch
          {
            r = "nope";
            goto IL_AAD;
          }
        }
        r = "[]";
        goto IL_A79;
      }
      IL_AAD:
      Thread.Sleep(50);
      APIServer.server.Stop();
      continue;
      IL_A79:
      byte[] bytes = Encoding.UTF8.GetBytes(r);
      context.Response.ContentLength64 = (long)bytes.Length;
      context.Response.OutputStream.Write(bytes, 0, bytes.Length);
      goto IL_AAD;
    }
    APIServer.HileJig();
  }
  catch (Exception ex)
  {
    Console.WriteLine("{api} oh no! error! the server will now restart.");
    File.WriteAllText(Environment.CurrentDirectory + "\\crashlog.txt", ex.ToString());
    Thread.Sleep(5000);
    Program.ExecuteAsAdmin(Environment.CurrentDirectory + "\\COVAULT-19.exe", "");
    Environment.Exit(0);
  }
}
