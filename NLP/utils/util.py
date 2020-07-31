def removeBlank(lines): 
    for idx in range(len(lines)):
        lines[idx] = lines[idx].strip() 
    filtered_lines = [line for line in lines if line != ""]
    return filtered_lines 