import http.client
import urllib.parse
import requests

if __name__ == '__main__':

    r = requests.post("http://sara.gov.cn/cms/web/PlaceSelect.do", data={'pageSize':50000})
    text = r.text;
    f = open("output.html", "w+")
    f.write(text)
    f.close()