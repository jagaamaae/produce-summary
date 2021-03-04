def melon_count(day_number, path):
    """Given day number & path to the deliveries, produces a report. Opens the deliveries file at different paths, 
    processes each line, generates report in all uppercase.
    """

    print("Day", day_number)
    delivery_log = open(path)

    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')

        melon, count, amount = words

        print (f"Delivered {count} {melon}s for a total of  $ {amount}")


    delivery_log.close()


melon_count(1, "um-deliveries-20140519.txt")
melon_count(2, "um-deliveries-20140520.txt")
melon_count(3, "um-deliveries-20140521.txt")