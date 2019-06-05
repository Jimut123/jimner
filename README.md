# JIMNER 
[![PyPI version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=1.2.3)](https://pypi.org/project/jimner/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)
![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)
![Contribute](https://img.shields.io/badge/-contribute-0a0a0a.svg?style=flat&colorA=0a0a0a)



A BANNER PROTOTYPE FOR CLI/UNIX/LINUX/WINDOWS.

Better than `Pyfiglet`, because this uses JSON portable data !

The main utilities are:
* generate text banner for PATCH
* generate text banner for Command Line Interface(CLI)
* generate banner for almost any text, in 314 font samples!
* For decorating programs, README or TEXT decoration
* ASCII art


Note: 
* All the scripts are automated!
* A total of 314 fonts are present!


## Installation

```
$ sudo pip install jimner
```

## Features

```python
>>from jimner import jimner
>>a=jimner()
>>a.__get_dir__()
shows the directory/Path
>>a.__get_all_fonts__()
['1Row', '3-D', '3D Diagonal', '3D-ASCII', '3x5', '4Max', '5 Line Oblique', 'AMC 3 Line', 'AMC 3 Liv1', 'AMC AAA01', 'AMC Neko', 'AMC Razor', 'AMC Razor2', 'AMC Slash', 'AMC Slider', 'AMC Thin', 'AMC Tubes', 'AMC Untitled', 'ANSI Shadow', 'ASCII New Roman', 'Abraxis-Big', 'Abraxis-Small', 'Acrobatic', 'Alligator', 'Alligator2', 'Alpha', 'Alphabet', 'Arrows', 'Avatar', 'Banner', 'Banner3', 'Banner3-D', 'Banner4', 'Barbwire', 'Basic', 'Bear', 'Bell', 'Benjamin', 'Bent', 'Big', 'Big Chief', 'Big Money-ne', 'Big Money-nw', 'Big Money-se', 'Big Money-sw', 'Bigfig', 'Binary', 'Blest', 'Block', 'Blocks', 'Bloody', 'Boie', 'Boie2', 'Bolger', "Bone's Font", 'Braced', 'Bright', 'Broadway', 'Broadway KB', 'Bubble', 'Bulbhead', 'CaMiZ', 'Caligraphy', 'Caligraphy2', 'Calvin S', 'Cards', 'Catwalk', 'CeA', 'CeA2', 'Cheese', 'Chiseled', 'Chunky', 'Coinstak', 'Cola', 'Colossal', 'Computer', 'Contessa', 'Contrast', 'Cosmike', 'Crawford', 'Crawford2', 'Crazy', 'Cricket', 'Cursive', 'Cyberlarge', 'Cybermedium', 'Cybersmall', 'Cygnet', 'DANC4', 'DWhistled', 'DaiR', 'Dancing Font', 'Decimal', 'Def Leppard', 'Delta Corps Priest 1', 'Diamond', 'Diet Cola', 'Digital', 'Doh', 'Doom', 'Dot Matrix', 'Double', 'Double Shorts', 'Dr Pepper', 'Efti Chess', 'Efti Font', 'Efti Italic', 'Efti Piti', 'Efti Robot', 'Efti Wall', 'Efti Water', 'Electronic', 'Elite', 'Epic', 'Fender', 'Filter', 'Filth', 'Fire Font-k', 'Fire Font-s', 'Flipped', 'Flower Power', 'FoGG', 'Four Tops', 'Fraktur', 'Fun Face', 'Fun Faces', 'Fuzzy', 'Galactus', 'Georgi16', 'Georgia11', 'Ghost', 'Ghoulish', 'Glenyn', 'Glue', 'Goofy', 'Gothic', 'Graceful', 'Gradient', 'Graffiti', 'Greek', "HeX's Font", 'Heart Left', 'Heart Right', 'Hellfire', 'Henry 3D', 'Hex', 'Hieroglyphs', 'Hollywood', 'Horizontal Left', 'Horizontal Right', 'ICL-1900', 'Impossible', 'Invita', 'Isometric1', 'Isometric2', 'Isometric3', 'Isometric4', 'Italic', 'Ivrit', 'JS Block Letters', 'JS Bracket Letters', 'JS Capital Curves', 'JS Cursive', 'JS Stick Letters', 'Jacky', 'Jazmine', 'Jerusalem', 'Katakana', 'Kban', 'Keyboard', 'Knob', 'LCD', 'Larry 3D', 'Lean', 'Letters', 'Lil Devil', 'Line Blocks', 'Linux', 'Lockergnome', 'Madrid', 'Marquee', 'Maxfour', 'MeDi', 'Mer', 'Merlin1', 'Merlin2', 'Mike', 'Mini', 'Mirror', 'Mnemonic', 'Modular', 'Morse', 'Moscow', 'Mshebrew210', 'Muzzle', 'NScript', 'NT Greek', 'NV Script', 'Nancyj', 'Nancyj-Fancy', 'Nancyj-Underlined', 'Nipples', 'O8', 'OS2', 'Octal', 'Ogre', 'Old Banner', "Patorjk's Cheese", 'Patorjk-HeX', 'Pawp', 'Peaks', 'Peaks Slant', 'Pebbles', 'Pepper', 'Poison', 'PsY', 'PsY2', 'Puffy', 'Puzzle', 'Pyramid', 'Rammstein', 'Rectangles', 'Reeko Font 1', 'Relief', 'Relief2', 'Reverse', 'Ribbit', 'Ribbit2', 'Ribbit3', 'Roman', 'Rotated', 'Rounded', 'Rowan Cap', 'Rozzo', 'Runic', 'Runyc', 'S Blood', 'SL Script', 'Santa Clara', 'Script', 'Serifcap', 'Shadow', 'Shimrod', 'Short', 'Slant', 'Slant Relief', 'Slide', 'Small', 'Small Caps', 'Small Isometric1', 'Small Keyboard', 'Small Poison', 'Small Script', 'Small Shadow', 'Small Slant', 'Small Tengwar', 'Soft', 'Sony', 'Speed', 'Spliff', 'Stacey', 'Stampate', 'Stampatello', 'Standard', 'Star Strips', 'Star Wars', 'Stellar', 'Stforek', 'Stick Letters', 'Stop', 'Straight', 'Stronger Than All', 'Sub-Zero', 'Swamp Land', 'Swan', 'Sweet', 'THIS', 'TRaC', 'TRaC Mini', 'TRaC Tiny', "TRaC's Old School Font", 'Tanja', 'Tengwar', 'Term', 'Test1', 'The Edge', 'Thick', 'Thin', 'Thorned', 'Three Point', 'Ticks', 'Ticks Slant', 'Tiles', 'Tinker-Toy', 'Tombstone', 'Train', 'Trek', 'Tsalagi', 'Tubular', 'Twiggy', 'Twisted', 'Two Point', 'USA Flag', 'Univers', 'Varsity', 'Wavy', 'Weird', 'Wet Letter', 'Whimsy', 'Wow', 'X-Pose', 'X99', 'X992', 'Zodi']
>>a.__font_is_present__('Zodi')
True
>>a.get_banner_from_text('X992','jimner')
             ,·´¨'`·,'           ,.-·.           ,·'´¨;.  '                                ,.         ,·´'; '                    _,.,  °            ,. -  .,                  
            :,   .:´\           /    ;'\'        ;   ';:\           .·´¨';\           ;'´*´ ,'\       ,'  ';'\°           ,.·'´  ,. ,  `;\ '      ,' ,. -  .,  `' ·,          
            ;   :\:::\         ;    ;:::\       ;     ';:'\      .'´     ;:'\         ;    ';::\      ;  ;::'\          .´   ;´:::::\`'´ \'\      '; '·~;:::::'`,   ';\       
           ;  ,':::\·´'       ';    ;::::;'     ;   ,  '·:;  .·´,.´';  ,'::;'        ;      '\;'      ;  ;:::;         /   ,'::\::::::\:::\:'      ;   ,':\::;:´  .·´::\'     
,.,      .'  ,'::::;''         ;   ;::::;      ;   ;'`.    ¨,.·´::;'  ;:::;         ,'  ,'`\   \      ;  ;:::;        ;   ;:;:-·'~^ª*';\'´         ;  ·'-·'´,.-·'´:::::::';   
;   '\   ;  ,'::::;           ';  ;'::::;      ;  ';::; \*´\:::::;  ,':::;‘         ;  ;::;'\  '\    ;  ;:::;         ;  ,.-·:*'´¨'`*´\::\ '     ;´    ':,´:::::::::::·´'     
 \  ';',·'  ,'::::;           ;  ';:::';      ';  ,'::;   \::\;:·';  ;:::; '       ;  ;:::;  '\  '\ ,'  ;:::;'       ;   ;\::::::::::::'\;'       ';  ,    `·:;:-·'´          
  '\    ,.'\::::;''           ';  ;::::;'     ;  ';::;     '*´  ;',·':::;‘        ,' ,'::;'     '\   ¨ ,'\::;'       ;  ;'_\_:;:: -·^*';\         ; ,':\'`:·.,  ` ·.,         
    \¯\::::\:;' ‘              \*´\:::;‘      \´¨\::;          \¨\::::;           ;.'\::;        \`*´\::\; °         ';    ,  ,. -·:*'´:\:'\°     \·-;::\:::::'`:·-.,';       
     '\::\;:·´'                 '\::\:;'       '\::\;            \:\;·'           \:::\'          '\:::\:' '          \`*´ ¯\:::::::::::\;' '      \::\:;'` ·:;:::::\::\'     
       ¯       °                  `*´‘           '´¨               ¨'               \:'             `*´'‚               \:::::\;::-·^*'´            '·-·'       `' · -':::''  
                                                                                                                          `*´¯                                                

```

## Fonts

<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/1Row.json" alt="1Row" target="_blank">1Row</a></b>
<pre>
_T  |  |\/|  |_|  ~|~  
                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/3-D.json" alt="3-D" target="_blank">3-D</a></b>
<pre>
      **  **                          **   
     /** //                          /**   
     /**  **  **********   **   **  ****** 
     /** /** //**//**//** /**  /** ///**/  
     /** /**  /** /** /** /**  /**   /**   
 **  /** /**  /** /** /** /**  /**   /**   
//*****  /**  *** /** /** //******   //**  
 /////   //  ///  //  //   //////     //   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/3D Diagonal.json" alt="3D Diagonal" target="_blank">3D Diagonal</a></b>
<pre>
                                                                            
         ,---._                                                             
       .-- -.' \                       ____                        ___      
       |    |   :   ,--,             ,'  , `.                    ,--.'|_    
       :    ;   | ,--.'|          ,-+-,.' _ |           ,--,     |  | :,'   
       :        | |  |,        ,-+-. ;   , ||         ,'_ /|     :  : ' :   
       |    :   : `--'_       ,--.'|'   |  ||    .--. |  | :   .;__,'  /    
       :          ,' ,'|     |   |  ,', |  |,  ,'_ /| :  . |   |  |   |     
       |    ;   | '  | |     |   | /  | |--'   |  ' | |  . .   :__,'| :     
   ___ l          |  | :     |   : |  | ,      |  | ' |  | |     '  : |__   
 /    /\    J   : '  : |__   |   : |  |/       :  | : ;  ; |     |  | '.'|  
/  ../  `..-    , |  | '.'|  |   | |`-'        '  :  `--'   \    ;  :    ;  
\    \         ;  ;  :    ;  |   ;/            :  ,      .-./    |  ,   /   
 \    \      ,'   |  ,   /   '---'              `--`----'         ---`-'    
  "---....--'      ---`-'                                                   
                                                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/3D-ASCII.json" alt="3D-ASCII" target="_blank">3D-ASCII</a></b>
<pre>
    ___       ___       _____ ______        ___  ___       _________    
   |\  \     |\  \     |\   _ \  _   \     |\  \|\  \     |\___   ___\  
   \ \  \    \ \  \    \ \  \\\__\ \  \    \ \  \\\  \    \|___ \  \_|  
 __ \ \  \    \ \  \    \ \  \\|__| \  \    \ \  \\\  \        \ \  \   
|\  \\_\  \    \ \  \    \ \  \    \ \  \    \ \  \\\  \        \ \  \  
\ \________\    \ \__\    \ \__\    \ \__\    \ \_______\        \ \__\ 
 \|________|     \|__|     \|__|     \|__|     \|_______|         \|__| 
                                                                        
                                                                        
                                                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/3x5.json" alt="3x5" target="_blank">3x5</a></b>
<pre>
                         
 ##   #              #   
  #       ###  # #  ###  
  #   #   ###  # #   #   
# #   ##  # #  ###   ##  
 #                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/4Max.json" alt="4Max" target="_blank">4Max</a></b>
<pre>
 88888  88  8b    d8  88   88  888888  
    88  88  88b  d88  88   88    88    
o.  88  88  88YbdP88  Y8   8P    88    
"bodP'  88  88 YY 88  `YbodP'    88    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/5 Line Oblique.json" alt="5 Line Oblique" target="_blank">5 Line Oblique</a></b>
<pre>
                                                             
          / /                                                
         / /      ( )       _   __                  __  ___  
        / /      / /      // ) )  ) )    //   / /    / /     
       / /      / /      // / /  / /    //   / /    / /      
 ((___/ /      / /      // / /  / /    ((___( (    / /       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC 3 Line.json" alt="AMC 3 Line" target="_blank">AMC 3 Line</a></b>
<pre>
  .  .-.  .  .  . .  .-.  
  |   |   |\/|  | |   |   
`-'  `-'  '  `  `-'   '   
                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC 3 Liv1.json" alt="AMC 3 Liv1" target="_blank">AMC 3 Liv1</a></b>
<pre>
.:;.;:.           .:;S;:.  .:;S;:.  .        
      S  .:;s;:'   )             S  S:;s;:'  
     :'           `:;S;:'  `:;S;:'  `        
                                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC AAA01.json" alt="AMC AAA01" target="_blank">AMC AAA01</a></b>
<pre>
    .S    .S    .S_SsS_S.     .S       S.    sdSS_SSSSSSbs   
   .SS   .SS   .SS~S*S~SS.   .SS       SS.   YSSS~S%SSSSSP   
   S%S   S%S   S%S `Y' S%S   S%S       S%S        S%S        
   S%S   S%S   S%S     S%S   S%S       S%S        S%S        
   S&S   S&S   S%S     S%S   S&S       S&S        S&S        
   S&S   S&S   S&S     S&S   S&S       S&S        S&S        
   S&S   S&S   S&S     S&S   S&S       S&S        S&S        
   S&S   S&S   S&S     S&S   S&S       S&S        S&S        
   d*S   S*S   S*S     S*S   S*b       d*S        S*S        
  .S*S   S*S   S*S     S*S   S*S.     .S*S        S*S        
sdSSS    S*S   S*S     S*S    SSSbs_sdSSS         S*S        
YSSY     S*S   SSS     S*S     YSSP~YSSY          S*S        
         SP            SP                         SP         
         Y             Y                          Y          
                                                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Neko.json" alt="AMC Neko" target="_blank">AMC Neko</a></b>
<pre>
      SSSSS                                                            
      SSSSS  SSSSS  .sSSSsSS SSsSSSSS  .sSSS s.     .sSSSSSSSSSSSSSs.  
      S SSS  S SSS  S SSS  SSS  SSSSS  S SSS SSSs.  SSSSS S SSS SSSSS  
      S  SS  S  SS  S  SS   S   SSSSS  S  SS SSSSS  SSSSS S  SS SSSSS  
      S..SS  S..SS  S..SS       SSSSS  S..SS SSSSS  `:S:' S..SS `:S:'  
      S:::S  S:::S  S:::S       SSSSS  S:::S SSSSS        S:::S        
      S;;;S  S;;;S  S;;;S       SSSSS  S;;;S SSSSS        S;;;S        
SSSSS S%%%S  S%%%S  S%%%S       SSSSS  S%%%S SSSSS        S%%%S        
`:;SSsSSSSS  SSSSS  SSSSS       SSSSS  SSSSSsSSSSS        SSSSS        
                                                                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Razor.json" alt="AMC Razor" target="_blank">AMC Razor</a></b>
<pre>
                                  ___          ___  ___   ___  
       .'|    .'|    .'|\/|`.    |   | |`.    `._|=|   |=|_.'  
     .'  |  .'  |  .'  |  |  `.  |   | |  `.       |   |       
     |   |  |   |  |   |  |   |  |   | |   |       |   |       
___  |   |  |   |  |   |  |   |  `.  | |   |       `.  |       
`._|=|__.'  |___|  |___|  |___|    `.|=|___|         `.|       
                                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Razor2.json" alt="AMC Razor2" target="_blank">AMC Razor2</a></b>
<pre>
     .     .        . .    .        . .        . .    .     
     |`+.  |`+.  .+'|=|`+.=|`+.  .+'| |`+.  .+'|=|`+.=|`+.  
     |  |  |  |  |  | `+ | `+ |  |  | |  |  |.+' |  | `+.|  
     |  |  |  |  |  |  | |  | |  |  | |  |       |  |       
     |  |  |  |  |  |  | |  | |  |  | |  |       |  |       
.    |  |  |  |  |  |  | |  | |  |  | |  |       |  |       
|`+. |  |  |  |  |  |  | |  | |  |  | |  |       |  |       
`+.|=|.+'  |.+'  `+.|  |.|  |+'  `+.|=|.+'       |.+'       
                                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Slash.json" alt="AMC Slash" target="_blank">AMC Slash</a></b>
<pre>
      s.                                         
      SS.  s.   .s5ssSs.   .s    s.   .s5SSSSs.  
      S%S  SS.     SS SS.        SS.     SSS     
      S%S  S%S  sS SS S%S  sS    S%S     S%S     
      S%S  S%S  SS :; S%S  SS    S%S     S%S     
      S%S  S%S  SS    S%S  SS    S%S     S%S     
      `:;  `:;  SS    `:;  SS    `:;     `:;     
.,;   ;,.  ;,.  SS    ;,.  SS    ;,.     ;,.     
`:;;;;;:'  ;:'  :;    ;:'  `:;;;;;:'     ;:'     
                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Slider.json" alt="AMC Slider" target="_blank">AMC Slider</a></b>
<pre>
                                                              
         |  |        .'. .`.        |         |  `````|`````  
         |  |      .'   `   `.      |         |       |       
.        |  |    .'           `.    |         |       |       
`..____..'  |  .'               `.  `._______.'       |       
                                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Thin.json" alt="AMC Thin" target="_blank">AMC Thin</a></b>
<pre>
    .-.  .-.  .-.-. .-.-.  .-.   .-.  .-..-..-.  
    | |  | |  | |~.-.~| |  | |   | |   ~ | | ~   
    | |  | |  | |  ~  | |  | |   | |     | |     
    | |  | |  | |     | |  | |   | |     | |     
 __ | |  | |  | |     | |  | | _ | |     | |     
`--'`-'  `-'  `-'     `-'  `-'`-'`-'     `-'     
                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Tubes.json" alt="AMC Tubes" target="_blank">AMC Tubes</a></b>
<pre>
        d  d  d s   sb  d       b  sss sssss  
        S  S  S  S S S  S       S      S      
        S  S  S   S  S  S       S      S      
        S  S  S      S  S       S      S      
d       P  S  S      S  S       S      S      
 S     S   S  S      S   S     S       S      
  "sss"    P  P      P    "sss"        P      
                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/AMC Untitled.json" alt="AMC Untitled" target="_blank">AMC Untitled</a></b>
<pre>
    ,'',                                              
    ;  ;                                              
    ;  ;  ,'',  ,'',,'',,'',  ,',  ,',  ,'',,'',,'',  
    ;  ;  ;  ;  ;  ;', ;', ;  ; ;  ; ;  ',,';  ;',,'  
    ;  ;  ;  ;  ;  ; ; ; ; ;  ; ;  ; ;      ;  ;      
,'',;  ;  ;  ;  ;  ; ; ; ; ;  ; ',,' ;      ;  ;      
',,'',,'  ',,'  ',,' ',' ','  ',,'',,'      ',,'      
                                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/ANSI Shadow.json" alt="ANSI Shadow" target="_blank">ANSI Shadow</a></b>
<pre>
     ██╗ ██╗ ███╗   ███╗ ██╗   ██╗ ████████╗ 
     ██║ ██║ ████╗ ████║ ██║   ██║ ╚══██╔══╝ 
     ██║ ██║ ██╔████╔██║ ██║   ██║    ██║    
██   ██║ ██║ ██║╚██╔╝██║ ██║   ██║    ██║    
╚█████╔╝ ██║ ██║ ╚═╝ ██║ ╚██████╔╝    ██║    
 ╚════╝  ╚═╝ ╚═╝     ╚═╝  ╚═════╝     ╚═╝    
                                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/ASCII New Roman.json" alt="ASCII New Roman" target="_blank">ASCII New Roman</a></b>
<pre>
  _,     __,    __, _,  _, _,   ____,  
 (-|    (-|    (-|\/|  (-|  \  (-|     
 __|,    _|_,   _| _|,  _|__/   _|,    
(       (      (       (       (       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Abraxis-Big.json" alt="Abraxis-Big" target="_blank">Abraxis-Big</a></b>
<pre>
               '                          /¯¯¯¯¯¯\                         ‘                        '                                                                                        
'                                        ¦\______/¦‚ ‚                         /¯¯¯¯¯¯¯¯¦                                 '                       /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\                     
             ¦\¯¯¯¯¯¯¯¯¯\                ¦'¦::::::::::¦'¦‚ ‚  ¦¯¯¯¯¯¯¯¯\/ '/¦:.          ¦            '/¯¯¯¯¯¯¯¯¯\ /¯¯¯¯¯¯¯¯¯'\                  '¦:.                                  ”¦    
             '\:\               \        '\¦:::::::::'¦/      ¦:.            ¦\/ /            '¦     ¦\                 '¦¦:.               /¦   ¦\______/¦:°       ¦\_______/¦              
              ¦::¦:.             ¦°    ¦\¯¯¯¯¯¯¯¯\ ’          ¦:.            '\¦/              ¦      \¦:.              '¦¦:.               ¦/   ¦'¦:::::::::'¦ ¦:.       ¦ ¦:::::::::::¦”¦  
/¯¯¯¯¯¯¯¯/'¦:.             ¦‚‚         '\'\              \‚‚  ¦:.             '¦:.             ¦      /                 /\                 \‚‚   '\¦:::::::::¦/¦:.       '¦\¦::::::::::'¦/   
¦:.            ¦;¦:.             ¦‚‚     \¦:.            ¦„   ¦:.             '¦:.             ¦     ¦:.                ¦ '¦:.                ¦    ¯¯¯¯¯ '/          '\ ¯¯¯¯¯¯’              
¦\________\¦________/¦°                   ¦:.            ¦„   ¦________/'\________‚¦                 ¦\__________\/__________/¦                             ¦\______/¦                       
¦:¦::::::::::::::¦¦::::::::::::'¦:¦‚‚    /              /¦‚   ¦::‚:::::’:::::¦'¦'¦::::::::::::::'¦   ¦:¦:::::::::::::::::¦¦:::::::::::::::::¦:¦             ¦'¦::::::::::¦'¦                 
'\¦::::::::::::::¦¦:::::::::::::¦/°‚    '¦________'¦/         ¦::::‚::::’::::¦'¦'¦::::::::::::::'¦   '\¦:::::::::::::::::¦¦:::::::::::::::::”¦/             '\¦:::::::::”¦/                  
  ¯¯¯¯¯¯¯¯° ¯¯¯¯¯¯¯                     '¦::::::::::::::'¦     ¯¯¯¯¯¯¯¯ ” ¯¯¯¯¯¯¯¯‚                    ¯¯¯¯¯¯¯¯¯¯ º¯¯¯¯¯¯¯¯¯                                  ¯¯¯¯¯º                         
'                                       '¦::::::::::::::'¦                 ‘                                                                 '                                               
                               '       ’ ¯¯¯¯¯¯¯¯ ’           ‘                                     '                                                                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Abraxis-Small.json" alt="Abraxis-Small" target="_blank">Abraxis-Small</a></b>
<pre>
                    ___                                                        ’            
                   ¦___¦”‚‚   ¦˜¨¯¯¨˜\          ’                            ’              
        '¦˜¨¯¨˜¦° ¦\˜¨¯¨˜\‚   ¦:.     ¦\\/˜¨¯¯¨˜¦°   ¦˜¨¯¨˜¦'¦˜¨¯¨˜'¦‘‘  ¦˜¨¯¯¨˜˜¨¯¯¨˜¦°    
¦˜¨¯¨˜/ ¦:.    ¦„  \¦:.   '¦º ¦:.     ¦ \/¦:.     ¦  ¦:.   / '\     '¦‚‚ ¦\__/    \__'/¦’   
¦\___'\¦_'__'¦‚    /___/¦º    ¦____¦\'¦/¦____¦’      ¦\___\/___/¦”       ¦'¦¯ '\__'/`)/¦ ¦  
¦ ¦¯)/¯¦¯ ¯)/ ¦    ¦¯`)/'¦;¦‚ ¦¯`)/¯'¦:. ¦¯\(¯¯¦‚    ¦ ¦ ¯`)/¯¯  ¦ ¦’    '\¦__¦`)/'¦__'¦/°  
’\¦___¦¦____¦      ¦___¦/‚‚   ¦____¦:. ¦____¦        '\¦______;¦/’’           '¦__¦‘’   ‚   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Acrobatic.json" alt="Acrobatic" target="_blank">Acrobatic</a></b>
<pre>
         __o__     o                                      o      
           |     _<|>_                                   <|>     
          / \                                            < >     
          \o/      o     \o__ __o__ __o     o       o     |      
           |      <|>     |     |     |>   <|>     <|>    o__/_  
          < >     / \    / \   / \   / \   < >     < >    |      
  \        |      \o/    \o/   \o/   \o/    |       |     |      
   o       o       |      |     |     |     o       o     o      
   <\__ __/>      / \    / \   / \   / \    <\__ __/>     <\__   
                                                                 
                                                                 
                                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Alligator.json" alt="Alligator" target="_blank">Alligator</a></b>
<pre>
     :::::::::::        :::::::::::          :::   :::       :::    :::    :::::::::::  
        :+:                :+:             :+:+: :+:+:      :+:    :+:        :+:       
       +:+                +:+            +:+ +:+:+ +:+     +:+    +:+        +:+        
      +#+                +#+            +#+  +:+  +#+     +#+    +:+        +#+         
     +#+                +#+            +#+       +#+     +#+    +#+        +#+          
#+# #+#                #+#            #+#       #+#     #+#    #+#        #+#           
#####             ###########        ###       ###      ########         ###            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Alligator2.json" alt="Alligator2" target="_blank">Alligator2</a></b>
<pre>
:::::::::::  :::::::::::  ::::    ::::   :::    :::  :::::::::::  
    :+:          :+:      +:+:+: :+:+:+  :+:    :+:      :+:      
    +:+          +:+      +:+ +:+:+ +:+  +:+    +:+      +:+      
    +#+          +#+      +#+  +:+  +#+  +#+    +:+      +#+      
    +#+          +#+      +#+       +#+  +#+    +#+      +#+      
#+# #+#          #+#      #+#       #+#  #+#    #+#      #+#      
 #####       ###########  ###       ###   ########       ###      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Alpha.json" alt="Alpha" target="_blank">Alpha</a></b>
<pre>
          _____                     _____                     _____                     _____                 _____           
         /\    \                   /\    \                   /\    \                   /\    \               /\    \          
        /::\    \                 /::\    \                 /::\____\                 /::\____\             /::\    \         
        \:::\    \                \:::\    \               /::::|   |                /:::/    /             \:::\    \        
         \:::\    \                \:::\    \             /:::::|   |               /:::/    /               \:::\    \       
          \:::\    \                \:::\    \           /::::::|   |              /:::/    /                 \:::\    \      
           \:::\    \                \:::\    \         /:::/|::|   |             /:::/    /                   \:::\    \     
           /::::\    \               /::::\    \       /:::/ |::|   |            /:::/    /                    /::::\    \    
  _____   /::::::\    \     ____    /::::::\    \     /:::/  |::|___|______     /:::/    /      _____         /::::::\    \   
 /\    \ /:::/\:::\    \   /\   \  /:::/\:::\    \   /:::/   |::::::::\    \   /:::/____/      /\    \       /:::/\:::\    \  
/::\    /:::/  \:::\____\ /::\   \/:::/  \:::\____\ /:::/    |:::::::::\____\ |:::|    /      /::\____\     /:::/  \:::\____\ 
\:::\  /:::/    \::/    / \:::\  /:::/    \::/    / \::/    / ~~~~~/:::/    / |:::|____\     /:::/    /    /:::/    \::/    / 
 \:::\/:::/    / \/____/   \:::\/:::/    / \/____/   \/____/      /:::/    /   \:::\    \   /:::/    /    /:::/    / \/____/  
  \::::::/    /             \::::::/    /                        /:::/    /     \:::\    \ /:::/    /    /:::/    /           
   \::::/    /               \::::/____/                        /:::/    /       \:::\    /:::/    /    /:::/    /            
    \::/    /                 \:::\    \                       /:::/    /         \:::\__/:::/    /     \::/    /             
     \/____/                   \:::\    \                     /:::/    /           \::::::::/    /       \/____/              
                                \:::\    \                   /:::/    /             \::::::/    /                             
                                 \:::\____\                 /:::/    /               \::::/    /                              
                                  \::/    /                 \::/    /                 \::/____/                               
                                   \/____/                   \/____/                   ~~                                     
                                                                                                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Alphabet.json" alt="Alphabet" target="_blank">Alphabet</a></b>
<pre>
    J                    t   
    J  ii                t   
    J      mmmm   u  u  ttt  
J   J  ii  m m m  u  u   t   
 JJJ   ii  m m m   uuu   tt  
                             
                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Arrows.json" alt="Arrows" target="_blank">Arrows</a></b>
<pre>
     >=>                                  >=>    
     >=>   >>                             >=>    
     >=>       >===>>=>>==>   >=>  >=>  >=>>==>  
     >=>  >=>   >=>  >>  >=>  >=>  >=>    >=>    
     >=>  >=>   >=>  >>  >=>  >=>  >=>    >=>    
>>   >=>  >=>   >=>  >>  >=>  >=>  >=>    >=>    
 >===>    >=>  >==>  >>  >=>    >==>=>     >=>   
                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Avatar.json" alt="Avatar" target="_blank">Avatar</a></b>
<pre>
    _   _   _       _      _____  
   / | / \ / \__/| / \ /\ /__ __\ 
   | | | | | |\/|| | | ||   / \   
/\_| | | | | |  || | \_/|   | |   
\____/ \_/ \_/  \| \____/   \_/   
                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Banner.json" alt="Banner" target="_blank">Banner</a></b>
<pre>
       #                                
       #   #   #    #   #    #   #####  
       #   #   ##  ##   #    #     #    
       #   #   # ## #   #    #     #    
 #     #   #   #    #   #    #     #    
 #     #   #   #    #   #    #     #    
  #####    #   #    #    ####      #    
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Banner3.json" alt="Banner3" target="_blank">Banner3</a></b>
<pre>
      ##  ####  ##     ##  ##     ##  ########  
      ##   ##   ###   ###  ##     ##     ##     
      ##   ##   #### ####  ##     ##     ##     
      ##   ##   ## ### ##  ##     ##     ##     
##    ##   ##   ##     ##  ##     ##     ##     
##    ##   ##   ##     ##  ##     ##     ##     
 ######   ####  ##     ##   #######      ##     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Banner3-D.json" alt="Banner3-D" target="_blank">Banner3-D</a></b>
<pre>
::::::'##: '####: '##::::'##: '##::::'##: '########: 
:::::: ##: . ##::  ###::'###:  ##:::: ##: ... ##..:: 
:::::: ##: : ##::  ####'####:  ##:::: ##: ::: ##:::: 
:::::: ##: : ##::  ## ### ##:  ##:::: ##: ::: ##:::: 
'##::: ##: : ##::  ##. #: ##:  ##:::: ##: ::: ##:::: 
 ##::: ##: : ##::  ##:.:: ##:  ##:::: ##: ::: ##:::: 
. ######:: '####:  ##:::: ##: . #######:: ::: ##:::: 
:......::: ....:: ..:::::..:: :.......::: :::..::::: 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Banner4.json" alt="Banner4" target="_blank">Banner4</a></b>
<pre>
.......## .#### .##.....## .##.....## .######## 
.......## ..##. .###...### .##.....## ....##... 
.......## ..##. .####.#### .##.....## ....##... 
.......## ..##. .##.###.## .##.....## ....##... 
.##....## ..##. .##.....## .##.....## ....##... 
.##....## ..##. .##.....## .##.....## ....##... 
..######. .#### .##.....## ..#######. ....##... 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Barbwire.json" alt="Barbwire" target="_blank">Barbwire</a></b>
<pre>
     ><<                              ><<   
     ><<  ><                          ><<   
     ><<     ><<< ><< ><<  ><<  ><< ><>< >< 
     ><< ><<  ><<  ><  ><< ><<  ><<   ><<   
     ><< ><<  ><<  ><  ><< ><<  ><<   ><<   
><   ><< ><<  ><<  ><  ><< ><<  ><<   ><<   
 ><<<<   ><< ><<<  ><  ><<   ><<><<    ><<  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Basic.json" alt="Basic" target="_blank">Basic</a></b>
<pre>
   d88b  d888888b  .88b  d88.  db    db  d888888b  
   `8P'    `88'    88'YbdP`88  88    88  `~~88~~'  
    88      88     88  88  88  88    88     88     
    88      88     88  88  88  88    88     88     
