b# H1Voter
Increase votes on hackerone reports




#Usage

python voter.py listfile reportsIds   votecounts  <optional startingindex>   
python voter.py download 15882,158876    40          10     100

Args 

- File   		 : The file containing ids , you can use download to use the built-in list

- Ids  		     : Reports ids to vote , if many separate them by comma 

- votescount     : could be asigned to 'max' to get the maximum value of available votes
  	if you canceled the process you can resume it using startindex

- Startindex      : Optional to start from where you last stopped ' if the script crashed after bot bum 44 , you can asign startindex to 45'
                   
                 
![1](http://i.imgur.com/e7cJmzb.png)
![1](http://i.imgur.com/XBx2vj0.png)

