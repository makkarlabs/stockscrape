import urllib2
import json
from bs4 import BeautifulSoup, SoupStrainer
from scrape import get_data

html = get_data('http://www.nseindia.com/live_market/dynaContent/live_watch/fxTracker/optChainDataByExpDates.jsp?symbol=USDINR&instrument=OPTCUR&expiryDt=27MAR2013')

opttbl = SoupStrainer('div', {'class': 'opttbldata'})
data = BeautifulSoup(html, 'html.parser', parse_only=opttbl)
tbldata = data.find_all('tr')
jsonObj = []

for i in tbldata:
	cellData = i.find_all('td')
	callsObj = []
	putsObj = []
	strikePrice = 0
	counter = 0
	#print cellData
	for j in cellData:
		if counter == 0:
			counter + 1
			continue
		elif counter < 10:
			putsObj.append(j.get_text())
		elif counter == 10:
			strikePrice = j.get_text()
		elif counter > 10:
			callsObj.append(j.get_text())
		else:
			print json.dumps({"puts": putsObj, "calls": callsObj})
		counter = counter + 1
		print counter
		print j.get_text()