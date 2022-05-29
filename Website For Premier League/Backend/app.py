import json
import decimal
from datetime import date

from flask import Flask, request, jsonify, abort, session, redirect, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import mysql.connector

cursor = mysql.connector.connect(
 host="sql4.freemysqlhosting.net",
 user="sql4489693",
 password="siR2x9tU2A",
 database="sql4489693"
)



app = Flask(__name__)

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return (float(o) for o in [o])
        elif isinstance(o, date):
            return str(o.strftime("%Y-%m-%d"))
        else:
            return super(DecimalEncoder, self).default(o)

#LOCAl
# app.config["MYSQL_USER"] = "root"
# app.config["MYSQL_PASSWORD"] = "welcome123"
# app.config["MYSQL_HOST"] = "localhost"
# app.config["MYSQL_DB"] = "PremierLeague"
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# app.config["JSON_AS_ASCII"] = False


app.config["MYSQL_USER"] = "sql4489693"
app.config["MYSQL_PASSWORD"] = "siR2x9tU2A"
app.config["MYSQL_HOST"] = "sql4.freemysqlhosting.net"
app.config["MYSQL_DB"] = "sql4489693"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["JSON_AS_ASCII"] = False


# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)



# app.json_encoder = DecimalEncoder
mysql = MySQL(app)


#Login Form 
@app.route("/api/login/", methods = ['POST'])
@cross_origin(supports_credentials=True)
def login_post():
    if (
        not request.json
        or not "email" in request.json
        or not "password" in request.json
        ):
            return "something missing", 400

    cursor = mysql.connection.cursor()
    email = str(request.json['email'])
    password = str(request.json['password'])
    
    query = "SELECT * FROM `user`\
             WHERE userEmail = %s\
                   AND password = %s;"
    
    cursor.execute(query, (email,password))
    data = cursor.fetchall()

    if len(data) == 0:
        return "Incorrect User name or Password",400
    

    return "Logged In Successfully",200


#Simple Logout
@app.route("/api/logout/", methods=["POST"])
def logout():
    return "logged out Successfully",200


#Write Review in a specific Match
@app.route("/api/matches/<string:season>/<string:homeTeam>/<string:awayTeam>/writereview/", methods=["POST"])
def matchReview(season,homeTeam,awayTeam):
    if (
            not request.json
            or not "rating" in request.json
            or not "review" in request.json
            or not "email" in request.json
        ):
            return "something missing", 400

    userEmail = str(request.json['email'])
    rating    = float(request.json['rating'])/10.0
    review    = str(request.json['review'])

    #Rating should be between 0 and 1 
    if(rating > 1 or rating < 0):
        return HttpResponseBadRequest("Rating is not between 0 and 1")
        
    season = season.replace('-','/')
    print("HI", season)
    homeTeam = homeTeam.replace('-',' ')
    awayTeam = awayTeam.replace('-',' ')
    print(season," " ,homeTeam, " ",awayTeam, " " ,rating," " ,review)
    # print(season, homeTeam, awayTeam)
    
    cursor = mysql.connection.cursor()
    try:    
        cursor.execute("INSERT INTO usermatchreview (userEmail, matchSeason,homeClubName,awayClubName,rating,textReview) VALUES(%s,%s,%s,%s,%s,%s)",(userEmail, season, homeTeam, awayTeam, rating, review))
        mysql.connection.commit()
    except: 
        return "You have already a review in this Match!",404

    return "Submission has been recorded Successfully",200



#Get All Matches
@app.route("/api/matches/", methods = ['GET'])
def matches():
    cursor = mysql.connection.cursor()
    query = f"""SELECT * FROM `match`;"""
    cursor.execute(query)
    matches = cursor.fetchall()
    
    return jsonify(matches)

