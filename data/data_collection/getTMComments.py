import requests
import json
import urllib.request
import re

# Get the comment url from url of goods detail url
def geturl(url_detail):

    req = requests.get(url_detail)
    jsondata = req.text[15:]
    info = re.search('itemId:"[0-9]*",sellerId:"[0-9]*",shopId:"[0-9]*"',jsondata)
    info = info.group(0)
    info = info.split(',')
    itemId = info[0].split(':')[1][1:-1]
    sellerId = info[1].split(':')[1][1:-1]
    shopId = info[1].split(':')[1][1:-1]
    return itemId, sellerId, shopId

# Download the comment images    
def getImage(url_detail):      

    url_s = 'https://rate.tmall.com/list_detail_rate.htm?'
    itemId, sellerId, shopId = geturl(url_detail)
    url_itemId = 'itemId='+itemId+'&'
    url_spuId = 'spuId='+shopId+'&'
    url_sellerId = 'sellerId='+sellerId+'&'
    url_order = "order=3&"
    url_append ='append=⊙&'
    count = 0
    for pages in range(0,99):
        url_currentPage ="currentPage="+str(pages+1)+"&"
        url = url_s+url_itemId+url_spuId+url_sellerId+url_order+url_currentPage+url_append+'content=1'


        req = requests.get(url)
        jsondata = req.text[15:]
        try:
            data = json.loads(jsondata)
        except:
            continue

        print('page:',data['paginator']['page'])
        for i in data["rateList"]:
            for url_image in i['pics']:
                if count<9:
                    name = '0000'+str(count+1)+'.jpg'
                elif count<99:
                    name = '000'+str(count+1)+'.jpg'
                elif count<999:
                    name= '00'+str(count+1)+'.jpg'
                elif count<9999:
                    name= '0'+str(count+1)+'.jpg'
                else:
                    name= str(count+1)+'.jpg'
                        
                conn = urllib.request.urlopen("http:"+url_image)
                f = open(name, 'wb')
                f.write(conn.read())
                f.close()
                count+=1

if __name__=="__main__":

    url_detail = 'https://detail.tmall.com/item.htm?spm=a1z10.5-b-s.w4011-14601288098.32.218191f88EYy6o&id=45492997665&rn=c00b3253858596ec80a7c4e9431e2848&abbucket=9'
    getImage(url_detail)
