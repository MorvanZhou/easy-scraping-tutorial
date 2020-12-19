#!/usr/bin/python3

import sys
import requests
import bs4
RED = '\033[31m'
END = '\033[0m'
ascii_art = RED \
    + """                                                                                                                                                                                                


                                                                                                                     
                                                                                                                     
                                           iiii  kkkkkkkk             iiii                                           
                                          i::::i k::::::k            i::::i                                          
                                           iiii  k::::::k             iiii                                           
                                                 k::::::k                                                            
wwwwwww           wwwww           wwwwwwwiiiiiii  k:::::k    kkkkkkkiiiiiiippppp   pppppppppyyyyyyy           yyyyyyy
 w:::::w         w:::::w         w:::::w i:::::i  k:::::k   k:::::k i:::::ip::::ppp:::::::::py:::::y         y:::::y 
  w:::::w       w:::::::w       w:::::w   i::::i  k:::::k  k:::::k   i::::ip:::::::::::::::::py:::::y       y:::::y  
   w:::::w     w:::::::::w     w:::::w    i::::i  k:::::k k:::::k    i::::ipp::::::ppppp::::::py:::::y     y:::::y   
    w:::::w   w:::::w:::::w   w:::::w     i::::i  k::::::k:::::k     i::::i p:::::p     p:::::p y:::::y   y:::::y    
     w:::::w w:::::w w:::::w w:::::w      i::::i  k:::::::::::k      i::::i p:::::p     p:::::p  y:::::y y:::::y     
      w:::::w:::::w   w:::::w:::::w       i::::i  k:::::::::::k      i::::i p:::::p     p:::::p   y:::::y:::::y      
       w:::::::::w     w:::::::::w        i::::i  k::::::k:::::k     i::::i p:::::p    p::::::p    y:::::::::y       
        w:::::::w       w:::::::w        i::::::ik::::::k k:::::k   i::::::ip:::::ppppp:::::::p     y:::::::y        
         w:::::w         w:::::w         i::::::ik::::::k  k:::::k  i::::::ip::::::::::::::::p       y:::::y         
          w:::w           w:::w          i::::::ik::::::k   k:::::k i::::::ip::::::::::::::pp       y:::::y          
           www             www           iiiiiiiikkkkkkkk    kkkkkkkiiiiiiiip::::::pppppppp        y:::::y           
                                                                            p:::::p               y:::::y            
                                                                            p:::::p              y:::::y             
                                                                           p:::::::p            y:::::y              
                                                                           p:::::::p           y:::::y               
                                                                           p:::::::p          yyyyyyy                
                                                                           ppppppppp                                 
                                                                                                                     

                             [++] wikipy is simple wikipedia scraper [++]    
                                    Coded By: Ankit Dobhal                                
                                    Let's Begin To Scrape..!            
-------------------------------------------------------------------------------
wikipy version 1.0
""" \
    + END
print(ascii_art)

res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))

res.raise_for_status()
#Just to raise the status code
wiki = bs4.BeautifulSoup(res.text,"lxml")
elems = wiki.select('p')
for i in range(len(elems)):
    print(elems[i].getText())
