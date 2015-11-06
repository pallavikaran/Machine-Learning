# Machine-Learning
automated essay grader


Report:
1. Abstract
2. keywords
3. Introduction
4. Background/ requirements
4.1. Machine learning 
4.1.1 Data Collection
4.1.2 Data pre-processing
4.1.3 Development of models -Algorithms
4.2 Classififcation of Algorithms
4.3 Related work
5. Methodology
5.1 Feature selection
5.2 Impelmenting machine learning algorithms
5.3 Developing the scoring system (Architecture)
6. Results
6.1 Description of qualitative essay data set
6.2 co-relation based attribute selection
6.3 Machine learning algorithms 
a) True positive (TP): The actual negative class outcome is predicted as negative class from
the model
b) False positive (FP): The actual negative class outcome is predicted as a positive class
outcome. It leads to Type-1 error
c) False negative (FN): The actual positive class outcome is predicted as negative class from
the model. It leads to Type-2 error
d) True negative (TN): The actual class outcome excluded is also predicted to be excluded
from the model
Based on these four parameters the performance of algorithms can be adjudged by calculating the
following ratios.
TP FP TN FN
TP TN
Accuracy
+ + +
+
(%) =
TP FN
TP
TPR
+
(%) =
FP TN
FP
FPR
+
(%) =
TP FP

Accuracy table for multiple algorithms

ROC curve
<Insert comparision between the differnt algorithms used for AES)
6.4 Developing the essay scoring program system as a package
7. Conclusions
8.CODE and screen shots
9.References
