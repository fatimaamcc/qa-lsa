#from selenium import webdriver
#-*- coding: utf-8 -*-
import re
import urlparse

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

with open("sitemap.txt") as file:
        for line in file:
            substring = "https://essentials.salesforce.com/"
            if substring in line:
                start = line.find('h')
                end = findnth(line, "<", 2)
                print(line[start:end])
            # #path = urlparse(line)
            # urls = re.findall('https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+', line)
            # #print(line)

            # line.find('h')
            # start = line.find('h')
            # end = line.rfind('/')
            # #print(line[, start[, end]])
            # print(line)

