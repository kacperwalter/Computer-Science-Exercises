"""its still a implementing stacks"""
from stack import Stack

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

print("\nLet's play Towers of Hanoi!!")
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(num_disks)

num_optimal_moves = (2**num_disks) - 1

print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))

"""i still dont know how to use list comprehension xD"""
def get_input():
    choices = [stack.get_name()[0] for stack in stacks]
    pass
