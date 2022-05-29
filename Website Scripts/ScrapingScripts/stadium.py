from library import *

#Load the CSV File 



def extractingStadiumAttributes(stadiumInfos):
    mapper = {}
    for line in stadiumInfos: 
            info = line.text.split('\n')

            for l in info: 
                feature = l.split(':')

                if(len(feature) !=2): 
                    continue 
                if(len(feature[0].split(' ')) > 10):
                    continue
                splittedFeature = feature[0].split(' ')
            
                if 'Capacity' in splittedFeature or 'capacity' in splittedFeature:
                    temp = feature[1].split(' ')
                    mapper["Capacity"] = int(temp[1].replace(',', ''))
                    
                elif feature[0] == 'Record PL attendance' or 'attendance' in splittedFeature or 'Attendance' in splittedFeature:
                    temp = feature[1].split(" ")
                    i = 0
                    while temp[i] == '':
                        i+=1
                    mapper["Record PL attendance"] = int(temp[i].replace(',', ''))
                elif feature[0] == 'Built' or feature[0] == 'Opened':
                    mapper['Building Year'] = feature[1]
                elif feature[0] == 'Pitch size':
                    temp = feature[1].split('x')
                    mapper['Pitch Length'] = float(temp[0].replace(',' , '')[:-1].replace('m',''))
                    mapper['Pitch Width']  = float(temp[1].replace(',', '')[:-1].replace('m',''))
                
                elif feature[0] == 'Stadium address':
                    
                    temp = feature[1].split(',')
                    diff = 4 - len(temp)
                    mapper['Street'] = temp[1-diff]
                    mapper['City'] = temp[2-diff].replace(' ', '')
                    mapper['Postal Code'] = temp[3-diff]
    return mapper
        

def main():
    
    stadiumDF = np.array(load_csvFile("./StadiumHelperTable.csv"))
    stadiumNames = list(stadiumDF[:,0])
    stadiumLinks = list(stadiumDF[:,1])
    driver = openBrowser('https://www.premierleague.com/','/html/body/div[2]/div/div/div[1]/div[5]/button[1]')

    stadium_list = []
    cnt = 0
    for stadiumLink in stadiumLinks:
        driver.get(stadiumLink)
        time.sleep(4)
        stadiumInfo = driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div[2]/div/ul/li[2]')
        stadiumInfo.click()
        #Extract important information
        mapper = {}
        stadiumInfos = driver.find_elements_by_xpath('//*[@id="mainContent"]/div[3]/div[3]/div[2]/p')
        mapper['Stadium Name'] = stadiumNames[cnt]
        
        tempMapper =  extractingStadiumAttributes(stadiumInfos)
                
        #check whether the feature exists or not 
        features = ['Street', 'City', 'Postal Code', 'Pitch Length', 'Pitch Width', 'Building Year', 'Capacity', 'Record PL attendance']

        for feature in features: 
            if tempMapper.get(feature) is None:
                mapper[feature] = None
            else: 
                mapper[feature] = tempMapper[feature]

        cnt +=1
        stadium_list.append(mapper)
        print("Mapper: ", mapper)
        time.sleep(2)


    df_stadium = pd.DataFrame(stadium_list)
    df_stadium.to_csv(r'StadiumTable.csv',index=True)


                



if __name__ == "__main__":
    main()