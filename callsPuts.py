import urllib2
import json
from bs4 import BeautifulSoup, SoupStrainer
from scrape import get_data

html = get_data('http://www.nseindia.com/live_market/dynaContent/live_watch/fxTracker/optChainDataByExpDates.jsp?symbol=USDINR&instrument=OPTCUR&expiryDt=27MAR2013')

opttbl = SoupStrainer('div', {'class': 'opttbldata'})
data = BeautifulSoup(html, 'html.parser', parse_only=opttbl)
tbldata = data.find_all('tr')
tbldata.pop(0)
tbldata.pop(0)
jsonObj = []

f = open('option.html', 'w')
f.write(html)
f.close()

for i in tbldata:
	cellData = i.find_all('td', align='right')
	callsObj = {}
	putsObj = {}
	strikePrice = 0
	counter = 0

	callsObj['OI'] = cellData[0].get_text()
	putsObj['OI'] = cellData[16].get_text()

	callsObj['Volume'] = cellData[1].get_text()
	putsObj['Volume'] = cellData[15].get_text()

	callsObj['IV'] = cellData[2].get_text()
	putsObj['IV'] = cellData[14].get_text()

	temp = cellData[3].get_text()
	ind1 = temp.find('>', 0, len(temp))
	ind2 = temp.find('<', ind1+1, len(temp))
	ltp = temp[ind1+2:ind2]
	callsObj['LTP'] = ltp
	temp = cellData[13].get_text()
	ind1 = temp.find('>', 0, len(temp))
	ind2 = temp.find('<', ind1+1, len(temp))
	ltp = temp[ind1+2:ind2]
	putsObj['LTP'] = ltp
	
	callsObj['BidQty'] = cellData[4].get_text()
	putsObj['BidQty'] = cellData[9].get_text()

	callsObj['BidPrice'] = cellData[5].get_text()
	putsObj['BidPrice'] = cellData[10].get_text()

	callsObj['AskQty'] = cellData[7].get_text()
	putsObj['AskQty'] = cellData[12].get_text()

	callsObj['AskPrice'] = cellData[6].get_text()
	putsObj['AskPrice'] = cellData[11].get_text()

	strikePrice = cellData[8].get_text().encode('utf-8').strip()

	jsonObj.append(json.dumps({'StrikePrice': strikePrice, 'Calls': callsObj, 'Puts': putsObj}))

print jsonObj