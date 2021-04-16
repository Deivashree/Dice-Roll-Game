import os;

# Clear the command prompt screen
def ClearScreen():
	if os.name == "nt":
		os.system("cls");
	else:
		os.system("clear");

# Show table (assuming dictionary data structure for listData[row])
def ShowTableByDictionary(title, listRowNames, listColNames, listColKeys, listData):
	
    # Show title
    print(title);

    noRowNames = True if len(listRowNames) == 0 else False;

    # Find the maximum length of row names
    rmaxLen = 0 if len(listRowNames) == 0 else max([len(rname) for rname in listRowNames]);
    
    # Find the maximum length for columns
    cmaxLen = {listColKeys[col]:len(listColNames[col]) for col in range(len(listColKeys))};
    for row in range(len(listData)):
        for colKey in listData[row]:
            cmaxLen[colKey] = max(cmaxLen[colKey], len(str(listData[row][colKey])));

    # Create header string with listColNames
    listStart = [] if noRowNames else [' ' * rmaxLen];
    listColNamesJustified = [listColNames[col].center(cmaxLen[ listColKeys[col] ]) for col in range(len(listColKeys))];
    listHeaderName = listStart + listColNamesJustified;
    header = " | ".join(listHeaderName);

    # Create Border
    listHeaderNameLength = [len(c) for c in listHeaderName];
    listColBorder = ["-" * l for l in listHeaderNameLength];
    border = "-+-".join(listColBorder);

    # Show full headers (border + header + border)
    print(f"+-{border}-+");
    print(f"| {header} |");
    print(f"+-{border}-+");

    # Show all rows of data
    for row in range(len(listData)):
        # Create row string
        # Add row name as the first element in listRowStr
        listRowStr = [] if noRowNames else [listRowNames[row].ljust(rmaxLen)];
        # Add column data from listData[row]
        col = 0;
        for colKey in listColKeys:
            if colKey in listData[row]:
                colStr = str(listData[row][colKey]);
                listRowStr.append(colStr.rjust(cmaxLen[colKey]));
            else:
                listRowStr.append(" " * cmaxLen[colKey]);
            # Increment column
            col += 1;
        # Construct a row string from listRowStr
        rowStr = " | ".join(listRowStr);

        # Show row string
        print(f"| {rowStr} |");
        print(f"+-{border}-+");
    # end line
    print();

# Show table (assuming list data structure for listData[row])
def ShowTableByList(title, listRowNames, listColNames, listData):
	
    # Show title
    print(title);

    noRowNames = True if len(listRowNames) == 0 else False;

    # Find the maximum length for row names
    rmaxLen = 0 if len(listRowNames) == 0 else max([len(rname) for rname in listRowNames]);
    
    # Find the maximum length for columns
    cmaxLen = [len(colName) for colName in listColNames];
    for row in range(len(listData)):
        for col in range(len(listData[row])):
            cmaxLen[col] = max(cmaxLen[col], len(str(listData[row][col])));

    # Create header string with listColNames
    listStart = [] if noRowNames else [' ' * rmaxLen];
    listColNamesJustified = [listColNames[col].center(cmaxLen[col]) for col in range(len(listColNames))];
    listHeaderName = listStart + listColNamesJustified;
    header = " | ".join(listHeaderName);

    # Create Border
    listHeaderNameLength = [len(c) for c in listHeaderName];
    listColBorder = ["-" * l for l in listHeaderNameLength];
    border = "-+-".join(listColBorder);

    # Show full headers (border + header + border)
    print(f"+-{border}-+");
    print(f"| {header} |");
    print(f"+-{border}-+");

    # Show all rows of data
    for row in range(len(listData)):
        # Create row string
        # Add row name as the first element in listRowStr
        listRowStr = [] if noRowNames else [listRowNames[row].ljust(rmaxLen)];
        # Add column data from listData[row]
        for col in range(len(listData[row])):
            if listData[row][col] != None:
                colStr = str(listData[row][col]);
                listRowStr.append(colStr.rjust(cmaxLen[col]));
            else:
                listRowStr.append(" " * cmaxLen[col]);

        # Construct a row string from listRowStr
        rowStr = " | ".join(listRowStr);

        # Show row string
        print(f"| {rowStr} |");
        print(f"+-{border}-+");

    # end line
    print();


	
if __name__ == "__main__":

    
    names = ["Alice", "Bob", "Cindy"];
    subjects = ["Engineering", "Arts", "Programming", "Business"];

    # Marks organized in a list for each student, to be used for ShowTableByList()
    marksList = [ 
        [20.5, None, 41.0, 82.39], # Alice's marks
        [None, 53.1, 91.26, 65.1], # Bob's marks
        [64.5, 33.321, None, None], # Cindy's marks
    ];

    # Marks organized in a dictionary for each student, to be used for ShowTableByDictionary()
    marksDictList = [ 
        {"Engineering": 20.5, "Programming": 41.0, "Business": 82.39}, # Alice's marks
        {"Arts": 53.1, "Programming": 91.26, "Business": 65.1}, # Bob's marks
        {"Engineering": 64.5, "Arts": 33.321}, # Cindy's marks
    ];

    # Show table (data stored as list of list)
    ShowTableByList("Coursework", names, subjects, marksList);

    # Show table (data stored as list of dictionary)
    ShowTableByDictionary("Coursework", names, subjects, subjects, marksDictList);