#Get All Reviews for a specific Match using dynamic URL 
@app.route("/api/matches/<string:season>/<string:homeTeam>/<string:awayTeam>/allreview/", methods=["GET"])
def getAllReviews(season,homeTeam,awayTeam):
  
    season = season.replace('-','/')
    homeTeam = homeTeam.replace('-',' ')
    awayTeam = awayTeam.replace('-',' ')
    print(season, homeTeam, awayTeam)
    
    cursor = mysql.connection.cursor()
    query = "\
            SELECT userEmail, matchSeason, homeClubName, awayClubName, rating , textReview \
            FROM usermatchreview \
            WHERE matchSeason = %s\
            AND homeClubName = %s\
            AND awayClubName = %s;"
    cursor.execute(query, (season,homeTeam, awayTeam))
    
    # except: 
    #     return "Recheck your inputs again!"

    data = cursor.fetchall()

    return jsonify(data)


# get reviews of a specific match using search 
@app.route("/api/getmatchreview/", methods=["POST"])
def getMatchReview():
    cursor = mysql.connection.cursor()

    season = str(request.json['season'])
    homeTeam    =   str(request.json['homeTeam'])
    awayTeam    =   str(request.json['awayTeam'])

    query = "\
            SELECT userEmail, matchSeason, homeClubName, awayClubName, rating , textReview \
            FROM usermatchreview \
            WHERE matchSeason = %s\
            AND homeClubName = %s\
            AND awayClubName = %s;"
    
    cursor.execute(query, (season,homeTeam, awayTeam))
    
    data = cursor.fetchall()


    return jsonify(data)   





@app.route("/api/user/<string:email>/", methods=["GET"])
def getuserInfo(email):
    cursor = mysql.connection.cursor()

    query = "SELECT  userEmail, userName, gender, birthDate, favouriteClubName\
            FROM `user` u\
            WHERE u.userEmail = %s;"

    cursor.execute(query,(email,))
    data = cursor.fetchall()

    return jsonify(data)



@app.route("/api/user/<string:email>/allreviews/", methods=["GET"])
def reviewUserInfo(email):
    cursor = mysql.connection.cursor()

    query = "SELECT matchSeason, homeClubName, awayClubName, rating, textReview\
            FROM `user` u INNER JOIN usermatchreview  ur ON u.userEmail = ur.userEmail\
            WHERE u.userEmail = %s;"

    cursor.execute(query,(email,))
    data = cursor.fetchall()

    return jsonify(data)


@app.route("/api/register/", methods=["POST"])
def register():
    print(request.json)
    if (
        not request.json
        or not "username" in request.json
        or not "email" in request.json
        or not "password" in request.json
        or not "birthdate" in request.json
        or not "favouriteClubTeam" in request.json
        or not "gender" in request.json
    ):
        return "something missing", 400


    userEmail = str(request.json["email"])
    username = str(request.json["username"])
    password = str(request.json["password"])
    birthdate = str(request.json["birthdate"])
    favouriteTeam = str(request.json["favouriteClubTeam"])
    gender = str(request.json["gender"])

    cursor = mysql.connection.cursor()
    #Handling the corner cases 
    #what if the email already exists, user name exists, or password less than 8 in temrs of length 
    query1 = "SELECT * FROM `user`"
    cursor.execute(query1) 
    users = cursor.fetchall()
    users = list(users)
    if len(password) < 8: 
        return "This password length is very low!",400
    print("ABOVE,", userEmail, " ", username)
    print(users)
    for user in users:
        if(len(user) < 2):
            continue
        if userEmail == user['userEmail']:
            return HttpResponseBadRequest("This Email already exists!")
        elif username == user['userName']:
            return HttpResponseBadRequest("This User Name already exists!")
    #Use try and catch for any other errors during insertion 
    
    cursor = mysql.connection.cursor()

    try: 
        query = "INSERT INTO `user` VALUES(%s,%s,%s,%s,%s,%s)"

        cursor.execute(query, (userEmail, username, password, gender, birthdate, favouriteTeam))
        
        mysql.connection.commit()

    except: 
        return "The Email or User Name you have entered already exists",400

    
    return "Registered Successfully",200

@app.route("/api/teams/<pk>/", methods=["GET"])
def teamInfo(pk):
    #clubName clubWebsite stadiumName playerName season clubWebsite dataOfBirth
    cursor = mysql.connection.cursor()
    print(pk)
    query = "SELECT *\
        FROM club C inner Join playerinclubseason pf\
        ON C.clubName = pf.clubName\
        AND C.clubName = %s"
    
    cursor.execute(query, (pk.replace("-"," "),))
    
    teamInfo = cursor.fetchall()
    for t in teamInfo: 
         t['dateOfBirth'] = str(t['dateOfBirth'].strftime("%Y-%m-%d"))
    # mysql.connection.commit()

    # print(teamInfo)
    return jsonify(teamInfo)


