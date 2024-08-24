# FUNCTIONS:-

# marks1 = [45, 78, 86, 77]
# percentage1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100


# marks2 = [23, 54, 89, 65]
# percentage2 = (sum(marks2)/400)*100

# print(percentage1,percentage2)
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)