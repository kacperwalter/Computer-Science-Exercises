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