db. 88     .88.    88  88  88  88b  d88     88     
Y8888P   Y888888P  YP  YP  YP  ~Y8888P'     YP     
                                                   
                                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bear.json" alt="Bear" target="_blank">Bear</a></b>
<pre>
   _     _       _     _       _     _       _     _       _     _    
  (c).-.(c)     (c).-.(c)     (c).-.(c)     (c).-.(c)     (c).-.(c)   
   / ._. \       / ._. \       / ._. \       / ._. \       / ._. \    
 __\( Y )/__   __\( Y )/__   __\( Y )/__   __\( Y )/__   __\( Y )/__  
(_.-/'-'\-._) (_.-/'-'\-._) (_.-/'-'\-._) (_.-/'-'\-._) (_.-/'-'\-._) 
   || J ||       || I ||       || M ||       || U ||       || T ||    
 _.' `-' '._   _.' `-' '._   _.' `-' '._   _.' `-' '._   _.' `-' '._  
(.-./`-'\.-.) (.-./`-'\.-.) (.-./`-'\.-.) (.-./`-'\.-.) (.-./`-'\.-.) 
 `-'     `-'   `-'     `-'   `-'     `-'   `-'     `-'   `-'     `-'  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bell.json" alt="Bell" target="_blank">Bell</a></b>
<pre>
  _______                        .    
 '   /     `  , _ , _    ,   .  _/_   
     |     |  |' `|' `.  |   |   |    
     |     |  |   |   |  |   |   |    
  `--/     /  /   '   /  `._/|   \__/ 
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Benjamin.json" alt="Benjamin" target="_blank">Benjamin</a></b>
<pre>
.]||\/||_|"|"
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bent.json" alt="Bent" target="_blank">Bent</a></b>
<pre>
        |\¯¯¯\           |\¯¯¯\_'      /¯¯¯¯\        '          |\¯¯¯\|\¯¯¯\         |¯¯¯¯¯¯¯¯|'         
         \|     |'       |:|     '|'  /       _'\/¯¯¯¯\_'       '\|     |\|     '|   |\_______/|°        
 /¯¯¯/|'|     '|'        '\/     /|   |\      \ \_/\      \      '|     '\|      |_  '\|::·|    |·::|/'  
|\     '\|'|     '|'     /     '/:|   |:\      \:::/       /|    '|             |      ¯¯|    |¯¯'       
|:"\__,\|___'|°         /___/::|°     |::\____\/      /::|       '|\____/|__|_            '|__'|         
 \::|'¯` ||'¯`'¯|°     |'¯`;´'|::/    '\::|'¯`;/____,/:::|°      '|:|'¯`;´'|\|'¯`|_       |'¯`;,| _ '    
   \|::·.'||::·.·|'    |::·.· |/  _     '\|::·.|'¯`'v'¯`|::'/     \|::·.· | |::·|         |::·.´'|       
    ¯¯¯ ¯¯¯ '           ¯¯¯                ¯¯|::·.·  ,|:/'          ¯¯¯   ¯          _    ¯¯¯            
                           _'                  ¯¯¯¯   '                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Big.json" alt="Big" target="_blank">Big</a></b>
<pre>
       _    _                          _    
      | |  (_)                        | |   
      | |   _    _ __ ___     _   _   | |_  
  _   | |  | |  | '_ ` _ \   | | | |  | __| 
 | |__| |  | |  | | | | | |  | |_| |  | |_  
  \____/   |_|  |_| |_| |_|   \__,_|   \__| 
                                            
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Big Chief.json" alt="Big Chief" target="_blank">Big Chief</a></b>
<pre>
__________ _____ ________ ________ ______ 
        __                                
        /      ,                          
-------/-- ----- ---_--_- -------- --_/_- 
      /      /     / /  )   /   /    /    
_(___/____ _/___ _/_/__/_ _(___(__ _(_ __ 
                                          
                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Big Money-ne.json" alt="Big Money-ne" target="_blank">Big Money-ne</a></b>
<pre>
    /$$$$$  /$$                              /$$     
   |__  $$ |__/                             | $$     
      | $$  /$$  /$$$$$$/$$$$   /$$   /$$  /$$$$$$   
      | $$ | $$ | $$_  $$_  $$ | $$  | $$ |_  $$_/   
 /$$  | $$ | $$ | $$ \ $$ \ $$ | $$  | $$   | $$     
| $$  | $$ | $$ | $$ | $$ | $$ | $$  | $$   | $$ /$$ 
|  $$$$$$/ | $$ | $$ | $$ | $$ |  $$$$$$/   |  $$$$/ 
 \______/  |__/ |__/ |__/ |__/  \______/     \___/   
                                                     
                                                     
                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Big Money-nw.json" alt="Big Money-nw" target="_blank">Big Money-nw</a></b>
<pre>
   $$$$$\  $$\                              $$\      
   \__$$ | \__|                             $$ |     
      $$ | $$\  $$$$$$\$$$$\   $$\   $$\  $$$$$$\    
      $$ | $$ | $$  _$$  _$$\  $$ |  $$ | \_$$  _|   
$$\   $$ | $$ | $$ / $$ / $$ | $$ |  $$ |   $$ |     
$$ |  $$ | $$ | $$ | $$ | $$ | $$ |  $$ |   $$ |$$\  
\$$$$$$  | $$ | $$ | $$ | $$ | \$$$$$$  |   \$$$$  | 
 \______/  \__| \__| \__| \__|  \______/     \____/  
                                                     
                                                     
                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Big Money-se.json" alt="Big Money-se" target="_blank">Big Money-se</a></b>
<pre>
    _____   __                               __      
   |     \ |  \                             |  \     
    \$$$$$  \$$  ______ ____    __    __   _| $$_    
      | $$ |  \ |      \    \  |  \  |  \ |   $$ \   
 __   | $$ | $$ | $$$$$$\$$$$\ | $$  | $$  \$$$$$$   
|  \  | $$ | $$ | $$ | $$ | $$ | $$  | $$   | $$ __  
| $$__| $$ | $$ | $$ | $$ | $$ | $$__/ $$   | $$|  \ 
 \$$    $$ | $$ | $$ | $$ | $$  \$$    $$    \$$  $$ 
  \$$$$$$   \$$  \$$  \$$  \$$   \$$$$$$      \$$$$  
                                                     
                                                     
                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Big Money-sw.json" alt="Big Money-sw" target="_blank">Big Money-sw</a></b>
<pre>
    _____   __                               __      
   /     | /  |                             /  |     
   $$$$$ | $$/   _____  ____    __    __   _$$ |_    
      $$ | /  | /     \/    \  /  |  /  | / $$   |   
 __   $$ | $$ | $$$$$$ $$$$  | $$ |  $$ | $$$$$$/    
/  |  $$ | $$ | $$ | $$ | $$ | $$ |  $$ |   $$ | __  
$$ \__$$ | $$ | $$ | $$ | $$ | $$ \__$$ |   $$ |/  | 
$$    $$/  $$ | $$ | $$ | $$ | $$    $$/    $$  $$/  
 $$$$$$/   $$/  $$/  $$/  $$/   $$$$$$/      $$$$/   
                                                     
                                                     
                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bigfig.json" alt="Bigfig" target="_blank">Bigfig</a></b>
<pre>
                    
  |  o  __      _|_ 
\_|  |  ||| |_|  |_ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Binary.json" alt="Binary" target="_blank">Binary</a></b>
<pre>
01001010 01101001 01101101 01110101 01110100 
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Blest.json" alt="Blest" target="_blank">Blest</a></b>
<pre>
        '.·´¯/|°    '.·´¯/|                 '/¯¯`·.‘         '.·´¯/| |\¯`·.'     .·´¯/|¯¯|\¯`·.°       
        |\__\|°     |\__\|         '.·´¯¯\/ /\     \ ‘       |    |;| |'|    |  |__/ /   /| |__|‘      
        |\¯¯`·.     |\¯¯`·.‘      /     '/\_/;.;|    '\'‘    |    |/  \|    |   |  '|/   /;'|\'|   '|  
        |:|     |   |:|     '|° '/     '/'.'| '|;.'/     /|' |    |    |    |   |_/   /'; '| '|__|     
|\¯¯'\ '\|     '|   |.|     '|° |      | '\|_|'/__.·´ |‘     |`·._`·./    '|°     |   |;.'/    ‘       
|;`·._.\/__.·'|     |/__.·´|    |`·.__'\    '|    |;' '/     | .;|  /__.·´|°      |`·._`·.°            
'\.; |   ||  '|; '| |¯`;|:  |   |  '|    |    '|__'|.·´      '`·.|_|¯`;|;;;|      |  '|   '|'          
 '`·.|_.||_.|.·'‘   |__'|.·´'   `·.|__.|   ‘                       |__|.·´        `·.|__'|'‚           
       °                                          ‘                                       ‘            
°                                   ‘                                           ‘                      
             °                             ‘                                                    ‘      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Block.json" alt="Block" target="_blank">Block</a></b>
<pre>
                                                            
       _|    _|                                    _|       
       _|          _|_|_|  _|_|      _|    _|    _|_|_|_|   
       _|    _|    _|    _|    _|    _|    _|      _|       
 _|    _|    _|    _|    _|    _|    _|    _|      _|       
   _|_|      _|    _|    _|    _|      _|_|_|        _|_|   
                                                            
                                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Blocks.json" alt="Blocks" target="_blank">Blocks</a></b>
<pre>
 .----------------.   .----------------.   .----------------.   .----------------.   .----------------.  
| .--------------. | | .--------------. | | .--------------. | | .--------------. | | .--------------. | 
| |     _____    | | | |     _____    | | | | ____    ____ | | | | _____  _____ | | | |  _________   | | 
| |    |_   _|   | | | |    |_   _|   | | | ||_   \  /   _|| | | ||_   _||_   _|| | | | |  _   _  |  | | 
| |      | |     | | | |      | |     | | | |  |   \/   |  | | | |  | |    | |  | | | | |_/ | | \_|  | | 
| |   _  | |     | | | |      | |     | | | |  | |\  /| |  | | | |  | '    ' |  | | | |     | |      | | 
| |  | |_' |     | | | |     _| |_    | | | | _| |_\/_| |_ | | | |   \ `--' /   | | | |    _| |_     | | 
| |  `.___.'     | | | |    |_____|   | | | ||_____||_____|| | | |    `.__.'    | | | |   |_____|    | | 
| |              | | | |              | | | |              | | | |              | | | |              | | 
| '--------------' | | '--------------' | | '--------------' | | '--------------' | | '--------------' | 
 '----------------'   '----------------'   '----------------'   '----------------'   '----------------'  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bloody.json" alt="Bloody" target="_blank">Bloody</a></b>
<pre>
 ▄▄▄██▀▀▀  ██▓  ███▄ ▄███▓  █    ██  ▄▄▄█████▓ 
   ▒██    ▓██▒ ▓██▒▀█▀ ██▒  ██  ▓██▒ ▓  ██▒ ▓▒ 
   ░██    ▒██▒ ▓██    ▓██░ ▓██  ▒██░ ▒ ▓██░ ▒░ 
▓██▄██▓   ░██░ ▒██    ▒██  ▓▓█  ░██░ ░ ▓██▓ ░  
 ▓███▒    ░██░ ▒██▒   ░██▒ ▒▒█████▓    ▒██▒ ░  
 ▒▓▒▒░    ░▓   ░ ▒░   ░  ░ ░▒▓▒ ▒ ▒    ▒ ░░    
 ▒ ░▒░     ▒ ░ ░  ░      ░ ░░▒░ ░ ░      ░     
 ░ ░ ░     ▒ ░ ░      ░     ░░░ ░ ░    ░       
 ░   ░     ░          ░       ░                
                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Boie.json" alt="Boie" target="_blank">Boie</a></b>
<pre>
          '|¯¯¯¯|`·.    |¯¯¯¯|`·.    '/¯¯¯¯/\\,//\¯¯¯¯\`·.'        |¯¯¯¯|`·|¯¯¯¯|`·.       /¯¯¯¯/|¯¯¯¯|\¯¯¯¯\`·.          
          '|·´`·.·´|::: |.·´`·.·|::: |·´`·.·´|::'\/:':|`·.·´`·|::: |.·´`·.·|::|`·.·´`·|::: ¯¯¯¯  |`·.·´`·|`·¯¯¯¯`·.       
|¯¯¯¯|  |·´`·.·´|:::    |.·´`·.·|::: |·´`·.·´|::: `·.|`·.·´`·|:::  |.·´`·.·|::|`·.·´`·|:::  ¨¨¨¨¨¨¨¨|`·.·´`·|:::¨¨¨¨¨¨¨¨¨ 
'\____\/____/`·.'       |____|:::    |____|:::    |____|:::        '\____\/____/`·.'                |____|:::             
  `·.::::::::::::'`·./' '`·.:::::`·. '`·.:::::`·.    '`·.:::::`·.   '`·.:::::::::::::`·./'          '`·.:::::`·.          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Boie2.json" alt="Boie2" target="_blank">Boie2</a></b>
<pre>
          '|¯¯¯¯|`·. |¯¯¯¯|`·. '/¯¯¯¯/\\,//\¯¯¯¯\`·.'     |¯¯¯¯|`·|¯¯¯¯|`·.    /¯¯¯¯/|¯¯¯¯|\¯¯¯¯\`·.       
          '|÷÷÷÷|::: |÷÷÷÷|::: |÷÷÷÷|::'\/:':|       |::: |       |::|÷÷÷÷|::: ¯¯¯¯  |÷÷÷÷|`·¯¯¯¯`·.       
|¯¯¯¯|  |÷÷÷÷|:::    |÷÷÷÷|::: |÷÷÷÷|::: `·.|÷÷÷÷|:::     |÷÷÷÷|::|÷÷÷÷|:::     ¨¨¨¨¨¨¨¨|÷÷÷÷|:::¨¨¨¨¨¨¨¨¨ 
'\____\/____/`·.'    |____|::: |____|:::    |____|:::     '\____\/____/`·.'             |____|:::          
         '`·.:::::`·.       
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bolger.json" alt="Bolger" target="_blank">Bolger</a></b>
<pre>
    888  ,e,                             d8    
    888   "   888-~88e-~88e  888  888  _d88__  
    888  888  888  888  888  888  888   888    
    888  888  888  888  888  888  888   888    
|   88P  888  888  888  888  888  888   888    
 \__8"   888  888  888  888  "88_-888   "88_/  
                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bone's Font.json" alt="Bone's Font" target="_blank">Bone's Font</a></b>
<pre>
 |¯¯¯¯¯¯¯¯¯¯¯|'            |\¯¯¯\‚       '/¯¯¯¯|  |¯¯¯¯\‚              |\¯¯¯\  |\¯¯¯\ °          |¯¯¯¯¯¯¯¯¯¯|           
 |____       ___|'         | |     |'    |        '\/         |‚       | |     '|°| |     '|'    |___       ___|        
 |____|      |__¸|‘       °'\|     |'    |'\     '|\   /|     /'|'‚   °'/     '/  '/     /|‘     |     |      |     |   
 |¯¯¯'|'|      |           '°|     |'    | '|   °'| '\/ '|    '|°|'‚   |       \'/      | |'     |___|    °'|___|‘      
 |\__¸'\|__¸¸'|             '|\__¸'\'    ''/___'\  | /___'\/'          |\_____/|__¸\'                  |___'|‘          
 | |     ||     '|          '| |     |   '|       |'\|/|       |       | |       '| |     |            |      |'        
'°\|___||___|               °\|__¸'|     '|____|  °|____|             °'\|____'|/|___|‘                |__¸¸'|'         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Braced.json" alt="Braced" target="_blank">Braced</a></b>
<pre>
   .-.  .-.  .-.  .-.  .-. .-.  .-----.  
   | |  { |  }  \/  {  | } { |  `-' '-'  
{`-' }  | }  | {  } |  \ `-' /    } {    
 `---'  `-'  `-'  `-'   `---'     `-'    
                                         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bright.json" alt="Bright" target="_blank">Bright</a></b>
<pre>
.######. .######. .##...##. .##..##. .######. 
.....##. ...##... .###.###. .##..##. ...##... 
.....##. ...##... .##.#.##. .##..##. ...##... 
.##..##. ...##... .##...##. .##..##. ...##... 
..####.. .######. .##...##. ..####.. ...##... 
........ ........ ......... ........ ........ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Broadway.json" alt="Broadway" target="_blank">Broadway</a></b>
<pre>
                                      .         .                                                
           8 8888   8 8888           ,8.       ,8.           8 8888      88  8888888 8888888888  
           8 8888   8 8888          ,888.     ,888.          8 8888      88        8 8888        
           8 8888   8 8888         .`8888.   .`8888.         8 8888      88        8 8888        
           8 8888   8 8888        ,8.`8888. ,8.`8888.        8 8888      88        8 8888        
           8 8888   8 8888       ,8'8.`8888,8^8.`8888.       8 8888      88        8 8888        
           8 8888   8 8888      ,8' `8.`8888' `8.`8888.      8 8888      88        8 8888        
88.        8 8888   8 8888     ,8'   `8.`88'   `8.`8888.     8 8888      88        8 8888        
`88.       8 888'   8 8888    ,8'     `8.`'     `8.`8888.    ` 8888     ,8P        8 8888        
  `88o.    8 88'    8 8888   ,8'       `8        `8.`8888.     8888   ,d8P         8 8888        
    `Y888888 '      8 8888  ,8'         `         `8.`8888.     `Y88888P'          8 8888        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Broadway KB.json" alt="Broadway KB" target="_blank">Broadway KB</a></b>
<pre>
   _    _    _       _     _____  
  | |  | |  | |\/|  | | |   | |   
\_|_|  |_|  |_|  |  \_\_/   |_|   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bubble.json" alt="Bubble" target="_blank">Bubble</a></b>
<pre>
   _      _      _      _      _   
  / \    / \    / \    / \    / \  
 ( J )  ( i )  ( m )  ( u )  ( t ) 
  \_/    \_/    \_/    \_/    \_/  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Bulbhead.json" alt="Bulbhead" target="_blank">Bulbhead</a></b>
<pre>
  ____   ____   __  __   __  __   ____  
 (_  _) (_  _) (  \/  ) (  )(  ) (_  _) 
.-_)(    _)(_   )    (   )(__)(    )(   
\____)  (____) (_/\/\_) (______)  (__)  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/CaMiZ.json" alt="CaMiZ" target="_blank">CaMiZ</a></b>
<pre>
|¯¯¯¯¯¯¯¯¯¯¯|        |¯¯¯¯¯¯¯¯¯|'     |¯¯¯¯\/¯¯¯¯|        |¯¯¯¯| |'¯¯¯’|      |¯¯¯¯¯¯¯¯¯¯¯|          
 `·––-\     \—·´     |__/|     |\__|‚ |                |  |       | |      '| `·––\       '/—·´'     
|¯¯¯| |      |     ' |¯¯\|     |/¯¯|‚ |     '|\_/|'    ’| |       U      ’|         |       |'’      
'\___\|___/          |_________|'     |___|    |___|       \________'/              |____|'’         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Caligraphy.json" alt="Caligraphy" target="_blank">Caligraphy</a></b>
<pre>
                                                                          
        ***** **                                                          
     ******  **** *    *                                           *      
    **   *  * ****    ***                                         **      
   *    *  *   **      *                                          **      
       *  *                                     **   ****       ********  
      ** **          ***      *** **** ****      **    ***  *  ********   
      ** **           ***      *** **** ***  *   **     ****      **      
    **** **            **       **  **** ****    **      **       **      
   * *** **            **       **   **   **     **      **       **      
      ** **            **       **   **   **     **      **       **      
      ** **            **       **   **   **     **      **       **      
      ** **            **       **   **   **     **      **       **      
      ** **            **       **   **   **      ******* **      **      
      *  *             *** *    ***  ***  ***      *****   **      **     
  **     *              ***      ***  ***  ***                            
 ****   *                                                                 
 *  * **                                                                  
*    **                                                                   
     *                                                                    
                                                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Caligraphy2.json" alt="Caligraphy2" target="_blank">Caligraphy2</a></b>
<pre>
                                                                          
        ##### ##                                                          
     ######  /### /    #                                                  
    /#   /  / ###/    ###                                          #      
   /    /  /   ##      #                                          ##      
       /  /                                                       ##      
      ## ##          ###      ### /### /###     ##   ####       ########  
      ## ##           ###      ##/ ###/ /##  /   ##    ###  /  ########   
    /### ##            ##       ##  ###/ ###/    ##     ###/      ##      
   / ### ##            ##       ##   ##   ##     ##      ##       ##      
      ## ##            ##       ##   ##   ##     ##      ##       ##      
      ## ##            ##       ##   ##   ##     ##      ##       ##      
      ## ##            ##       ##   ##   ##     ##      ##       ##      
      ## ##            ##       ##   ##   ##     ##      /#       ##      
      #  #             ### /    ###  ###  ###     ######/ ##      ##      
  ##     /              ##/      ###  ###  ###     #####   ##      ##     
 ####   /                                                                 
 /  # #/                                                                  
/    ##                                                                   
     #                                                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Calvin S.json" alt="Calvin S" target="_blank">Calvin S</a></b>
<pre>
 ╦ ┬ ┌┬┐ ┬ ┬ ┌┬┐ 
 ║ │ │││ │ │  │  
╚╝ ┴ ┴ ┴ └─┘  ┴  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cards.json" alt="Cards" target="_blank">Cards</a></b>
<pre>
.------. .------. .------. .------. .------. 
|J.--. | |I.--. | |M.--. | |U.--. | |T.--. | 
| :(): | | (\/) | | (\/) | | (\/) | | :/\: | 
| ()() | | :\/: | | :\/: | | :\/: | | (__) | 
| '--'J| | '--'I| | '--'M| | '--'U| | '--'T| 
`------' `------' `------' `------' `------' 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Catwalk.json" alt="Catwalk" target="_blank">Catwalk</a></b>
<pre>
     _//                              _//   
     _//  _/                          _//   
     _//     _/// _// _//  _//  _// _/_/ _/ 
     _// _//  _//  _/  _// _//  _//   _//   
     _// _//  _//  _/  _// _//  _//   _//   
_/   _// _//  _//  _/  _// _//  _//   _//   
 _////   _// _///  _/  _//   _//_//    _//  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/CeA.json" alt="CeA" target="_blank">CeA</a></b>
<pre>
      l¯¯l  )¯¯) l¯¯l\_\/_/l¯¯l /¯¯/ /¯¯/ l¯¯l\¯¯ /l¯¯l  
(¯¯(/__/   (__(  ¯¯  l__l ¯¯ '  
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/CeA2.json" alt="CeA2" target="_blank">CeA2</a></b>
<pre>
      'l¯¯l     (¯¯(      /¯¯/\_/\¯¯\°   /¯¯/ /¯¯/'   l¯¯¯¯¯l   
 \¯¯\l__l        )__)     \__\    /__/   \__\/__'\     ¯l__l¯‘  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cheese.json" alt="Cheese" target="_blank">Cheese</a></b>
<pre>
          |˜¨¯¨˜ |     |˜¨¯¨˜'|'‚    '|'˜¨¯¨'˜¯\/'˜¨¯¨'˜˜¨¯'\‚      |˜¨¯¨˜'| |˜¨¯¨˜'|    /˜¨¯¨˜˜¨¯¨˜˜¨¯¨˜˜¨¯¨˜\       
          |       |‘   |      '|     /             '/|\       \'‚   |      | |      '|   \¸_¸_¸_      _¸_¸_¸/'        
          |       |‘   |      '|    '|      '|\    '/ / |       |   |      | |      '|     '¯\(¯/     '/ ¯)/¯         
 |˜¨¯¨˜'| |       l    |      '|   '/      '/\ \_/ / /       /|     |      | |      '|          |     '|              
 |      '| |       |‚  |      '|  '|       |  \|_|/ /       / '|    |      | |      '|        '/     '/|'‚            
 |\¸_¸_¸\|¸_¸_¸|       |¸_¸_¸|    |\¸_¸_¸\       |¸_¸_¸'|  /‘       |\¸_¸_\|¸_¸¸_|'‚         /¸_¸_/ '|'‚              
 | |˜¨¯¨˜'||˜¨¯¨˜'|    |˜¨¯¨˜'|°  | |˜¨¯¨˜'|      '|˜¨¯¨˜˜'| /‘     | |˜¨¯¨'||˜¨¯¨˜'|'‚     |˜¨¯¨˜'| /        °       
 '\|¸_¸_¸||¸_¸_¸|‘     |¸_¸_¸|     \|¸_¸_¸|      '|¸_¸_¸'|/'        '\|¸_¸_||¸_¸_'|'        '|¸_¸_'|/                 
   '¯\(¯   ¯)/¯‘        ¯\(¯'        ¯\(¯         '¯)/¯'  '           '¯\(¯ '¯)/¯'           '¯\(¯                    
             '‚                         '                                      '                                      
      °                                              '             '                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Chiseled.json" alt="Chiseled" target="_blank">Chiseled</a></b>
<pre>
      ,--.-,     .=-.-.           ___                    ,--.--------.   
     |==' -|    /==/_ /    .-._ .'=.'\    .--.-. .-.-.  /==/,  -   , -\  
     |==|- |   |==|, |    /==/ \|==|  |  /==/ -|/=/  |  \==\.-.  - ,-./  
   __|==|, |   |==|  |    |==|,|  / - |  |==| ,||=| -|   `--`\==\- \     
,--.-'\=|- |   |==|- |    |==|  \/  , |  |==|- | =/  |        \==\_ \    
|==|- |=/ ,|   |==| ,|    |==|- ,   _ |  |==|,  \/ - |        |==|- |    
|==|. /=| -|   |==|- |    |==| _ /\   |  |==|-   ,   /        |==|, |    
\==\, `-' /    /==/. /    /==/  / / , /  /==/ , _  .'         /==/ -/    
 `--`----'     `--`-`     `--`./  `--`   `--`..---'           `--`--`    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Chunky.json" alt="Chunky" target="_blank">Chunky</a></b>
<pre>
   _____   __                      __    
 _|     | |__| .--------. .--.--. |  |_  
|       | |  | |        | |  |  | |   _| 
|_______| |__| |__|__|__| |_____| |____| 
                                         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Coinstak.json" alt="Coinstak" target="_blank">Coinstak</a></b>
<pre>
     O))                              O))   
     O))  O)                          O))   
     O))     O))) O)) O))  O))  O)) O)O) O) 
     O)) O))  O))  O)  O)) O))  O))   O))   
     O)) O))  O))  O)  O)) O))  O))   O))   
