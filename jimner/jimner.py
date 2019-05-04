import json
from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm
import json
import os




class jimner:
    """
    This is the modified version of Pyfiglet, cause I didn't knew it existed ;) when I built this. This is different in the sense that it uses
    JSON data, which is very much portable, and doesn't requires REGEX operations!
    """

    def __init__(self):
        self.SCRIPT_DIR = os.path.dirname(__file__)
    def __get_dir__(self):
        return self.SCRIPT_DIR
    def __get_all_fonts__(self):
        with open(os.path.join(self.SCRIPT_DIR+'/fonts/data.json')) as f:
            data = json.load(f)
        ALL_FONTS = []
        for items in data:
            ALL_FONTS.append(items)
        return ALL_FONTS
    
    def __font_is_present__(self,font_name):
        with open(os.path.join(self.SCRIPT_DIR+'/fonts/data.json')) as f:
            data = json.load(f)
        try:
            if len(data[font_name])>0:
                return True
        except Exception as e:
            print(e)
            return False
    
    def print_actual_banner(self,get_list):
        # this returns the actual banner by taking the list as input
        print(get_list)
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

        with open(self.SCRIPT_DIR+"/fonts/"+file_banner_name) as f:
            data = json.load(f)
        for letters in get_banner_text:
            # to make the actual list containing the banner elements
            if data[letters]!="":
                make_list.append(data[letters])
        #print(make_list)
        return make_list    

    
    def get_banner_from_text(self,get_ban_name,get_text):
        
        self.print_actual_banner(self.get_banner_text(get_ban_name,get_text))





