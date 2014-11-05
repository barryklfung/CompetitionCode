import urllib2
import requests

f = open ('jinput.txt', 'r')
data = []
url_base = "http://services.odata.org/Northwind/Northwind.svc/Products/$count?$filter="
for line in f:
    data.append(line.strip().replace(' ','%20'))
 
for i in range(len(data)):
    url  = url_base+data[i]
    content = urllib2.urlopen(url).read()
    print content