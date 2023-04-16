for line in open('items.txt', 'r').read().splitlines():
    open('splitted.txt', 'a').write(f"{line.split(':')[2]}\n")
