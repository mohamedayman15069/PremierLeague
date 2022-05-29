from library import *

def gettingPastSeasonsPage(): 
    #Choose the Past Seasons 
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(1)
    filter = driver.find_element(By.CSS_SELECTOR, "div[class='pageFilter__filter-btn']")
    filter.click()
    filterBySeason = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div[1]/div/section/div[1]/div[2]')
    filterBySeason.click()
    wait = WebDriverWait(driver,40)

    wait.until(EC.visibility_of_element_located((By.ID, 'dd-compSeasons')))

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.current[data-dropdown-current='compSeasons']")))

def applyFilter():
    applyFilter = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div[1]/div/section/div[4]')
    applyFilter.click()

def scrollDown(): 
    # Scroll down
    current_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 	# Scroll step
        try:
            time.sleep(4)
            new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height
        except:
            print("Failed: ", new_height)
        if new_height == current_height: # Compare with last scroll height
            break

        # time.sleep(3)
        current_height = new_height
        # time.sleep(3)
        
    print("scorlled till",current_height)




url = 'https://www.premierleague.com/players'
driver =  openBrowser(url, '/html/body/div[1]/div/div/div[1]/div[5]/button[1]')
gettingPastSeasonsPage()




options = driver.find_elements_by_css_selector("ul[data-dropdown-list='compSeasons'] li")

time.sleep(2)
firstTime = True
count = 0
playerLinkSet = set()
seasonPlayerLinks = []

numberofPlayers = 0
for option in options:
    if count < 4: 
        if firstTime == False: 
            gettingPastSeasonsPage()
        option.click()
        applyFilter()
        scrollDown()
        firstTime = False
        time.sleep(2)
        players = driver.find_elements(By.XPATH,'//*[@id="mainContent"]/div[2]/div[1]/div/div/table/tbody/tr')
        print("Number of Players",len(players))
        playerSeasonLinks = []
        
        for player in players:
            link = player.find_element(By.TAG_NAME,'a').get_attribute('href')
            attr = player.find_elements(By.TAG_NAME,'td')
            # print(attr)
            [playerName,position,nationality] = attr
            # print(position.text)
            if link not in playerLinkSet:
                playerLinkSet.add(link)
                seasonPlayerLinks.append({
                    "Player Link" :link,
                    "Player Name" : playerName.text,
                    "Season"      : Season[count],
                    "Position": position.text,
                    "nationality": nationality.text
                    })
                numberofPlayers+=1       
        count+=1
 
    else:
        break

print("Number of Unique Players in 4 seasons: ",numberofPlayers)


df = pd.DataFrame(seasonPlayerLinks)

df.to_csv(r'playerInfoPart1.csv',index=True)