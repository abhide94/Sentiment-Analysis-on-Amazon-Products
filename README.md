# Sentiment-Analysis-on-Amazon-Products


## Introduction

Sentiment analysis is the process of detecting positive or negative sentiment in text. It’s often used by businesses to detect sentiment in social data, gauge brand reputation, and understand customers.

Since customers express their thoughts and feelings more openly than ever before, sentiment analysis is becoming an essential tool to monitor and understand that sentiment. Automatically analyzing customer feedback, such as opinions in survey responses and social media conversations, allows brands to learn what makes customers happy or frustrated, so that they can tailor products and services to meet their customers’ needs.

This project was completed using Jupyter Notebook and Python with Pandas, NumPy, Matplotlib and Scikit-Learn.

## Resources
 Python Version: 3.7

 Packages: Pandas, Numpy, Matplotlib, Seaborn, Natural Language Toolkit

 Project Basis: Internship with Technocolabs
 
## Data Preprocessing
Data preprocessing is a data mining technique that is used to transform raw data into a useful and efficient format.

* Examined transaction data looking for inconsistencies, missing data and outliers
* Cleaned the data using ordinal mapping and filling of missing values and outliers with statistical best fit values

### Data Transformation
* In data transformation, we have transformed some of the texts written in the Reviews column into a vector form for the Machine Learning processing.

### Data Visualization 
* Data visualization is an interdisciplinary field that deals with the graphic representation of data.

![download (1)](https://user-images.githubusercontent.com/85448559/125897405-fe01807b-4774-4ba9-805c-2a156505ed5e.png)

## Model Building and Hypertuning

Support Vector Machine (SVM) is a relatively simple Supervised Machine Learning Algorithm used for classification and/or regression. In SVM, we plot each data item in the dataset in an N-dimensional space, where N is the number of features/attributes in the data. SVM can only perform binary classification.

To perform SVM on multi-class problems, we can create a binary classifier for each class of the data. The two results of each classifier will be:

• The data point belongs to that class OR

• The data point does not belong to that class.

### Linear SVM: 
Linear SVM is used for linearly separable data, which means if a dataset can be classified into two classes by using a single straight line, then such data is termed as linearly separable data, and classifier is used called as Linear SVM classifier.

![download (2)](https://user-images.githubusercontent.com/85448559/125898106-a28af59c-49c9-4e2c-96d9-fa7841975d71.png)


### Gaussian Radial Basis Function (RBF) SVM:
RBF SVM Kernel is popular because of its similarity to K-Nearest Neighborhood Algorithm. It has the advantages of K-NN and overcomes the space complexity problem as RBF Kernel Support Vector Machines just needs to store the support vectors during training and not the entire dataset.

![download (3)](https://user-images.githubusercontent.com/85448559/125898164-f002a59f-92bc-4025-be6e-53c1e1a0cfc7.png)


### Fine-Tuning:
Fine-tuning, in general, means making small adjustments to a process to achieve the desired output or performance.

![download4](https://user-images.githubusercontent.com/72228043/125901804-968b47c6-1ae2-47a0-8b8e-cab90558ef6e.png)

### Comparison among the models

![download5](https://user-images.githubusercontent.com/72228043/125901998-163fc133-e8ff-41cb-9e31-d1334cdf8d59.png)


## Model Deployment

Deployment of an ML-model simply means the integration of the model into an existing production environment which can take in an input and return an output that can be used in making practical business decisions.

In the deployment part, we have included 2 sections:
1. Web Page Deployment
2. Flask Server

We created a website using HTML Programming and used Flask Server to connect it to the server.
Here, customers can log-in to provide the product feedback and we can predict the customer’s sentiment towards the purchased product.

## Website link: https://amaz-review.herokuapp.com/




 






