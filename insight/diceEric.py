#n=One die: 6 loops is (6+0) choose n = 6
#n=Two dice: 6+5+4+3+2+1 = 21 loops is (6+1) choose n = 7C2 = 21
#n=Three dice: 21+15+10+6+3+1 = 56 loops is (6+2) choose n = 8C3 = 56
#n=Four dice: 56+35+20+10+4+1 = 126
# In general for n dice the count is (n+5) choose n = (n+5)!/5!/n!
# = (n+5)(n+4)(n+3)(n+2)(n+1)/5!

def brian_probs(prob):
    N = len(prob)
    allrolls = {}
    if N == 0:
        return allrolls

    for i in range(6):
        allrolls[str(i+1)] = prob[0][i]

    for i in range(1,N):
        newallrolls = allrolls.copy()
        for k in allrolls:
            for j in range(6):
                newallrolls[k+str(j+1)] = allrolls[k]*prob[i][j]
        allrolls = newallrolls

    for k in sorted(allrolls.items()):
        print k

    return allrolls

def dec_to_sex(n):
    """Convert a decimal integer to a six-element base six integer list.
    
    Arguments:
    n -- base 10 integer

    Example:
    dec_to_sex(1) = [0,0,0,0,0,1]
    dec_to_sex(6) = [0,0,0,0,1,0]
    dec_to_sex(36) = [0,0,0,1,0,0]
    dec_to_sex(121) = [0,0,0,3,2,1]
    """

    out = []
    place = 1;

    while n:
        val = n % 6 #(6**place)
        n /= 6 #(6**place) #val
        out.insert(0,val)
        place += 1

    return [0]*(6-len(out)) + out

def nan_probs(prob):
    """Nan's method: Print probability for each possible comb. of dice rolls.
    
    Arguments:
    prob -- List of n lists of 6 elements. prob[i][d-1] is the probability that
        die i rolls value d (d = 1 to 6)
        
    Example:
    print_probs([[.3, .25, .2, .1, .1, .05]])
    # prints:
    #   P([1]) = 0.3
    #   P([2]) = 0.25
    #   P([3]) = 0.2
    #   P([4]) = 0.1
    #   P([5]) = 0.1
    #   P([6]) = 0.05
    
    """
    n = len(prob)

    # there are 6^n possible rolls
    for i in range(6**n):
        inds = dec_to_sex(i)
        inds = inds[::-1]
        
        p = 1
        for die in range(n):
            p *= prob[die][inds[die]]

        print "P(", inds, ") = ", p

def print_probs(prob):
    """Print probability for each possible combination of dice rolls.
    
    Arguments:
    prob -- List of n lists of 6 elements. prob[i][d-1] is the probability that
        die i rolls value d (d = 1 to 6)
        
    Example:
    print_probs([[.3, .25, .2, .1, .1, .05]])
    # prints:
    #   P([1]) = 0.3
    #   P([2]) = 0.25
    #   P([3]) = 0.2
    #   P([4]) = 0.1
    #   P([5]) = 0.1
    #   P([6]) = 0.05
    """

    n = len(prob)
    inds = [1]*n;

    count = 0;

    # this loop runs until all reach their maximum value of 6,
    #   when the sum becomes 6*n.
    while sum(inds) <= 6*n:
        count += 1
        p = 1;
        for die in range(n):
            p *= prob[die][inds[die]-1]

        print "P(",inds,") = ",p

#        inds = increment_dice(inds)
        inds = increment_dice_nondecreasing(inds)

        # if inds is False, we have exhausted all dice combinations
        if not inds:
            print "Counted", count, "total for n =", n, "."
            return


def increment_dice(inds):
    """Increment the face value of a list of dice.
    
    Arguments:
    inds -- List of n integers 1 to 6.
    
    increment_dice increases the face value of the right-most die, resetting
    it to 1 if it exceeds 6 and rolling over the next die to the left.
    
    Returns false if trying to increment a list of all dice at their maximum
    values.
    
    Examples:
    increment_dice([1 1 1]) returns [1 1 2]
    increment_dice([1 1 6]) returns [1 2 1]
    increment_dice([1 6 6]) returns [2 1 1]
    increment_dice([6 6 6]) returns False
    
    """

    incrementDie = len(inds)-1

    while True:
        inds[incrementDie] += 1
        
        if incrementDie==0 and inds[incrementDie] > 6:
            # the left-most die rolled over: we're done here
            return False
        if inds[incrementDie] > 6:
            # incrementDie rolled over, reset this one and move one die left
            inds[incrementDie] = 1
            incrementDie-=1
        else:
            # we incremented one die. it didn't roll over. we're done.
            break

    return inds


def increment_dice_nondecreasing(inds):
    """Increment the values of a list of dice so the values are nondecreasing.
    
    Arguments:
    inds -- List of n integers 1 to 6.
    
    increment_dice increases the face value of the right-most die, resetting
    it to 1+the next die to the left if it exceeds 6, and rolling over the
    next die to the left.
    
    Returns false if trying to increment a list of all dice at their maximum
    values.
    
    Examples:
    increment_dice_nondecreasing([1 1 1]) returns [1 1 2]
    increment_dice_nondecreasing([1 1 6]) returns [1 2 2]
    increment_dice_nondecreasing([1 6 6]) returns [2 2 2]
    increment_dice_nondecreasing([6 6 6]) returns False
    
    """

    incrementDie = len(inds)-1

    while True:
        inds[incrementDie] += 1
        
        if incrementDie==0 and inds[incrementDie] > 6:
            # the left-most die rolled over: we're done here
            return False
        if inds[incrementDie] > 6:
            # incrementDie rolled over, reset this one and move one die left
            inds[incrementDie] = 1 #+inds[incrementDie-1]
            incrementDie-=1
        else:
            # we incremented one die. it didn't roll over. we're done.
            break

    # all dice to the right of the left-most die that rolled over are set to
    # the value of that left-most die. so the above would go from
    # [1, 6, 6] to [2, 1, 1] then this changes it to [2, 2, 2]
    for ind in range(incrementDie,len(inds)):
        inds[ind] = inds[incrementDie]

    return inds


def main():
    print "One die:"
    brian_probs([[.3, .25, .2, .1, .1, .05]])
    
    print "Two dice:"
    brian_probs([[.3, .25, .2, .1, .1, .05],
                 [.166, .166, .166, .166, .166, .166]])

    print "One die:"
    nan_probs([[.3, .25, .2, .1, .1, .05]])
    
    print "Two dice:"
    nan_probs([[.3, .25, .2, .1, .1, .05],
                 [.166, .166, .166, .166, .166, .166]])

def mainx():
    print "One die:"
    print_probs([[.3, .25, .2, .1, .1, .05]])
    
    print "Two dice:"
    print_probs([[.3, .25, .2, .1, .1, .05],
                 [.166, .166, .166, .166, .166, .166]])

    print "Three dice:"
    print_probs([[.3, .25, .2, .1, .1, .05],
                 [.166, .166, .166, .166, .166, .166],
                 [.166, .166, .166, .166, .166, .166]])

    print "Six dice:"
    print_probs([[.3, .25, .2, .1, .1, .05],
                 [.166, .166, .166, .166, .166, .166],
                 [.166, .166, .166, .166, .166, .166],
                 [.166, .166, .166, .166, .166, .166],
                 [.166, .166, .166, .166, .166, .166],
                 [.166, .166, .166, .166, .166, .166]])


if __name__ == '__main__':
    main()