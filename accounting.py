melon_cost = 1.00

def payment_log(the_file) :
    opened_file = open(the_file)
    for line in opened_file:
        line = line.rstrip()
        words = line.split('|')
        customer_name, melon_count, customer_paid = words[1]
        customer_expected = melon_count * melon_cost
        print((f"{customer_name} paid ${customer_paid:.2f},",
            f"expected ${customer_expected:.2f}")
    

payment_log("customer-orders.txt")



##customer1_expected = customer1_melons * melon_cost
##if customer1_expected != customer1_paid:
#    print(f"{customer1_name} paid ${customer1_paid:.2f},",
#          f"expected ${customer1_expected:.2f}"
#          )
