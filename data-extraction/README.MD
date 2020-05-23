### Data extraction 

* Features for mortality prediction and length of stay prediction are replicated according to [this work](https://arxiv.org/pdf/1910.00964v2.pdf)
* Different from the authors, we are operating on eICU database v2.0

#### Extraction

* Run `extract-features.ipynb` with eICU credentials to download `rawdata.csv` file
* Summary of features and tables where the feature was extracted from are as follows:

| Feature 					| Table location 	| Data type |
| --- 						| --- 				| --- 		| 
| Heart rate 				| 					| Numerical	| 
| Mean arterial pressure  	| 					| Numerical	|
| Diastolic blood pressure	| 					| Numerical	|	
| Systolic blood pressure 	| 					| Numerical	|
| O2 						| 					| Numerical	| 
| Respiratory rate 			| 					| Numerical	| 
| Temperature 				| 					| Numerical | 
| Glucose 					| 					| Numerical	| 
| FiO2						| 					| Numerical	| 
| pH 						| 					| Numerical	| 
| Height 					| 					| Numerical	| 
| Weight 					| 					| Numerical	| 
| Age 						| 					| Numerical	| 
| Admission diagnosis 		| 					| Categorical| 
| Ethnicity 				| 					| Categorical|
| Gender 					| 					| Categorical| 
| Glasgow Coma Score Total  | 					| Categorical| 
| Glasgow Coma Score Eyes	| 					| Categorical| 
| Glasgow Coma Score Motor  | 					| Categorical| 
| Glasgow Coma Score Verbal	| 					| Categorical| 
