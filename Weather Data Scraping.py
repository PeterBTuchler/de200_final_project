## USING BEAUTIFUL SOUP:
## Scrape weather data in a number of cities with baseball teams
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# ---- IN ORDER TO GET AROUND DELAY IN DATA TABLE LOADING, THIS ALLOWS THE WEB PAGE TO FULLY LOAD: From https://bojanstavrikj.github.io/content/page1/wunderground_scraper
def render_page(url):
    driver = webdriver.Chrome('C:/Users/pbtuc/Documents/chromedriver_win32/chromedriver')
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r
# ----

weather_stations = ['KMKE', 'KSNA', 'KSTL', 'KPHX', 'KLGA', 'KPHL', 'KDET', 'KDEN', 'KBUR', 'KBOS', 'KDFW', 'KCVG', 'KMDW', 'KMCI', 'KMIA', 'KHOU', 'KDCA', 'KOAK', 'KSFO', 'KBWI', 'KSAN', 'KPIT', 'KCLE', 'CYTZ', 'KSEA', 'KMSP', 'KPIE',  'KATL']
year = 2015
for station in weather_stations:                        # Loops through all weather stations for outomated scraping (because it will take about 30 hours)
    date_range = []
    for month in [4, 5, 6, 7, 8, 9]:                    # These nested loops create every date from April 1st to September 30th: the baseball season
        if month == 4 or month == 6 or month == 9:
            for day in list(range(1,31)):
                the_date = f'{year}-{month}-{day}'
                date_range.append(the_date)
        else:
            for day in list(range(1,32)):
                the_date = f'{year}-{month}-{day}'
                date_range.append(the_date)


    filename = f"{station}_{year}.txt"
    f = open(filename, 'w+', encoding="utf-8")


    for date in date_range:
        url = f'https://www.wunderground.com/history/daily/{station}/date/{date}'		# Changes url in a for loop
        r = render_page(url)
        soup = BeautifulSoup(r, "html.parser")


        if soup.find_all('div', {'class': 'columns small-12'})[2].find_all('tbody') == []:           # Avoids errors if there is no data
            pass
        else:                                                                                        # Uses beautiful soup to pull info from the correct data table in html and then parse it into the relavent variables
            summary_data_temp = soup.find_all('div', {'class': 'columns small-12'})[2].find_all('tbody')[0]
            summary_data_temp = soup.find_all('div', {'class': 'columns small-12'})[2].find_all('tbody')[0]
            summary_data_precip = soup.find_all('div', {'class': 'columns small-12'})[2].find_all('tbody')[1]
            summary_data_wind = soup.find_all('div', {'class': 'columns small-12'})[2].find_all('tbody')[3]
            summary_data_pressure = soup.find_all('div', {'class': 'columns small-12'})[2].find_all('tbody')[4]

            high_temp = summary_data_temp.find_all('tr')[0].find_all('td')[0].text
            low_temp = summary_data_temp.find_all('tr')[1].find_all('td')[0].text
            avg_temp = summary_data_temp.find_all('tr')[2].find_all('td')[0].text
            h24_precipitation = summary_data_precip.find_all('tr')[0].find_all('td')[0].text
            max_wind_speed = summary_data_wind.find_all('tr')[0].find_all('td')[0].text
            sea_level_pressure = summary_data_pressure.find_all('tr')[0].find_all('td')[0].text

            data_line = f"{station},{date},{high_temp},{low_temp},{avg_temp},{h24_precipitation},{max_wind_speed},{sea_level_pressure}\n"               # Print to the file in the correct format
            f.write(data_line)

    f.close()
