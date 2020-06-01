### Data extraction 

* Features for mortality prediction and length of stay prediction are replicated according to [this work](https://arxiv.org/pdf/1910.00964v2.pdf)
* Different from the authors, we are operating on eICU database v2.0

#### Extraction

* Run `extract-features.ipynb` with eICU credentials to download `rawdata.csv` file
* Summary of features and tables where the feature was extracted from are as follows:

| Feature 					| Table location 	| Data type |
| --- 						| --- 				| --- 		| 
| Heart rate 				| apacheapsvar		| Numerical	| 
| Mean arterial pressure  	| formula        	| Numerical	|
| Diastolic blood pressure	| vitalaperiodic	| Numerical	|	
| Systolic blood pressure 	| vitalaperiodic	| Numerical	|
| O2 						| apacheapsvar		| Numerical	| 
| Respiratory rate 			| apacheapsvar		| Numerical	| 
| Temperature 				| apacheapsvar		| Numerical | 
| Glucose 					| apacheapsvar		| Numerical	| 
| FiO2						| apacheapsvar		| Numerical	| 
| pH 						| apacheapsvar		| Numerical	| 
| Height 					| patient			| Numerical	| 
| Weight 					| patient			| Numerical	| 
| Age 						| patient			| Numerical	| 
| Admission diagnosis 		| patient			| Categorical| 
| Ethnicity 				| patient			| Categorical|
| Gender 					| patient			| Categorical| 
| Glasgow Coma Score Total  | 					| Numerical| 
| Glasgow Coma Score Eyes	| apacheapsvar		| Numerical| 
| Glasgow Coma Score Motor  | apacheapsvar		| Numerical| 
| Glasgow Coma Score Verbal	| apacheapsvar		| Numerical| 

mean arterial pressure = SBP + 2(DBP)
GCS total = GCS sum of eyes, motor, verbal