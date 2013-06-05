#!/usr/bin/python
"""
causes.py v2.0
Author: Brian J. Boates
Date: Feb. 9, 2012

Compute the size of the social network of causes.
Will work for any word in principle.
"""

def levenshtein_of_1(word1,word2):
    """
    word1: a single word as a string
    word2: a single word as a string

    Return: True/False if the Levenshtein distance between words is/isn't 1
    """
    # tmp will be a list of all possible Levenshtein distances of
    # 1 from word1 to be compared with word2
    list1, list2 = [], []

    # Skip if wor1 == word2 (L distance of 0)
    if word1 == word2:
        pass

    # Skip comparisons of words that differ by 2 or more letters
    elif abs( len(word1) - len(word2) ) >= 2:
        pass

    # If word1 and word2 have same length
    elif len(word1) == len(word2):
        # if only one different letter, L1 by substitution
        if [word1[i] == word2[i] for i in range(len(word1))].count(False) == 1:
            list2.append(word2)

    ### can also add other simple checks for speed in the future ###

    else:

        ### append all deletion word1 words ###
        # loop over letter in word1
        for i in range(len(word1)):
            list2.append( word1[:i] + word1[i+1:] )    

        ### append all deletion word2 words ###
        # (faster than substituting alphabet into word1)
        # loop over letter in word2 
        for i in range(len(word2)):
            list1.append( word2[:i] + word2[i+1:] )    

    # Check for matches between word2 with list2 items
    # and word1 with list1 items
    if word2 in list2 or word1 in list1:
        return True
    else:
        return False


def friends_list(word,words):
    """
    word = a single word as a string
    words = a list of words, each as a string

    a friend is defined as a word with a Levenshtein distance of 1

    Return: a list of friends
    """
    # Create list to append L1 words to
    friends = []
    
    # Loop over all words in words list:
    for w in words:
        # Determine if word and w are L1
        if levenshtein_of_1(word,w):
            friends.append(w)

    return friends


def scan_network(network,words,keys0=['']):
    """
    network = dictionary of words and their friends lists
    words = list for words, each as a string

    this is a recursive function and calls itself until
    the network has been exhausted

    Return: completed network dictionary
    """
#    print len(network.keys())
    
    # Set new_keys as False initially
    new_keys = False
    
    # A list of words that are already in the network (except those already checked)
    keys = [k for k in network.keys() if k not in keys0]

    # Loop over "not-checked" words in the network
    for k in keys:

#        print k

        # Loop over all of k's friends
        for f in network[k]:

            # Make sure f is not already in network dict.
            if f not in network.keys():

                # Create new key for f with a value of its friends list
                network[f] = friends_list(f,words)

                new_keys = True
#                print len(network.keys()),len(network[f])

    # Perform scan until no more new keys (friends) are found
    if new_keys:
        network = scan_network(network,words,keys)

    return network
    

def main():

    # make sure word.list file is present
    try:
        f = open('word.list','r')
        words = f.readlines()
        f.close()
    except:
        print '\n Make sure word.list file is present\n'
        sys.exit(1)

    # Strip whitespace off of words in words list
    for i in range(len(words)):
        words[i] = words[i].strip()

    # friends is a special list of only 'causes' friends (L1 distance)
    friends = friends_list('causes',words)
    
    # initialize an overall network dictionary which will conatin all
    # words in 'causes' network and their respective friends list
    network = { 'causes': friends }

    # Complete the network through a recursive scan
    network = scan_network(network,words)

    print
    print '"causes" has '+str(len(network['causes']))+' friends'
    print
    print 'The size of the social network for the word'
    print '"causes" (not including itself) is ', len(network.keys())-1
    print


if __name__ == '__main__':
    main()
