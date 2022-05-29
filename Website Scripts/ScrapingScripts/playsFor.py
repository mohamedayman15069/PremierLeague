#This script will scrape the playerNames for Each club in each season 

from turtle import position
from library import *

def openFilterPage():
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(2)
    filter = driver.find_element(By.CSS_SELECTOR, "div[class='pageFilter__filter-btn']")
    filter.click()

def Seasonfilter():
    #Choose the Past Seasons 
    # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(1)
    filterBySeason = driver.find_element(By.CSS_SELECTOR, "div[class='current']")
    # filterBySeason = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[2]/div[1]/div/section/div[1]/div[2]')
    filterBySeason.click()
    wait = WebDriverWait(driver,40)
    wait.until(EC.visibility_of_element_located((By.ID, 'dd-compSeasons')))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.current[data-dropdown-current='compSeasons']")))

def clubFilter():
    # filterByClub = driver.find_element(By.XPATH,'//*[@id="mainContent"]/div[2]/div[1]/div/section/div[2]/div[2]')
    filterByClub = driver.find_element(By.CSS_SELECTOR, 'div[data-dropdown-current="clubs"]')
    filterByClub.click()

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

playsForList = []

#First Automate the seasons 


#get the Filter Page
openFilterPage()
time.sleep(2)
Seasonfilter()

seasons = driver.find_elements_by_css_selector("ul[data-dropdown-list='compSeasons'] li")

seasons[0].click()
#get the Club Names 
time.sleep(1)
clubFilter()


cnt = 0
firsTime = True
for season in seasons[:4]:

    if firsTime == False:
        openFilterPage()
        # time.sleep(5)
        Seasonfilter()
        # time.sleep(5)
        season.click()
        # time.sleep(15)
        clubFilter()      # Open Club Filter Section
    firsTime = False
    firstTimeClub = True
    clubs = driver.find_elements_by_css_selector("ul[data-dropdown-list='clubs'] li")
    for club in clubs[1:]:
        if firstTimeClub == False:
            openFilterPage()  # Open Filter Page again for the next club
            clubFilter()      # Open Club Filter Section
        firstTimeClub = False
        clubName = club.text
        print(clubName)
        club.click()      #Click on the Club
        applyFilter()     # Apply filter to start scraping 
        time.sleep(1)
        scrollDown()
        time.sleep(2)
        #Get Player Names
        players = driver.find_elements(By.XPATH,'//*[@id="mainContent"]/div[2]/div/div/div/table/tbody/tr')
        print("Number of Players",len(players))
        for player in players:
            attr = player.find_elements(By.TAG_NAME,'td')
            [playerName, position, _] = attr 
            mapper = {
                "Club Name": clubName,
                "Season"   : Season[cnt], 
                "Player Name": playerName.text
            }
            playsForList.append(mapper)
            print(mapper)
    cnt +=1

            

        

    

df = pd.DataFrame(playsForList)

df.to_csv(r'PlayerForTable.csv',index=True)



        
        
