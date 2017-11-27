import json, csv, sys
from pprint import pprint

# with open('2nd_step/data.json', 'r') as inf, open('3rd_step/data.csv', 'w') as outf:
# 	data = json.load(inf)
# 	writer = csv.writer(outf)

# 	writer.writerow(['date', 'category', 'issue', 'name', 'price'])

# 	for date in data:
# 		for category in data[date]:
# 			for row in data[date][category]:
# 				row_array = row.split(",")
# 				writer.writerow([date, category.replace("\n",""), row_array[0].replace("\n",""), row_array[1].replace("\n",""), row_array[2].replace("\n","")])

stats = {
	'total': 0,
	'magazines': 0,
	'books': 0,
	'comics': 0,
	'comics_dc': 0,
	'comics_marvel': 0	
}

with open('3rd_step/data.csv', 'r') as inf:
	reader = csv.DictReader(inf)
	lines = list(reader)

	for line in lines:
		if line['date'][0:4] != '2016':
			continue

		if line['category'] == 'MERCHANDISE':
			continue

		stats['total'] += 1

		if not line['category'] in ['MAGAZINES', 'BOOKS']:
			stats['comics'] += 1

		if line['category'] == 'MAGAZINES':
			stats['magazines'] += 1

		if line['category'] == 'BOOKS':
			stats['books'] += 1

		if line['category'] == 'DC COMICS':
			stats['comics_dc'] += 1

		if line['category'] == 'MARVEL COMICS':
			stats['comics_marvel'] += 1

	pprint(stats)