O)   O)) O))  O))  O)  O)) O))  O))   O))   
 O))))   O)) O)))  O)  O))   O))O))    O))  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cola.json" alt="Cola" target="_blank">Cola</a></b>
<pre>
         .;;;                                              .    
          .;'      .-.                                 ...;...  
         .;'       `-'    . ,';.,';.        ,  :        .'      
.-.     .;'       ;'      ;;  ;;  ;;       ;   ;      .;        
`.     .;      _.;:._.   ';  ;;  ';      .'`..:;._  .;          
  `;;;;;;'              _;        `-'                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Colossal.json" alt="Colossal" target="_blank">Colossal</a></b>
<pre>
  888888  d8b                           888     
    "88b  Y8P                           888     
     888                                888     
     888  888  88888b.d88b.   888  888  888888  
     888  888  888 "888 "88b  888  888  888     
     888  888  888  888  888  888  888  888     
     88P  888  888  888  888  Y88b 888  Y88b.   
     888  888  888  888  888   "Y88888   "Y888  
   .d88P                                        
 .d88P"                                         
888P"                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Computer.json" alt="Computer" target="_blank">Computer</a></b>
<pre>
    8                              
    8   e   eeeeeee  e   e  eeeee  
    8e  8   8  8  8  8   8    8    
    88  8e  8e 8  8  8e  8    8e   
e   88  88  88 8  8  88  8    88   
8eee88  88  88 8  8  88ee8    88   
                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Contessa.json" alt="Contessa" target="_blank">Contessa</a></b>
<pre>
   .              ,  
   | * ._ _  . . -+- 