@app.route("/api/teams/<clubName>/<season>/", methods=["GET"])
def squadInSeason(clubName, season):
    #clubName clubWebsite stadiumName playerName season clubWebsite dataOfBirth
    cursor = mysql.connection.cursor()
    query = "SELECT *\
        FROM club C inner Join playerinclubseason pf\
        ON C.clubName = pf.clubName\
        AND C.clubName = %s\
        AND season = %s;"
    
    cursor.execute(query, (clubName.replace("-"," "),season.replace("-","/")))
    
    teamInfo = cursor.fetchall()
    for t in teamInfo: 
         t['dateOfBirth'] = str(t['dateOfBirth'].strftime("%Y-%m-%d"))
    # mysql.connection.commit()

    # print(teamInfo)
    return jsonify(teamInfo)

@app.route("/api/teams/", methods=["GET"])
def teams():

    #clubName clubWebsite stadiumName playerName season clubWebsite dataOfBirth

    query = "SELECT * FROM club;"
   
    cursor = mysql.connection.cursor()

    cursor.execute(query)
    teams = cursor.fetchall()

    return jsonify(teams)


@app.route("/api/players/", methods=["GET", "POST"])
def players():
    if request.method == "GET":
        #clubName clubWebsite stadiumName playerName season clubWebsite dataOfBirth

        query = "SELECT playerName,nationality FROM player;"
    
        cursor = mysql.connection.cursor()

        cursor.execute(query)
        players = cursor.fetchall()
 
        return jsonify(players)


    elif request.method == "POST": #POST 
        nationality = request.json["nationality"]
        
        print(nationality)

        query = "SELECT * FROM player p \
                WHERE p.nationality = %s;"
    
        cursor = mysql.connection.cursor()

        try:
            cursor.execute(query,(nationality,))
            players = cursor.fetchall()
        
        except: 
            return "something Wrong",404

        for player in players: 
                player['dateOfBirth'] = str(player['dateOfBirth'].strftime("%Y-%m-%d"))

        # if(len)
        return jsonify(players)



@app.route("/api/players/<string:Name>/", methods=["GET"])
def playerInfo(Name):

    cursor = mysql.connection.cursor()

    query = "\
            SELECT *\
            FROM player p inner Join playerinclubseason pf ON p.playerName = pf.playerName\
            WHERE (p.playerName) = %s"	
    

    Name = Name.replace("."," ")
    print(Name)
    cursor.execute(query, (Name,))
    playerInfo = cursor.fetchall()
    playersInfo = list(playerInfo)
    for playerInfo in playersInfo:
        playerInfo['dateOfBirth'] = str(playerInfo['dateOfBirth'].strftime("%Y-%m-%d"))
        playerInfo['pf.dateOfBirth'] = str(playerInfo['pf.dateOfBirth'].strftime("%Y-%m-%d"))

        

    print(playersInfo)


    return jsonify(playersInfo)


 

@app.route("/api/playerInfoFromName/", methods = ["POST"])

def playerInfoFromName():
    data = request.get_json()
    firstName = data['firstName']
    fullName = ""
    fullName += firstName
    lstName = data['lastName']

    if len(lstName) != 0:
        fullName +=" "
        fullName += lstName
    


    cursor = mysql.connection.cursor()

    query = "\
            SELECT *\
            FROM player p inner Join playerinclubseason pf ON p.playerName = pf.playerName\
            WHERE (p.playerName) = %s"	
    
    try:
        cursor.execute(query, (fullName,))
        playerInfo = cursor.fetchall()
        playersInfo = list(playerInfo)
        
        for playerInfo in playersInfo:
            playerInfo['dateOfBirth'] = str(playerInfo['dateOfBirth'].strftime("%Y-%m-%d"))
            playerInfo['pf.dateOfBirth'] = str(playerInfo['pf.dateOfBirth'].strftime("%Y-%m-%d"))
    except: 
        return "This Name Does not Exist", 404
    
    
    return jsonify(playersInfo)




