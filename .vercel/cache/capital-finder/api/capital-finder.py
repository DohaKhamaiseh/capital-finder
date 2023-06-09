from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):
       def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        print(dic)
        capital = dic.get("capital")

        if capital:
            url = "https://restcountries.com/v3.1/capital/"
            res = requests.get(url+capital)
            data = res.json()
            result = data[0]["name"]["common"]
        
    
        str = capital + " is the capital of " + result + "."   
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(str.encode('utf-8'))
        return