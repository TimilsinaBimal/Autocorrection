# Autocorrection
Autocorrection of a given word using the probability distribution and edit distances. The probability is calculated using the formula:   
## P(w) = C(w) / N
**where,**    
*C(W) = Number of times the word appear in text corpus   
N = Number of words in corpus*

This program suggests words upto two edit distances sorted by their probability distribution.

### Running the Project
1. Clone the repository to your local computer.   
```
git clone  https://github.com/TimilsinaBimal/Autocorrection.git
```
2. Change Directory and Run
```
cd Autocorrection/
``` 
***Windows***   
```
python main.py
```   
***Linux/MacOS***     
```
python3 main.py
  ```   
