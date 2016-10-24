def add():
    fh = open("todolist.txt", "w")
    input("Add an item: ")
    fh.close

def list():
    fh = open("todolist.txt", "r")
    print("You saved the following to-do items:")
    print(fh.readlines())

def mark():
    fh = open("todolist.txt", "r")
    print(fh.readlines())
    index = input("Which one you want to mark as completed: ")


def archive():
    fh = open("todolist.txt", )
    del(list.item[index])

while True:
    print("Please specify a command: add, list, mark, archive: ")

    if input("Please specify a command: add, list, mark, archive: ") == "add":
        print("Add an item: ", add())


