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
    mushroom = DataSet(name="mushrooms")
    print(mushroom)

    # print out the line 1 and 2 of actual .csv file
    #print(mushroom.examples[0])
    #print(mushroom.examples[1])

    # number of attributes
    print("attributes =",mushroom.attrs)

    # determines the target attribute 
    # according to professor, the target attribute is the one that is eliminated
    # and the others are the ones we want to be making questions on
    print("mushroom.target =",mushroom.target)

    # to specify target, 0 = edible
    mushroom = DataSet(name="mushrooms", target=0)
    print("mushroom new target")
    print("mushroom.target =",mushroom.target)

    # attr_names=True, takes the first line and interprets it as lavels
    # instead part of the dataset
    mushroom = DataSet(name="mushrooms", target=0, attr_names=True)
    print("mushroom.target =",mushroom.target)
    print("mushroom.attr_names =",mushroom.attr_names)

    # get all posible values for specific atribute
    # example attribute 0 should only have edible=e, poisonous=p
    print("values for edible",mushroom.values[0])






if __name__ == '__main__':
    main()