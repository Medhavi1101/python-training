from A6_LinkedList import LinkedList

def main():
    list = LinkedList()
    for node in range(10,20):
        list.append(node)

    print(list.info())

    print(f'Element present at index {1}: {list.get(1)}')
    

    print('Adding elements to list')
    list.insert(1, 1)
    list.insert(4, 6)
    list.insert(5, 7)
    list.info()
    print(list.info())

    print('Removing elements from list')
    list.remove(2)
    list.remove(8)

    list.info()






if(__name__=='__main__'):
    main()