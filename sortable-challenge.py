if __name__ == "__main__":
    from json import loads, dumps
    from sys import argv, exit
    if len(argv) < 3:
        print "Usage: python sortable-challenge.py products.txt listings.txt"
        exit(1)
    else:
        products_filename, listings_filename = argv[1], argv[2]

        # A more realistic approach would be to assume the files are too large,
        # and operate line by line. I assume the products can be fit into
        # memory, but the listings cannot.
        products = {}
        results = {}
        with open(products_filename, "r") as products_file:
            for line in products_file:
                product = loads(line)
                product_name = product[u"product_name"]
                products[product_name] = product
                results[product_name] = []

        with open(listings_filename, "r") as listings_file:
            for line in listings_file:
                listing = loads(line)
                title = listing[u"title"]
                for product_name, product in products.iteritems():
                    manufacturer = product[u"manufacturer"]
                    model = product[u"model"]
                    if manufacturer in title and model in title:
                        results[product_name].append(listing)

        with open("results.txt", "w") as results_file:
            for product_name, listings in results.iteritems():
                results_file.write("{")
                results_file.write("\"product_name\":\"{}\",\"listings\":"
                        .format(product_name))
                results_file.write(dumps(listings, separators=(",",":")))
                results_file.write("}")
                results_file.write("\n")
