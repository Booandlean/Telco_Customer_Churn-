# README

## Git repo:

[data](https://github.com/Booandlean/Telco_Customer_Churn-/tree/master/data)
*Contains project data*

[src](https://github.com/Booandlean/Telco_Customer_Churn-/tree/master/src)
*Contains .py files of methods used*

[.gitignore](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/.gitignore)
*Tells git what to ignore*

[EDA_+_Vis.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/EDA_%2B_Vis.ipynb)
*Contains work for EDA and project visualizations*

[FSMs.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/FSMs.ipynb)
*Contains work done to create first simple models*

[Final_Model_(old).ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Final_Model_(old).ipynb)
*Contains final model from first workthrough*

[Final_Model_(new).ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Final_Model_(new).ipynb)
*Contains final model from second workthrough*

[Final_Notebook.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Final_Notebook.ipynb)
*Contains final notebook with discussion of modeling process and results*

[Modeling_Part_2.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Modeling_Part_2.ipynb)
*Contains work done for parameter tuning between FSMs and Final Model*

[Recall_modeling.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Recall_modeling.ipynb)
*Contains work done for parameter tuning models with recall score in mind*

[Recall_modeling_plus_SMOTE.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Recall_modeling_plus_SMOTE.ipynb)
*Same as prior notebook but using SMOTE to fight bias*

[README.md](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/README.md)
#### *you are here*

## Goal:
This project aims to create a model that can take in data about customers of the telco company and predicts if they are going to churn or not.

## About the data
This project uses [this dataset from kaggle](https://www.kaggle.com/blastchar/telco-customer-churn). It has numerical and categorical data from 7043 customers ranging from their total yearly charges to if the customer has dependents or of they are a senior citizen (etc.).

## How do I use this?
#### yml file/ enviorment
Before you use jupyer notebook to look at the .ipynb notebooks the environment needs to be set up. Open your terminal and navigate to the folder which contains telco.yml. Run:

'conda env create -f telco.yml' 

Then run: 

'conda activate telco'

to activate the environment. If you do not have pykernel installed, run: 

'pip install --user ipykernel' 

in the terminal. Once this is done, run: 

'python -m ipykernel install --user --name=telco' 

Upon opening jupyer notebook, go to the 'new' button with the down arrow. You should see 'telco' under the 'notebook' tab. Once you click 'telco' the environment will be set up, and you can now run the code within the notebooks. 

#### What do I do now?
Running the code blocks in order within the .ipynb notebooks will work just fine. For the sake of replicating my work I made them in the order of EDA + Vis, FSMs, Modeling_Part_2, Final_Model, then Final_Notebook. 

## Results

(old and incorrect)
In the end the best performing model for accuracy was the random forest with a .79. I will note that other times I had run it without the random state it had managed to go over .8, however it would be hacky of me to keep rolling the virtual dice to do so. 


(New and better)
The accuracy score may be lower than the first time around with a score about .77 and the recall score may only be .56 but this new model is signifigantly less biased towards guessing 'not churned' than before now that it has a more balanced dataset. My goal was to lower the number of false negatives (incorrectly guessing that a customer will churn when they will not) and I did succeed at that goal. However, now there are more false postives (incorrectly guessing that a customer will not churn when they will) which is a new problem. 

Based on the visualizations made earlier it is looking like customers with monthly contracts are especially likely to churn. Additonal traits to look out for are customers who are senior citizens, have no partner, no dependents, pay their bills with an electronic check, and did not purchase any tech support and/ or online security plans. 

## Next Steps

The next time I work on this project I am palnning on doing things differently. 

The new goal will be to lower the number of false positives. The way that I was looking at it originaly was that FP's did not look to be a huge problem, and there were a number of false negatives that I thought could cause additional costs. After using SMOTE and balancing the number of curned vs not churned customers this changed. Predicting that people will not leave when in reality they will will lead to a greater loss of revenue than spending extra on staying customers. This is why I will be optimizing the models with false positives in mind in the future. 

I would also like to try messing with the data itself more, perhaps using different encoders and scalers and using a data balancing technique other than SMOTE. 

I will return to this project eventualy, but for now I wish to practice other things. 