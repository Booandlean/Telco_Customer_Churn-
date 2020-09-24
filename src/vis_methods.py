def vis_compare(column, buul = True):
    
    print('Key:')
    print('Churned + Not Churned, Churned, Not Churned')
    print(df[column].value_counts())
    fig, ax = plt.subplots(1, 3, figsize = (15,4))
    
    a = sns.countplot(df[column], ax=ax[0])
    b = sns.countplot(churn_df[column], ax=ax[1])
    c = sns.countplot(no_churn_df[column], ax=ax[2])
#rotate long text if categorical variables 
    if buul == False:
        a.set_xticklabels(a.get_xticklabels(), rotation = 30)
        b.set_xticklabels(b.get_xticklabels(), rotation = 30)
        c.set_xticklabels(c.get_xticklabels(), rotation = 30)
#titles    
    a.set_title('Churned + Not Churned')
    b.set_title('Churned')
    c.set_title('Not Churned')