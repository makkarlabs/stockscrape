import urllib2
import json

class ClassName(object):

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
        

def get_data():
    req = urllib2.Request('http://www.nseindia.com/marketinfo/fxTracker/priceWatchData.jsp?instrument=FUTCUR&currency=ALL')
    req.add_header('User-Agent','Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Ubuntu Chromium/24.0.1312.56 Chrome/24.0.1312.56 Safari/537.17')
    req.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    resp = urllib2.urlopen(req);
    #print resp.read()
    return resp.read()

def parse_data(html):
    data = html.split("-;-")[1]
    if len(data) > 1:
        contracts = data.split("~")
        data_arr = [];
        for element in contracts:
            e = {}
            e['contract'] = element.split(":")[0]
            e['bb_qty'] = element.split(":")[6]
            e['bb_price'] = element.split(":")[7]   
            e['ba_price'] = element.split(":")[8]
            e['ba_qty'] = element.split(":")[9]
            e['spread'] = float(e['ba_price'])-float(e['bb_price'])
            e['ltp'] = element.split(":")[10]
            e['volume'] = element.split(":")[11]
            e['oi'] = element.split(":")[12]
            e['value'] = element.split(":")[13]
            e['notrades'] = element.split(":")[14]
            data_arr.append(e)
        return json.dumps(data_arr)
    else:
        return ""

if __name__=="__main__":
    print parse_data(get_data())
