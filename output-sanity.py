if __name__ == "__main__":
    from json import loads
    from sys import argv, exit
    if len(argv) < 2:
        print "Usage: python output-sanity.py results.txt"
        exit(1)
    with open(argv[1], "r") as f:
        for line in f:
            product = loads(line)
    print "Yay!"
