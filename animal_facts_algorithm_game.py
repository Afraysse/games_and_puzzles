""" Animal knowledge tree. 

Interacts with user to dynamically create a tree of questions and animal names.

- Asks questions until the program makes a guess. 
- If True, prints 'I rule!'
- If False, it inquires the name of actual (correct) animal and a 
question to distinguish the actual answer from the old (incorrect) guess
- Adds new node with animal and new quesiton to the tree 

"""
class Tree:

    def __init__(self, data, left=None, right=None):
        """ Instantiate attributes of new tree."""
        self.data = data 
        self.left = left
        self.right = right 

    def __str__(self):
        """ Prints string rep of data."""
        return str(self.data)

def yes(question):
    """ Helper function. """
    answer = input(question).lower()
    return answer[0] == "y"

def animal_tree():
    """ Builds a tree and adds a node each time a guess is made incorrectly."""
    # start with singleton tree 
    root = Tree("bird")

    # loop until quits 
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # walk tree nodes 
        tree = root 
        while tree.left is not None:
            prompt = tree.data + "?"
            if yes(prompt):
                tree = tree.right 
            else:
                tree = tree.left 

        # computer makes a guess 
        guess = tree.data 
        prompt = "Is it a " + guess + "?"
        if yes(prompt):
            print "I win!"
            continue 

        # gather new information 
        prompt = "What is the animal called? "
        animal = input(prompt)
        prompt = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # add new information to tree 
        tree.data = question 
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)











