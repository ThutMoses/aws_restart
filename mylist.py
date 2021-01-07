#2.create a function changedata(mylist), which take a list as argument and changes the values in mylist. Display the contents of the list

myBasket = ['apples', 'oranges', 'pineapple']

def changedata(mylist):
    mylist.append("cherry")
    mylist.append("kiwi")

    for item in mylist:
        print (item)

    mylist[0] = "Guava"
    mylist[2] = "pear"

    for item in mylist:
        print (item)

changedata(myBasket)
