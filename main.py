

def split():

    content = open('items.txt', 'r').read().splitlines()

    for info_d in content:
        split = info_d.split(':')[2]
        w = open('splitted.txt', 'a')
        w.write(f"{split}\n")


split()