@app.route("/api/stadium/", methods=["POST", "GET"])
def homeTeamFromStadium():
    if request.method == 'POST':
            
        query = "\
                        select clubName \
                        from club C INNER JOIN stadium S \
                        ON C.stadiumName = S.stadiumName \
                        AND S.stadiumName = %s"
        
        cursor = mysql.connection.cursor()

        cursor.execute(query, (request.json['stadium'],))
        teamName = cursor.fetchall()
        
        return jsonify(teamName)
    elif request.method == 'GET':
        query = "select * from stadium;"
        cursor = mysql.connection.cursor()
        
        cursor.execute(query)
        info = cursor.fetchall()

        return jsonify(info)

@app.route("/api/stadium/<string:stadiumName>", methods=["GET"])
def stadiumInfo(stadiumName):
        query = "select * from stadium s inner join club c ON c.stadiumName = s.stadiumName AND s.stadiumName = %s;"
        cursor = mysql.connection.cursor()
        
        cursor.execute(query, (stadiumName.replace("-"," "),))
        info = cursor.fetchall()

        return jsonify(info)



@app.route("/api/positions/", methods=["POST"])
def showAllPlayersForACertainPosition():
    cursor = mysql.connection.cursor()

    query = "\
            SELECT * \
            FROM player \
            where player.position = %s\
            "
    cursor.execute(query, (request.json["position"],))
    
    players = cursor.fetchall()

    for playerInfo in players:
        playerInfo['dateOfBirth'] = str(playerInfo['dateOfBirth'].strftime("%Y-%m-%d"))    

    return jsonify(players)


#BONUS
@app.route("/api/teamcity/", methods=["POST"])
def showAllTeamsInGivenCity():

    query = "\
            select C.clubName \
            from club C INNER JOIN stadium S \
            ON C.stadiumName = S.stadiumName\
            AND S.addressCity = %s\
            "
    cursor = mysql.connection.cursor()
    cursor.execute(query, (request.json['city'],))
    
    teams = cursor.fetchall()
    
    return jsonify(teams)



# TOP TEAM 

@app.route("/api/toptenteams/", methods=["GET"])
def topTenTeamsByMatch():
    
    query = "\
        SELECT C.ClubName,  SUM(CASE\
            WHEN C.ClubName = M.homeClubName AND M.HomeGoals > M.awayGoals THEN 1\
            WHEN C.ClubName = M.awayClubName AND M.AwayGoals > M.homeGoals THEN 1\
            ELSE 0\
        END) As Score\
        FROM club C INNER JOIN `match` M\
        ON C.clubName = M.homeClubName OR C.ClubName = M.awayClubName\
        GROUP BY C.clubName\
        ORDER BY 2 DESC\
        LIMIT 10;"
    cursor = mysql.connection.cursor()

    cursor.execute(query)
    top10TeamsByMatch = cursor.fetchall()
    
    return jsonify(top10TeamsByMatch)

@app.route("/api/toptenteamsbyhome/", methods=["GET"])
def topTenTeamsByHomeMatch():
    
    query = "\
        SELECT C.ClubName, SUM(CASE\
            WHEN C.ClubName = M.homeClubName AND M.HomeGoals > M.awayGoals THEN 1\
            ELSE 0\
        END) As Score\
        FROM club C INNER JOIN `match` M\
        ON C.clubName = M.homeClubName \
        GROUP BY C.clubName\
        ORDER BY 2 DESC\
        LIMIT 10;"

    cursor = mysql.connection.cursor()

    cursor.execute(query)
    top10TeamsByHomeMatch = cursor.fetchall()
    
    return jsonify(top10TeamsByHomeMatch)

