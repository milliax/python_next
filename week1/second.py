import numpy as np

def print_digit(arr):
    print("[",end="")
    for e in arr:
        print("{:0.2f}".format(e),end=" ")
    print("]")


all_score = np.random.randint(100,size=[150])
all_score = all_score.reshape(30,5)

total = all_score.sum(axis=0)
average = total/30
_max = all_score.max(axis=0)
_min = all_score.min(axis=0)
std = all_score.std(axis=0)

arranged = np.sqrt(all_score)
arranged = arranged * 10

arranged[arranged<60] = 39
failed = arranged[arranged == 39] 

print("各科總分: {}".format(total))
print("各科平均: ", end="")
print(average.round(2))
#print_digit(average)
print("各科最高分: {}".format(_max))
print("各科最低分: {}".format(_min))
print("各科標準差: ",end="")
#print_digit(std)
print(std.round(2))
print("調整後分數: ")
print(arranged.round(2))

#print (arranged)
print("全班不及格科目數: {}".format(len(failed)))
#print(all_score)