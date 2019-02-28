# Ensemble Learning

## Introduction

Ensemble Learning is a group of learning models which aggregate multiple weak learning models together to get a better performance. The most straightforward example is that you want to make a decision whether to watch a movie (a classification problem), then you can ask all of your friends (weak classifiers), then you have several ways to evaluate each one's rating on this movie: (1) you take all their opinions as the same. (2) you consider more about the opinions from those who are movie directors, etc. These are all basic ideas of ensemble learning.

## Basic Ensemble Techniques
### 2.1 Max Voting

The max voting method is generally used for classification problems. In this technique, multiple models are used to make predictions for each data point. The predictions by each model are considered as a ‘vote’. The predictions which we get from the majority of the models are used as the final prediction.

```python
model1 = tree.DecisionTreeClassifier()
model2 = KNeighborsClassifier()
model3= LogisticRegression()

model1.fit(x_train,y_train)
model2.fit(x_train,y_train)
model3.fit(x_train,y_train)

pred1=model1.predict(x_test)
pred2=model2.predict(x_test)
pred3=model3.predict(x_test)

final_pred = np.array([])
for i in range(0,len(x_test)):
    final_pred = np.append(final_pred, mode([pred1[i], pred2[i], pred3[i]]))
```

Or using sklearn.ensemble import VotingClassifier instead.

### 2.2 Averaging

Similar to the max voting technique, multiple predictions are made for each data point in averaging. In this method, we take an average of predictions from all the models and use it to make the final prediction. Averaging can be used for making predictions in regression problems or while calculating probabilities for classification problems.

```python
model1 = tree.DecisionTreeClassifier()
model2 = KNeighborsClassifier()
model3= LogisticRegression()

model1.fit(x_train,y_train)
model2.fit(x_train,y_train)
model3.fit(x_train,y_train)

pred1=model1.predict_proba(x_test)
pred2=model2.predict_proba(x_test)
pred3=model3.predict_proba(x_test)

finalpred=(pred1+pred2+pred3)/3
```

### 2.3 Weighted Average

This is an extension of the averaging method. All models are assigned different weights defining the importance of each model for prediction. For instance, if two of your colleagues are critics, while others have no prior experience in this field, then the answers by these two friends are given more importance as compared to the other people.

```python
model1 = tree.DecisionTreeClassifier()
model2 = KNeighborsClassifier()
model3= LogisticRegression()

model1.fit(x_train,y_train)
model2.fit(x_train,y_train)
model3.fit(x_train,y_train)

pred1=model1.predict_proba(x_test)
pred2=model2.predict_proba(x_test)
pred3=model3.predict_proba(x_test)

finalpred=(pred1*0.3+pred2*0.3+pred3*0.4)
```

## Advanced Ensemble Techniques

### 3.1 Stacking
### 3.2 Blending
### 3.3 Bagging
### 3.4 Boosting

## Algorithms based on Bagging and Boosting
### 4.1 Bagging meta-estimator
### 4.2 Random Forest
### 4.3 AdaBoost
### 4.4 GBM
### 4.5 XGB
### 4.6 Light GBM
### 4.7 CatBoost
