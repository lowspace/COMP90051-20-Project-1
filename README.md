# COMP90051-20-Project-1

## Team Info
**Team Num**: 65

**Team Name**: [Time Is Money](https://www.kaggle.com/c/comp90051-2020-sem2-proj1/leaderboard)

**Teammates**:
  - Zhizhang LIN
  - Xiaowen JIN
  - Wei LI
  
## Data Set
Number of UserID: 20,000<br>
Number of Followee: 4,867,136<br>
Number of Edge/Link:24,004,361<br>

## Kaggle Result

| Individual Feature | Type 1      | Type 2      | Type 3      |
| :---               | :---:       |   :---:     |   :---:     |  
| *Jaccard*          | 0.73706   |   0.78049          |  **0.87331**    |
| *Cosine*           | 0.79743     |    0.69522       |**0.90504**|
| *Common Neighbors* | 0.73067| 0.68997|0.62689|
| *Adar*             | **0.80140** | ------- | 0.64677|
|*KNN1*|0.48147|
|*KNN2*|0.43365
|*KNN3*|0.43693
|*KNN4*|0.43676

| Model | AUC     | 
| :---               | :---:       |
|RF| **0.85922**|
|LR| 0.79229|

## Score and Comments

Kaggle competition: 15.66/16

Final report: 11.2/14

Total: 26.8/30

Comment in critical analysis (7.2/9):
> Good work! The report covers the key aspects: sampling, feature generation, learning and model selection. While the features considered were relatively simple, they performed surprisingly well - especially "cosine similarity". A couple of classifiers were considered, including a non-linear one. Tuning was done via cross-validation to avoid overfitting, however it's unclear how the final model was selected (test AUCs are reported, so may be overfitting). The sampling was naive - missing edges were treated as fake and there was no attempt to match the test set. It was great that you mentioned future directions to explore - including node embeddings.

Comment in clarity and structure (4/5):
> The report was a pleasure to read. It was well-structured and clear. I appreciated the use of tables to summarise the results and features. Some space could have been put to better use expanding on insights/motivations etc., rather than defining well-known concepts (e.g. random forest, logistic regression, ROC-AUC). Good referencing.
