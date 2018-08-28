# from linkedListInsertion import Node
from linkedListInsertion import LinkedList

aList = LinkedList()

N = int(input('How many elements: '))
print('A. Insert at the Beginning')
print('B. Insert at the end')
choice = input('Enter your choice: ')

for i in range(N):

    if choice.upper() == 'A':
        data = int(input('\nEnter data: '))
        aList.insertAtBeginning(data)
        print('List in forward: ', end="")
        aList.printListForward()
    elif choice.upper() == 'B':
        data = int(input('\nEnter data: '))
        aList.insertAtEnd(data)
        print('List: ', end="")
        aList.printListForward()
    else:
        print('Wrong Choice!')
        break