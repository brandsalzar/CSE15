# Exercise 1: Implement Euclid's Algorithm for finding the greatest common divi-
# sor of two integers
def gcd(a, b):
    # Provide the correct implementation
    if (a % b) == 0:
        a, b = b,a%b
        return a
    else:
        return gcd(b, (a % b))

print gcd(128, 60)
# Expected output: 4

# Exercise 2: Consider the following representation of mathematical expressions:
# a list of tuples, where each tuple has exactly 2 elements, a coefficient and a
# term. For example, the expression:

# 2x + 5y - 3z is represented as [(2, x), (5, y), (-3, z)]

# We sometimes need to simplify expressions by grouping together like terms. For example:

# 2x + 5y + 4x = 6x + 5y

# Implement the function groupLikeTerms, where the input exp is a mathematical
# expression represented as a list of tuples, and it should return a simplified
# mathematical expression represented as a list of tuples.
def groupLikeTerms(exp):
    # Provide the correct implementation
    likeSet = []
    for i in range(len(exp)):
        for j in range(2):
            if(exp[i][1] != exp[j+1][1] and exp[i][0] == exp[j+1][0]):
                likeSet.append(exp[1])
            elif(exp[i][1] == exp[j+1][1] and exp[i][0] != exp[j+1][0]):
                add = exp[i][0] + exp[j+1][0]
                vari = exp[i][1]
                tuple = (add, vari)
                likeSet.append(tuple)
            else:
                break
    return likeSet

print groupLikeTerms([(5, "x"), (5, "y"), (-3, "x")])
# Expected output: [(2, 'x'), (5, 'y')]

# Exercise 3: We sometimes need to substitute expressions into other expressions.
#For example if we have the expression 2x + 5y, and we know that x = 3a - b, we
#can substitute the expression for x into the original expression, resulting in:
# 6a - 2b + 5y.

# Implement the substitution function below. It should take an expression (list
#of tuples), a term, and another expression. It should substitute the occurences
#of term in exp, with value. The result should be in its simplest form, i.e.
#like terms should be grouped together

# For example: substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)]) results in
#[(-5, 9), (2, 23)]
def substitute(exp, term, value):
    # Provide the correct implementation
    subSet = []
    #for i in range(len(exp)):
    for j in range(len(exp)): #1
        if(term == exp[j][1]):
            mulTuple = exp[j][0] * value[j][0]
            mulTuple2= exp[j][0] * value[j+1][0]
            tuple  = [(exp[j][0], value)]
            tuple2 = [(mulTuple,value[j][1]),(mulTuple2,value[j+1][1]), exp[j+1]]
            tuple3 = groupLikeTerms(tuple2)
            subSet.append(tuple3[j])
            subSet.append(tuple2[j])

    return subSet

print substitute([(2, 5), (-1, 9)], 5, [(1, 23), (-2, 9)])
# Expected output: [(-5, 9), (2, 23)]

# Exercise 4: Using the functions you implemented above, implement the Extended
#Euclidean Algorithm, which returns the GCD of two integers a, and b, as a linear
#combination of a and b.

# For example: extended_euclid(101, 23) results in (1, [(22, 23), (-5, 101)]),
#where the GCD is 1 and it can be expressed as 22*23 - 5*101
def extended_euclid(a, b):
    # Provide the correct implementation
    g = gcd(a,b)
    if a%b == g:
        return substitute(extended_euclid((a%b,[(1,a),(-(a/b),b)])))
    return(g,[(b-1,b),(-((a/b)+1),a)])

print extended_euclid(101, 23)
# Expected output: (1, [(22, 23), (-5, 101)])

# Exercise 5: Use the Extended Euclidean Algorithm to implement the function for
# multiplicative inverses. As you know, a multiplicative inverse n modulo m is
#guaranteed to exist if n and m are relatively prime. If they are not, your
#algorithm should return None (which is the null value of Python), otherwise, if
# n and m are relatively prime, you should return the inverse of n modulo m.
def inverse(n, m):
    # Provide the correct implementation
    mO = m
    y = 0
    x = 1
    if(m == 1):
        return 0

    while(n > 1):
        q = n // m
        t = m
        m = n % m
        n = t
        t = y

        y = x-q*y
        x = t

    if(x < 0):
        x = x + mO
    return x

print inverse(23, 101)
# Expected output: 22
