## Model Assumption
### the probability of potential existance of relationship between a pair of ID: (A, B)

##### (1) 
if B is followed by more people, then its more likely to be followed by A.
##### (2) 
if A has followed more IDs, then it is more likely to follow B.
##### (3) 
if A and B are both followed by more people, then A and B are more likely to follow each other.
##### (4) 
if B is in the same cluster of more IDs in the following list of A, then A is more likely to follow B.

## Model 
A random forest (RF) classifer trained by features of the links.
+ Links = A directed edge/link between two nodes/vertices
+ Features = Description of the attributions of the link, such as the similarity, clustering, degree, and so on.

## Problems
- [ ] This classifer will be fed only with one label data, which may cause the classifer pay much more attention on that label
- [ ] The number of links is huge, thus it may cost a lot of time and memory to train the model, how can we balance/ trade-off the two?
- [ ] How to avoid outfitting prolbem of RF?
