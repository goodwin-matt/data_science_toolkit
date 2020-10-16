# Data Science Toolkit Creation Guide

### Goal
My goal is to be able to understand and explain chosen topics from a high-level overview AND from a detailed view. I want to be able to know each topic well enough that I feel completely confident and comfortable talking about it in meetings or interviews and really know what is going on under the hood. I do not expect myself to be an expert on these topics and to have read in-depth papers on them, but hope to get there over time for some subjects after I feel I have established a firm base.

The goal is also to become an expert in one or two areas but have a broad overview of different data science topics. In other words have a T shaped skills distribution. This is overwhelming at times because there is so much to focus on or learn, but it is important to stay current and keep my basic skills current since this will keep doors open. The hard part is figuring out where to go deep on. 

### Plan of Action
1. Read and take notes on what I feel are the essential topics of data science (found below)
2. Get code stack together of these topics where applicable
3. Get an empty room and practice teaching these topics. Refine my elevator pitch and uncover areas that need working on.
4. Write up Anki cards
5. Repeat 1-4 until satisfied with knowledge
6. Post notes and code on website
7. Start diving deeper into topics or on the fringes


### Essential topics to focus on first
* Theory of learning
    * Talk about the layers of knowledge we have. 
        * The first layer is the complete truth, the deterministic relationship (which we won’t have)
        * The next layer is this probabilistic viewpoint where we acknowledge our uncertainty. This is almost like a model in and of itself. We won’t be able to know this distribution perfectly though because we only work with finite data. The more data you have the more likely we are approaching our true distribution and Bayes classifier
        * The next layer above this is a model that might either attempt to approach the distribution (generative), the conditional posterior (discriminative) or just a good old function (discriminative function) with the given data. 
        * Talk about the transfer learning issue. One are this occurs in is when we our training data comes from a different distribution than the test data. This is a problem because our model is trying to approximate the true distribution using that training data but if our test data comes from a completely different distribution then we are going to be off.
    * Theoretical optimization, etc. X  
    * Bias vs. Variance tradeoff X
    * Curse of dimensionality  x
        * Hughes phenomenon
    * No free lunch theorem x
    * Restricted estimators (Chapter 1 of Elements) x
* Model evaluation
    * Cross-validation and training topics (Chapter 7 of Elements)
    * Metrics
        * AUC
        * Precision/Recall
        * F-Score
        * Confusion matrix
        * R^2
        * Gini index
        * Cross validation metrics
        * Matrix of true positives, etc.
        * Cross entropy
    * Overfitting and underfitting
    * Bootstrapping
        * Along with this talk about visualizing uncertainty
    * Optimizing hyperparameters
* Supervised Models
    * Decision Trees 
    * GLM’s (Linear regression (difference between approaches), Logistic regression X, Poisson regression)
    * Ridge vs. lasso regression vs. Elastic net
    * Naive Bayes
    * k-Nearest neighbor
    * Neural networks
* Unsupervised Learning
    * PCA
    * tSNE
* Ensembles
    * Bagging 
    * Boosting 
    * Random Forrest
* Statistics
    * Bootstrapping (how does this relate to Bayesian statistics)
    * Random variable - basic probability definitions, go over Casella/Berger hw, create a probability cheat sheet
    * Different significance tests
* General
    * Logistic scale
    * Optimization algorithms in general (global vs. local, constraints, gradient descent)
    * Occam’s Razor

Everything in Scikit learn package 

