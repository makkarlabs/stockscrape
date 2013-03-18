import urllib2
import json
        

def get_data(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Ubuntu Chromium/24.0.1312.56 Chrome/24.0.1312.56 Safari/537.17')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    resp = urllib2.urlopen(req);
    #print resp.read()
    return resp.read()

def parse_data_all(url):
    html = get_data(url)
    data2 = html.split("-;-")
    if len(data2) > 1:
        data = data2[1]
        if len(data) > 1:
            contracts = data.split("~")
            data_arr = [];
            for element in contracts:
                got_ba_price = 0;
                got_bb_price = 0;
                e = {}
                if element.split(":")[0] != "-":
                    e['contract'] = element.split(":")[0]
                if element.split(":")[1] != "-":
                    e['type'] = element.split(":")[1]
                if element.split(":")[2] != "-":
                    e['conversion'] = element.split(":")[2]
                if element.split(":")[3] != "-":
                    e['timestamp'] = element.split(":")[3]
                if element.split(":")[6] != "-":
                    e['bb_qty'] = element.split(":")[6]
                if element.split(":")[7] != "-":
                    e['bb_price'] = element.split(":")[7]
                    got_bb_price = 1 
                if element.split(":")[8] != "-":
                    e['ba_price'] = element.split(":")[8]
                    got_ba_price = 1
                if element.split(":")[9] != "-":
                    e['ba_qty'] = element.split(":")[9]
                if got_ba_price == 1 and got_bb_price == 1:
                    e['spread'] = "{0:.4f}".format(float(e['ba_price'])-float(e['bb_price']))
                if element.split(":")[10] != "-":
                    e['ltp'] = element.split(":")[10]
                if element.split(":")[11] != "-":
                    e['volume'] = element.split(":")[11]
                if element.split(":")[12] != "-":
                    e['oi'] = element.split(":")[12]
                if element.split(":")[13] != "-":
                    e['value'] = element.split(":")[13]
                if element.split(":")[14] != "-":
                    e['notrades'] = element.split(":")[14]
                data_arr.append(e)
            return json.dumps(data_arr)
        else:
            return ""
            
def obtain_data(option):
    if option == "ALL":
        return parse_data_all('http://www.nseindia.com/marketinfo/fxTracker/priceWatchData.jsp?instrument=FUTCUR&currency=ALL')
    elif option == "USDINR":
        return parse_data_all('http://www.nseindia.com/marketinfo/fxTracker/priceWatchData.jsp?instrument=FUTCUR&currency=USDINR')
    elif option == "GBPINR":
        return parse_data_all('http://www.nseindia.com/marketinfo/fxTracker/priceWatchData.jsp?instrument=FUTCUR&currency=GBPINR')
    elif option == "EURINR":
        return parse_data_all('http://www.nseindia.com/marketinfo/fxTracker/priceWatchData.jsp?instrument=FUTCUR&currency=EURINR')
    elif option == "JYPINR":
        return parse_data_all('http://www.nseindia.com/marketinfo/fxTracker/priceWatchData.jsp?instrument=FUTCUR&currency=JYPINR')
    else:
        return ""

if __name__=="__main__":
    print obtain_data("USDINR")
