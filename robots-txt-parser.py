import concurrent.futures
import requests
import threading
import sys
import time
import re
from colorama import Fore, Style
inputfile=sys.argv[1]
outputfile=sys.argv[2]
output=open(outputfile, "a")
with open(inputfile, "r") as f:
	inputurl = [line.rstrip() for line in f]
threadLocal = threading.local()
pattern="\/[a-zA-Z0-9\/_-]*"
endpoints=[]
count = len(inputurl)
print("number of urls = " + str(count))
def get_session():
    if not hasattr(threadLocal, "session"):
        threadLocal.session = requests.Session()
    return threadLocal.session
def check_sub(url):
	try :
		session=get_session()
		res=session.get(url, timeout=2 , allow_redirects=False )
		if res.status_code == 200 and ("Disallow" or "Allow") in res.text:
			print("Collecting end-points from :- " + url)
			lines=re.findall(pattern, res.text)
			for line in lines:
				if line not in endpoints:
					endpoints.append(line)
				else:
					pass
		else :
			pass
	except:
		pass
def itterate_url(inputurl):
	url=inputurl+"/robots.txt"
	check_sub(url)
	
if __name__ == "__main__":
	start_time = time.time()
	with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
       		executor.map(itterate_url, inputurl)
	duration = time.time() - start_time
	print("finished in : " + str(duration) + "  sec")
print("=" * 80)
print("The Unique endpoints are : " + "\n")
for endpoint in endpoints:
	if "//" in endpoint:
		pass
	else:
		print(endpoint)
		output.write(endpoint + "\n")
