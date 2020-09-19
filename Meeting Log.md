## 31/08/20
- [x] Clarify the task
- [x] Fill *Team Agreements*
- [x] Disscuss some ideas about the task, such as recommender system, link prediction, and classification
- [x] Set the goal of the next meeting

## 02/09/20
- [x] Literature review disccusion about the task
- [ ] Design the algorithm to implement
- [x] Proposed two challenges: unbalance train set and sparse vector space.
- [x] Need to implement dimensionality reduction methods on training dataset
- [x] Proposed four potential models: logistic regression, SVM, decision tree, and NN

## 04/09/20
- [ ] Literature review about the models and dimensionality reduction methods
- [x] XiaoWen proposed a workflow: cluster the nodes - define and cal the similarity between two nodes - draw conclusion

## 07/09/20
- [x] Certain the model: built a vector space to describe link, then use this representation to train a random forest classifer
+ vector space = multiple features of link, such as path similarity, subgraph similarity, clustering coefficient, and so on
+ train RF = using k-flod to construct training set and validation set
- [x] Complete the programming of *Jaccard similarity*

## 09/09/20
- [ ] Identify what features or measurements we should use in our vector space
- [ ] Discuss the idea and implement of RF

## 08/09/20
1. Computing type 2 and type 3 occupies too much time, thus as for now, only considering type 1 similarity.
2. Train data = sub date of *train.txt*. Since the link number of original train set is too large to compute the similarity on the link.
- [ ] Discuss RF latter

## 09/09/20 - 10/09/20
- [x] Multiple processing to compute similarity
- [x] Complete CN feature similarity computing
- [x] Try to mix type2 and type 3 and expect to obtain a promising result

## 11/09/20
- [x] Construct negative dataset
- [x] Try random forset, with similarity features

## 12/09/20
- [x] Complete KNN similarity computing, but it has a bad performance

## 13/09/20 - 16/09/20
- [x] Using memory to record the scores of training data, validation data, and test data
- [x] Compute Adar similarity, but discard type 2 due to computation limitation
- [x] Tune hype-parameters of RF
- [x] Try to solve the overfitting problem of RF and logistic regression

## 17/09/20 - 19/09/20
- [x] Complete report in Overleaf
