from library import *


def gettingPastSeasonsPage(): 
    #Choose the Past Seasons 
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)
    filter = driver.find_element(By.CSS_SELECTOR, "div[class='pageFilter__filter-btn']")
    filter.click()

    filterBySeason = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div[1]/section/div[3]/div[2]')
    filterBySeason.click()
    wait = WebDriverWait(driver,40)

    wait.until(EC.visibility_of_element_located((By.ID, 'dd-compSeasons')))

    drop_down_click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.current[data-dropdown-current='compSeasons']")))


def get_all_availbleSeasons():
    # Getting all availble seasons 
    drop_down = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div[1]/section/div[3]/ul')
    all_seasons = list(drop_down.text.split())
    return all_seasons


def applyFilter():
    applyFilter = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div[1]/section/div[6]')
    applyFilter.click()


def scrollDown(): 
    # Scroll down
    current_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 	# Scroll step
        time.sleep(5) 	# Wait to load page
        try:
            new_height = driver.execute_script("return document.body.scrollHeight") # Calculate new scroll height
        except:
            print("Failed: ", new_height)
        if new_height == current_height: # Compare with last scroll height
            break
        current_height = new_height
        
    print("scorlled till",current_height)

def getEachPageLink(val):

    links = driver.find_elements_by_css_selector("li div[class='fixture postMatch']")

    counter = 0
    matchLinks = []

    for elem in links:
        # print("http:"+elem.get_attribute("data-href"))
        matchLinks.append("http:"+elem.get_attribute("data-href"))
        counter+=1

    print("Number of Matches: ", counter)
    return matchLinks



url='https://www.premierleague.com/results?co=1&se=418&cl=-1'
path = '/html/body/div[2]/div/div/div[1]/div[5]/button[1]'
driver = openBrowser(url, path)

gettingPastSeasonsPage()
all_seasons = get_all_availbleSeasons()
options = driver.find_elements_by_css_selector("ul[data-dropdown-list='compSeasons'] li")
time.sleep(1)
firstTime = True
count = 0

homeList = []
awayList = []

Date = []

matchLinkSeasons = []
for option in options:
        if count < 4: 
            if firstTime == False: 
                gettingPastSeasonsPage()
            option.click()
            applyFilter()
            scrollDown()
            firstTime = False
            time.sleep(5)
            matchLinkSeasons.append(getEachPageLink(count))
            count+=1


# Loop for each link to get the needed information 
cnt = 0
list_ = []

for matchLinks in matchLinkSeasons:
    for elem in matchLinks:
        time.sleep(1)
        driver.get(elem)
        #date
        date = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section[2]/div[2]/section/div[1]/div/div[1]/div[1]')
        #Stadium
        stadium = driver.find_element_by_xpath('//*[@id="mainContent"]/div/section[2]/div[2]/section/div[1]/div/div[1]/div[3]')
        # stadiumName.append(stadium.text)
        Date.append(date)
        wait = WebDriverWait(driver,40)
        stats = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]')))
        stats.click()
        time.sleep(2)
        #goals 
        Goals = driver.find_element_by_css_selector("div[class='score fullTime']")
        # print("GOALS: ", )
        goals = Goals.text.split('-')
        #Name

        homeName = driver.find_element_by_css_selector("div[class='team home']").text
        awayName = driver.find_element_by_css_selector("div[class='team away']").text

        bodyText = driver.find_elements(By.XPATH,'//*[@id="mainContent"]/div/section[2]/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr')
        hMapper = {}
        aMapper = {}
        for line in bodyText:
            # print(line.text)
            line_value = line.find_elements(By.TAG_NAME,'td')
            [Home, attr, Away] = line_value
            hMapper[attr.text] = Home.text
            aMapper[attr.text] = Away.text
        
        neededAttributes = ['Possession %', 'Shots','Yellow cards','Fouls conceded', 'Red cards']
        mapper = {}
        #Name
        mapper['Home Name'] = homeName
        mapper['Away Name'] = awayName
        mapper['Season']    = Season[cnt]
        stadium_part = stadium.text.split(',')
        mapper['Stadium Name'] = stadium_part[0]
        # awayMapper = {}
        
        for attribute in neededAttributes:
            if attribute == 'Poessession %':
                mapper['Home Possession'] = hMapper[attribute]
                mapper['Away Possession'] = aMapper[attribute]
            elif hMapper.get(attribute) is None: 
                mapper["Home "+attribute] = 0
                mapper["Away "+attribute] = 0
            else: 
                mapper["Home "+attribute] = hMapper[attribute]
                mapper["Away "+attribute] = aMapper[attribute]
        
        
        #Goals
        mapper['Home Goals'] = goals[0]
        mapper['Away Goals'] = goals[1]

  
        print(mapper)
        list_.append(mapper)
        time.sleep(2)
    cnt +=1

df = pd.DataFrame(list_)
df.to_csv(r'MatchTable.csv',index=True)
