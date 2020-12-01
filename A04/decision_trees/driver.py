"""
We the undersigned promise that we have in good faith attempted to follow the
principles of pair programming. Although we were free to discuss ideas with
others, the implementation is our own. We have shared a common workspace and
taken turns at the keyboard for the majority of the work that we are submitting.
Furthermore, any non programming portions of the assignment were done
independently. We recognize that should this not be the case, we will be
subject to penalties as outlined in the course syllabus.

Pair Programmer 1: Jason Kramer, 11/30/20
Pair Programmer 2: Carlos Gamino Reyes, 11/30/20
"""

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
    mushroom_data = DataSet(name="mushrooms", target=0, attr_names=True)
    mushroom_tree = DecisionTreeLearner(mushroom_data, p_value=0.05)
    mushroom_result = cross_validation(DecisionTreeLearner, mushroom_data)

    zoo_data = DataSet(name="zoo", target=17, exclude = [0], attr_names=True)
    zoo_tree = DecisionTreeLearner(zoo_data, p_value=0.05)
    zoo_result = cross_validation(DecisionTreeLearner, zoo_data)

    mushroom_error = mushroom_result[0]
    mushroom_model = mushroom_result[1]

    zoo_error = zoo_result[0]
    zoo_model = zoo_result[1]

    #Standard Deviations and Means:
    print("Mushroom Mean Error: ", mean(mushroom_error))
    print("Mushroom Stdev Error: ", stdev(mushroom_error))
    print("Zoo Mean Error: ", mean(zoo_error))
    print("Zoo Stdev Error: ", stdev(mushroom_error))

    #Example of Zoo Decision Tree
    zoo = DataSet(name="zoo", target=17, exclude = [0], attr_names=True)
    learner = DecisionTreeLearner(zoo, p_value=0.05)
    learner.chi_annotate(.05)
    print("\nZoo Tree Before Pruning:", learner.tree)
    learner.prune(0.05)
    print("\nZoo Tree After Pruning:", learner.tree)


    #Example of Mushroom Decision Tree
    mushrooms = DataSet(name="mushrooms", target=3, attr_names=True)
    learner = DecisionTreeLearner(mushrooms, p_value=0.05)
    learner.chi_annotate(.05)
    print("\nMushroom Tree Before Pruning:", learner.tree)
    learner.prune(0.05)
    print("\nMushroom Tree After Pruning:", learner.tree)


if __name__ == '__main__':
    main()