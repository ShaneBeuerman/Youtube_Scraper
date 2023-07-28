from selenium import webdriver
from datetime import date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/feed/trending"
driver = webdriver.Chrome()
today = date.today()
trending = open('Trending_' + today.strftime("%B_%d_%Y") + '.txt', 'w', encoding="utf-8")
trending.write("Trending videos on youtube as of " + today.strftime("%B %d, %Y") + '\n\n')

driver.get(url)

try:
    contents = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )
    videos = contents.find_elements('id', "video-title")
    
    for video in videos:
        name = video.get_attribute('title')
        if name:
            trending.write(name)
            if len(videos) - videos.index(video) != 1:
                trending.write("\n")
    trending.close()
finally:
    driver.quit()
