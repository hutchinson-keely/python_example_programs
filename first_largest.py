"""
Python program to find the largest element and its location.
"""

def largest_element(a, loc=True):
    element = a[0]
    maxloc = 0
    for i in range(0,len(a)):
        if a[i] > element:
            element=a[i]
            maxloc = i
    if loc==True:
        return element, maxloc
    return element


if __name__ == "__main__":

    a = [1,2,3,2,1]
    print("Largest element is {:}".format(largest_element(a)))
