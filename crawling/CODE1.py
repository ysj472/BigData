#=======================
# CODE1 program
#=======================
import urllib.request
from datetime import datetime
client_id = '5O6wYctRdBZR8lfqjEoT'
client_secret = '5jN1kP8Z2Q'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    print('----call url = ', url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("----[%s] Url Request Success" % datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.now(), url))
        return None
