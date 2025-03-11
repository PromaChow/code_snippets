def load_and_process_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    
    result = []
    line_num = 1
    
    for line in lines:
        data = line.strip().split(',')
        
        try:
            if len(data) < 3:
                print("Error: Line " + str(line_num) + " does not have enough values")
                line_num = line_num + 1
                continue
            
            item = {}
            item["id"] = data[0]
            item["name"] = data[1]
            item["value"] = float(data[2])
            

            if item["value"] <= 0:
                print("Warning: Line " + str(line_num) + " has zero or negative value")
            else:
                if item["value"] < 100:
                    item["category"] = "low"
                if item["value"] >= 100 and item["value"] < 500:
                    item["category"] = "medium"
                if item["value"] >= 500:
                    item["category"] = "high"
            
            result.append(item)
        except:
            print("Error processing line " + str(line_num))
        
        line_num = line_num + 1
    

    file.close()
    return result
