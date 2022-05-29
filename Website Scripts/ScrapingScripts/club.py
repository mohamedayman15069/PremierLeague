from library import *


def gettingSeasonPage(): 
    #Choose the Past Seasons 
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)
    filter = driver.find_element(By.CSS_SELECTOR, "div[class='pageFilter__filter-btn']")
    filter.click()

    filterBySeason = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/section/div[1]')
    filterBySeason.click()
    wait = WebDriverWait(driver,40)

    wait.until(EC.visibility_of_element_located((By.ID, 'dd-compSeasons')))

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.current[data-dropdown-current='compSeasons']")))

def applyFilter():
    applyFilter = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div/section/div[3]')
    applyFilter.click()



count = 0
firstTime = True

url='https://www.premierleague.com/clubs'
path = '/html/body/div[1]/div/div/div[1]/div[5]/button[1]'
driver = openBrowser(url, path)


gettingSeasonPage()
options = driver.find_elements_by_css_selector("ul[data-dropdown-list='compSeasons'] li")

cnt = 0
firstTime = True 
clubInfo = []
visited = {}
for option in options: 
    if cnt <= 3:
        if firstTime == False:
            gettingSeasonPage()

        time.sleep(2)
        option.click()
        applyFilter()
        time.sleep(2)
        clubs = driver.find_element(By.CLASS_NAME, 'dataContainer').find_elements(By.TAG_NAME, 'li')
        for club in clubs: 
            [clubName,StadiumName,_] = club.text.split("\n")
            premierLeagueLink = club.find_element(By.TAG_NAME,'a').get_attribute('href') 
            key = (clubName, StadiumName, premierLeagueLink) 
            if key in visited:
                continue
            else:
                clubInfo.append((clubName, StadiumName, premierLeagueLink))
                visited[key] = 1 
        firstTime = False
    cnt+=1

#Get Official Website 
clubList = []
stadiumList = []
for club in clubInfo: 
    driver.get(club[2])
    time.sleep(2)
    officialWebsite = driver.find_element(By.XPATH, '//*[@id="mainContent"]/header/div[2]/div/div/div[2]/div[2]/a').text
    

    stadiumWebsite = driver.find_element(By.XPATH, '//*[@id="mainContent"]/header/div[2]/div/div/div[2]/div[1]/a').get_attribute('href')
    print(stadiumWebsite)
    clubList.append(
        {
            "club Name": club[0],
            "Stadium Name": club[1], 
            "Official Website": officialWebsite
        })

    stadiumList.append(
        {
            "Stadium Name": club[1],
            "stadium Website": stadiumWebsite
        })


df = pd.DataFrame(clubList)
df_stadium = pd.DataFrame(stadiumList)

df.to_csv(r'ClubTable.csv',index=True)
df_stadium.to_csv(r'StadiumHelperTable.csv',index=True)


