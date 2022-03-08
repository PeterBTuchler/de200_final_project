Here is information on the files uploaded to Github:

Weather Data Scraping.py
	This python code scrapes weather data from weather underground using BeautifulSoup and Selenium and stores it in CSV format in seperate text files for each stadium and year.

Weather Data Combiner.py
	This code combines the data from all of the seperate text files and merges them into one large text file merged_2015.txt. The formatting of the dates has been changed to match the baseball dataset and the weather station has been swapped with the stadium id.

CYTZ_2015.txt and all simmilar ****_2015.txt files store the scraped data from weather underground for each stadium.

merged_2015.txt is the reformatted and merged weather data from all of the ****_2015.txt files.

game_logs_excel.xlsx is a file that contains all of the baseball dataset, but no weather information.

baseball_weather_dataset.csv is a csv file that contains all of the baseball data and the weather data combined. It is 140 MB and we used it to create our graphs for analysis.