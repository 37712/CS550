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

from collections import namedtuple

import numpy as np
import scipy.stats

from ml_lib.ml_util import argmax_random_tie, normalize, remove_all, best_index
from ml_lib.decision_tree_support import DecisionLeaf, DecisionFork


class DecisionTreeLearner:
    """DecisionTreeLearner - Class to learn decision trees and predict classes
    on novel exmaples
    """

    # Typedef for method chi2test result value (see chi2test for details)
    chi2_result = namedtuple("chi2_result", ('value', 'similar'))

    def __init__(self, dataset, debug=False, p_value=None):
        """
        DecisionTreeLearner(dataset)
        dataset is an instance of ml_lib.ml_util.DataSet.
        """

        # Hints: Be sure to read and understand the DataSet class
        # as you will use it throughout.

        # ---------------------------------------------------------------
        # Do not modify these lines, the unit tests will expect these fields
        # to be populated correctly.
        self.dataset = dataset

        # degrees of freedom for Chi^2 tests is number of categories minus 1
        self.dof = len(self.dataset.values[self.dataset.target]) - 1

        # Learn the decison tree
        self.tree = self.decision_tree_learning(dataset.examples, dataset.inputs)
        # -----------------------------------------------------------------

        self.debug = debug

    def __str__(self):
        "str - Create a string representation of the tree"
        if self.tree is None:
            result = "untrained decision tree"
        else:
            result = str(self.tree)  # string representation of tree
        return result

    def decision_tree_learning(self, examples, attrs, parent=None, parent_examples=()):
        """
        decision_tree_learning(examples, attrs, parent_examples)
        Recursively learn a decision tree
        examples - Set of examples (see DataSet for format)
        attrs - List of attribute indices that are available for decisions
        parent - When called recursively, this is the parent of any node that
           we create.
        parent_examples - When not invoked as root, these are the examples
           of the prior level.
        """

        # Hints:  See pseudocode from class and leverage classes
        # DecisionFork and DecisionLeaf

        # If there are no examples
        if len(examples) == 0: 
            return DecisionLeaf(self.plurality_value(parent_examples), self.count_targets(parent_examples), parent=parent)
        # If all examples are in the same class
        elif self.all_same_class(examples):
            return DecisionLeaf(examples[0][self.dataset.target], self.count_targets(examples), parent=parent)
        # If there are no remaining attributes
        elif len(attrs) == 0:
            return DecisionLeaf(self.plurality_value(examples), self.count_targets(examples), parent=parent)
        else:
            a = self.choose_attribute(attrs, examples) #Returns the index with the highest information gain
            attribute = attrs[a] #Gives the value of the attribute with the highest importance
            xtree = DecisionFork(attribute, self.count_targets(examples), attr_name=attrs[a])
            split = self.split_by(attribute,examples)
            attrs.pop(a) # remove attribute a from attrs list
            for v in split:
                subtree = self.decision_tree_learning(v[1], attrs, parent_examples=examples)
                xtree.add(v[0], subtree)
            
            return xtree
            
    def plurality_value(self, examples):
        """
        Return the most popular target value for this set of examples.
        (If target is binary, this is the majority; otherwise plurality).
        """
        popular = argmax_random_tie(self.dataset.values[self.dataset.target],
                                    key=lambda v: self.count(self.dataset.target, v, examples))
        return popular

    def count(self, attr, val, examples): # val = the string of actual class?
        """Count the number of examples that have example[attr] = val."""
        return sum(e[attr] == val for e in examples)

    def count_targets(self, examples):
        """count_targets: Given a set of examples, count the number of examples
        belonging to each target.  Returns list of counts in the same order
        as the DataSet values associated with the target
        (self.dataset.values[self.dataset.target])
        """

        tidx = self.dataset.target # index of target attribute
        target_values = self.dataset.values[tidx]  # Class labels across dataset

        # Count the examples associated with each target
        counts = [0 for i in target_values]
        for e in examples:
            target = e[tidx]
            position = target_values.index(target)
            counts[position] += 1
        
        return counts

    def all_same_class(self, examples):
        """Are all these examples in the same target class?"""
        class0 = examples[0][self.dataset.target]
        return all(e[self.dataset.target] == class0 for e in examples)

    def choose_attribute(self, attrs, examples):
        """Choose the attribute with the highest information gain."""
        gain_value = -1
        for attr in attrs:
            tmp_value = self.information_gain(attr, examples)
            # If new information gain is better, store the new one
            if gain_value < tmp_value:
                gain_value = tmp_value
                attribute = attr

        # Returns the attribute index
        return attrs.index(attribute)

    def information_gain(self, attr, examples): # the quality of a split
        """Return the expected reduction in entropy for examples from splitting by attr."""
        
        arr = self.split_by(attr, examples) #Splits by flying

        #Calculating the totals per subgroup:
        subTotals = []
        totalElems = 0
        for subgroup in arr:
            subTotals.append(len(subgroup[1]))
            totalElems = totalElems + len(subgroup[1])
        subTotals[:] = [x / totalElems for x in subTotals]
        
        #Calculating the original entropy:
        originalEntropy = self.information_per_class(examples)

        # Calculate the remainder:
        remainder = 0
        for i, group in enumerate(arr):
            entropy = self.information_per_class(group[1])
            remainder = remainder + (entropy * subTotals[i])

        informationGain = originalEntropy - remainder

        return informationGain

    def split_by(self, attr, examples):
        """split_by(attr, examples)
        Return a list of (val, examples) pairs for each val of attr.
        """
        return [(v, [e for e in examples if e[attr] == v]) for v in self.dataset.values[attr]]

    def predict(self, x):
        "predict - Determine the class, returns class index"
        return self.tree(x)  # Evaluate the tree on example x

    def __repr__(self):
        return repr(self.tree)

    @classmethod
    def information_content(cls, class_counts):
        # new commnet from professor
        """info = information_content(class_counts)
        Given an iterable of counts associated with classes
        compute the empirical entropy.

        Example: 3 class problem where we have 3 examples of class 0,
        2 examples of class 1, and 0 examples of class 2:
        information_content((3, 2, 0)) returns ~ .971

        Hint: Ignore zero counts; function normalize may be helpful
        """

        # Hint: remember discrete values use log2 when computing probability
        y = []
        for x in class_counts:
            if(x > 0):
                y.append(x / sum(class_counts))
        
        return scipy.stats.entropy(y, base=2)

    def information_per_class(self, examples):
        """information_per_class(examples)
        Given a set of examples, use the target attribute of the dataset
        to determine the information associated with each target class
        Returns information content per class.
        """
        # Hint:  list of classes can be obtained from
        # self.dataset.values[self.dataset.target]

        target_split = self.split_by(self.dataset.target, examples) #Splits by target, which is class (mammal/bird)
        return_group = []
        for subgroup in target_split:
            return_group.append(len(subgroup[1]))

        return self.information_content(return_group) # return [5, 6] when target class is mammal/bird

    def prune(self, p_value):
        """Prune leaves of a tree when the hypothesis that the distribution
        in the leaves is not the same as in the parents as measured by
        a chi-squared test with a significance of the specified p-value.

        Pruning is only applied to the last DecisionFork in a tree.
        If that fork is merged (DecisionFork and child leaves (DecisionLeaf),
        the DecisionFork is replaced with a DecisionLeaf.  If a parent of
        and DecisionFork only contains DecisionLeaf children, after
        pruning, it is examined for pruning as well.
        """

        # Hint - Easiest to do with a recursive auxiliary function, that takes
        # a parent argument, but you are free to implement as you see fit.
        # e.g. self.prune_aux(p_value, self.tree, None)
        if isinstance(self.tree, DecisionFork):
            for branch in self.tree.branches.values():     
                if isinstance(branch, DecisionFork):
                    self.prune_aux(p_value, branch)

    # will go through all children of decision fork and assing chi2 test value
    def prune_aux(self, p_value, branch):

        # if decision leaf, no pruning needed, so return false
        if isinstance(branch, DecisionLeaf):
            return False

        # if it is a decision fork
        else:
            # Search through the children of the DecisionFork
            for key in branch.branches:
                # if the decision fork needs to be pruned
                if self.prune_aux(p_value, branch.branches[key]): 
                    # Get the distribution and result from the DecisionFork to create DecisionLeaf
                    dist = branch.branches[key].distribution
                    examples = self.get_examples(branch.branches[key].distribution)
                    result = self.plurality_value(examples)
                    # Replace DecisionFork with DecisionLeaf
                    branch.branches[key] = DecisionLeaf(result, dist, None)

            #Calculate Chi2 value for DecisionFork
            branch.chi2 = self.chi2test(p_value, branch)
            #Return true if DecisionFork needs to be pruned
            return branch.chi2.similar
    
    # Helper method that gets examples based on a given distribution
    def get_examples(self, distribution):
        examples = []
        for i in range(len(distribution)):
            # If the class is included, append it to examples
            if distribution[i]:
                examples.append(self.dataset.examples[i]) 
        return examples
            

    def chi_annotate(self, p_value):
        """chi_annotate(p_value)
        Annotate each DecisionFork with the tuple returned by chi2test
        in attribute chi2.  When present, these values will be printed along
        with the tree.  Calling this on an unpruned tree can significantly aid
        with developing pruning routines and verifying that the chi^2 statistic
        is being correctly computed.
        """
        # Call recursive helper function
        self.__chi_annotate_aux(self.tree, p_value)

    def __chi_annotate_aux(self, branch, p_value):
        """chi_annotate(branch, p_value)
        Add the chi squared value to a DecisionFork.  This is only used
        for debugging.  The decision tree helper functions will look for a
        chi2 attribute.  If there is one, they will display chi-squared
        test information when the tree is printed.
        """

        if isinstance(branch, DecisionLeaf):
            return  # base case
        else:
            # Compute chi^2 value of this branch
            branch.chi2 = self.chi2test(p_value, branch)
            # Check its children
            for child in branch.branches.values():
                self.__chi_annotate_aux(child, p_value)

    def chi2test(self, p_value, fork):
        """chi2test - Helper function for prune
        Given a DecisionFork and a p_value, determine if the children
        of the decision have significantly different distributions than
        the parent.

        Returns named tuple of type chi2result:
        chi2result.value - Chi^2 statistic
        chi2result.similar - True if the distribution in the children of the
           specified fork are similar to the the distribution before the
           question is asked.  False indicates that they are not similar and
           that there is a significant difference between the fork and its
           children
        """

        if not isinstance(fork, DecisionFork):
            raise ValueError("fork is not a DecisionFork")

        # Hint:  You need to extend the 2 case chi^2 test that we covered
        # in class to an n-case chi^2 test.  This part is straight forward.
        # Whereas in class we had positive and negative samples, now there
        # are more than two, but they are all handled similarly.

        # Don't forget, scipy has an inverse cdf for chi^2
        # scipy.stats.chi2.ppf

        value = 0
        for p in fork.branches.values():
            for n in range(len(fork.distribution)):

                # calculate p-hat
                p_hat = fork.distribution[n] * (sum(p.distribution)/sum(fork.distribution))
                
                if p_hat != 0:
                    value += ((p.distribution[n] - p_hat) **2)/ p_hat

        # tuple type result to return
        chi2result = namedtuple("chi2result", ["value", "similar"])
        change = scipy.stats.chi2.ppf(1 - p_value, self.dof)
        
        similar = True
        if value >= change:
            similar = False
        
        return chi2result(value, similar)
