#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import os
import sys
import time

input_file = "list.txt"
output_file = "result.txt"
error_file = "error.txt"

server = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20130522?"
format = "format=json"
app_id = "&applicationId="

def createUrl(isbn):
    return server + format + app_id + "&isbn=" + isbn.replace("-", "")

def getImageUrl(url):
    response = urllib2.urlopen(url)
    data = response.read()
    decode_json_data = json.loads(data)
    print (decode_json_data['count'])
    if decode_json_data['count'] == 0:
        return "http://seven-moon.main.jp/images/no.gif"

    items = decode_json_data['Items']
    item = items[0]
    item = item['Item']
    image_url = item['largeImageUrl']
    return image_url

def main():
    print "main"
    fin = open(input_file, "r")
    fout = open(output_file, "w")
    ferr = open(error_file, "w")
    for row in fin:
        api_url = createUrl(row)
        image_url = getImageUrl(api_url)
        print image_url
        if image_url == "http://seven-moon.main.jp/images/no.gif":
            ferr.write(api_url)
            ferr.flush()
        fout.write(image_url + "\n")
        fout.flush()
        time.sleep(0.5)

    fin.close()
    fout.close()
    ferr.close()

if __name__ == "__main__":
    main()
