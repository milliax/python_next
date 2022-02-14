import numpy as np

def init(x):
    x = int(x*100)
    return x

class_grades = np.random.random((7,37))
class_grades = class_grades.reshape(7*37)
class_grades = list(map(init,class_grades))

class_grades = np.array(class_grades)
class_grades = class_grades.reshape(37,7)


print(class_grades)

for i in range(len(class_grades)):
    print("{}: {}".format(i,*class_grades[i]))