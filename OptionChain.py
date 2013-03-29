import sys
import urllib2
import json
from bs4 import BeautifulSoup, SoupStrainer
from scrape import get_data

def get_options_data(expiryDt):
    if expiryDt == "":
        return json.dumps({'Error': 0})
    html = get_data('http://www.nseindia.com/live_market/dynaContent/live_watch/fxTracker/optChainDataByExpDates.jsp?symbol=USDINR&instrument=OPTCUR&expiryDt='+expiryDt)
    opttbl = SoupStrainer('div', {'class': 'opttbldata'})
    data = BeautifulSoup(html, 'html.parser', parse_only=opttbl)
    tbldata = data.find_all('tr')
    if tbldata == []:
        return json.dumps({'Error': 1})
    tbldata.pop(0)
    tbldata.pop(0)
    jsonObj = []

    for i in tbldata:
        cellData = i.find_all('td', align='right')
        callsObj = {}
        putsObj = {}
        strikePrice = 0
        counter = 0
        table = { ord(u'-'): None}

        callsObj['OI'] = cellData[0].get_text().translate(table)
        putsObj['OI'] = cellData[16].get_text().translate(table)

        callsObj['Volume'] = cellData[1].get_text().translate(table)
        putsObj['Volume'] = cellData[15].get_text().translate(table)

        callsObj['IV'] = cellData[2].get_text().translate(table)
        putsObj['IV'] = cellData[14].get_text().translate(table)

        temp = cellData[3].get_text()
        ind1 = temp.find('>', 0, len(temp))
        ind2 = temp.find('<', ind1+1, len(temp))
        ltp = temp[ind1+2:ind2]
        callsObj['LTP'] = ltp.translate(table)

        temp = cellData[13].get_text()
        ind1 = temp.find('>', 0, len(temp))
        ind2 = temp.find('<', ind1+1, len(temp))
        ltp = temp[ind1+2:ind2]
        putsObj['LTP'] = ltp.translate(table)
	
        callsObj['BidQty'] = cellData[4].get_text().translate(table)
        putsObj['BidQty'] = cellData[9].get_text().translate(table)

        callsObj['BidPrice'] = cellData[5].get_text().translate(table)
        putsObj['BidPrice'] = cellData[10].get_text().translate(table)

        callsObj['AskQty'] = cellData[7].get_text().translate(table)
        putsObj['AskQty'] = cellData[12].get_text().translate(table)

        callsObj['AskPrice'] = cellData[6].get_text().translate(table)
        putsObj['AskPrice'] = cellData[11].get_text().translate(table)

        temp = cellData[8].get_text()
        ind1 = temp.find('a0', 0, len(temp))
        ind2 = temp.find('/', ind1, len(temp))
        strikePrice = temp[ind1+2:ind2]

        jsonObj.append(json.dumps({'StrikePrice': strikePrice, 'Calls': callsObj, 'Puts': putsObj}))
    return jsonObj

def get_options_dates():
    html = get_data('http://www.nseindia.com/live_market/dynaContent/live_watch/fxTracker/optChainDataByExpDates.jsp?symbol=USDINR&instrument=OPTCUR')
    optDates = SoupStrainer('select', {'id': 'expirydate'})
    data = BeautifulSoup(html, 'html.parser', parse_only=optDates).find_all("option")
    data.pop(0)
    dates = []
    for i in data:
        dates.append(i.get_text())
    return json.dumps({'options_dates':dates})
         
if __name__=="__main__":
    for i in sys.argv:
        if i.find('.py') + 1:
            continue
        else:
            print get_options_data(i)
