## robots-txt-parser.py
collect robots.txt endpoint for allowed and disallowed endpoints from a list of subdomains 
## Discription 
This tool collects endpoints from robots.txt files from a list of subdomains and give you the unique list of these endpoints so you could use it in all subdomains in directory brute forcing 
## Install 
1- git clone https://github.com/smackerdodi/robots-txt-parser.py.git 

2- cd robots-txt-parser 

3- pip3 install -r requirements.txt
## Usage 
python3.9 robots-txt-parser.py subs.txt unique-list.txt

subs.txt : a text file contains subdomains list start with http or https 

unique-list : the output of the tool 
