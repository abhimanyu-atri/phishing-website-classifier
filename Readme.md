## **Phishing Website Classifier**

## **Overview**
An machine learning model that classifies a website as phising website or not by using various classification algorithm and comparing their results.

## **Dataset**

## **Libraries Used**
Following libraries are used in this whole project
numpy
pandas
seaborn
sciket-learn
matplotlib
Pickle
## **Workflow**
->Pandas is used to load the dataset.
->Separation of features from target variable.
->Seborn is used to display the heatmap of features.
->Division of the dataset into 80-20 for training and testing.
->Then KNN algorithm is applied by using hyperparameter tuning for best results.
->For hyperparameter tuning GridSearchCV is used.
->Then accuracy and confusion matrix is calculated.
->Similarly Naive Bayes, Support vector machine(SVM), decsion tree and Random forest is applied.
->Then pickle dump is used to store the accuracy to the file.
## **Result**
Following are the result of hyperparameter tuning and algoritms applied.
**K Nearest Neighbour**
<img src"\results\KNN.png">

**Naive bayes**
<img src"\results\NB.png">

**Support Vector Machine**
<img src"\results\SVM.png">

**Decision Tree**
<img src"\results\DT.png">

**Random Forest**   
<img src"\results\RF.png">

## Command
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace notebooks/*.ipynb