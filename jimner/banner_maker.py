import json
from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm
import json

class jimner:

    def print_actual_banner(self,get_list):
        # this returns the actual banner by taking the list as input
        
        art_split = [art.split("\n") for art in get_list]
        zipped = zip(*art_split)

        for elems in zipped:
            print("".join(elems))
            #pass
        

    def get_banner_text(self,get_banner_name, get_banner_text):
        # get the banner and text
        file_banner_name = get_banner_name+".json"
        # firstly clean the text!

        make_list = []
        try:
            
            with open(file_banner_name) as f:
                data = json.load(f)
            for letters in get_banner_text:
                # to make the actual list containing the banner elements
                if data[letters]!="":
                    make_list.append(data[letters])
            #print(make_list)
            return make_list    
        except:
            #print("No file exists or something went wrong!")
            return -1
        
if __name__ == "__main__":
    a = jimner()

    with open('data.json') as f:
        data = json.load(f)

    total_font_present = []
    for item in data:
        #print(item)
        total_font_present.append(item)
    for font in total_font_present:
        try:
            list_ = a.get_banner_text(font,'Jimner123')
            #print(list_)
            print(font ,"=> ")
            a.print_actual_banner(list_)
        except:
            pass




