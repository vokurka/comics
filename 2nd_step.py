import csv, sys, glob, pprint, json
from urllib.parse import unquote
from datetime import datetime

data = {}

for file in glob.glob('1st_step/**'):
	print(file)

	date = file.replace("1st_step/Export?format=csv&releaseDate=", "")
	date = unquote(date)
	datetime_object = datetime.strptime(date, '%m/%d/%Y')
	date = datetime_object.strftime('%Y-%m-%d')

	data[date] = {}

	state = 'title'
	title = 'n/a'

	with open(file,'r') as inf:
		for line in inf:
			print(state+": "+line, end="")
			if state == 'title':
				title = line
				state = 'after title newline'
				print("next state: "+state)
				data[date][title] = []
				continue

			if state == 'after title newline' and line == "\n":
				state = 'data row'
				print("next state: "+state)
				continue
			elif state == 'after title newline' and line != "\n":
				print('unexpected state combination after title')
				sys.exit(1)

			if state == 'data row' and line == "\n":
				state = 'title'
				print("next state: "+state)
				continue
			elif state == 'data row' and len(line) > 10:
				data[date][title].append(line)
				print("next state: "+state)
				continue
			else:
				print('unexpected state combination after data')
				sys.exit(1)

with open('2nd_step/data.json', 'w') as outfile:
    json.dump(data, outfile)