drinks = ['coke', 'fanta', 'sprite']
choc = ['galaxy', 'mars', 'snickers']
crisps = ['bikers', 'skips', 'mccoys']

vending_machine = [drinks, choc, crisps]


def print_vending_machine(v):
    for row in v:
        print "\t|\t".join(row)
        print '----------------------------------'


def offer_vending():
    print_vending_machine(vending_machine)

    r = int(raw_input('Enter row number: '))
    c = int(raw_input('Enter col number: '))

    print "You picked: %s" % vending_machine[r][c]


offer_vending()