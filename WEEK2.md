#### WEEK 2
### Instructions to get eICU postgres locally
https://eicu-crd.mit.edu/tutorials/install_eicu_locally/
### Article
https://www.nature.com/articles/sdata2018178
### Schema 
https://mit-lcp.github.io/eicu-schema-spy/
1. How many unique hospitals? how many ICUs? 
2. How many procedures have ICD9/10 codes available?
3. What are the top 10 diseases that patients suffer from? 
4. Identify all the patients with heart disease 
	* Can be patients admitted on drugs that treat heart disease (can find just a subset)
5. Identify all the patients that were admitted and on diabetes drugs (what are these?)
	* Find the unique drugs and figure out which are diabetes usually
6. What types of visits do patients come to the ICU for? (ie unique procedures) top 5
identify all the patients with 3 types of heart procedures 
7. What is the average length of stay for most patients in the ICU? 
	* Can you check the above for patients that are diabetic + patients that suffer from heart disease? 
8. How many patients with diabetes and how many patients with heart disease die before they are released from their stay? 
	* Possible to plot the progression?
9. Dataset hiccup -> some hospital stays > ICU stays 
	* This is a problem with the data and I'd like to know how many of these there are and I want to see the output table
