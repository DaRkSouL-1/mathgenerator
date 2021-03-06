from  .__init__ import *


def geometricMeanFunc(maxValue=100, maxNum=4):
    a=random.randint(1,maxValue)
    b=random.randint(1,maxValue)
    c=random.randint(1,maxValue)
    d=random.randint(1,maxValue)
    num=random.randint(2,4)
    if num==2:
      product=a*b
    elif num==3:
      product=a*b*c
    elif num==4:
      product=a*b*c*d

    ans=product**(1/num)
    if num==2:
      problem=f"Geometric mean of {num} numbers {a} and {b} = "
      solution = f"({a}*{b})^(1/{num}) = {ans}"
    elif num==3:
      problem=f"Geometric mean of {num} numbers {a} , {b} and {c} = "
      solution = f"({a}*{b}*{c})^(1/{num}) = {ans}"
    elif num==4:
      problem=f"Geometric mean of {num} numbers {a} , {b} , {c} , {d} = "
      solution = f"({a}*{b}*{c}*{d})^(1/{num}) = {ans}"
    return problem,solution
