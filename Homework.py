#import
import random


#Function 1: Generate new groups
def generate_groups(first_round, round_num):

    groups = []

    for i in range(5):
        group = []

        for j in range(4):

            #The new row index
            new_row = (i + j * (round_num - 1)) % 5

            student = first_round[new_row][j]
            group.append(student)

        groups.append(group)

    return groups

#Function 2: print the result
def print_groups(groups, round_num):
    print("Round", round_num, "grouping is:")
    
    for i in range(5):
        print("Group", i + 1, ":", groups[i])


def main():

#Parrt 1: 输入姓名，检查人数 Input student names
    while True:
        name = input("Enter 20 names of students")
        student_name = name.split(", ")
        list_length = len(student_name)
        if list_length != 20:
            print("There are not 20 names! Try again!")
        else:
            print("There are 20 names! Correct!")
            break
        
    #Part 2: 第一次分组 Generate the first round
    random.shuffle(student_name)
    first_round = [student_name[i:i+4] for i in range(0, 20, 4)]
    print_groups(first_round, 1)


    #Part 3:询问程序是否继续 Generate additional rounds

    count = 1

    while True:
        answer = input("Continue? (y/n): ")

        if answer.lower() == "n":
            print("Program ended.")
            break
        
        elif answer.lower() == "y":
            if count < 5:
                count += 1
                new_groups = generate_groups(first_round, count)
                print_groups(new_groups, count)
                
            else:
                print("Error! There is no new grouping!")
                break

if __name__ == "__main__":
    main()         
        
