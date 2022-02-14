## About the traning dataset
The traning dataset consists of more than 1000 customer reviews from Vietname e-commerce websites in categories: Clothing, Shoes, Bags, Luggage, Watches, and other Fashion accessories.

It were crawled and labeled        

The data can be downloaded [here](https://drive.google.com/file/d/1JlZpgM5uBZI-xeayv-AnXnW_OQjzaUYP/view?usp=sharing).
 
#   About 100k reviews 

## How were the training data prepared
The training data have been processed through following steps:

  1. Customer reviews from e-commerce websites were crawled. The crawled data include **reviews** (text) and **rating** (integers 1-5 corresponding to 1-5 rating stars).
  
  2. The **rating** data were converted into 3 class labels:
  
    1-2 stars => class label 0 (negative) 
    4-5 stars => class label 1 (positive) 
    3 stars   => class label 2 (neutral)
   
  3. The **class labels** were then manually reassigned. 

The dataset is saved in *utf-8 csv* format with 2 columns: **label**, **review**. There are about 100.000 reviews in the training data.




