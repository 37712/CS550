"""
Machine learning
decision trees
"""
import time


from ml_lib.ml_util import DataSet

from decision_tree import  DecisionTreeLearner

from ml_lib.crossval import cross_validation

from statistics import mean, stdev
    
"""
classify mushroom and zoo data set
use crossval.py to conduct two 10-fold cross-validation decision tree experiments
one without prunning and one with prunning, p-value = 0.05
restaurant, and tiny_animal_set are good for debugging

driver.py should print the mean error and standard deviation of the
zoo and mushroom datasets using both unpruned and pruned decision trees
In addition, you should print out one unpruned decision tree and one pruned decision
tree for each class. Call method chi_annotate on the tree before you print it so
that you can see the 𝜒^2 statistic for each decision node.
"""

    
def main():
    """
    Machine learning with decision trees.
    Runs cross validation on data sets and reports results/trees
    """
    raise NotImplementedError

if __name__ == '__main__':
    main()