\__| | [ | ) (_|  |  
                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Contrast.json" alt="Contrast" target="_blank">Contrast</a></b>
<pre>
.%%%%%%. .%%%%%%. .%%...%%. .%%..%%. .%%%%%%. 
.....%%. ...%%... .%%%.%%%. .%%..%%. ...%%... 
.....%%. ...%%... .%%.%.%%. .%%..%%. ...%%... 
.%%..%%. ...%%... .%%...%%. .%%..%%. ...%%... 
..%%%%.. .%%%%%%. .%%...%%. ..%%%%.. ...%%... 
........ ........ ......... ........ ........ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cosmike.json" alt="Cosmike" target="_blank">Cosmike</a></b>
<pre>
    ....:::::: ::: .        :     ...    ::: :::::::::::: 
 ;;;;;;;;;```` ;;; ;;,.    ;;;    ;;     ;;; ;;;;;;;;'''' 
 ''`  `[[.     [[[ [[[[, ,[[[[,  [['     [[[      [[      
,,,    `$$     $$$ $$$$$$$$"$$$  $$      $$$      $$      
888boood88     888 888 Y88" 888o 88    .d888      88,     
"MMMMMMMM"     MMM MMM  M'  "MMM  "YmmMMMM""      MMM     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Crawford.json" alt="Crawford" target="_blank">Crawford</a></b>
<pre>
  ____   ____   ___ ___   __ __   ______  
 |    | l    j |   T   T |  T  T |      T 
 l__  |  |  T  | _   _ | |  |  | |      | 
 __j  |  |  |  |  \_/  | |  |  | l_j  l_j 
/  |  |  |  |  |   |   | |  :  |   |  |   
\  `  |  j  l  |   |   | l     |   |  |   
 \____j |____j l___j___j  \__,_j   l__j   
                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Crawford2.json" alt="Crawford2" target="_blank">Crawford2</a></b>
<pre>
  ____   ____   ___ ___   __ __   ______  
 |    | |    | |   |   | |  |  | |      | 
 |__  |  |  |  | _   _ | |  |  | |      | 
 __|  |  |  |  |  \_/  | |  |  | |_|  |_| 
/  |  |  |  |  |   |   | |  :  |   |  |   
\  `  |  |  |  |   |   | |     |   |  |   
 \____j |____| |___|___|  \__,_|   |__|   
                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Crazy.json" alt="Crazy" target="_blank">Crazy</a></b>
<pre>
    .---.                                                  
    |   |                                                  
    '---'  .--.   __  __   ___                             
    .---.  |__|  |  |/  `.'   `.                           
    |   |  .--.  |   .-.  .-.   '                    .|    
    |   |  |  |  |  |  |  |  |  |                  .' |_   
    |   |  |  |  |  |  |  |  |  |     _    _     .'     |  
    |   |  |  |  |  |  |  |  |  |    | '  / |   '--.  .-'  
    |   |  |  |  |  |  |  |  |  |   .' | .' |      |  |    
    |   |  |__|  |__|  |__|  |__|   /  | /  |      |  |    
 __.'   '                          |   `'.  |      |  '.'  
|      '                           '   .'|  '/     |   /   
|____.'                             `-'  `--'      `'-'    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cricket.json" alt="Cricket" target="_blank">Cricket</a></b>
<pre>
  _______    __                         __    
 |   _   |  |__|  .--------.  .--.--.  |  |_  
 |___|   |  |  |  |        |  |  |  |  |   _| 
 |.  |   |  |__|  |__|__|__|  |_____|  |____| 
 |:  1   |                                    
 |::.. . |                                    
 `-------'                                    
                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cursive.json" alt="Cursive" target="_blank">Cursive</a></b>
<pre>
  ___                        
 (   >                   _/_ 
  __/_  o  ______   . .  /   
 / /   <_ / / / <_ (_/_ <__  
<_/                          
                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cyberlarge.json" alt="Cyberlarge" target="_blank">Cyberlarge</a></b>
<pre>
 _____  _____  _______  _     _  _______ 
   |      |    |  |  |  |     |     |    
 __|    __|__  |  |  |  |_____|     |    
                                         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cybermedium.json" alt="Cybermedium" target="_blank">Cybermedium</a></b>
<pre>
 _  _  _  _  _  _  ___  
 |  |  |\/|  |  |   |   
_|  |  |  |  |__|   |   
                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cybersmall.json" alt="Cybersmall" target="_blank">Cybersmall</a></b>
<pre>
    _  _  _  _  _  _  ___ 
 ___|  |  |\/|  |__|   |  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Cygnet.json" alt="Cygnet" target="_blank">Cygnet</a></b>
<pre>
                    
.-. .            .  
  ; . .-.-. . . -|- 
`'  ' ' ' ' '-'  '- 
                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/DANC4.json" alt="DANC4" target="_blank">DANC4</a></b>
<pre>
  \O     \O/  \O/    \O    '\   /` 
  _|# .___Y    Y      |_     \ /   
_| |      |   / \    /  |     X    
   |_     |_ _| |_ ./   |_   /O\   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/DWhistled.json" alt="DWhistled" target="_blank">DWhistled</a></b>
<pre>
J i m u t 
          
          
          
          
          
          
          
J i m u t 
          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/DaiR.json" alt="DaiR" target="_blank">DaiR</a></b>
<pre>
               ¸.·´¯¯¯¯)         .·´¯¯¯.·´|       .·´¯¯¯`·. ¸.-—.¸             .·´¯¯/|_ '                     _.·-·.¸_'      /( '   
              /       /|\( ‘'  (        (   |°   /    /`·.   `·.       \'   .·´     /|\   `·.‚'   ' ¸.-~·*¨¯        ¯`·-·´    )‘    
     )`·.     |       | '\|‘ ' |`·.¸     `·.'|  |\    \   `·.__.·')    )‚  /       / | ')     `·.‚' |`·.(¯¯¯¯`·.   (`·.__.·´|'      
 ¸.·´    )    '\       \'      `·.¸ )       )   |  \   |`·.¸__ .·´ ¸.·´|‘  |       '·-'·´        |   `·.|¯¯¯¯¯')   '\·.__.·´'       
(       (____)       )'  '       .·´___.·´|     `·.  \(       (   ( ¸.·´'  |                    |                /      \     '     
|`·——————·´'|'                   |       |   |‘     `·.|       ).·´|       |`·.________.·'|'                    |'·._.·´¨|   °    ' 
 `·.¸_________¸.·´‘'             |____|.·´'                    |.·´ '  °   `·.¸_______¸.·´°                     '·._.·´¯'           
                                                               '              '                                    '                
                                                '                                                '                             '    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Dancing Font.json" alt="Dancing Font" target="_blank">Dancing Font</a></b>
<pre>
     _                        __  __       _   _     _____    
  U |"| u         ___       U|' \/ '|u  U |"|u| |   |_ " _|   
 _ \| |/         |_"_|      \| |\/| |/   \| |\| |     | |     
| |_| |_,-.       | |        | |  | |     | |_| |    /| |\    
 \___/-(_/      U/| |\u      |_|  |_|    <<\___/    u |_|U    
  _//        .-,_|___|_,-.  <<,-,,-.    (__) )(     _// \\_   
 (__)         \_)-' '-(_/    (./  \.)       (__)   (__) (__)  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Decimal.json" alt="Decimal" target="_blank">Decimal</a></b>
<pre>
74 105 109 117 116 
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Def Leppard.json" alt="Def Leppard" target="_blank">Def Leppard</a></b>
<pre>
                                                               
                                                               
                                           :                   
  itttttttt   t                            Ef                  
  fDDK##DDi   Ej              ..       :   E#t       GEEEEEEEL 
     t#E      E#,            ,W,     .Et   E#t       ,;;L#K;;. 
     t#E      E#t           t##,    ,W#t   E#t          t#E    
     t#E      E#t          L###,   j###t   E#t fi       t#E    
     t#E      E#t        .E#j##,  G#fE#t   E#t L#j      t#E    
     t#E      E#t       ;WW; ##,:K#i E#t   E#t L#L      t#E    
   jfL#E      E#t      j#E.  ##f#W,  E#t   E#tf#E:      t#E    
   :K##E      E#t    .D#L    ###K:   E#t   E###f        t#E    
     G#E      E#t   :K#t     ##D.    E#t   E#K,         t#E    
      tE      E#t   ...      #G      ..    EL            fE    
       .      ,;.            j             :              :    
                                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Delta Corps Priest 1.json" alt="Delta Corps Priest 1" target="_blank">Delta Corps Priest 1</a></b>
<pre>
     ▄█   ▄█      ▄▄▄▄███▄▄▄▄    ███    █▄       ███      
    ███  ███    ▄██▀▀▀███▀▀▀██▄  ███    ███  ▀█████████▄  
    ███  ███▌   ███   ███   ███  ███    ███     ▀███▀▀██  
    ███  ███▌   ███   ███   ███  ███    ███      ███   ▀  
    ███  ███▌   ███   ███   ███  ███    ███      ███      
    ███  ███    ███   ███   ███  ███    ███      ███      
    ███  ███    ███   ███   ███  ███    ███      ███      
█▄ ▄███  █▀      ▀█   ███   █▀   ████████▀      ▄████▀    
▀▀▀▀▀▀                                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Diamond.json" alt="Diamond" target="_blank">Diamond</a></b>
<pre>
     /\\                              /\\   
     /\\  /\                          /\\   
     /\\     /\\\ /\\ /\\  /\\  /\\ /\/\ /\ 
     /\\ /\\  /\\  /\  /\\ /\\  /\\   /\\   
     /\\ /\\  /\\  /\  /\\ /\\  /\\   /\\   
/\   /\\ /\\  /\\  /\  /\\ /\\  /\\   /\\   
 /\\\\   /\\ /\\\  /\  /\\   /\\/\\    /\\  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Diet Cola.json" alt="Diet Cola" target="_blank">Diet Cola</a></b>
<pre>
      .----.                                                  
        /            .-.                                 /    
       /             `-'   .  .-. .-.       )  (     ---/---  
..-.   /            /       )/   )   )     (    )      /      
`.   /           _.(__.    '/   /   (       `--':     /       
  `-'                                `-'                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Digital.json" alt="Digital" target="_blank">Digital</a></b>
<pre>
 +-+  +-+  +-+  +-+  +-+ 
 |J|  |i|  |m|  |u|  |t| 
 +-+  +-+  +-+  +-+  +-+ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Doh.json" alt="Doh" target="_blank">Doh</a></b>
<pre>
                                                                                                   
                                                                                                   
          JJJJJJJJJJJ   iiii                                                        tttt           
          J:::::::::J  i::::i                                                    ttt:::t           
          J:::::::::J   iiii                                                     t:::::t           
          JJ:::::::JJ                                                            t:::::t           
            J:::::J   iiiiiii     mmmmmmm    mmmmmmm    uuuuuu    uuuuuu   ttttttt:::::ttttttt     
            J:::::J   i:::::i   mm:::::::m  m:::::::mm  u::::u    u::::u   t:::::::::::::::::t     
            J:::::J    i::::i  m::::::::::mm::::::::::m u::::u    u::::u   t:::::::::::::::::t     
            J:::::j    i::::i  m::::::::::::::::::::::m u::::u    u::::u   tttttt:::::::tttttt     
            J:::::J    i::::i  m:::::mmm::::::mmm:::::m u::::u    u::::u         t:::::t           
JJJJJJJ     J:::::J    i::::i  m::::m   m::::m   m::::m u::::u    u::::u         t:::::t           
J:::::J     J:::::J    i::::i  m::::m   m::::m   m::::m u::::u    u::::u         t:::::t           
J::::::J   J::::::J    i::::i  m::::m   m::::m   m::::m u:::::uuuu:::::u         t:::::t    tttttt 
J:::::::JJJ:::::::J   i::::::i m::::m   m::::m   m::::m u:::::::::::::::uu       t::::::tttt:::::t 
 JJ:::::::::::::JJ    i::::::i m::::m   m::::m   m::::m  u:::::::::::::::u       tt::::::::::::::t 
   JJ:::::::::JJ      i::::::i m::::m   m::::m   m::::m   uu::::::::uu:::u         tt:::::::::::tt 
     JJJJJJJJJ        iiiiiiii mmmmmm   mmmmmm   mmmmmm     uuuuuuuu  uuuu           ttttttttttt   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   
                                                                                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Doom.json" alt="Doom" target="_blank">Doom</a></b>
<pre>
   ___   _                       _    
  |_  | (_)                     | |   
    | |  _   _ __ ___    _   _  | |_  
    | | | | | '_ ` _ \  | | | | | __| 
/\__/ / | | | | | | | | | |_| | | |_  
\____/  |_| |_| |_| |_|  \__,_|  \__| 
                                      
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Dot Matrix.json" alt="Dot Matrix" target="_blank">Dot Matrix</a></b>
<pre>
          _  _  _               _                                                               _             
         (_)(_)(_)             (_)                                                             (_)            
            (_)              _  _                _  _   _  _          _         _            _ (_) _  _       
            (_)             (_)(_)              (_)(_)_(_)(_)        (_)       (_)          (_)(_)(_)(_)      
            (_)                (_)             (_)   (_)   (_)       (_)       (_)             (_)            
     _      (_)                (_)             (_)   (_)   (_)       (_)       (_)             (_)     _      
    (_)  _  (_)              _ (_) _           (_)   (_)   (_)       (_)_  _  _(_)_            (_)_  _(_)     
     (_)(_)(_)              (_)(_)(_)          (_)   (_)   (_)         (_)(_)(_) (_)             (_)(_)       
                                                                                                              
                                                                                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Double.json" alt="Double" target="_blank">Double</a></b>
<pre>
    __  __  ___  ___  __ __  ______ 
    ||  ||  ||\\//||  || ||  | || | 
    ||  ||  || \/ ||  || ||    ||   
 |__||  ||  ||    ||  \\_//    ||   
                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Double Shorts.json" alt="Double Shorts" target="_blank">Double Shorts</a></b>
<pre>
   __  __  ___  __  __ __  _____  
   ||  ||  || \/ |  || ||   ||    
|__||  ||  ||    |  \\_//   ||    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Dr Pepper.json" alt="Dr Pepper" target="_blank">Dr Pepper</a></b>
<pre>
  _   _                   _    
 | | <_> ._ _ _   _ _   _| |_  
_| | | | | ' ' | | | |   | |   
\__/ |_| |_|_|_| `___|   |_|   
                               

</pre>
'J'
'i'
'm'
'u'
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Chess.json" alt="Efti Chess" target="_blank">Efti Chess</a></b>
<pre>
######### 
##[`'`']# 
###|::|## 
###|::|## 
######### 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Font.json" alt="Efti Font" target="_blank">Efti Font</a></b>
<pre>
   _                    
  | | ()   _ _      ||  
n_| | || |/ \ \ |U| | ] 
\__/  L| L_n_n| \_/ L|  
                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Italic.json" alt="Efti Italic" target="_blank">Efti Italic</a></b>
<pre>
    __                        
   / /   ()   _            /7 
n_/ /   /7   / \'\  /7/7  /_7 
\_,'   //   /_nn_/ /__/  //   
                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Piti.json" alt="Efti Piti" target="_blank">Efti Piti</a></b>
<pre>
 ()         
 || i m u t 
[_|         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Robot.json" alt="Efti Robot" target="_blank">Efti Robot</a></b>
<pre>
    _   _                  _   
   ( ) (_)                ( )  
 _ | |  _   __  __   _ _  | |  
((_( ) ( ) ( _`'_ ) ( U ) ( _) 
 \__/  /_\ /_\`'/_\ /___\ /_\  
                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Wall.json" alt="Efti Wall" target="_blank">Efti Wall</a></b>
<pre>
                  .      .          ___            o                       
    -`^'-       .  .:::.           /_\ `*       ` /_\ '         ()_()      
    (o o)         :(o o):  .      (o o)        - (o o) -        (o o)      
ooO--(_)--Ooo- ooO--(_)--Ooo- ooO--(_)--Ooo- ooO--(_)--Ooo- ooO--`o'--Ooo- 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Efti Water.json" alt="Efti Water" target="_blank">Efti Water</a></b>
<pre>
  _   o                _  
  ))  _   _  _   _     )L 
 ((  ((  ((`1(  ((_(  ((  
._))                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Electronic.json" alt="Electronic" target="_blank">Electronic</a></b>
<pre>
 ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄   ▄▄       ▄▄   ▄         ▄   ▄▄▄▄▄▄▄▄▄▄▄  
▐░░░░░░░░░░░▌ ▐░░░░░░░░░░░▌ ▐░░▌     ▐░░▌ ▐░▌       ▐░▌ ▐░░░░░░░░░░░▌ 
 ▀▀▀▀▀█░█▀▀▀   ▀▀▀▀█░█▀▀▀▀  ▐░▌░▌   ▐░▐░▌ ▐░▌       ▐░▌  ▀▀▀▀█░█▀▀▀▀  
      ▐░▌          ▐░▌      ▐░▌▐░▌ ▐░▌▐░▌ ▐░▌       ▐░▌      ▐░▌      
      ▐░▌          ▐░▌      ▐░▌ ▐░▐░▌ ▐░▌ ▐░▌       ▐░▌      ▐░▌      
      ▐░▌          ▐░▌      ▐░▌  ▐░▌  ▐░▌ ▐░▌       ▐░▌      ▐░▌      
      ▐░▌          ▐░▌      ▐░▌   ▀   ▐░▌ ▐░▌       ▐░▌      ▐░▌      
      ▐░▌          ▐░▌      ▐░▌       ▐░▌ ▐░▌       ▐░▌      ▐░▌      
 ▄▄▄▄▄█░▌      ▄▄▄▄█░█▄▄▄▄  ▐░▌       ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌      ▐░▌      
▐░░░░░░░▌     ▐░░░░░░░░░░░▌ ▐░▌       ▐░▌ ▐░░░░░░░░░░░▌      ▐░▌      
 ▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀   ▀         ▀   ▀▀▀▀▀▀▀▀▀▀▀        ▀       
                                                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Elite.json" alt="Elite" target="_blank">Elite</a></b>
<pre>
 ▐▄▄▄ ▪   • ▌ ▄ ·.  ▄• ▄▌ ▄▄▄▄▄ 
  ·██ ██  ·██ ▐███▪ █▪██▌ •██   
▪▄ ██ ▐█· ▐█ ▌▐▌▐█· █▌▐█▌  ▐█.▪ 
▐▌▐█▌ ▐█▌ ██ ██▌▐█▌ ▐█▄█▌  ▐█▌· 
 ▀▀▀• ▀▀▀ ▀▀  █▪▀▀▀  ▀▀▀   ▀▀▀  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Epic.json" alt="Epic" target="_blank">Epic</a></b>
<pre>
_________ _________  _______            _________ 
\__    _/ \__   __/ (       ) |\     /| \__   __/ 
   )  (      ) (    | () () | | )   ( |    ) (    
   |  |      | |    | || || | | |   | |    | |    
   |  |      | |    | |(_)| | | |   | |    | |    
   |  |      | |    | |   | | | |   | |    | |    
|\_)  )   ___) (___ | )   ( | | (___) |    | |    
(____/    \_______/ |/     \| (_______)    )_(    
                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fender.json" alt="Fender" target="_blank">Fender</a></b>
<pre>
|''||''|                                ||     
   ||      ''                           ||     
   ||      ||   '||),,(|,   '||  ||`  ''||''   
   ||      ||    || || ||    ||  ||     ||     
'..|'     .||.  .||    ||.   `|..'|.    `|..'  
                                               
                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Filter.json" alt="Filter" target="_blank">Filter</a></b>
<pre>
     d8p     8888  d88b_o8b  888  888  888888888  
     88p     8888  d88 8'8b  888  888     '88d    
     88P     8888  d88   8b  888  888    '888     
  88888'     8888  Y88   8P  888PP888  '88p       
                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Filth.json" alt="Filth" target="_blank">Filth</a></b>
<pre>
          '\·. _ .·/'  .· ´ ¯ ` ·.    \· . _ . ·· . _ . ·/       \·. _ .·/                \· . ______ . ·/'        
            \      |   `· . _ . ·´     '\                '/'      |'     /   \·._ .·/‘    /· ´ ¯`.    .´¯· .\ '    
 \· ._.·/'   |     |   \· . _ . ·/    '  |     |·.·|'     |'      |     |     |'    /             |'   |           
  '\     `·-·´     /°   |        '|‘    '|     '\ '/      |'      '\     `·-·´    /‘   '         /     \           
    `· . __ . ·´ °     /· ´ ¯ ` ·\    ' /·´ ¯ `·\´ ¯ ` ·\  '        `· . __ . ·´‘   '     '     /·´ ¯ `·\   ‘      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fire Font-k.json" alt="Fire Font-k" target="_blank">Fire Font-k</a></b>
<pre>
                                        
                                    )   
   (     (        )        (     ( /(   
   )\    )\      (        ))\    )\())  
  ((_)  ((_)     )\  '   /((_)  (_))/   
 _ | |   (_)   _((_))   (_))(   | |_    
| || |   | |  | '  \()  | || |  |  _|   
 \__/    |_|  |_|_|_|    \_,_|   \__|   
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fire Font-s.json" alt="Fire Font-s" target="_blank">Fire Font-s</a></b>
<pre>
                                        
                                    )   
   (     (        )        (     ( /(   
   )\    )\      (        ))\    )\())  
  ((_)  ((_)     )\  '   /((_)  (_))/   
 _ | |   (_)   _((_))   (_))(   | |_    
| || |   | |  | '  \()  | || |  |  _|   
 \__/    |_|  |_|_|_|    \_,_|   \__|   
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Flipped.json" alt="Flipped" target="_blank">Flipped</a></b>
<pre>
  _            ____   ____      _  
 / |    ____  |_   | |   _|  __| | 
| |__  |____|  _< <  |  |_  |__  | 
 \___|        |____| |____|    |_| 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Flower Power.json" alt="Flower Power" target="_blank">Flower Power</a></b>
<pre>
     .-./`)    .-./`)   ,---.    ,---.    ___    _   ,---------.   
     \ '_ .')  \ .-.')  |    \  /    |  .'   |  | |  \          \  
    (_ (_) _)  / `-' \  |  ,  \/  ,  |  |   .'  | |   `--.  ,---'  
      / .  \    `-'`"`  |  |\_   /|  |  .'  '_  | |      |   \     
 ___  |-'`|     .---.   |  _( )_/ |  |  '   ( \.-.|      :_ _:     
|   | |   '     |   |   | (_ o _) |  |  ' (`. _` /|      (_I_)     
|   `-'  /      |   |   |  (_,_)  |  |  | (_ (_) _)     (_(=)_)    
 \      /       |   |   |  |      |  |   \ /  . \ /      (_I_)     
  `-..-'        '---'   '--'      '--'    ``-'`-''       '---'     
                                                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/FoGG.json" alt="FoGG" target="_blank">FoGG</a></b>
<pre>
            /¯¯¯¯¯/|           |\¯¯¯¯¯¯\            |\¯¯¯¯¯¯¯\                            |\¯¯¯¯¯¯\  |\¯¯¯¯¯¯\'                  /¯¯¯¯¯¯¯¯¯¯¯¯¯¯\                  
           |         |;| °     |;|          |       |;|           |\'\/¯¯¯¯¯¯/|           |;|           | |;|          |'       |                           |      
           |         |;|'‚     |;|          |       |/           /|;;\/|        |;|°      |/           /|'|/          /|'       |\_____        _____/|'            
|¯¯¯¯¯| \         \|'          |/          /|‘     /           /  |;;|;|\        \|      /           /;;/          /;;|°        |;||¯¯¯¯||      ||¯¯¯¯||;|         
|\        \/          /|      /          /;;|'    |            |    \|/  |        |°   /           /;;/          /;;;/          |;||       ||\      \      '||;|   
|;;\____/\____./;|            |          |;'/°    |\______ \       /        /|         |           |;/          |; ;/‘           \||____||;;\      \__'||/         
|;;||¯¯¯||;||¯¯¯||;;'|        |\_____\/‘          |;||¯¯¯¯¯||      /_____/;|           |\          \|           |/‘                 ¯¯¯   \;;|      | ¯            
|;;||     ||;||     '||;/°    |;||¯¯¯¯||'         |;||         ||     ||¯¯¯¯ ||;'|     |;;\______\______\'‚                                  \/      /|‘           
 \'||___||;||___||/'          |;||       ||'       \||_____||     ||        ||';|      |;;||¯¯¯¯¯||'||¯¯¯¯¯||      °                        /___ /;;|'             
     ¯¯      ¯¯'               \||____||°             ¯¯¯¯        ||____ ||/           |;;||         ||'||         ||‘                      ||¯¯||;;;/             
        '                        ¯¯¯¯°                                  ¯¯¯ ‘           \'||_____'||'||_____||                              ||   '||;/             
                      '                °                                                   ¯¯¯¯       ¯¯¯¯                                  ||__||/                
                     '        '‚                                                                                                              ¯ ‘                  
'                                   '‚                                                                                                      '                      
               '                        '‚                                                                                     '                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Four Tops.json" alt="Four Tops" target="_blank">Four Tops</a></b>
<pre>
~~|~ '                  |  
  |  | |/~\ /~\  |   | ~|~ 
\_|  | |   |   |  \_/|  |  
                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fraktur.json" alt="Fraktur" target="_blank">Fraktur</a></b>
<pre>
      .               .                                               s     
  .x88888x.          @88>                                            :8     
 :8**888888X.  :>    %8P       ..    .     :        x.    .         .88     
 f    `888888x./      .      .888: x888  x888.    .@88k  z88u      :888ooo  
'       `*88888~    .@88u   ~`8888~'888X`?888f`  ~"8888 ^8888    -*8888888  
 \.    .  `?)X.    ''888E`    X888  888X '888>     8888  888R      8888     
  `~=-^   X88> ~     888E     X888  888X '888>     8888  888R      8888     
         X8888  ~    888E     X888  888X '888>     8888  888R      8888     
         488888      888E     X888  888X '888>     8888 ,888B .   .8888Lu=  
 .xx.     88888X     888&    "*88%""*88" '888!`   "8888Y 8888"    ^%888*    
'*8888.   '88888>    R888"     `~    "    `"`      `Y"   'YP        'Y"     
  88888    '8888>     ""                                                    
  `8888>    `888                                                            
   "8888     8%                                                             
    `"888x:-"                                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fun Face.json" alt="Fun Face" target="_blank">Fun Face</a></b>
<pre>
       _      wW  Ww   \\\    ///   wWw  wWw    (o)__(o)  
     _||\     (O)(O)   ((O)  (O))   (O)  (O)    (__  __)  
    (_'\       (..)     | \  / |    / )  ( \      (  )    
     (  |       ||      ||\\//||   / /    \ \      )(     
   (\_) |      _||_     || \/ ||   | \____/ |     (  )    
    `-`.)     (_/\_)    ||    ||   '. `--' .`      )/     
       (               (_/    \_)    `-..-'       (       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fun Faces.json" alt="Fun Faces" target="_blank">Fun Faces</a></b>
<pre>
       _      wW  Ww   \\\    ///   wWw  wWw    (o)__(o)  
     _||\     (O)(O)   ((O)  (O))   (O)  (O)    (__  __)  
    (_'\       (..)     | \  / |    / )  ( \      (  )    
     (  |       ||      ||\\//||   / /    \ \      )(     
      \ |      _||_     || \/ ||   | \____/ |     (  )    
   (\__)|     (_/\_)    ||    ||   '. `--' .`      )/     
    `--.)              (_/    \_)    `-..-'       (       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Fuzzy.json" alt="Fuzzy" target="_blank">Fuzzy</a></b>
<pre>
   .-.  _                    .-.  
   : : :_;                  .' `. 
 _ : : .-. ,-.,-.,-. .-..-. `. .' 
: :; : : : : ,. ,. : : :; :  : :  
`.__.' :_; :_;:_;:_; `.__.'  :_;  
                                  
                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Galactus.json" alt="Galactus" target="_blank">Galactus</a></b>
<pre>
        '|¯¯¯¯|       |¯¯¯¯|     |¯¯¯¯|\|¯¯¯¯|/|¯¯¯¯|            '|¯¯¯¯| '|¯¯¯¯|           |\¯¯.·´|¯¯¯¯|`·.¯¯/|          
        '|       |    |       |  |       | |       | |       |   '|       | '|       |     |:'\/::::|       |:::'\/::|   
        '|____|       |____|     |____|\|____|/|____|            '|____| '|____|           '\:'|':.·´|____|`·.:|::/'     
        '|¯¯¯¯|       |¯¯¯¯|     |¯¯¯¯|:|:::::::|:|¯¯¯¯|         '|¯¯¯¯| '|¯¯¯¯|             \|/   '|¯¯¯¯|   \|/'        
  '/\    |       |    |       |  |       |\|:::::::|/|       |   '|       | '|       |             |       |'            
 /__`·.|____|         |____|     |____|  ¯¯¯¯ '|____|            |\____\/____/|'                   |____|'               
'|:::::::|:::::::|'‚  |:::::::|  |:::::::|          '|:::::::|   |'|:::::::|:::::::'|'|‘           |:::::::|'            
'|:::::::|:::::::|°   |:::::::|  |:::::::|          '|:::::::|   \|:::::::|:::::::'|/'‚            |:::::::|'            
 ¯¯¯¯ ¯¯¯¯             ¯¯¯¯'      ¯¯¯¯            ¯¯¯¯'            ¯¯¯¯ ¯¯¯¯                        ¯¯¯¯                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Georgi16.json" alt="Georgi16" target="_blank">Georgi16</a></b>
<pre>
                                                    
                                                    
     ____                                           
     `MM' 68b                                       
      MM  Y89                                /      
      MM  ___  ___  __    __    ___   ___   /M      
      MM  `MM  `MM 6MMb  6MMb   `MM    MM  /MMMMM   
      MM   MM   MM69 `MM69 `Mb   MM    MM   MM      
      MM   MM   MM'   MM'   MM   MM    MM   MM      
      MM   MM   MM    MM    MM   MM    MM   MM      
(8)   MM   MM   MM    MM    MM   MM    MM   MM      
((   ,M9   MM   MM    MM    MM   YM.   MM   YM.  ,  
 YMMMM9   _MM_ _MM_  _MM_  _MM_   YMMM9MM_   YMMM9  
                                                    
                                                    
                                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Georgia11.json" alt="Georgia11" target="_blank">Georgia11</a></b>
<pre>
                                                          
            ,,                                            
   `7MMF'   db                                     mm     
     MM                                            MM     
     MM   `7MM   `7MMpMMMb.pMMMb.   `7MM  `7MM   mmMMmm   
     MM     MM     MM    MM    MM     MM    MM     MM     
     MM     MM     MM    MM    MM     MM    MM     MM     
(O)  MM     MM     MM    MM    MM     MM    MM     MM     
 Ymmm9    .JMML. .JMML  JMML  JMML.   `Mbod"YML.   `Mbmo  
                                                          
                                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ghost.json" alt="Ghost" target="_blank">Ghost</a></b>
<pre>
                       _   .-')                    .-') _     
                      ( '.( OO )_                 (  OO) )    
     ,--.    ,-.-')    ,--.   ,--.)  ,--. ,--.    /     '._   
 .-')| ,|    |  |OO)   |   `.'   |   |  | |  |    |'--...__)  
( OO |(_|    |  |  \   |         |   |  | | .-')  '--.  .--'  
| `-'|  |    |  |(_/   |  |'.'|  |   |  |_|( OO )    |  |     
,--. |  |   ,|  |_.'   |  |   |  |   |  | | `-' /    |  |     
|  '-'  /  (_|  |      |  |   |  |  ('  '-'(_.-'     |  |     
 `-----'     `--'      `--'   `--'    `-----'        `--'     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ghoulish.json" alt="Ghoulish" target="_blank">Ghoulish</a></b>
<pre>
  .-,.-.,-. .'(    )\   )\        .-.   .-,.-.,-.  
  ).-, ,-.( \  )  (  ',/ /    ,'  /  )  ) ,, ,. (  
      ))    ) (    )    (    (  ) | (   \( |(  )/  
 .-._((     \  )  (  \(\ \    ) '._\ )     ) \     
(      )     ) \   `.) /  )  (  ,   (      \ (     
 '._.\(       )/       '.(    )/ ._.'       )/     
                                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Glenyn.json" alt="Glenyn" target="_blank">Glenyn</a></b>
<pre>
____  ____  _     _     ____  
|_  \ |___\ |\/\  || \  |_ _\ 
,_/ / | /   |   \ ||_|\   ||  
\__/  |/    |/v\/ |___/   |/  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Glue.json" alt="Glue" target="_blank">Glue</a></b>
<pre>
 "   |¯|    |¯|   '/¯/|¯|\¯\ '    |¯| |¯|     '/¯/|¯|\¯\°   
 |¯| |! |   |¯|   |! | |_| |! |   |! | |! |   |_| |! | |_|‘ 
 |_|/_/'    |_|   |_|    "|_|     '\_\|_|     "   |_|       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Goofy.json" alt="Goofy" target="_blank">Goofy</a></b>
<pre>
___     _ _      __           _     ___    _ _        __ 
  (_   |  (_    _)  |        |  |  |   |  |  (__    __)  
    |  |    |  |    |  |\/|  |  |  |   |  |     |  |     
 _  |  |    |  |    |  |  |  |  |  |   |  |     |  |     
( |_|  |   _|  |_   |  |  |  |  |   \_/   |     |  |     
_\    /__ (      )_ |  |__|  |_ _\       /__ ___|  |____ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Gothic.json" alt="Gothic" target="_blank">Gothic</a></b>
<pre>
                                   
 _-_,,                         ,   
(  //    '                    ||   
  _||   \\  \\/\\/\\  \\ \\  =||=  
  _||   ||  || || ||  || ||   ||   
   ||   ||  || || ||  || ||   ||   
-__-,   \\  \\ \\ \\  \\/\\   \\,  
                                   
                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Graceful.json" alt="Graceful" target="_blank">Graceful</a></b>
<pre>
   __    __    _  _   _  _   ____  
 _(  )  (  )  ( \/ ) / )( \ (_  _) 
/ \) \   )(   / \/ \ ) \/ (   )(   
\____/  (__)  \_)(_/ \____/  (__)  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Gradient.json" alt="Gradient" target="_blank">Gradient</a></b>
<pre>
eeeeeee. eee. eee......eee. eee..eee. eeeeeeeee. 
@@@@@@@: @@@: @@@@::::@@@@: @@@::@@@: @@@@@@@@@: 
----%%%- %%%- %%%%%--%%%%%- %%%--%%%- ---%%%---- 
++++&&&+ &&&+ &&&&&&&&&&&&+ &&&++&&&+ +++&&&++++ 
****|||* |||* |||*||||*|||* |||**|||* ***|||**** 
!!==!!!= !!!= !!!==!!==!!!= !!!==!!!= ===!!!==== 
:::::::# :::# :::######:::# ::::::::# ###:::#### 
@.....@@ ...@ ...@@@@@@...@ @......@@ @@@...@@@@ 
                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Graffiti.json" alt="Graffiti" target="_blank">Graffiti</a></b>
<pre>
     ____. .__                      __    
    |    | |__|   _____    __ __  _/  |_  
    |    | |  |  /     \  |  |  \ \   __\ 
/\__|    | |  | |  Y Y  \ |  |  /  |  |   
\________| |__| |__|_|  / |____/   |__|   
                      \/                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Greek.json" alt="Greek" target="_blank">Greek</a></b>
<pre>
                                       
    ___                                
   / _ \                               
  ( (_| |_   _    _   _   _   _   ___  
 _ \ _   _) | |  | | | | | | | | (   ) 
| |___| |   | |  | |_| | | |_| |  | |  
 \_____/     \_) | ._,_|  \___/    \_) 
                 | |                   
                 |_|                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/HeX's Font.json" alt="HeX's Font" target="_blank">HeX's Font</a></b>
<pre>
            |\¯¯¯¯¯¯¯¯\_'          /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\ '                          /¯¯¯¯¯¯¯¯¯¯¯¯¯'\                    |\¯¯¯¯¯¯¯¯\'\¯¯¯¯¯¯¯¯\  '                  /¯¯¯¯¯¯¯¯¯¯¯¯\   /¯¯¯¯¯¯¯¯\ '                   
            '\ \              \'  |\___'''/\          '\\_____/|_             ° '/                          \ '       '\'\'             |'|            ° '| _   |\   °''                 '\/               '/|_  
              \|              '|  |:|:::::'|'|'\          '\::::::::|:|_       /        //        \\         \°         \'\           ''||\          *' °|      |:'\                        /\______'/:'|        
               |              '|  |:|:::::'|'| '|           |:::::::|:|_     '/         \\_____//          \            ' \|            \/           °'/|       |:::\__________/\   \'|::::::::::|::'|           
               |              '|  '\|:::::'|/' '|           |:::::::|/  '   /    °''      \:::::::'|/            \'_'     '|\                        '°\|       |:::'|:::::::::::::::::|:''\   \:::::::::'|*'/_  
  /¯¯¯¯¯/ /              '/|       '¯¯¯¹''  /          '/'¯¯¯¯  '         '/________/|::::::|\________\°                 ' |:'\                        '°\ _'   '\::'|:::::::::::::::::|:::'\ ° \::::::::|/ '    
 |         |'/________'/°'|       /¯¯¯¯\/          '//¯¯¯¯¯\              |::::::::::::::|:|¯¯¯'|:|::::::::::::::|        '|:::\_________/\        \_             ''\|:::::::::::::::::|:::::\   \'¯¯¯  _'       
'|\_____\:::::::::::::::|:°|°     \_________________'/|°                  |::::::::::::::|:|   _ |:|::::::::::::::|       '|::°|:::::::::::::::|/____°'/|°          '¯¯¯¯¯¯¯¯¯¯|::::::'\   \    _'               
'|:|:::::::::|:::::::::::::°|:'/_ '|:::::::::::::::::::::::::::::|''|'    |::::::::::::::|/     _'\|::::::::::::::|      ' ''\::|:::::::::::::::|'::::'°:°'|:|°      '°*              |:::::::|    | _'          
'|:|:::::::::|::::::::::::°:|/_'  '|:::::::::::::::::::::::::::::|''|'    '¯¯¯¯¯¯¯¯ _        ¯¯¯¯¯¯¯¯                        '\|:::::::::::::::|:::::::::|:|°                         |::::::/   '/|      '      
 \|:::::::::|¯¯¯¯¯¯¯¯³  '         '|:::::::::::::::::::::::::::::|/_'                                      _'                  ¯¯¯¯¯¯¯¯°|:::::::::|/                                                     '       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Heart Left.json" alt="Heart Left" target="_blank">Heart Left</a></b>
<pre>
 .-.-.   .-.-.   .-.-.   .-.-.   .-.-.  
( J .'  ( i .'  ( m .'  ( u .'  ( t .'  
 `.(     `.(     `.(     `.(     `.(    
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Heart Right.json" alt="Heart Right" target="_blank">Heart Right</a></b>
<pre>
.-.-.   .-.-.   .-.-.   .-.-.   .-.-.   
'. J )  '. i )  '. m )  '. u )  '. t )  
  ).'     ).'     ).'     ).'     ).'   
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Hellfire.json" alt="Hellfire" target="_blank">Hellfire</a></b>
<pre>
          |¯¯¯¯|      |¯¯¯¯|      \¯¯¯¯\       '/¯¯¯¯/             |¯¯¯¯|'|¯¯¯¯|°        /¯¯¯¯/|¯¯¯¯|\¯¯¯¯\              
          | .:::. |   | .:::. |    | .::...||¯¯¯|| .:::  |‘        |.::....|'|.::....|° |\____\|::....:|/____/|'         
'|¯¯¯¯| |.:::..:|     |.:::..:|    |:::... |'\__/'|:::....|        |::.... |'|...::::|° '\|;;;;;;;'|:::... |';;;;;;;|/“  
|\____\|____|°        |____|      /____/|\_'_/|\____\             |\____\|____|'           ¯¯¯¯|____|¯¯¯¯“               
| |;;;;;;;;;;;;;;;|°  |;;;;;;;|  '|;;;;;;;'|'|      |'|;;;;;;;'|' |'|;;;;;;;;;;;;;;;;|            |;;;;;;;|              
'\|_________|‘        |____|     '|____'|/      '\|____'|'        '\|_________|                   |____|“                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Henry 3D.json" alt="Henry 3D" target="_blank">Henry 3D</a></b>
<pre>
     _     __                               _     
     L]    LJ     _ _____       _    _     FJ_    
     | L         J '_  _ `,    J |  | L   J  _|   
     | |   FJ    | |_||_| |    | |  | |   | |-'   
.--__J J  J  L   F L LJ J J    F L__J J   F |__-. 
J\_____/  J__L  J__L LJ J__L  J\____,__L  \_____/ 
 J_____/  |__|  |__L LJ J__|   J____,__F  J_____F 
                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Hex.json" alt="Hex" target="_blank">Hex</a></b>
<pre>
4A 69 6D 75 74 
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Hieroglyphs.json" alt="Hieroglyphs" target="_blank">Hieroglyphs</a></b>
<pre>
  _     ;.  ,-==.     <~)_              
 `-)   ; |   (  (\     ( v~\            
 _/,'  `.|    |\.\\     \_/'   .-==-.   
(___)    |   _]_]`\\    /\    /______\  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Hollywood.json" alt="Hollywood" target="_blank">Hollywood</a></b>
<pre>
           _______                                                  
          (,     /'                                              /' 
               /'                                            --/'-- 
             /'          O      ,__________                  /'     
   _       /'          /'      /'    )     )    /'    /    /'       
 /' `    /'          /'      /'    /'    /'   /'    /'   /'         
(_____,/'           (__    /'    /'    /(__  (___,/(__  (__         
                                                                    
                                                                    
                                                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Horizontal Left.json" alt="Horizontal Left" target="_blank">Horizontal Left</a></b>
<pre>
 _    __    _     _    _______    ______     _         
| /___\ \  | |___| |  `._   __|  /_____ `.  | /_____   
| ______/  |  ___  |   _<  <__    _____\ |  | ______/  
|_\        |_|   |_|  /_______|  \______.`  |_\        
                                                       
                                                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Horizontal Right.json" alt="Horizontal Right" target="_blank">Horizontal Right</a></b>
<pre>
 __    _    _     _    _______     ______          _   
/ /___\ |  | |___| |  |__   _.'  .' _____\   _____\ |  
\______ |  |  ___  |   __>  >_   | /_____   \______ |  
      /_|  |_|   |_|  |_______\  '.______/        /_|  
                                                       
                                                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/ICL-1900.json" alt="ICL-1900" target="_blank">ICL-1900</a></b>
<pre>
J i m u t 
  *       
*   *     
      * * 
*         
          
        * 
    * *   
          
          
          
          
  *       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Impossible.json" alt="Impossible" target="_blank">Impossible</a></b>
<pre>
             _                _              _   _           _                       _        
            /\ \             /\ \           /\_\/\_\ _      /\_\                    /\ \      
            \ \ \            \ \ \         / / / / //\_\   / / /         _          \_\ \     
            /\ \_\           /\ \_\       /\ \/ \ \/ / /   \ \ \__      /\_\        /\__ \    
           / /\/_/          / /\/_/      /  \____\__/ /     \ \___\    / / /       / /_ \ \   
  _       / / /            / / /        / /\/________/       \__  /   / / /       / / /\ \ \  
 /\ \    / / /            / / /        / / /\/_// / /        / / /   / / /       / / /  \/_/  
 \ \_\  / / /            / / /        / / /    / / /        / / /   / / /       / / /         
 / / /_/ / /         ___/ / /__      / / /    / / /        / / /___/ / /       / / /          
/ / /__\/ /         /\__\/_/___\     \/_/    / / /        / / /____\/ /       /_/ /           
\/_______/          \/_________/             \/_/         \/_________/        \_\/            
                                                                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Invita.json" alt="Invita" target="_blank">Invita</a></b>
<pre>
      _____                       
     (, /      ,                  
       /          ___        _/_  
   ___/__    _(_  // (_ (_(_ (__  
 /   /                            
(__ /                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Isometric1.json" alt="Isometric1" target="_blank">Isometric1</a></b>
<pre>
       ___                       ___            ___            ___      
      /\  \         ___         /\__\          /\__\          /\  \     
      \:\  \       /\  \       /::|  |        /:/  /          \:\  \    
  ___ /::\__\      \:\  \     /:|:|  |       /:/  /            \:\  \   
 /\  /:/\/__/      /::\__\   /:/|:|__|__    /:/  /  ___        /::\  \  
 \:\/:/  /      __/:/\/__/  /:/ |::::\__\  /:/__/  /\__\      /:/\:\__\ 
  \::/  /      /\/:/  /     \/__/~~/:/  /  \:\  \ /:/  /     /:/  \/__/ 
   \/__/       \::/__/            /:/  /    \:\  /:/  /     /:/  /      
                \:\__\           /:/  /      \:\/:/  /      \/__/       
                 \/__/          /:/  /        \::/  /                   
                                \/__/          \/__/                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Isometric2.json" alt="Isometric2" target="_blank">Isometric2</a></b>
<pre>
                               ___            ___                     
    ___                       /\  \          /\  \                    
   /\__\        ___          |::\  \         \:\  \          ___      
  /:/__/       /\__\         |:|:\  \         \:\  \        /\__\     
 /::\  \      /:/__/       __|:|\:\  \    ___  \:\  \      /:/  /     
 \/\:\  \    /::\  \      /::::|_\:\__\  /\  \  \:\__\    /:/__/      
  ~~\:\  \   \/\:\  \__   \:\~~\  \/__/  \:\  \ /:/  /   /::\  \      
     \:\__\   ~~\:\/\__\   \:\  \         \:\  /:/  /   /:/\:\  \     
     /:/  /      \::/  /    \:\  \         \:\/:/  /    \/__\:\  \    
    /:/  /       /:/  /      \:\__\         \::/  /          \:\__\   
    \/__/        \/__/        \/__/          \/__/            \/__/   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Isometric3.json" alt="Isometric3" target="_blank">Isometric3</a></b>
<pre>
    ___                        ___            ___                   
   /  /\        ___           /__/\          /__/\           ___    
  /  /:/       /  /\         |  |::\         \  \:\         /  /\   
 /__/::\      /  /:/         |  |:|:\         \  \:\       /  /:/   
 \__\/\:\    /__/::\       __|__|:|\:\    ___  \  \:\     /  /:/    
    \  \:\   \__\/\:\__   /__/::::| \:\  /__/\  \__\:\   /  /::\    
     \__\:\     \  \:\/\  \  \:\~~\__\/  \  \:\ /  /:/  /__/:/\:\   
     /  /:/      \__\::/   \  \:\         \  \:\  /:/   \__\/  \:\  
    /__/:/       /__/:/     \  \:\         \  \:\/:/         \  \:\ 
    \__\/        \__\/       \  \:\         \  \::/           \__\/ 
                              \__\/          \__\/                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Isometric4.json" alt="Isometric4" target="_blank">Isometric4</a></b>
<pre>
                                  ___            ___                     
       ___           ___         /  /\          /  /\           ___      
      /__/\         /__/\       /  /::|        /  /:/          /__/\     
      \__\:\        \__\:\     /  /:|:|       /  /:/           \  \:\    
  ___ /  /::\       /  /::\   /  /:/|:|__    /  /:/             \__\:\   
 /__/\  /:/\/    __/  /:/\/  /__/:/_|::::\  /__/:/     /\       /  /::\  
 \  \:\/:/~~    /__/\/:/~~   \__\/  /~~/:/  \  \:\    /:/      /  /:/\:\ 
  \  \::/       \  \::/            /  /:/    \  \:\  /:/      /  /:/__\/ 
   \__\/         \  \:\           /  /:/      \  \:\/:/      /__/:/      
                  \__\/          /__/:/        \  \::/       \__\/       
                                 \__\/          \__\/                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Italic.json" alt="Italic" target="_blank">Italic</a></b>
<pre>
                       
   /   '   _       _/  
(_/   /   //)  (/  /   
                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ivrit.json" alt="Ivrit" target="_blank">Ivrit</a></b>
<pre>
      _    _                          _    
     | |  (_)   _ __ ___     _   _   | |_  
  _  | |  | |  | '_ ` _ \   | | | |  | __| 
 | |_| |  | |  | | | | | |  | |_| |  | |_  
  \___/   |_|  |_| |_| |_|   \__,_|   \__| 
                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/JS Block Letters.json" alt="JS Block Letters" target="_blank">JS Block Letters</a></b>
<pre>
  __  _  __  __  __ __  _____ 
__) || ||  \/  ||  |  ||_   _|
\___/|_||_|\/|_| \___/   |_|  
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/JS Bracket Letters.json" alt="JS Bracket Letters" target="_blank">JS Bracket Letters</a></b>
<pre>
   .-..-..-.   .-..-. .-. .---. 
.-.| || ||  `.'  || { } |{_   _}
| {} || || |\ /| || {_} |  | |  
`----'`-'`-' ` `-'`-----'  `-'  
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/JS Capital Curves.json" alt="JS Capital Curves" target="_blank">JS Capital Curves</a></b>
<pre>
  ____,  ____,  _____,    __   _,  ____, 
 (-|    (-|    (-| | |   (-|  |   (-|    
 _ |     _|__,  _| | |_,   |__|_,  _|    
(__/    (      (                  (      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/JS Cursive.json" alt="JS Cursive" target="_blank">JS Cursive</a></b>
<pre>
                               
    .   .   ,____,         -/- 
  _/_ _/_ _/ / / (_ _(_/_ _/_  
 _/_                           
(/                             
                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/JS Stick Letters.json" alt="JS Stick Letters" target="_blank">JS Stick Letters</a></b>
<pre>
                      ___  
   |  |   |\/|  |  |   |   
\__/  |   |  |  \__/   |   
                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Jacky.json" alt="Jacky" target="_blank">Jacky</a></b>
<pre>
  ________     _____      __    __      __    __    ________   
 (___  ___)   (_   _)     \ \  / /      ) )  ( (   (___  ___)  
     ) )        | |       () \/ ()     ( (    ) )      ) )     
    ( (         | |       / _  _ \      ) )  ( (      ( (      
 __  ) )        | |      / / \/ \ \    ( (    ) )      ) )     
( (_/ /        _| |__   /_/      \_\    ) \__/ (      ( (      
 \___/        /_____(  (/          \)   \______/      /__\     
                                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Jazmine.json" alt="Jazmine" target="_blank">Jazmine</a></b>
<pre>
                                
  o   o                     o   
  8                         8   
  8  o8  ooYoYo.  o    o   o8P  
  8   8  8' 8  8  8    8    8   
  8   8  8  8  8  8    8    8   
oP'   8  8  8  8  `YooP'    8   
...: :.. ..:..:.. :.....: ::..: 
:::: ::: :::::::: ::::::: ::::: 
:::: ::: :::::::: ::::::: ::::: 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Jerusalem.json" alt="Jerusalem" target="_blank">Jerusalem</a></b>
<pre>
                                       
     _   ___    __   __.  ___  __   __ 
    | | |_  |   \ \ / /  |_  | \ \ / / 
 _  | |   | |    \ V /     | | |  V /  
| |_| |   | |  ___\  \     | | | |\ \  
 \___/    | | |______|     |_| |_| \_\ 
          |_|                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Katakana.json" alt="Katakana" target="_blank">Katakana</a></b>
<pre>
              ######    #########  ##########       #      
##########      #               #           #    #######   
         #  ##########          #          #      # #      
         #      #       ########   ########       # #      
         #      #              #       ##      ##########  
         #      #              #     ##             #      
#########        ####   ########   ##               #      
                                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Kban.json" alt="Kban" target="_blank">Kban</a></b>
<pre>
   '||'   ||                           .    
    ||   ...   .. .. ..    ... ...   .||.   
    ||    ||    || || ||    ||  ||    ||    
    ||    ||    || || ||    ||  ||    ||    
|| .|'   .||.  .|| || ||.   '|..'|.   '|.'  
 '''                                        
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Keyboard.json" alt="Keyboard" target="_blank">Keyboard</a></b>
<pre>
                                                  
 _______   _______   _______   _______   _______  
|\     /| |\     /| |\     /| |\     /| |\     /| 
| +---+ | | +---+ | | +---+ | | +---+ | | +---+ | 
| |   | | | |   | | | |   | | | |   | | | |   | | 
| |J  | | | |i  | | | |m  | | | |u  | | | |t  | | 
| +---+ | | +---+ | | +---+ | | +---+ | | +---+ | 
|/_____\| |/_____\| |/_____\| |/_____\| |/_____\| 
                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Knob.json" alt="Knob" target="_blank">Knob</a></b>
<pre>
 ___         _______ _   _________   _________           _  
(  _)       (_______(_) (______   ) (  _______)  _______| | 
| |_______               _____(   ) | |_______  (_______  | 
(_________)             (_________) (_________)         |_| 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/LCD.json" alt="LCD" target="_blank">LCD</a></b>
<pre>
         _                         
    |                         |    
    |    +    |- -           -+-   
|   |    |    | | |  | |      |    
 ---                  --       -   
                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Larry 3D.json" alt="Larry 3D" target="_blank">Larry 3D</a></b>
<pre>
 _____                                      __       
/\___ \     __                             /\ \__    
\/__/\ \   /\_\      ___ ___      __  __   \ \ ,_\   
   _\ \ \  \/\ \   /' __` __`\   /\ \/\ \   \ \ \/   
  /\ \_\ \  \ \ \  /\ \/\ \/\ \  \ \ \_\ \   \ \ \_  
  \ \____/   \ \_\ \ \_\ \_\ \_\  \ \____/    \ \__\ 
   \/___/     \/_/  \/_/\/_/\/_/   \/___/      \/__/ 
                                                     
                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Lean.json" alt="Lean" target="_blank">Lean</a></b>
<pre>
                                                                       
         _/        _/                                         _/       
        _/                  _/_/_/  _/_/       _/    _/    _/_/_/_/    
       _/        _/        _/    _/    _/     _/    _/      _/         
_/    _/        _/        _/    _/    _/     _/    _/      _/          
 _/_/          _/        _/    _/    _/       _/_/_/        _/_/       
                                                                       
                                                                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Letters.json" alt="Letters" target="_blank">Letters</a></b>
<pre>
    JJJ  iii                        tt     
    JJJ       mm mm mmmm   uu   uu  tt     
    JJJ  iii  mmm  mm  mm  uu   uu  tttt   
JJ  JJJ  iii  mmm  mm  mm  uu   uu  tt     
 JJJJJ   iii  mmm  mm  mm   uuuu u   tttt  
                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Lil Devil.json" alt="Lil Devil" target="_blank">Lil Devil</a></b>
<pre>
             _       <-. (`-')               (`-')       
            (_)         \(OO )_       .->    ( OO).->    
   <-.--.   ,-(`-')  ,--./  ,-.) ,--.(,--.   /    '._    
 (`-'| ,|   | ( OO)  |   `.'   | |  | |(`-') |'--...__)  
 (OO |(_|   |  |  )  |  |'.'|  | |  | |(OO ) `--.  .--'  
,--. |  |  (|  |_/   |  |   |  | |  | | |  \    |  |     
|  '-'  /   |  |'->  |  |   |  | \  '-'(_ .'    |  |     
 `-----'    `--'     `--'   `--'  `-----'       `--'     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Line Blocks.json" alt="Line Blocks" target="_blank">Line Blocks</a></b>
<pre>
      _   _____   _________    _    _   _______  
     | |   | |   | | | | | \  | |  | |    | |    
 _   | |   | |   | | | | | |  | |  | |    | |    
|_|__|_|  _|_|_  |_| |_| |_|  \_|__|_|    |_|    
                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Linux.json" alt="Linux" target="_blank">Linux</a></b>
<pre>
  .-. .-. .-.-.-. .-..-. .---. 
 ,| | | | | | | | | || | `| |' 
`---' `-' `-'-'-' `----'  `-'  
                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Lockergnome.json" alt="Lockergnome" target="_blank">Lockergnome</a></b>
<pre>
    ::| ++               :|   
::> ::| :|  :\/|  :\:|  :::|  
 ::::/  :|  :::|  `::|   :|   
                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Madrid.json" alt="Madrid" target="_blank">Madrid</a></b>
<pre>
/=\                 |-  
_ |  =  /=\=\  | |  |   
\=/  |  | | |  \=/  \=  
                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Marquee.json" alt="Marquee" target="_blank">Marquee</a></b>
<pre>
     .::                              .::   
     .::  .:                          .::   
     .::     .::: .:: .::  .::  .:: .:.: .: 
     .:: .::  .::  .:  .:: .::  .::   .::   
     .:: .::  .::  .:  .:: .::  .::   .::   
.:   .:: .::  .::  .:  .:: .::  .::   .::   
 .::::   .:: .:::  .:  .::   .::.::    .::  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Maxfour.json" alt="Maxfour" target="_blank">Maxfour</a></b>
<pre>
~~|~ '                  |  
  |  | |/~\ /~\  |   | ~|~ 
\_|  | |   |   |  \_/|  |  
                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/MeDi.json" alt="MeDi" target="_blank">MeDi</a></b>
<pre>
          '|¯¯¯¯|      |¯¯¯¯|      '/¯¯¯¯/|¯¯¯¯|\¯¯¯¯\'            \¯¯¯¯\ '|¯¯¯¯|                 '|¯¯¯¯|'          
          '|       |   |¯¯¯¯|      |       | |       | |       |    |       | |       |   |¯¯¯¯||       ||¯¯¯¯|     
|¯¯¯¯|  |       |      |       |   |       | |       | |       |    |       | |       |   |____||       ||____|     
'\____\/____/'         |____|      |____| |____| |____|             '\____\|____|                ' |____|'          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Mer.json" alt="Mer" target="_blank">Mer</a></b>
<pre>
|¯¯¯¯¯¯||      O     |¯¯¯\/¯¯¯|       |'¯¯|¯¯'|°   |¯¯¯¯¯|°     
/¯¯|   |¯   |¯¯¯¯|   |            '|  |         |  |         |  
\____|      |____|   |.__|\/|__.|      \____/ '     ¯|__|¯      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Merlin1.json" alt="Merlin1" target="_blank">Merlin1</a></b>
<pre>
      ___     __       ___      ___   ____  ____    ___________   
     |"  |   |" \     |"  \    /"  | ("  _||_ " |  ("     _   ")  
     ||  |   ||  |     \   \  //   | |   (  ) : |   )__/  \\__/   
     |:  |   |:  |     /\\  \/.    | (:  |  | . )      \\_ /      
  ___|  /    |.  |    |: \.        |  \\ \__/ //       |.  |      
 /  :|_/ )   /\  |\   |.  \    /:  |  /\\ __ //\       \:  |      
(_______/   (__\_|_)  |___|\__/|___| (__________)       \__|      
                                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Merlin2.json" alt="Merlin2" target="_blank">Merlin2</a></b>
<pre>
    _         _        _                   _         _      
 __/\\__    _/\\_    _/\\___ _____    ___ /\\     __/\\__   
(_    _))  (____))  (_      v    ))  /  //\ \\   (__  __))  
  \  \\     /  \\    /  :   <\   \\  \:.\\_\ \\    /  \\    
/\/ .:\\   /:.  \\  /:. |   //   //   \  :.  //   /:.  \\   
\__  _//   \__  //  \___|  //\  //   (_   ___))   \__  //   
   \//        \//        \//  \//      \//           \//    
                                                            
                                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Mike.json" alt="Mike" target="_blank">Mike</a></b>
<pre>
                    _  
  |  _|  ||\  |/|    | 
  |                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Mini.json" alt="Mini" target="_blank">Mini</a></b>
<pre>
                              
   |   o   ._ _          _|_  
 \_|   |   | | |   |_|    |_  
                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Mirror.json" alt="Mirror" target="_blank">Mirror</a></b>
<pre>
 _       _                         _  
| |     (_)   ___ __ _   _   _   _| | 
| |  _  | |  / _ ' _` | | | | | |__ | 
| |_| | | | | | | | | | | |_| |  _| | 
 \___/  |_| |_| |_| |_| |_.__/  |__/  
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Mnemonic.json" alt="Mnemonic" target="_blank">Mnemonic</a></b>
<pre>
Jimut
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Modular.json" alt="Modular" target="_blank">Modular</a></b>
<pre>
     ___   ___    __   __   __   __   _______  
    |   | |   |  |  |_|  | |  | |  | |       | 
    |   | |   |  |       | |  | |  | |_     _| 
    |   | |   |  |       | |  |_|  |   |   |   
 ___|   | |   |  |       | |       |   |   |   
|       | |   |  | ||_|| | |       |   |   |   
|_______| |___|  |_|   |_| |_______|   |___|   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Morse.json" alt="Morse" target="_blank">Morse</a></b>
<pre>
.--- .. -- ..- - 
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Moscow.json" alt="Moscow" target="_blank">Moscow</a></b>
<pre>
                                   
# # #  #   #  #   #  #   #  #####  
 ###   #  ##  ## ##   # #     #    
  #    # # #  # # #    #      #    
 ###   ##  #  #   #   #       #    
# # #  #   #  #   #  #        #    

</pre>
'J'
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Mshebrew210.json" alt="Mshebrew210" target="_blank">Mshebrew210</a></b>
<pre>
          
| \/ | \> 
| _\ | L\ 
|         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Muzzle.json" alt="Muzzle" target="_blank">Muzzle</a></b>
<pre>
 __                          
   |  >  |\ /|  |  |  >>|<<  
<< |  |  | < |  |  |    |    
|__'  |  |   |  '<<'    |    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/NScript.json" alt="NScript" target="_blank">NScript</a></b>
<pre>
     gg                                                       
    dP8,                                                I8    
   dP Yb                                                I8    
  ,8  `8,      gg                                    88888888 
  I8   Yb      ""                                       I8    
  `8b, `8,     gg     ,ggg,,ggg,,ggg,    gg      gg     I8    
   `"Y88888    88    ,8" "8P" "8P" "8,   I8      8I     I8    
       "Y8     88    I8   8I   8I   8I   I8,    ,8I    ,I8,   
        ,88, _,88,_ ,dP   8I   8I   Yb, ,d8b,  ,d8b,  ,d88b,  
    ,ad88888 8P""Y8 8P'   8I   8I   `Y8 8P'"Y88P"`Y8 88P""Y88 
  ,dP"'   Yb                                                  
 ,8'      I8                                                  
,8'       I8                                                  
I8,      ,8'                                                  
`Y8,___,d8'                                                   
  "Y888P"                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/NT Greek.json" alt="NT Greek" target="_blank">NT Greek</a></b>
<pre>
                                       
    ___                                
   / _ \                               
  ( (_| |_   _    _   _   _   _   ___  
 _ \ _   _) | |  | | | | | | | | (   ) 
| |___| |   | |  | |_| | | |_| |  | |  
 \_____/     \_) | ._,_|  \___/    \_) 
                 | |                   
                 |_|                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/NV Script.json" alt="NV Script" target="_blank">NV Script</a></b>
<pre>
     gg                                                       
    dP8,                                                I8    
   dP Yb                                                I8    
  ,8  `8,      gg                                    88888888 
  I8   Yb      ""                                       I8    
  `8b, `8,     gg     ,ggg,,ggg,,ggg,    gg      gg     I8    
   `"Y88888    88    ,8" "8P" "8P" "8,   I8      8I     I8    
       "Y8     88    I8   8I   8I   8I   I8,    ,8I    ,I8,   
        ,88, _,88,_ ,dP   8I   8I   Yb, ,d8b,  ,d8b,  ,d88b,  
    ,ad88888 8P""Y8 8P'   8I   8I   `Y8 8P'"Y88P"`Y8  8P""Y8  
  ,dP"'   Yb                                                  
 ,8'      I8                                                  
,8'       I8                                                  
I8,      ,8'                                                  
`Y8,___,d8'                                                   
  "Y888P"                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Nancyj.json" alt="Nancyj" target="_blank">Nancyj</a></b>
<pre>
       dP  oo                          dP    
       88                              88    
       88  dP  88d8b.d8b.  dP    dP  d8888P  
       88  88  88'`88'`88  88    88    88    
88.  .d8P  88  88  88  88  88.  .88    88    
 `Y8888'   dP  dP  dP  dP  `88888P'    dP    
                                             
                                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Nancyj-Fancy.json" alt="Nancyj-Fancy" target="_blank">Nancyj-Fancy</a></b>
<pre>
MMMMMMMM""M  oo                          dP    
MMMMMMMM  M                              88    
MMMMMMMM  M  dP  88d8b.d8b.  dP    dP  d8888P  
MMMMMMMM  M  88  88'`88'`88  88    88    88    
M. `MMM' .M  88  88  88  88  88.  .88    88    
MM.     .MM  dP  dP  dP  dP  `88888P'    dP    
MMMMMMMMMMM                                    
                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Nancyj-Underlined.json" alt="Nancyj-Underlined" target="_blank">Nancyj-Underlined</a></b>
<pre>
       dP  oo                          dP    
       88                              88    
       88  dP  88d8b.d8b.  dP    dP  d8888P  
       88  88  88'`88'`88  88    88    88    
88.  .d8P  88  88  88  88  88.  .88    88    
 `Y8888'   dP  dP  dP  dP  `88888P'    dP    
oooooooooo ooo ooooooooooo ooooooooo ooooooo 
                                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Nipples.json" alt="Nipples" target="_blank">Nipples</a></b>
<pre>
     {__                              {__   
     {__  {_                          {__   
     {__     {___ {__ {__  {__  {__ {_{_ {_ 
     {__ {__  {__  {_  {__ {__  {__   {__   
     {__ {__  {__  {_  {__ {__  {__   {__   
{_   {__ {__  {__  {_  {__ {__  {__   {__   
 {____   {__ {___  {_  {__   {__{__    {__  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/O8.json" alt="O8" target="_blank">O8</a></b>
<pre>
  ooooo   o88                                  o8    
   888    oooo   oo ooo oooo    oooo  oooo   o888oo  
   888     888    888 888 888    888   888    888    
   888     888    888 888 888    888   888    888    
   888    o888o  o888o888o888o    888o88 8o    888o  
8o888                                                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/OS2.json" alt="OS2" target="_blank">OS2</a></b>
<pre>
_____ooo_ _oo__ __________ ________ _oo____ 
______oo_ _____ oo_oo_oo__ oo____o_ _oo____ 
______oo_ _oo__ ooo_oo__o_ oo____o_ oooo___ 
oo____oo_ _oo__ oo__oo__o_ oo____o_ _oo____ 
oo____oo_ _oo__ oo__oo__o_ ooo___o_ _oo__o_ 
_ooooo___ oooo_ oo______o_ oo_ooo__ __ooo__ 
_________ _____ __________ ________ _______ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Octal.json" alt="Octal" target="_blank">Octal</a></b>
<pre>
112 151 155 165 164 
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ogre.json" alt="Ogre" target="_blank">Ogre</a></b>
<pre>
   __    _                       _    
   \ \  (_)  _ __ ___    _   _  | |_  
    \ \ | | | '_ ` _ \  | | | | | __| 
 /\_/ / | | | | | | | | | |_| | | |_  
 \___/  |_| |_| |_| |_|  \__,_|  \__| 
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Old Banner.json" alt="Old Banner" target="_blank">Old Banner</a></b>
<pre>
      #                            
      #  #  #    #  #    #  #####  
      #  #  ##  ##  #    #    #    
      #  #  # ## #  #    #    #    
#     #  #  #    #  #    #    #    
#     #  #  #    #  #    #    #    
 #####   #  #    #   ####     #    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Patorjk's Cheese.json" alt="Patorjk's Cheese" target="_blank">Patorjk's Cheese</a></b>
<pre>
                                                                               
        ____   ____       ______  _______     ____   ____   _________________  
       |    | |    |     |      \/       \   |    | |    | /                 \ 
       |    | |    |    /          /\     \  |    | |    | \______     ______/ 
       |    | |    |   /     /\   / /\     | |    | |    |    \( /    /  )/    
 ____  |    | |    |  /     /\ \_/ / /    /| |    | |    |     ' |   |   '     
|    | |    | |    | |     |  \|_|/ /    / | |    | |    |       |   |         
|    | |    | |    | |     |       |    |  | |    | |    |      /   //         
|\____\|____| |____| |\____\       |____|  / |\___\_|____|     /___//          
| |    |    | |    | | |    |      |    | /  | |    |    |    |`   |           
 \|____|____| |____|  \|____|      |____|/    \|____|____|    |____|           
    \(   )/     \(       \(          )/          \(   )/        \(             
     '   '       '        '          '            '   '          '             
                                                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Patorjk-HeX.json" alt="Patorjk-HeX" target="_blank">Patorjk-HeX</a></b>
<pre>
                                                                                                                  
          _____        ____________            ___________          ______   _____        ________    ________    
         |\    \_     /            \          /           \         \     \  \    \      /        \  /        \   
         \ \     \   |\___/\  \\___/|        /    _   _    \         \    |  |    |     |\         \/         /|  
          \|      |   \|____\  \___|/       /    //   \\    \         |   |  |    |     | \            /\____/ |  
           |      |         |  |           /    //     \\    \        |    \_/   /|     |  \______/\   \     | |  
   ______  |      |    __  /   / __       /     \\_____//     \       |\         \|      \ |      | \   \____|/   
  /     / /      /|   /  \/   /_/  |     /       \ ___ /       \      | \         \__     \|______|  \   \        
 |      |/______/ |  |____________/|    /________/|   |\________\      \ \_____/\    \             \  \___\       
 |\_____\      | /   |           | /   |        | |   | |        |      \ |    |/___/|              \ |   |       
 | |     |_____|/    |___________|/    |________|/     \|________|       \|____|   | |               \|___|       
  \|_____|                                                                     |___|/                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Pawp.json" alt="Pawp" target="_blank">Pawp</a></b>
<pre>
                                        
 ______    _                       _    
(______)  (_)                     (_)_  
     (_)   _    __   __    _   _  (___) 
 _   (_)  (_)  (__)_(__)  (_) (_) (_)   
( )__(_)  (_) (_) (_) (_) (_)_(_) (_)_  
 (____)   (_) (_) (_) (_)  (___)   (__) 
                                        
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Peaks.json" alt="Peaks" target="_blank">Peaks</a></b>
<pre>
     /^^                              /^^   
     /^^  /^                          /^^   
     /^^     /^^^ /^^ /^^  /^^  /^^ /^/^ /^ 
     /^^ /^^  /^^  /^  /^^ /^^  /^^   /^^   
     /^^ /^^  /^^  /^  /^^ /^^  /^^   /^^   
/^   /^^ /^^  /^^  /^  /^^ /^^  /^^   /^^   
 /^^^^   /^^ /^^^  /^  /^^   /^^/^^    /^^  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Peaks Slant.json" alt="Peaks Slant" target="_blank">Peaks Slant</a></b>
<pre>
     _________/\/\_      _/\/\___      ________________      ____________      ___/\/\_____ 
    _________/\/\_      ________      _/\/\/\__/\/\___      _/\/\__/\/\_      _/\/\/\/\/\_  
   _________/\/\_      _/\/\___      _/\/\/\/\/\/\/\_      _/\/\__/\/\_      ___/\/\_____   
  _/\/\____/\/\_      _/\/\___      _/\/\__/\__/\/\_      _/\/\__/\/\_      ___/\/\_____    
 ___/\/\/\/\___      _/\/\/\_      _/\/\______/\/\_      ___/\/\/\/\_      ___/\/\/\___     
______________      ________      ________________      ____________      ____________      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Pebbles.json" alt="Pebbles" target="_blank">Pebbles</a></b>
<pre>
  OooOoo                               
      O   o                            
      o                           O    
      O                          oOo   
      o   O   `oOOoOO.  O   o     o    
      O   o    O  o  o  o   O     O    
O     o   O    o  O  O  O   o     o    
`OooOO'   o'   O  o  o  `OoO'o    `oO  
                                       
                                       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Pepper.json" alt="Pepper" target="_blank">Pepper</a></b>
<pre>
  _                   
   /  .  _ _      _/_ 
(_/  /  / / / /_/ /   
                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Poison.json" alt="Poison" target="_blank">Poison</a></b>
<pre>
                                                    
     @@@   @@@   @@@@@@@@@@    @@@  @@@   @@@@@@@   
     @@@   @@@   @@@@@@@@@@@   @@@  @@@   @@@@@@@   
     @@!   @@!   @@! @@! @@!   @@!  @@@     @@!     
     !@!   !@!   !@! !@! !@!   !@!  @!@     !@!     
     !!@   !!@   @!! !!@ @!@   @!@  !@!     @!!     
     !!!   !!!   !@!   ! !@!   !@!  !!!     !!!     
     !!:   !!:   !!:     !!:   !!:  !!!     !!:     
!!:  :!:   :!:   :!:     :!:   :!:  !:!     :!:     
::: : ::    ::   :::     ::    ::::: ::      ::     
 : :::     :      :      :      : :  :       :      
                                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/PsY.json" alt="PsY" target="_blank">PsY</a></b>
<pre>
      .:;¦\¯`¯'¯'\\    ’   ¦\\¯`¯'¯'\\         '¦\\`'¯`'¯¯'\:;;'/¯¯\/¯`'¯`'¯¯'\; '      :;/¯`'¯`'¯`/¦.:;'¦\¯`'¯`'¯'\'    :;/¯`'¯`;'/¦¦¯`'¯`'¯¦¦\¯`'¯`’¯\\_      
      .:;¦;\',_, .:;\;  ’  ¦:;\',_, .:;\;      '¦:;\',_,  .:;'\/.:;/`\_/`\\_, .:;'\;    ;¦   -  --;'¦;¦ .:;¦;¦   - -:;'¦ /___:;/:;/  -  -.:;'/¦;¦__''__''¦      
      .:;¦ .;\\¯` .:;'\ ’  ¦ .:;\\¯` .:;'\     '¦  ;'\\¯`    .:;'/.:;¦;¦:;'¦¦¯`   `;;¦  ;¦\     -.:;\'¦ .:;¦/ -   -:;/¦  ¦¦¯`'¯`'`¦/     -  ';/;'¦;¦¦'¯`’¯`’`¦¦ 
¦\ ¯¯¯¯\.:;'¦;      ';¦'   '\ .:;'¦;      ';¦  ;\  ;'¦      .:;'/ .:;¦;¦:;'/     .:;'/¦ ;¦:;\  -   -:;\,,/   -  -:;/;¦   ¦L,  .:;'¦      -:;'¦.:;/;¦L,   .:;’¦  
¦:;\ ____\/_____/¦'        .:;\;/_____/¦'      .:;\;/_____/.:;/\¦„¦//____;'/;'¦         ;¦ .:;\__________;/:;'¦            ¯¯¯;¦\__'___\;/    ¯¯¯¯¯             
¦.:;¦¦¯`'`':;¦¦¯`'¯¯`'¦;¦'  .:;¦¦¯`'¯¯`’'¦;¦       ;¦¦¯`'¯`''¦¦:;’/  .:;¦¦¯`'¯`'`¦¦:;¦  :;\ .:;¦¦¯`'¯`'¯`'¯’ .:;¦.:;/         .:;¦;¦¦¯`'¯`'’¦¦                  
;\:;¦      ;’¦;       ;¦;¦  .:;'¦;      ’';¦;¦     ;¦;       ;¦;'/   .:;¦';       ;¦;/   .:;\:;¦;             .:;¦;`/         .:;¦;¦;   PsY™                    
.:;\¦L_   ;'¦L_  .:;¦/''    .:;'¦L_  .:;;¦/'     .:;¦L,_ .:;¦/     .:;¦L_    .'¦/ '        .:;\¦L_          .:;'¦/  `          .:;\¦L_  .:;¦                    
         ¯¯     ¯¯   ’              ¯¯¯  ’                ¯¯               ¯¯                       ¯¯¯¯¯¯¯    ’'                       ¯¯                 '    
                        ’                                                                                            '                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/PsY2.json" alt="PsY2" target="_blank">PsY2</a></b>
<pre>
    '|¯¯| |¯¯|   |¯¯'\/'¯¯'|    |¯¯| |¯¯|     |¯¯¯¯¯¯¯|    
 __|   '| |   '| |   '|\/|   '| |   '|,|   '|  ¯¯|   '|¯¯’ 
\____/'   |__|   |__|  |__|     '\____ /'         '|__|’'  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Puffy.json" alt="Puffy" target="_blank">Puffy</a></b>
<pre>
 _____                           _    
(___  )  _                      ( )_  
    | | (_)   ___ ___    _   _  | ,_) 
 _  | | | | /' _ ` _ `\ ( ) ( ) | |   
( )_| | | | | ( ) ( ) | | (_) | | |_  
`\___/' (_) (_) (_) (_) `\___/' `\__) 
                                      
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Puzzle.json" alt="Puzzle" target="_blank">Puzzle</a></b>
<pre>
     _          _          _          _          _     
   _( )__     _( )__     _( )__     _( )__     _( )__  
 _|     _|  _|     _|  _|     _|  _|     _|  _|     _| 
(_ J _ (_  (_ I _ (_  (_ M _ (_  (_ U _ (_  (_ T _ (_  
  |_( )__|   |_( )__|   |_( )__|   |_( )__|   |_( )__| 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Pyramid.json" alt="Pyramid" target="_blank">Pyramid</a></b>
<pre>
  ^     ^     ^     ^     ^   
 /J\   /i\   /m\   /u\   /t\  
<___> <___> <___> <___> <___> 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Rammstein.json" alt="Rammstein" target="_blank">Rammstein</a></b>
<pre>
      _____                                                   
   __|_    |__    ____     ____    __     __   _       __     
  |    |      |  |    |   |    \  /  |   |  | | |    _|  |_   
 _|    |      |  |    |   |     \/   |   |  |_| |   |_    _|  
|______|    __|  |____|   |__/\__/|__|   |______|     |__|    
     |_____|                                                  
                                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Rectangles.json" alt="Rectangles" target="_blank">Rectangles</a></b>
<pre>
                                
    __   _                 _    
 __|  | |_|  _____   _ _  | |_  
|  |  | | | |     | | | | |  _| 
|_____| |_| |_|_|_| |___| |_|   
                                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Reeko Font 1.json" alt="Reeko Font 1" target="_blank">Reeko Font 1</a></b>
<pre>
                          (`·.               )\                                                                                 '                                                                                          
                            )  `·.   .·´( .·´  (                                                                                '                                                                                          
                    .·´( .·´:..::(,(::--  ' '\:·´             (`·.              )\               (`·.              ')\                                /(      .·´( )`·.                     (`·.                  )\       
                    );; :--  ' '             _\’'              )  `·.   .·´( .·´  (               )  `·.   .·´( .·´  ('                      )\      )  `·._):::.....::)'’                    )  `·.      .·´( .·´  (      
                .·´/\                ,..:´:::'/'       .·´( .·´:..::(,(::--  ' '\:·´      .·´( .·´:..::(,(::--  ' '\:·.·´('            )\ .·´ .:`·.(:;;  --  ' '\:. :(.·´)    )\      .·´( .·´:..::(,__(::..--  ' '\:·´('  
                )/:::'\...:/I       I::::::::/          \:::....::::·´         _\’'       );; :--   ’             _\::.. `·.)`·.   .·´  (,): --  ' '              \....:::`·.(  (     );; :--  ' ’                  _\::/  
                '\:::/:::/::I       I;;::· ´              )..:::·´      ,..:´:::'/'   .·´/\                ,..:´:::'/)::::..::::(  ):.::/\                 ,..::´/:::......:::·´  .·´/\                   ,.. : ´:::'/:’ ’ 
                  \/;:-´I:::I       I           ’         `·::/       /::::::::/      )/:::'\...:´/         `·;:;;:/·· ´´ ¯¯¯/’    `·:/::::\...:´/       /:::::'/`·:'/¯¯¯ /   ’   )/:::'\__..:´/       /::::::::::/   ' '  
     /(                 I:::I       I           ’            /       /;;::· ´          \:::/::::/                            '/       \::::/::::/      /;::::-'   '/       /       \:::/:::::·'/       /:::;;::· ´'        
    ):. `·.             I::/       /           '’           /       /                   '\/;::-'/       /:·,       .·´/      /'         \/;::-'/      /          /       /    '     '\/;::::-'/       /· ´                 
   /::...::( .·´(       I:/       /      '      ’   (`·.)':/       /             '     (`·.)':/       /:::/      /::/      /                 /      /          /       /             (`·.)':/       /'                     
  /¯¯¯¯ / ).. `·.    I/       /         '    ’        ):./       /                       ):./       /`·;/      /:·/      /'                '/      /          /       /     '          ):./       /'                '      
 /\        \:...:::(. · ´       /                    '\:/       /                  '    '\:/       /   /      /  /      /                 /I      'I         /       /                '\:/       /'                        
/:::`·.    ¯¯¯¯         ,.::/                         /       /                          /____/   /      '/  /      /                   /::/`· ,    ` ·,_’/       /        '           /       /'                 '        
\::::::::·.______..::::::/        '                 '/,..::·´/                     '    /:::::-  ´´  ,  - ´´´     .·´'/                I:/::::::::` · , ___,.·:/                     '/,..::·´/'                           
  `·::::::/::::::::::/:::;:·´                      '/:::::::/                      '  /::`*..¸..-:/:`*..¸..-::::::::/                   `·:;::::::::::/:::::/:::/                  '/:::::::'/                             
      `·:/::::::::::/;· ´                         /:;:: · ´                          /:::::::/::/:::::::/::::::::- ´´           '            ` ·:;:::/:::::/;·´                   /:;:: · ´'                       '       
          ¯¯¯¯¯                            ’'     ¯                              ’'  `*-::;/::::`*-::;/::::-·· ´´                                   ¯¯¯                      ’     ¯                                   ’'  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Relief.json" alt="Relief" target="_blank">Relief</a></b>
<pre>
_________ _______ ___________ ___________ ___________ 
__/~~~~\_ /~~~~\_ /~~\__/~~\_ /~~\__/~~\_ /~~~~~~~~\_ 
___/~~\__ _/~~\__ /~~~\/~~~\_ /~~\__/~~\_ ___/~~\____ 
___/~~\__ _/~~\__ /~~~~~~~~\_ /~~\__/~~\_ ___/~~\____ 
___/~~\__ _/~~\__ /~~\__/~~\_ /~~\__/~~\_ ___/~~\____ 
/~~~~\___ /~~~~\_ /~~\__/~~\_ _/~~~~~~\__ ___/~~\____ 
_________ _______ ___________ ___________ ___________ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Relief2.json" alt="Relief2" target="_blank">Relief2</a></b>
<pre>
\\\\\\\\\ \\\\\\\ \\\\\\\\\\\ \\\\\\\\\\\ \\\\\\\\\\\ 
\\///// \ ///// \ /// \\/// \ /// \\/// \ ///////// \ 
\\\/// \\ \/// \\ //// //// \ /// \\/// \ \\\/// \\\\ 
\\\/// \\ \/// \\ /// / /// \ /// \\/// \ \\\/// \\\\ 
\\\/// \\ \/// \\ /// \\/// \ /// \\/// \ \\\/// \\\\ 
///// \\\ ///// \ /// \\/// \ \/////// \\ \\\/// \\\\ 
\\\\\\\\\ \\\\\\\ \\\\\\\\\\\ \\\\\\\\\\\ \\\\\\\\\\\ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Reverse.json" alt="Reverse" target="_blank">Reverse</a></b>
<pre>
========== ==== ========== ======= ====== 
=====    = ==== ========== ======= ====== 
======  == ==== ========== ======= ====== 
======  == ==== ========== ======= ==  == 
======  == =  = =  =  = == =  =  = =    = 
======  == ==== =        = =  =  = ==  == 
======  == =  = =  =  =  = =  =  = ==  == 
=  ===  == =  = =  =  =  = =  =  = ==  == 
=  ===  == =  = =  =  =  = =  =  = ==  == 
==     === =  = =  =  =  = ==    = ==   = 
========== ==== ========== ======= ====== 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ribbit.json" alt="Ribbit" target="_blank">Ribbit</a></b>
<pre>
          '|¯¯¯¯'|     |¯¯¯¯|     |!¯¯¯¯\   /¯¯¯¯!|         |¯¯¯¯|'  |¯¯¯¯|        |¯¯¯¯¯¯¯¯¯¯|‚          
          '|:·.·.·:'|  |¯¯¯¯|     |:·.·.·:|\'\/'/|:·.·.·:|  |:·.·.·:|'  |:·.·.·:|  |___:·.·.·:___|‚       
|¯¯¯¯|  |:·.·.·:'|     |:·.·.·:|  |:·.·.·:|:'\/':|:·.·.·:|  |:·.·.·:|'  |:·.·.·:|  |'`·v´|:·.·.·:|`·v´|‚  
|\____\/____/|         |____|     |____|\:::/|____|         |\____\/____/|         L,_,|____|L,_|'        
|:|'¯`·v´||'¯`·v´|:|   |¯`·v·´|   |¯`·v·´| '\/ '|'¯`v.´’|   |:|'¯`·v´||'¯`·v´|:|        '|'¯`·v´'|‚       
'\|L,__'||L,__'|/'     |L,__‚|    |L,__'|     |L,__,|       '\|L,__'||L,__'|/'          '|L,__‚|‚         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ribbit2.json" alt="Ribbit2" target="_blank">Ribbit2</a></b>
<pre>
 '      .·´¯.·´¦    ¦`·.¯`·.‚  ¦`·.¯`·.  ‚.·´¯.·´¦'     /¯¯/¦   ¦\¯¯\        .·´¯.·´/¯\`·.¯`·.'      
       |    |::‚¦   ¦::|    |  ¦::'|‚    \/    ‚|‚::¦' '|    |'¦   ¦'|    |' |__| ‚|    |‚ |__|‚     
 |¯¯| |    |.·´'    `·‚|    |  `·‚'|    |\/|    |.·´   '|    |/   '\|    |'  |'`v‚|·'|    |·.|'`v‚|‚ 
‚¦\__\|__'|'          ‚|__'|     /'__/¦::¦\__'\‚       ¦`·._`·..·´_.·´¦'     |__| '|__'|  |__|‚      
‚¦'|`v´||'`v´'|'      '|/`v´|   '|`v´`|'¦\/¦ |`v´`|' ‚ ¦::|'`v‚||'`v |'::‚¦'       '|'`v |           
 \|__||__'|'          '|__‚|    '|__'|/   \|'__'|‚'    `·‚|__||__|.·´ ‚            '|__'|‚           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ribbit3.json" alt="Ribbit3" target="_blank">Ribbit3</a></b>
<pre>
'      .·´¯.·´  `·.¯`·.‚  `·.¯`·.  ‚.·´¯.·´    '/¯¯/    \¯¯\ '     .·´¯.·´/¯\`·.¯`·.‚    
      |    |‚     |    |    '|‚    \/    ‚|‚   |    |     '|    |' |__| ‚|    |‚ |__|    
|¯¯| |    |‚      |    |    '|    |\/|    |‚   |    |     '|    |'       '|    |         
'\__\|__'|‚       |__'|    '/'__/   \__'\‚     '`·._`·..·´_.·´           '|__'|          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Roman.json" alt="Roman" target="_blank">Roman</a></b>
<pre>
   oooo   o8o                                       .    
   `888   `"'                                     .o8    
    888  oooo   ooo. .oo.  .oo.    oooo  oooo   .o888oo  
    888  `888   `888P"Y88bP"Y88b   `888  `888     888    
    888   888    888   888   888    888   888     888    
    888   888    888   888   888    888   888     888 .  
.o. 88P  o888o  o888o o888o o888o   `V88V"V8P'    "888"  
`Y888P                                                   
                                                         
                                                         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Rotated.json" alt="Rotated" target="_blank">Rotated</a></b>
<pre>
(            __     __    _,_ 
 `--|  --o   __<   (__   ( '  
                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Rounded.json" alt="Rounded" target="_blank">Rounded</a></b>
<pre>
 _______   _                          
(_______) (_)                    _    
     _     _   ____    _   _   _| |_  
 _  | |   | | |    \  | | | | (_   _) 
| |_| |   | | | | | | | |_| |   | |_  
 \___/    |_| |_|_|_| |____/     \__) 
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Rowan Cap.json" alt="Rowan Cap" target="_blank">Rowan Cap</a></b>
<pre>
   dMMMMMP      dMP      dMMMMMMMMb     dMP dMP   dMMMMMMP  
      dMP      amr      dMP"dMP"dMP    dMP dMP      dMP     
     dMP      dMP      dMP dMP dMP    dMP dMP      dMP      
dK .dMP      dMP      dMP dMP dMP    dMP.aMP      dMP       
VMMMP"      dMP      dMP dMP dMP     VMMMP"      dMP        
                                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Rozzo.json" alt="Rozzo" target="_blank">Rozzo</a></b>
<pre>
    888  ,e,                            d8    
    888   "   888 888 8e   8888 8888   d88    
    888  888  888 888 88b  8888 8888  d88888  
 e  88P  888  888 888 888  Y888 888P   888    
"8",P'   888  888 888 888   "88 88"    888    
                                              
                                              

</pre>
'i'
'm'
'u'
't'
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Runic.json" alt="Runic" target="_blank">Runic</a></b>
<pre>
 /      
/       
\   \   
 \   \  
     /  
    /   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Runyc.json" alt="Runyc" target="_blank">Runyc</a></b>
<pre>
 /                         
/                          
\   \                      
 \   \  |  |\/|  |\   /|\  
     /  |  |/\|  | |   |   
    /   |  |  |  | |   |   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/S Blood.json" alt="S Blood" target="_blank">S Blood</a></b>
<pre>
     @@@  @@@  @@@@@@@@@@   @@@  @@@  @@@@@@@ 
     @@!  @@!  @@! @@! @@!  @@!  @@@    @@!   
     !!@  !!@  @!! !!@ @!@  @!@  !@!    @!!   
 .  .!!   !!:  !!:     !!:  !!:  !!!    !!:   
 ::.::    :     :      :     :.:: :      :    
                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/SL Script.json" alt="SL Script" target="_blank">SL Script</a></b>
<pre>
  ___                        
 (   >                   _/_ 
  __/_  o  ______   . .  /   
 / /   <_ / / / <_ (_/_ <__  
<_/                          
                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Santa Clara.json" alt="Santa Clara" target="_blank">Santa Clara</a></b>
<pre>
    ___                        
   ( /    o                _/_ 
    /    ,   _ _ _    , ,  /   
  _/_    (_ / / / /_ (_/_ (__  
 //                            
(/                             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Script.json" alt="Script" target="_blank">Script</a></b>
<pre>
                                        
  /\    o                               
 |  |         _  _  _              _|_  
 |  |   |    / |/ |/ |    |   |     |   
  \_|/  |_/    |  |  |_/   \_/|_/   |_/ 
   /|                                   
   \|                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Serifcap.json" alt="Serifcap" target="_blank">Serifcap</a></b>
<pre>
   __   __   __  __   _  _   ____  
  (  ) (  ) (  \/  ) ( )( ) (_  _) 
 __)(   )(   )    (   )()(    )(   
(___/  (__) (_/\/\_)  \__/   (__)  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Shadow.json" alt="Shadow" target="_blank">Shadow</a></b>
<pre>
      |   _)                          |    
      |    |    __ `__ \     |   |    __|  
  \   |    |    |   |   |    |   |    |    
 \___/    _|   _|  _|  _|   \__,_|   \__|  
                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Shimrod.json" alt="Shimrod" target="_blank">Shimrod</a></b>
<pre>
 ,                 .    
 |  o              |    
 |  .  ;-.-.  . .  |-   
 |  |  | | |  | |  |    
-'  '  ' ' '  `-`  `-'  
                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Short.json" alt="Short" target="_blank">Short</a></b>
<pre>
 | . ,_     |- 
_| | ||| L| |_ 
               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Slant.json" alt="Slant" target="_blank">Slant</a></b>
<pre>
       __     _                           __  
      / /    (_)    ____ ___    __  __   / /_ 
 __  / /    / /    / __ `__ \  / / / /  / __/ 
/ /_/ /    / /    / / / / / / / /_/ /  / /_   
\____/    /_/    /_/ /_/ /_/  \__,_/   \__/   
                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Slant Relief.json" alt="Slant Relief" target="_blank">Slant Relief</a></b>
<pre>
______/\\\\\\\\\\\_         _______         _____________________         _______________         _______________         
 _____\/////\\\///__         _______         _____________________         _______________         _______________        
  _________\/\\\_____         __/\\\_         _____________________         _______________         _____/\\\______       
   _________\/\\\_____         _\///__         ____/\\\\\__/\\\\\___         __/\\\____/\\\_         __/\\\\\\\\\\\_      
    _________\/\\\_____         __/\\\_         __/\\\///\\\\\///\\\_         _\/\\\___\/\\\_         _\////\\\////__     
     _________\/\\\_____         _\/\\\_         _\/\\\_\//\\\__\/\\\_         _\/\\\___\/\\\_         ____\/\\\______    
      __/\\\___\/\\\_____         _\/\\\_         _\/\\\__\/\\\__\/\\\_         _\/\\\___\/\\\_         ____\/\\\_/\\__   
       _\//\\\\\\\\\______         _\/\\\_         _\/\\\__\/\\\__\/\\\_         _\//\\\\\\\\\__         ____\//\\\\\___  
        __\/////////_______         _\///__         _\///___\///___\///__         __\/////////___         _____\/////____ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Slide.json" alt="Slide" target="_blank">Slide</a></b>
<pre>
    ||  #|                    #|    
    ||       ##H H|   ## H|  ##HH|  
    ||  #|   ### HH|  ## H|   #|    
##  ||  #|   ## H H|  ## H|   #|    
 #HH|   #H|  ##   H|   #HH|   #H|   
                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small.json" alt="Small" target="_blank">Small</a></b>
<pre>
     _    _                     _    
  _ | |  (_)   _ __     _  _   | |_  
 | || |  | |  | '  \   | || |  |  _| 
  \__/   |_|  |_|_|_|   \_,_|   \__| 
                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Caps.json" alt="Small Caps" target="_blank">Small Caps</a></b>
<pre>
  ___     ___    _   _   _  _    _____  
 )_ _(   )_ _(  ) \_/ ( ) () (  )__ __( 
 _) |    _| |_  |  _  | | \/ |    | |   
)___(   )_____( )_( )_( )____(    )_(   
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Isometric1.json" alt="Small Isometric1" target="_blank">Small Isometric1</a></b>
<pre>
    ___        ___        ___        ___        ___    
   /\  \      /\  \      /\__\      /\__\      /\  \   
  _\:\  \    _\:\  \    /::L_L_    /:/ _/_     \:\  \  
 /\/::\__\  /\/::\__\  /:/L:\__\  /:/_/\__\    /::\__\ 
 \::/\/__/  \::/\/__/  \/_/:/  /  \:\/:/  /   /:/\/__/ 
  \/__/      \:\__\      /:/  /    \::/  /    \/__/    
              \/__/      \/__/      \/__/              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Keyboard.json" alt="Small Keyboard" target="_blank">Small Keyboard</a></b>
<pre>
 ____   ____   ____   ____   ____  
||J || ||i || ||m || ||u || ||t || 
||__|| ||__|| ||__|| ||__|| ||__|| 
|/__\| |/__\| |/__\| |/__\| |/__\| 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Poison.json" alt="Small Poison" target="_blank">Small Poison</a></b>
<pre>
                                              
    @@@  @@@  @@@@@@@@@@   @@@  @@@  @@@@@@@  
    @@!  @@!  @@! @@! @@!  @@!  @@@    @!!    
    !!@  !!@  @!! !!@ @!@  @!@  !@!    @!!    
.  .!!   !!:  !!:     !!:  !!:  !!!    !!:    
::.::    :     :      :     :.:: :      :     
                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Script.json" alt="Small Script" target="_blank">Small Script</a></b>
<pre>
                                  
  /|   o                     _|_  
 | |   |   /|/|/|    |  |     |   
  \|/  |/   | | |_/   \/|_/   |_/ 
  (|                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Shadow.json" alt="Small Shadow" target="_blank">Small Shadow</a></b>
<pre>
     |   _)                     |    
  \  |    |     ` \     |  |     _|  
 \__/    _|   _|_|_|   \_,_|   \__|  
                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Slant.json" alt="Small Slant" target="_blank">Small Slant</a></b>
<pre>
     __    _                   __  
 __ / /   (_)   __ _   __ __  / /_ 
/ // /   / /   /  ' \ / // / / __/ 
\___/   /_/   /_/_/_/ \_,_/  \__/  
                                   

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Small Tengwar.json" alt="Small Tengwar" target="_blank">Small Tengwar</a></b>
<pre>
       '   _ _   ?       
(_(_|  |  |_)_)  |  |~)  
    |               |    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Soft.json" alt="Soft" target="_blank">Soft</a></b>
<pre>
                                                 
     ,--.  ,--.                          ,--.    
     |  |  `--'  ,--,--,--.  ,--.,--.  ,-'  '-.  
,--. |  |  ,--.  |        |  |  ||  |  '-.  .-'  
|  '-'  /  |  |  |  |  |  |  '  ''  '    |  |    
 `-----'   `--'  `--`--`--'   `----'     `--'    
                                                 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Sony.json" alt="Sony" target="_blank">Sony</a></b>
<pre>
        '                         '‚                              ‘                                   '‚                                     
                       '   '‚                    ‘                                   °                                                       
                  '                  °                        ‘                                  '‚                                          
'                            °                             /¯¯¯\ '/¯¯¯¯\            '‚                                                       
            ____'            ____    °          |\¯¯¯¯\/'/|    '|/'/|       '|                        '‚              /¯¯¯¯/|'‚              
           |\____\ ‘        |\____\ '           |;|       /;/     '/;/       /|            /¯¯¯¯/;/¯¯¯¯'/|          '/       /;'| '‚         
          |\¯¯¯¯¯\          /¯¯¯¯¯/| ‘          |/      '/;/___/;/       /;'|            '/       /;/       '/;'|   |       '|\¯¯¯¯\         
          |;|         |°   '|        '|;|      '/      '/;;|     '|/       /;;'/'‚      '/      '/;/       '/;;/‘   |\       \'\____\‘       
 /¯¯¯¯'/|/        '/|      '|\        \| '‚   /      '/;;/'|__,'/       /;;/           /       '|/        /;;/      |;'\       \|       | '‚ 
'|____'|/_____/;'|         '|;\_____\'‚      '|____|;/       |____|;'/‘               '|_____/|____|;'/  '‚         '\;;'\____\___.|         
'|       ||         |;'/'   \;|         |‘   '|       |/        |       |/ '‚         '|        |;|       |/‘         \;;|       |'          
'|____||_____|/ '‚           \|_____|        '|____|         |____|      '‚           '|____,|/|____|‘                  \|____|'             

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Speed.json" alt="Speed" target="_blank">Speed</a></b>
<pre>
_________ _____                        _____  
______  / ___(_) _______ ___  ____  __ __  /_ 
___ _  /  __  /  __  __ `__ \ _  / / / _  __/ 
/ /_/ /   _  /   _  / / / / / / /_/ /  / /_   
\____/    /_/    /_/ /_/ /_/  \__,_/   \__/   
                                              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Spliff.json" alt="Spliff" target="_blank">Spliff</a></b>
<pre>
  ____   ___   __  __   __ __   ____  
  \_  \ /___\ /  \/  \ /  |  \ /    \ 
---|  | |   | |  \/  | |  |  | \-  -/ 
\_____/ \___/ \__ \__/ \_____/  |__|  
                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stacey.json" alt="Stacey" target="_blank">Stacey</a></b>
<pre>
   ____ ____ __________ _______ ________ 
   7  7 7  7 7        7 7  7  7 7      7 
___|  | |  | |  _  _  | |  |  | !__  __! 
7  !  | |  | |  7  7  | |  |  |   7  7   
|     | |  | |  |  |  | |  !  |   |  |   
!_____! !__! !__!__!__! !_____!   !__!   
                                         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stampate.json" alt="Stampate" target="_blank">Stampate</a></b>
<pre>
,-_/                 .   
'  |  .  ,-,-.  . .  |-  
   |  |  | | |  | |  |   
   |  '  ' ' '  `-'  `'  
/  |                     
`--'                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stampatello.json" alt="Stampatello" target="_blank">Stampatello</a></b>
<pre>
,-_/                 .   
'  |  .  ,-,-.  . .  |-  
   |  |  | | |  | |  |   
   |  '  ' ' '  `-^  `'  
/` |                     
`--'                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Standard.json" alt="Standard" target="_blank">Standard</a></b>
<pre>
      _    _                          _    
     | |  (_)   _ __ ___     _   _   | |_  
  _  | |  | |  | '_ ` _ \   | | | |  | __| 
 | |_| |  | |  | | | | | |  | |_| |  | |_  
  \___/   |_|  |_| |_| |_|   \__,_|   \__| 
                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Star Strips.json" alt="Star Strips" target="_blank">Star Strips</a></b>
<pre>
--------     --------     ********    ----    ----  ------------  
********     ********    ----------   ****    ****  ************  
  ---          ----     ************  ----    ----  ------------  
  ***          ****     ---  --  ---  ****    ****      ****      
  ---          ----     ***  **  ***  ----    ----      ----      
  ***   **     ****     ---  --  ---  ************      ****      
  --------   --------   ***  **  ***  ------------      ----      
  ********   ********   ---      ---  ************      ****      
                                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Star Wars.json" alt="Star Wars" target="_blank">Star Wars</a></b>
<pre>
       __    __   .___  ___.   __    __   .___________. 
      |  |  |  |  |   \/   |  |  |  |  |  |           | 
      |  |  |  |  |  \  /  |  |  |  |  |  `---|  |----` 
.--.  |  |  |  |  |  |\/|  |  |  |  |  |      |  |      
|  `--'  |  |  |  |  |  |  |  |  `--'  |      |  |      
 \______/   |__|  |__|  |__|   \______/       |__|      
                                                        

</pre>
'i'
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stellar.json" alt="Stellar" target="_blank">Stellar</a></b>
<pre>
     `..                          `..   
     `..                          `..   
     `.. `... `.. `..  `..  `.. `.`. `. 
     `..  `..  `.  `.. `..  `..   `..   
     `..  `..  `.  `.. `..  `..   `..   
`.   `..  `..  `.  `.. `..  `..   `..   
 `....   `...  `.  `..   `..`..    `..  
                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stforek.json" alt="Stforek" target="_blank">Stforek</a></b>
<pre>
 __     _    __ __    _  _    _____   
|_ \   | |  |  V  |  | || |  |_   _|  
 _\ |  | |  | \_/ |  | \/ |    | |    
/___|  |_|  |_| |_|   \__/     |_|    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stick Letters.json" alt="Stick Letters" target="_blank">Stick Letters</a></b>
<pre>
                      ___  
   |  |   |\/|  |  |   |   
\__/  |   |  |  \__/   |   
                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stop.json" alt="Stop" target="_blank">Stop</a></b>
<pre>
   _____   _                         
  (_____) (_)                  _     
     _     _   ____    _   _  | |_   
    | |   | | |    \  | | | | |  _)  
 ___| |   | | | | | | | |_| | | |__  
(____/    |_| |_|_|_|  \____|  \___) 
                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Straight.json" alt="Straight" target="_blank">Straight</a></b>
<pre>
                      
  |  .   _        |_  
__)  |  |||  |_|  |_  
                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Stronger Than All.json" alt="Stronger Than All" target="_blank">Stronger Than All</a></b>
<pre>
.________  .___  ._____.___  .____      _____._ 
:____.   \ : __| :         | |    |___  \__ _:| 
 __|  :/ | | : | |   \  /  | |    |   |   |  :| 
|     :  | |   | |   |\/   | |    :   |   |   | 
 \__. __/  |   | |___| |   | |        |   |   | 
    :/     |___|       |___| |. _____/    |___| 
    :                         :/                
                              :                 
                                                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Sub-Zero.json" alt="Sub-Zero" target="_blank">Sub-Zero</a></b>
<pre>
   __      __      __    __      __  __      ______   
  /\ \    /\ \    /\ "-./  \    /\ \/\ \    /\__  _\  
 _\_\ \   \ \ \   \ \ \-./\ \   \ \ \_\ \   \/_/\ \/  
/\_____\   \ \_\   \ \_\ \ \_\   \ \_____\     \ \_\  
\/_____/    \/_/    \/_/  \/_/    \/_____/      \/_/  
                                                      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Swamp Land.json" alt="Swamp Land" target="_blank">Swamp Land</a></b>
<pre>
 _________     ________       ___ __ __       __  __        _________   
/________/\   /_______/\     /__//_//_/\     /_/\/_/\      /________/\  
\__.::.__\/   \__.::._\/     \::\| \| \ \    \:\ \:\ \     \__.::.__\/  
  /_\::\ \       \::\ \       \:.      \ \    \:\ \:\ \       \::\ \    
  \:.\::\ \      _\::\ \__     \:.\-/\  \ \    \:\ \:\ \       \::\ \   
   \: \  \ \    /__\::\__/\     \. \  \  \ \    \:\_\:\ \       \::\ \  
    \_____\/    \________\/      \__\/ \__\/     \_____\/        \__\/  
                                                                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Swan.json" alt="Swan" target="_blank">Swan</a></b>
<pre>
                                
                                
.---.                       .   
    |   o                  _|_  
    |   .   .--.--.  .  .   |   
    ;   |   |  |  |  |  |   |   
`--'  -' `- '  '  `- `--`-  `-' 
                                
                                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Sweet.json" alt="Sweet" target="_blank">Sweet</a></b>
<pre>
                                               ___       
            .-.                               (   )      
     .-.   ( __)   ___ .-. .-.     ___  ___    | |_      
    ( __)  (''")  (   )   '   \   (   )(   )  (   __)    
    (''")   | |    |  .-.  .-. ;   | |  | |    | |       
     | |    | |    | |  | |  | |   | |  | |    | | ___   
     | |    | |    | |  | |  | |   | |  | |    | |(   )  
     | |    | |    | |  | |  | |   | |  | |    | | | |   
     | |    | |    | |  | |  | |   | |  ; '    | ' | |   
 ___ | |    | |    | |  | |  | |   ' `-'  /    ' `-' ;   
(   )' |   (___)  (___)(___)(___)   '.__.'      `.__.    
 ; `-' '                                                 
  .__.'                                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/THIS.json" alt="THIS" target="_blank">THIS</a></b>
<pre>
       ▄█   ▄▀▀█▀▄     ▄▀▀▄ ▄▀▄   ▄▀▀▄ ▄▀▀▄   ▄▀▀▀█▀▀▄  
 ▄▀▀▀█▀ ▐  █   █  █   █  █ ▀  █  █   █    █  █    █  ▐  
█    █     ▐   █  ▐   ▐  █    █  ▐  █    █   ▐   █      
▐    █         █        █    █     █    █       █       
  ▄   ▀▄    ▄▀▀▀▀▀▄   ▄▀   ▄▀       ▀▄▄▄▄▀    ▄▀        
   ▀▀▀▀    █       █  █    █                 █          
           ▐       ▐  ▐    ▐                 ▐          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/TRaC.json" alt="TRaC" target="_blank">TRaC</a></b>
<pre>
      /\           ‘                   /\‚                     /¯¯¯¯ |   /¯¯¯¯\ °                   /\ '                     /\                           
    /    \_________                  /    \‚                 /      /|  |  /  /|      |           /    \     '             /    \__________'              
   |                       \       /      /|               /      /::|  |/  /:/      /|‘         |\      \‚               |                        \°     
   |\____        _       \°       |      |:'|            /      /::::|__/:/      /::|            |:|      |    /'\‚       |\____         _       \'       
   |:|::::::|\      \::|\    /|   |      |:'|          /      /:::::/|:::|/      /::::|‘         |/      /|  /    \       |:|::::::|\       \:|\     /|°  
   |:|::::::|::\      \|::\/::|   |\      \/         /      /:::::/  |::/      /:::::/°         /      /::| |\      \     |:|::::::|::\       \::\/:::|   
    \|::::::|::::\      \:|:::|‘  |::\      \      /      /:::::/    |/      /:::::/'‚        /      /::::| |:|      '|    \|::::::|::::\       \:|:::|   
      ¯¯¯ \:::::\      \::/'      |:::|      |'   |      |:::::/    /      /:::::/'         /      /:::::/  |/      /|       ¯¯¯ \:::::\       \:::/‘     
   /¯¯¯¯¯¯\::::|      |/‘         \:::|      |°   |\      \::/     |      |:::::/‘        /      /:::::/'  /      /::|'‚             \::::|        |/'    
 /          /|\ '\:/      /|‘       \/      /|    |::\    /|/      |\      \::/‘         |      |:::::/  /      /::::|'‚               \'/        /|‘     
|\        /::|::\____/::|'         /      /::|    |::::\/::|       |::\    /|/           |\      \::/_/      (:::::/                   |\       /::|'     
|::\    /::::|:::|::::::|::'|'    |\    /::::|°   \::::|:::|       |::::\/::|            |::\______/|\    /|::/‘                       |::\   /::::|'     
|::::\/:::::/'\::|::::::|::/      |::\/:::::/       \::|::/        \::::|:::|‘           |:::|:::::::::|:|::\/::|/‘                    |:::'\/:::::/‘     
\::::|::::/    '\|::::::|/        |:::|::::/ '‚       \|/            \::|::/'             \::|:::::::::|:|::|:::|‘                     \::::|::::/ '‚     
  \::|::/        ¯¯¯‘              \::|::/                             \|/       °          \|:::::::::|/\::|::/   °                     \::|::/ '‚       
    \|/                              \|/                                                      ¯¯¯¯¯    \|/                                 \|/°           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/TRaC Mini.json" alt="TRaC Mini" target="_blank">TRaC Mini</a></b>
<pre>
        |¯¯¯|° |¯¯¯|     /¯¯\/¯ \'    |¯¯¯|_|¯¯'|  |¯¯¯¯¯¯¯|°   
(¯¯(_/     /|  |___|   /__ (\/)__\ ‘  |\______/|   |¯¯|__|¯¯|'  
\|¯¯¯¯¯¯|/     |___|  |___ |v|___|     \|_____|/‘   ¯¯|__|¯¯    
  ¯¯¯¯¯¯'        ‘             ‘                                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/TRaC Tiny.json" alt="TRaC Tiny" target="_blank">TRaC Tiny</a></b>
<pre>
       \¯¯(    (¯¯¯(      ')¯¯¯V¯¯¯(         ')¯¯¯)  ___        ________       
(¯¯(_/___)       )___)   (___(\/)___ )‘     (___(_(___(‘       |__/)   (\__|'  
  ¯¯              °                       °                        (___')°     
       °     '             ‘                                    
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/TRaC's Old School Font.json" alt="TRaC's Old School Font" target="_blank">TRaC's Old School Font</a></b>
<pre>
 /¯¯¯/¯¯\    '    /¯¯¯/¯¯\                   /¯¯¯/¯¯'\ ‘              /¯¯¯/¯¯\              /¯¯¯/¯\        
 \¯¯¯\     \      \¯¯¯\     \'         /¯¯¯/¯¯\|       \'      /¯¯¯/¯¯\¯\     \ '‚        /     /    /     
   \     \     \°   \     \     \   ‘ \¯¯¯\     __|\__/        \¯¯¯\     '\ \      \    /___/      \ ‘     
/¯¯¯/¯\|     |‘       \     \     \‘    \     \    \             \     \     '\| |\_ /  \___\_/\    \      
\___\____/              \___\__/          \___\_/                  \___\___/ °               '\___\__|     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tanja.json" alt="Tanja" target="_blank">Tanja</a></b>
<pre>
J)jjjjjj  ##                         t)    
    J)                             t)tTTT  
    J)    i)   m)MM MMM   u)   UU    t)    
J)  jj    i)  m)  MM  MM  u)   UU    t)    
J)  jj    i)  m)  MM  MM  u)   UU    t)    
 J)jj     i)  m)      MM   u)UUU     t)T   
                                           
                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tengwar.json" alt="Tengwar" target="_blank">Tengwar</a></b>
<pre>
                                      dP"Yb.                
                 db                   `b   'Yb              
                                                            
.dP' .dP'  dP'  'Yb  `Yb d88b d88b       'Yb    `Yb.d888b   
88   88    88    88   88P   88   8b       88     88'    8Y  
Y8   Y8   .88    88   88    8P   88       88     88     8P  
`Y88P`Y88P'88   .8P   88  .dP  .dP       .8P     88   ,dP   
           88        .888888888888b.             88         
           88                                    88         
           Y8.                                  .8P         

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Term.json" alt="Term" target="_blank">Term</a></b>
<pre>
Jimut
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Test1.json" alt="Test1" target="_blank">Test1</a></b>
<pre>
___________  _________  ___   ___  _____ _____  _________  
\____/ \__/  \__/ \__/ |   \ /   | \   / \   / /__     __\ 
_`%%%\_/%'   _`%\_/%'_ |____|____| /___\_/___\ `%%|___|%%' 
`BBBBB'      `BBBBBBB'  `BBBBBBB'  `BBBBBBBBB'     `B'     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/The Edge.json" alt="The Edge" target="_blank">The Edge</a></b>
<pre>
  ▄▄▄▄▄  ▄█  █▀▄▀█    ▄       ▄▄▄▄▀  
▄▀  █    ██  █ █ █     █   ▀▀▀ █     
    █    ██  █ ▄ █  █   █      █     
 ▄ █     ▐█  █   █  █   █     █      
  ▀       ▐     █   █▄ ▄█    ▀       
               ▀     ▀▀▀             
                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Thick.json" alt="Thick" target="_blank">Thick</a></b>
<pre>
 8888  w                     w    
   8   w  8d8b.d8b.  8   8  w8ww  
w  8   8  8P Y8P Y8  8b d8   8    
`Yw"   8  8   8   8  `Y8P8   Y8P  
                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Thin.json" alt="Thin" target="_blank">Thin</a></b>
<pre>
                          
    | o             |     
    | . ,-.-. .   . |---  
    | | | | | |   | |     
`---' ` ` ' ' `---' `---' 
                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Thorned.json" alt="Thorned" target="_blank">Thorned</a></b>
<pre>
 ___,   ___,   , ,   ,  ,   ___,  
',|    ' |    |\/|   |  |  ' |    
(_|     _|_,  | `|  '\__|    |    
       '      '  `      `    '    
                                  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Three Point.json" alt="Three Point" target="_blank">Three Point</a></b>
<pre>
~|~ .  _ _      _|_ 
L|  | | | | |_|  |  
                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ticks.json" alt="Ticks" target="_blank">Ticks</a></b>
<pre>
_________/\/\_ _/\/\___ ________________ ____________ ___/\/\_____ 
_________/\/\_ ________ _/\/\/\__/\/\___ _/\/\__/\/\_ _/\/\/\/\/\_ 
_________/\/\_ _/\/\___ _/\/\/\/\/\/\/\_ _/\/\__/\/\_ ___/\/\_____ 
_/\/\____/\/\_ _/\/\___ _/\/\__/\__/\/\_ _/\/\__/\/\_ ___/\/\_____ 
___/\/\/\/\___ _/\/\/\_ _/\/\______/\/\_ ___/\/\/\/\_ ___/\/\/\___ 
______________ ________ ________________ ____________ ____________ 

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Ticks Slant.json" alt="Ticks Slant" target="_blank">Ticks Slant</a></b>
<pre>
     _________/\/\_      _/\/\___      ________________      ____________      ___/\/\_____ 
    _________/\/\_      ________      _/\/\/\__/\/\___      _/\/\__/\/\_      _/\/\/\/\/\_  
   _________/\/\_      _/\/\___      _/\/\/\/\/\/\/\_      _/\/\__/\/\_      ___/\/\_____   
  _/\/\____/\/\_      _/\/\___      _/\/\__/\__/\/\_      _/\/\__/\/\_      ___/\/\_____    
 ___/\/\/\/\___      _/\/\/\_      _/\/\______/\/\_      ___/\/\/\/\_      ___/\/\/\___     
______________      ________      ________________      ____________      ____________      

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tiles.json" alt="Tiles" target="_blank">Tiles</a></b>
<pre>
     [..                              [..   
     [..  [.                          [..   
     [..     [... [.. [..  [..  [.. [.[. [. 
     [.. [..  [..  [.  [.. [..  [..   [..   
     [.. [..  [..  [.  [.. [..  [..   [..   
[.   [.. [..  [..  [.  [.. [..  [..   [..   
 [....   [.. [...  [.  [..   [..[..    [..  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tinker-Toy.json" alt="Tinker-Toy" target="_blank">Tinker-Toy</a></b>
<pre>
    o                   o   
    |  o                |   
    |     o-O-o  o  o  -o-  
\   o  |  | | |  |  |   |   
 o-o   |  o o o  o--o   o   
                            
                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tombstone.json" alt="Tombstone" target="_blank">Tombstone</a></b>
<pre>
  __  _  _, _  _,_  ___ 
 , |  |  |\/|  | |   |  
 ( |  |  |  |  | |   |  
  ~~  ~  ~  ~  `~'   ~  
                        

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Train.json" alt="Train" target="_blank">Train</a></b>
<pre>
      _       _                            _      
   _ | |     (_)      _ __      _  _      | |_    
  | || |     | |     | '  \    | +| |     |  _|   
  _\__/     _|_|_    |_|_|_|    \_,_|     _\__|   
_|"""""|  _|"""""|  _|"""""|  _|"""""|  _|"""""|  
"`-0-0-'  "`-0-0-'  "`-0-0-'  "`-0-0-'  "`-0-0-'  

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Trek.json" alt="Trek" target="_blank">Trek</a></b>
<pre>
        dBP      dBP      dBBBBBBb      dBP dBP   dBBBBBBP 
                               dBP                         
      dBP      dBP      dBPdBPdBP     dBP dBP      dBP     
  dB'dBP      dBP      dBPdBPdBP     dBP_dBP      dBP      
 dBBBBP      dBP      dBPdBPdBP     dBBBBBP      dBP       
                                                           

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tsalagi.json" alt="Tsalagi" target="_blank">Tsalagi</a></b>
<pre>
_____    ___    -|-              ___    
 |  \     |      |       ,  |~,  / \    
 |__/    .|()    |      @|  |    `  |   
 | \    ()|'     | _     |  /       |   
_|  \_   _|_      _|      \/     \_/    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Tubular.json" alt="Tubular" target="_blank">Tubular</a></b>
<pre>
     O~~                              O~~   
     O~~  O~                          O~~   
     O~~     O~~~ O~~ O~~  O~~  O~~ O~O~ O~ 
     O~~ O~~  O~~  O~  O~~ O~~  O~~   O~~   
     O~~ O~~  O~~  O~  O~~ O~~  O~~   O~~   
O~   O~~ O~~  O~~  O~  O~~ O~~  O~~   O~~   
 O~~~~   O~~ O~~~  O~  O~~   O~~O~~    O~~  
                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Twiggy.json" alt="Twiggy" target="_blank">Twiggy</a></b>
<pre>
*           |\¯¯\„       *     |\¯¯\       .·´¨¯¯\                  /¯¯/|     |\¯¯\           |)¯¯¯`·.__.·´¯¯¯(|' ‘          
_          '| ;   ';    _     '| ;   ';  '/     .·|\'\/¯¯¨`·. °    ';   ';'|     | ;   ';  '.·´___.·´)     )`·.__ `·.'       
             /   '/|‘'          /   '/|° ;    (|*'| '\/\       \‚  ';   ';/      \;   ';   |       '| (     (|   '|       |  
  /¯¯/| .·´ '.·´| |‘'       .·´ '.·´|*|° |\    '`·.\ | ';       ;  '|\   '\ '     /   '/|  |____'|*'|`·.* '`·..|____|        
 '|\__\(__(|_ |/ ''       '(__(|_ |/°    | '\___ )\|'/____/|       '| |`·._`·.·´_.·´|'|           *  '|   |)__')'            
 '| |   '||    |.·´‘       |    |.·´     '\ '|     |   | '    *| | *\|  '|        |  '|/°             `·.'|  * '|            
_'\|__||__'|‘              |__'|           \|__ '|   |___ '|/‘       '`·.|____ |.·´ '                    '|__*|              

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Twisted.json" alt="Twisted" target="_blank">Twisted</a></b>
<pre>
     __      __      __    __      __    __      _______    
    /_/\    /\_\    /_/\  /\_\    /\_\  /_/\   /\_______)\  
    ) ) )   \/_/    ) ) \/ ( (   ( ( (  ) ) )  \(___  __\/  
 _ /_/ /     /\_\  /_/ \  / \_\   \ \ \/ / /     / / /      
/_/\ \ \    / / /  \ \ \\// / /    \ \  / /     ( ( (       
)_) ) ) )  ( (_(    )_) )( (_(     ( (__) )      \ \ \      
\_\___\/    \/_/    \_\/  \/_/      \/__\/       /_/_/      
                                                            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Two Point.json" alt="Two Point" target="_blank">Two Point</a></b>
<pre>
 | o ._ _      _|_ 
_| | | | | |_|  |  

</pre>
'u'
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/USA Flag.json" alt="USA Flag" target="_blank">USA Flag</a></b>
<pre>
     :::  :::  :::=======   :::==== 
     :::  :::  ::: === ===  :::==== 
     ===  ===  === === ===    ===   
 ==  ===  ===  ===     ===    ===   
 ======   ===  ===     ===    ===   
                                    

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Univers.json" alt="Univers" target="_blank">Univers</a></b>
<pre>
                                                               
        88   88                                                
        88   ""                                        ,d      
        88                                             88      
        88   88   88,dPYba,,adPYba,    88       88   MM88MMM   
        88   88   88P'   "88"    "8a   88       88     88      
        88   88   88      88      88   88       88     88      
88,   ,d88   88   88      88      88   "8a,   ,a88     88,     
 "Y8888P"    88   88      88      88    `"YbbdP'Y8     "Y888   
                                                               
                                                               

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Varsity.json" alt="Varsity" target="_blank">Varsity</a></b>
<pre>
    _____     _                                _     
   |_   _|   (_)                              / |_   
     | |     __     _ .--..--.     __   _    `| |-'  
 _   | |    [  |   [ `.-. .-. |   [  | | |    | |    
| |__' |     | |    | | | | | |    | \_/ |,   | |,   
`.____.'    [___]  [___||__||__]   '.__.'_/   \__/   
                                                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Wavy.json" alt="Wavy" target="_blank">Wavy</a></b>
<pre>
___                       
  (   o   _ _        _)_  
\__)  (  ) ) )  (_(  (_   
                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Weird.json" alt="Weird" target="_blank">Weird</a></b>
<pre>
                          
   |  /              /    
   |     _ _        (___  
   ) |  | | ) |   ) |     
 _/  |  |  /  |__/  |__   
                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Wet Letter.json" alt="Wet Letter" target="_blank">Wet Letter</a></b>
<pre>
   .-,  ,-.            .-. .-.   _______  
   | |  |(|  |\    /|  | | | |  |__   __| 
   | |  (_)  |(\  / |  | | | |    )| |    
   | |  | |  (_)\/  |  | | | |   (_) |    
(`-' |  | |  | \  / |  | `-')|     | |    
 \_ )|  `-'  | |\/| |  `---(_)     `-'    
   (_)       '-'  '-'                     

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Whimsy.json" alt="Whimsy" target="_blank">Whimsy</a></b>
<pre>
   d8,    d8,                                   
  `8P    `8P                              d8P   
                                       d888888P 
  d88     88b   88bd8b,d88b  ?88   d8P   ?88'   
  ?88     88P   88P'`?8P'?8b d88   88    88P    
   88b   d88   d88  d88  88P ?8(  d88    88b    
   `88b d88'  d88' d88'  88b `?88P'?8b   `?8b   
    )88                                         
   ,88P                                         
`?888P                                          

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Wow.json" alt="Wow" target="_blank">Wow</a></b>
<pre>
;_][ ]][ ][\/][ ][_][ `][` 
</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/X-Pose.json" alt="X-Pose" target="_blank">X-Pose</a></b>
<pre>
        ____‚                ____‚              ____       ____'                ____         ____ '             ___     ___'          
       |\¯¯¯¯\              |\'¯¯¯¯'\         |\¯¯¯¯'\     |\'¯'¯¯'\‚          |\¯¯¯¯\      /¯¯¯¯/|           '/¯¯¯'\   /¯¯¯'\        
       |:'\      ;\   '     |:'\       ;\'    |::\      ;\   '|::\     ;\ '    |::\     ;'\    |      ;|:|    |       ;\/  ¸    ;'|   
        \::\     ;;\   ‘     \::\      ;;\‚    \::'\     ;;\  \:::|     ;'\‘    \::'|    ;;'|   |      ;|/'   |'\__/\ `  ;\\__/|      
     ___\'|     ;;'|           \:|      ;;|"     \:'|     ;;;\  \'/      ;;|     '\/     ;'/|  '|      ;|‘    | |'¯'|:'|    ;'|¯¯|'|  
  '/'¯'¯¯'/'|     ;;'|           |      ;;|"      '\|     ;;|\;\/;/|     ;;|     '|      ;'|'|  '|      ;|‘   \'|__|/|    ;'|__|/°    
 /      ;/:/     `;'/|'         /       ;/|       /      ;/|:'\_//      ;/|‘     '|      ;'|/  /      ;/|°      ¯¯ /    ;'/|¯¯‘       
'|      ;'|'/;/\    ;'|'|°     '|       ;|:|     |      ;|/\::|¯||     ;'|:'|'   |\'____'\/____/::|                 |     ;|'| °      
 |\_____/ | \___\‘'            '|\____'\´        |\____\  \|_|\____\'            |'|'¯¯¯¯'||¯¯¯¯|:'/‘               |\___'\   '       
 | |¯¯¯¯| '/\ |¯¯¯|°           '|:|¯¯¯¯'|'       |'|¯¯¯¯|   ¯'| |¯¯¯¯|°          \|'____'||____|/'                  |:|¯¯¯'|          
 '\|____'|/  '\|___|           ''\'|____'|°      \|____|      \|____'|“            ¯¯¯¯  ¯¯¯¯'                      '\|___'|°         
   ¯¯¯¯       ¯¯¯'                 ¯¯¯¯ ‚          ¯¯¯          ¯¯¯¯ °            '                                    ¯¯¯‘           
          ‘                      ‘                     '                                             '                                

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/X99.json" alt="X99" target="_blank">X99</a></b>
<pre>
      °              _                ',:'/¯/`:,                     _             _                           ,.,        ,.,                      ,.-~·-.,__,.-::^·- .,'   ‘     
               .´/: : :/:`;          /:/_/::::/';'             ,·´/:::::'`:,   ,:´/::::'`:,'               ,·'/:::/     '/:::/';     '           /:::::::::::::::::::::::::/'; '  
              /:/:_: /:::'i         /:'     '`:/::;‘         '/  /:::::::::'`·/::/::::::::/'\             '/:/;:;/    ,/:;:/:::'`,             /;:·–– :;:::::_ ;: – .,/::;i'‘     
             /·´     '`;:::;'       ;         ';:';‘         /,·'´ ¯¯'`·;:::/:;·´ ¯ '`·;/:::i            /·´    ;`   '\    '`;::::\           /´          ¯¯           ';::/      
             i         'i::;        |         'i::i        /            '`;':/            \:::';        /      /.      \     '`;:::',       ,:                          ,:/       
             ';        'i::;°       ';        ;'::i      ,'               `'               ';:::i°    ,'      ;':';       '\      \::'i'°   ';_,..–-.,_     _    _,.·´‘           
    ,. -.,   ';        ';::;        'i        'i::i'    ,'                                  ;::i‘'    ;     'i::/`':.,_,.:'i      ;:/°               ,·´'    '`·;'i¯              
   /:::::/`:.,;       ';::;'         ;       'i::;'     ;'       ,^,         ,:^,          'i::;°     i      ';/::::;::/::;'      i/'                i         'i:i'       ’      
  /;:-:;/:::::'|       ;:/`;‘        ';       i:/'     'i        ;:::\       ;/   ',         'i:;'    ';      '`·-:;_;:·'´       ,' °                ';        ';:i'     ’        
,´      `·:;:·'       ;/'::/          ';     ;/ °      'i       'i::/  \     /      ;        ;/        ';                      ,'                     i        i:/'               
';                     `;/'            ';   / °         ;      'i:/     `*'´       'i       ;/ °        '\                   ,·'                       ;      i/    °             
  '`·,           _,.-·'´ °              `'´       °     '`.    ,'                   '.     /              `·.,         ,. ·´                            \   '/'                   
       '`'*^*'´¯    ”                    ‘                 `*´                      `'*'´                       ¯`'´¯                                     ¯               °       

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/X992.json" alt="X992" target="_blank">X992</a></b>
<pre>
             ,·´¨'`·,'           ,.-·.           ,·'´¨;.  '                        .-,             ,'´¨';'               ,  . .,  °       
            :,   .:´\           /    ;'\'        ;   ';:\           .·´¨';\        ;  ';\          ,'   ';'\'      ;'´    ,   ., _';\'    
            ;   :\:::\         ;    ;:::\       ;     ';:'\      .'´     ;:'\     ';   ;:'\        ,'   ,'::'\     \:´¨¯:;'   `;::'\:'\   
           ;  ,':::\·´'       ';    ;::::;'     ;   ,  '·:;  .·´,.´';  ,'::;'     ';  ';::';      ,'   ,'::::;       \::::;   ,'::_'\;'   
,.,      .'  ,'::::;''         ;   ;::::;      ;   ;'`.    ¨,.·´::;'  ;:::;       ';  ';::;     ,'   ,'::::;'            ,'  ,'::;'  ‘    
;   '\   ;  ,'::::;           ';  ;'::::;      ;  ';::; \*´\:::::;  ,':::;‘       ';  ';::;    ,'   ,'::::;'             ;  ;:::;  °      
 \  ';',·'  ,'::::;           ;  ';:::';      ';  ,'::;   \::\;:·';  ;:::; '       \   '·:_,'´.;   ;::::;‘               ;  ;::;'  ‘      
  '\    ,.'\::::;''           ';  ;::::;'     ;  ';::;     '*´  ;',·':::;‘          \·,   ,.·´:';  ';:::';               ;  ;::;'‚        
    \¯\::::\:;' ‘              \*´\:::;‘      \´¨\::;          \¨\::::;              \:\¯\:::::\`*´\::;  '               ',.'\::;'‚       
     '\::\;:·´'                 '\::\:;'       '\::\;            \:\;·'                `'\::\;:·´'\:::'\'   '             \::\:;'‚        
       ¯       °                  `*´‘           '´¨               ¨'                              `*´°                    \;:'      ‘    
                                                                                                    '                        °            

</pre>
<b><a href="https://github.com/Jimut123/jimner/blob/master/jimner/fonts/Zodi.json" alt="Zodi" target="_blank">Zodi</a></b>
<pre>
       '      ‚          O  ‚  ’                  ____‚          ____  ‘      '          ‘            '      
         ____°         ____         _____    /¯¯¯¯\             |\¯¯¯'\  ___'          ___  ___  __"         
       |\¯¯¯¯'\       |\¯¯¯¯\°     |\¯¯¯¯¯'\/  /|\    ' \‚‚     '\|      ||\¯¯¯\°     |¯¯¯||¯¯¯||¯¯¯|        
       '\|      ' |‚   \|      ' | '\|      ' |\_/;/\'|   '  |  '/    ' /|'\|  '   |  |___||  °  ||___|      
 ___  |    '   |      ‚/      ' /| '/      ' /|\|'|/  /     /|° |    ' |/ '/     /|   |'¯'  '||     ||'¯' ¯| 
|¯¯¯'|\|  '     |     |      ' |/” |     '  |/      |___|/      |\___\'|    ' |/‘      ¯¯¯'|___| ¯¯¯'        
|\___\|\____\‚‚       |\____\°     |\____\      |'¯' ¯|         '\|'¯' ¯||\___\‘          '  |'¯' ¯|’        
'\|'¯' '¯|\|'¯' ' ¯|‚ '\|'¯' '¯ |  '\|'¯' ¯¯|      ¯¯¯°           ¯¯¯ '\|'¯' ¯|'             ¯¯¯             
   ¯¯¯   ¯¯¯¯            ¯¯¯¯        ¯¯¯¯”‚                                ¯¯¯''         ‘            '      
       '      ‚                              '        ' ‘          ‘            '        ‘            '      

</pre>


Acknowledgements :

* [patorJK](http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Old%20Banner&t=WISP)
* [pyfiglet](https://github.com/pwaller/pyfiglet)

Author:
* [Jimut Bahan Pal](https://jimut123.github.io/)
