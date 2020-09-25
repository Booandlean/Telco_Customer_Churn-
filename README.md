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
[Final_Model.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Final_Model.ipynb)
*Contains final model*
[Final_Notebook.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Final_Notebook.ipynb)
*Contains final notebook with discussion of modeling process and results*
[Modeling_Part_2.ipynb](https://github.com/Booandlean/Telco_Customer_Churn-/blob/master/Modeling_Part_2.ipynb)
*Contains work done for parameter tuning between FSMs and Final Model*
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

## Modeling Results

In the end the best performing model for accuracy was a random forest with a .79 accuracy score. I will note that other times I had run it without the random state it had managed to go over .8, however it would be hacky of me to keep rolling the virtual dice to do so. 

## Next Steps

For the next time I work on this project I am palnning on doing things differently. For starters I had used accuracy as my model performance score. Using accuracy is not necessarily a bad idea for predictive modeling, however while working with customer churn I am theoretically advising a company on how to allocate their funds on specific people who are at risk of churning. Mistakenly claiming someone may churn out while in reality they won't (this is in refrence to false negatives/ FN in the confusion matrix) could end up costing the company money that they do not need to spend on people they do not need to pay extra attention to. This is why I will be using the recall score over the accuracy score in the next iteration of this project. If I were doing this with false negatives in mind and tuning the mdoels for recall over accuracy, the KNN model would have likely won. 

One avenue that is definetly worth exploring is using something like SMOTE to even out the number of churned vs non churned customers. This will certainly be done in the phase 2 of this project, but I am mostly stopping for now as I want to work on other things.