@app.route("/api/toptenteamswithyellowcards/", methods=["GET"])
def topTenTeamsByYellowCards():
    
    query = "\
        SELECT C.ClubName, SUM(CASE\
            WHEN C.ClubName = M.homeClubName THEN M.homeYellowCard\
            WHEN C.ClubName = M.awayClubName THEN M.awayYellowCard\
            ELSE 0\
        END) AS Score\
        FROM club C INNER JOIN `match` M\
        ON C.clubName = M.homeClubName OR C.ClubName = M.awayClubName\
        GROUP BY C.clubName\
        ORDER BY 2 DESC\
        LIMIT 10;"
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    Top10TeamsHavingyellowCards = cursor.fetchall()
    
    return jsonify(Top10TeamsHavingyellowCards)



@app.route("/api/toptenteamsbyfouls/", methods=["GET"])
def topTenTeamsByFouls():
    query = "\
        SELECT C.ClubName,  SUM(CASE\
            WHEN C.ClubName = M.homeClubName THEN M.homeFouls\
            WHEN C.ClubName = M.awayClubName THEN M.awayFouls\
            ELSE 0\
        END) As Score\
        FROM club C INNER JOIN `match` M\
        ON C.clubName = M.homeClubName OR C.ClubName = M.awayClubName\
        GROUP BY C.clubName\
        ORDER BY 2 DESC\
        LIMIT 10"

    cursor = mysql.connection.cursor()

    cursor.execute(query)
    Top10TeamsHavingFouls = cursor.fetchall()
    
    return jsonify(Top10TeamsHavingFouls)

@app.route("/api/toptenteamsbyshots/", methods=["GET"])
def topTenTeamsByShots():
    query = "\
        SELECT C.ClubName, SUM(CASE\
            WHEN C.ClubName = M.homeClubName THEN M.homeShots\
            WHEN C.ClubName = M.awayClubName THEN M.awayShots\
            ELSE 0\
        END) As Score\
        FROM club C INNER JOIN `match` M\
        ON C.clubName = M.homeClubName OR C.ClubName = M.awayClubName\
        GROUP BY C.clubName\
        ORDER BY 2 DESC\
        LIMIT 10;"

    cursor = mysql.connection.cursor()

    cursor.execute(query)
    Top10TeamsHavingShots = cursor.fetchall()
    
    return jsonify(Top10TeamsHavingShots)

@app.route("/api/toptenteamsbyseason/<string:season>/", methods=["GET"])
def topWinningTeams(season):

    query = "\
        SELECT C.ClubName, season,  SUM(CASE\
            WHEN C.ClubName = M.homeClubName AND M.HomeGoals > M.awayGoals THEN 1\
            WHEN C.ClubName = M.awayClubName AND M.AwayGoals > M.homeGoals THEN 1\
            ELSE 0\
        END) AS WIN\
        FROM club C INNER JOIN `match` M\
        ON C.clubName = M.homeClubName OR C.ClubName = M.awayClubName\
        WHERE M.season = %s\
        GROUP BY 2, 1\
        ORDER BY 3 DESC\
        LIMIT 1;"
    #More generic but it is not working in remote server, but it is fine with local host
    # query = "CREATE OR REPLACE VIEW ClubWinning AS \
    #             ( \
    #                 Select HomeW.season, clubName, Hwin+ AWin AS Wins \
    #                 From club c Left Join(\
    #                     Select season, homeClubName, COUNT(*) AS Hwin \
    #                     From `match` \
    #                     Where homeGoals > awayGoals \
    #                     Group By season, homeClubName) HomeW ON HomeW.homeClubName = c.clubName \
    #                 Left Join(\
    #                     Select season, awayClubName, COUNT(*) AS AWin \
    #                     From `match` \
    #                     Where homeGoals < awayGoals\
    #                     Group By season, awayClubName) AwayW\
    #                 ON AwayW.awayClubName= c.clubName AND HomeW.season= AwayW.season) ;\
    #                 \
    #             Select ClubWinning.season, ClubWinning.clubName, ClubWinning.Wins\
    #             From ClubWinning \
    #             Where (season, Wins) IN (\
    #                 Select season, max(Wins)\
    #                 From ClubWinning\
    #                 Group By season)\
    #                 AND season = %s;"
    
    cursor = mysql.connection.cursor()

    cursor.execute(query, (season.replace("-","/"),))


    BestTeamsInASeason = cursor.fetchall()
    print(BestTeamsInASeason)
    return jsonify(BestTeamsInASeason)

