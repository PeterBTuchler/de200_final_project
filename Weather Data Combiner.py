weather_stations = ['KMKE', 'KSNA', 'KSTL', 'KPHX', 'KLGA', 'KPHL', 'KDET', 'KDEN', 'KBUR', 'KBOS', 'KDFW', 'KCVG', 'KMDW', 'KMCI', 'KMIA', 'KHOU', 'KDCA', 'KOAK', 'KSFO', 'KBWI', 'KSAN', 'KPIT', 'KCLE', 'CYTZ', 'KSEA', 'KMSP', 'KPIE',  'KATL', 'KMDW', 'KLGA']
stadiums = ['MIL06', 'ANA01', 'STL10', 'PHO01', 'NYC21', 'PHI13', 'DET05', 'DEN02', 'LOS03', 'BOS07', 'ARL02', 'CIN09', 'CHI12', 'KAN06', 'MIA02', 'HOU03', 'WAS11', 'OAK01', 'SFO03', 'BAL12', 'SAN02', 'PIT08', 'CLE08', 'TOR02', 'SEA03', 'MIN04', 'STP01', 'ATL02', 'CHI11', 'NYC20']
year = 2015

all_weather = []
city_count = 0
for station in weather_stations:
	day_count = 0
	filename = f"{station}_{year}.txt"
	f = open(filename, 'r', encoding="utf-8")
	season_weather = f.readlines()										# All the lines in the file as a list
	for line in season_weather:											# Loops through all the days at a specific location
		stad_line = line.replace(station, stadiums[city_count])			# Replaces weather station with respective stadium id and saves in stad_line
		date_old_format = stad_line.split(',')[1]
		date_old_format_split = date_old_format.split('-')
		date_new_format = ""
		if len(date_old_format_split[1]) == 2 and len(date_old_format_split[2]) == 2:										# ie 2015-12-19
			date_new_format = f"{date_old_format_split[0]}{date_old_format_split[1]}{date_old_format_split[2]}"
		elif len(date_old_format_split[1]) == 1 and len(date_old_format_split[2]) == 2:										# ie 2015-9-19
			date_new_format = f"{date_old_format_split[0]}0{date_old_format_split[1]}{date_old_format_split[2]}"
		elif len(date_old_format_split[1]) == 2 and len(date_old_format_split[2]) == 1:										# ie 2015-12-9
			date_new_format = f"{date_old_format_split[0]}{date_old_format_split[1]}0{date_old_format_split[2]}"
		elif len(date_old_format_split[1]) == 1 and len(date_old_format_split[2]) == 1:										# ie 2015-4-1
			date_new_format = f"{date_old_format_split[0]}0{date_old_format_split[1]}0{date_old_format_split[2]}"
		line_split = stad_line.split(',')
		line_split[1] = date_new_format					# Replaces old date format with new date format
		new_line = ','.join(line_split)					# Rejoins it into comma separated string
		season_weather[day_count] = new_line
		day_count += 1
	all_weather.extend(season_weather)
	f.close()
	city_count += 1

g = open('merged_2015.txt', 'w+', encoding="utf-8")
for weather in all_weather:					# Writes it all to the new file merged_2015.txt
	g.write(f"{weather}")
g.close()