### Things that would be nice:
Support vector machines
Look at how the impact of nearest neighbors is impacted as we increase dimensionality
Clustering metrics
Hierarchical clustering
k-means clustering
Common loss functions
VC Dimension and other theoretical underpinnings
Bayesian regression
PU learning (semi-supervised learning)
Transfer Learning
Reinforcement learning
Hidden Markov models
Mixture models (Gaussian mixture models)
Discriminant analysis
Factor analysis
Latent Dirichlet Allocation - X
Gaussian Process
Dirichlet Process
NLP - X
Singular value decomposition (whats the relation to PCA)
Simulated annealing
What is the training-set-size bias?
Power analysis
Bayesian models/Hierarchical models 
MLE
Permutation testing/Simulation testing
Central limit theorem
Law of large numbers - stuff from Dahls website
p-value and understand how to explain between Bayesian approach and frequentist approach (also look at that Berger homework Reese sent)
Parametric vs. Non-parametric
Rejection and importance sampling
EM algorithm
Look up Tuftes visualization book
GPU’s vs. CPU’s

* Technology
    * TensorFlow
    * Hadoop
    * Spark
    * What do the arguments mean in spark and hadoop

    * Parallel processing
        * dask , ipyparallel , joblib , numba
    * Internet connectivity

Neural networks/Deep learning
* Stanfords CS231 CNN course good source
* Krishevsky et al 2012 AlexNet first paper to really prove Neural nets were the bomb
* Andrew NG https://youtu.be/F1ka6a13S9I?t=1301
    * Large neural nets kick butt at scale, this is why we see more of them
    * He classifies DL into four categories
        * General DL (densley connected layers)
        * Sequence models
            * 1d sequences (Recurrent Neural Networks, GRU gated recurrent unit)
        * Image models
            * 2d and 3d (CNNs)
        * Other
            * Supervised learning Reinforcement learning
    * He thinks that the first three are driving industry and that last category is future AI research
    * The other trend he sees is end-to-end DL meaning outputting stuff more than numbers

    * Training error high? Try training longer, bigger model (this is implying you have high bias because you can’t even do well on data you’ve seen), keep doing that until you get low training error
        * Now ask if Dev error high, (if yes then you have high variance or have overfit so get more data, regularization or new model archecture)
        * Keep reforming till error goes down
    * Really the difference between deep learning and other models is that with deep learning we can just train it deeper and more data to get ourselved out of the pickle whereas before we had to use techniques such as regularization etc. Deep learning you can tune the model which is valuable but just making it deeper or more data can get you out of the issue
    * Think of it as two different spaces, the small data space and the large data space. In large data space deep learning wins.
    * People are talking less about Bias/Variance tradeoff because in the era of deep learning the connection between those two in the tradeoff is weaker (we can just train a bigger model vs. adding more features as we did in the logistic regression days)
    * Data synsthesis (enhancing our training set)
    * Make sure validation and test set are from same distribution



### Blogs to pay attention to

https://blog.udacity.com/2018/01/top-5-data-science-publications.html
https://community.modeanalytics.com/analytics-dispatch/archive/
https://dataelixir.com
https://www.oreilly.com/topics/data
https://www.datascienceweekly.org
https://www.analyticsvidhya.com
No Free Hunch
538


### Textbooks that have really helped
- Spark: the definitive guide. (By Chambers and Zaharia)
- Learning Spark (O'Reilly)
- Pattern Recognition and Machine Learning (By Chris Bishop)
- The Elements of Statistical Learning (Hastie, Tibshirani, Friedman)
- Weathermax solution manual to ESLII

### Papers to keep in mind
50 years of data science: Donoho
Deep Learning Review: LeCun, Bengio, Hinton
Statistical Modeling - Two Cultures: Breiman
Bayesian Estimation Supersedes the t Test: Kruschke
Why Should I Trust You? Explaining the Predictions of Any Classifier
The Central Role of the Propensity Score in Observational Studies for Causal Effects
On Discriminative and Generative classifiers - A comparison of logistic regression and naive Bayes
Performance Evaluation in Machine Learning - The Good, The Bad, The Ugly and The Way Forward
Probability Cheatsheet compiled by William chen
Sample Size and Power Calculations: Gelman
The Secrests of Machine Learning: Ten Things You Wish You Had Known Earlier to be More Effective at Data Analysis


### Web Links to keep track of

