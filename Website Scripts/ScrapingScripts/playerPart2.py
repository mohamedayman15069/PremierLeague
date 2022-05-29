from library import *
# from bs4 import BeautifulSoup

# from playerPart1 import *




url = 'https://www.premierleague.com/players'
driver =  openBrowser(url, '/html/body/div[1]/div/div/div[1]/div[5]/button[1]')

# print(playerLinkSet)

#Loop over all links 
allPlayerInfo = list(np.array(load_csvFile('./playerInfoPart1.csv')))


notWorkingLinks = []
PlayerList = []

for playerInfo in allPlayerInfo: 
    driver.get(playerInfo[0])
    time.sleep(2)
    playerName = playerInfo[1]
    season = playerInfo[2]
    position = playerInfo[3]
    nationality = playerInfo[4]
    clubName = None
    mapper = {}
    try:
        temp = driver.find_element_by_class_name('personalDetails')
        SourceHTML = temp.get_attribute('innerHTML')
        personalDetails = temp.text
        # print(personalDetails)
        splittedInfo = personalDetails.split('\n')
        playerName = driver.find_element(By.CSS_SELECTOR, "div[class='name t-colour']").text
        tmpClub = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[3]/div/div/div[3]/table/tbody/tr[1]')

        clubName = tmpClub.find_element(By.TAG_NAME,'a').get_attribute('href')
        clubName = clubName.replace('https://www.premierleague.com/clubs/','').split('/')[1].replace('-',' ')

        print(clubName)
    except: 
        notWorkingLinks.append(playerInfo[0])
    
    dateOfBirth = None 
    height = None 
    Weight =None
    index = SourceHTML.find('kg</div>')

    if index !=-1:
        weightInfo = SourceHTML[index - 5 : index]
        Weight = weightInfo.split('>')[1]
    
    # html_soup: BeautifulSoup = BeautifulSoup(SourceHTML, 'html.parser')
    # weightInfo = html_soup.find(class_="u-hide")
    # if weightInfo is not None:
    #     Weight = weightInfo.find(class_="info").text.replace('kg','')        



    print(Weight)
    lens = len(splittedInfo)
    if lens >= 2: 
        nationality = splittedInfo[2].split(" ")[0]
    if lens >= 4:
        dateOfBirth = splittedInfo[4].split(" ")[0]
    if lens >= 6: 
        height = splittedInfo[6].split(" ")[0].replace('cm','') #in cm



    mapper = {
        "Player Name": playerName,
        "Club Name"  : clubName,
        "Season"     : season,
        "Position"   : position,
        "Nationality": nationality,
        "Date Of Birth": dateOfBirth,
        "Height(cm)"   : height,
        'Weight(kg)'  : Weight
    }
    # print(personalDetails)
    print(mapper)
    PlayerList.append(mapper)



df = pd.DataFrame(PlayerList)
df.to_csv(r'PlayerTable.csv',index=True)