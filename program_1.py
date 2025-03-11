def process_sales_data(sales_data):

    total = 0
    for sale in sales_data:
        total = total + sale["amount"]
    

    highest = 0
    for sale in sales_data:
        if sale["amount"] > highest:
            highest = sale["amount"]
    

    lowest = 99999999
    for sale in sales_data:
        if sale["amount"] < lowest:
            lowest = sale["amount"]
    

    average = 0
    count = 0
    for sale in sales_data:
        average = average + sale["amount"]
        count = count + 1
    if count > 0:
        average = average / count
    

    north_count = 0
    south_count = 0
    east_count = 0
    west_count = 0
    for sale in sales_data:
        if sale["region"] == "north":
            north_count = north_count + 1
        if sale["region"] == "south":
            south_count = south_count + 1
        if sale["region"] == "east":
            east_count = east_count + 1
        if sale["region"] == "west":
            west_count = west_count + 1
    

    print("Total Sales: $" + str(total))
    print("Highest Sale: $" + str(highest))
    print("Lowest Sale: $" + str(lowest))
    print("Average Sale: $" + str(average))
    print("North: " + str(north_count))
    print("South: " + str(south_count))
    print("East: " + str(east_count))
    print("West: " + str(west_count))
