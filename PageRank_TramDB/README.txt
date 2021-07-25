Simple Python Search Spider, Page Ranker, and Visualizer

1. store data in a SQLITE3 database named: 'spider.sqlite'
This file can be removed at any time to restart the process.   

2.You should install the SQLite browser to view and modify the data: http://sqlitebrowser.org/

This program crawls a web site and pulls a series of pages into the
database, recording the links between pages.

Note: Windows has difficulty in displaying UTF-8 characters
in the console so for each console window you open, you may need
to type the following command before running this code: 
http://stackoverflow.com/questions/388490/unicode-characters-in-windows-command-line-how

SEARCH SPIDER:

1.Run spider.py
Enter web url or enter: http://www.dr-chuck.com/
['http://www.dr-chuck.com']

How many pages:1
1 http://www.dr-chuck.com/ 12
How many pages:

Later when you restart the program again and want it to crawl more
pages, it will not duplicate any pages already in the database. Upon 
restart it goes to a random non-crawled page and starts there. So 
each successive run of spider.py is additive.

Run spider.py

Restarting existing crawl.  Remove spider.sqlite to start a fresh crawl.
['http://www.dr-chuck.com']
How many pages:2
11 http://www.dr-chuck.com/dr-chuck/resume/pictures/index.htm (926) 0
3 http://www.dr-chuck.com/sakai-book (5843) 4
How many pages:

You can have multiple starting points in the same database - 
within the program these are called "webs".   The spider
chooses randomly amongst all non-visited links across all
the webs.

If you want to dump the contents of the spider.sqlite file, you can 
run spdump.py as follows:

spdump.py

(2, None, 1.0, 2, 'http://www.dr-chuck.com/dr-chuck/resume/index.htm')
(1, None, 1.0, 11, 'http://www.dr-chuck.com/dr-chuck/resume/pictures/index.htm')
(1, None, 1.0, 10, 'http://www.dr-chuck.com/dr-chuck/resume/speaking.htm')
(1, None, 1.0, 3, 'http://www.dr-chuck.com/sakai-book')
(1, None, 1.0, 1, 'http://www.dr-chuck.com')
5 rows.

This shows the number of incoming links, the old page rank, the new page
rank, the id of the page, and the url of the page.  The spdump.py program
only shows pages that have at least one incoming link to them.

Once you have a few pages in the database, you can run Page Rank on the
pages using the sprank.py program.  You simply tell it how many Page
Rank iterations to run.

run sprank.py 

How many iterations:2
1 0.375
2 0.3125
[(1, 1.0625), (2, 1.3125), (3, 0.5625), (10, 1.0625)]

You can dump the database again to see that page rank has been updated:

run spdump.py 

(2, 1.0, 1.3125, 2, 'http://www.dr-chuck.com/dr-chuck/resume/index.htm')
(1, 1.0, 1.0, 11, 'http://www.dr-chuck.com/dr-chuck/resume/pictures/index.htm')
(1, 1.0, 1.0625, 10, 'http://www.dr-chuck.com/dr-chuck/resume/speaking.htm')
(1, 1.0, 0.5625, 3, 'http://www.dr-chuck.com/sakai-book')
(1, 1.0, 1.0625, 1, 'http://www.dr-chuck.com')
5 rows.

You can run sprank.py as many times as you like and it will simply refine
the page rank the more times you run it.  You can even run sprank.py a few times
and then go spider a few more pages sith spider.py and then run sprank.py
to converge the page ranks.

If you want to restart the Page Rank calculations without re-spidering the 
web pages, you can use spreset.py

run spreset.py 
All pages set to a rank of 1.0

sprank.py 

How many iterations:30
1 0.375
2 0.3125
3 0.265625
4 0.23828125
5 0.2119140625
....
25 0.020788212646643878
26 0.01850957930623065
27 0.016480711060503472
28 0.014674230708656422
29 0.01306576191405523
30 0.011633600274123579
[(1, 0.9285564433295901), (2, 1.5299049781981426), (3, 0.6129821351426763), (10, 0.9285564433295901)]

For each iteration of the page rank algorithm it prints the average
change per page of the page rank.   The network initially is quite 
unbalanced and so the individual page ranks are changing wildly.
But in a few short iterations, the page rank converges.  You 
should run prank.py long enough that the page ranks converge.

If you want to visualize the current top pages in terms of page rank,
run spjson.py to write the pages out in JSON format to be viewed in a
web browser.
 
run spjson.py 
Creating JSON output on spider.js...
How many nodes? 10
Open force.html in a browser to view the visualization

View this data by opening the file force.html in your web browser.  
This shows an automatic layout of the nodes and links. You can click and 
drag any node and you can also double click on a node to find the URL
that is represented by the node.