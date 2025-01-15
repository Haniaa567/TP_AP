
def save_list_to_text_file(lst, filename):
    """
    Save a list to a text file, one item per line.

    Parameters:
        lst (list): The list to save.
        filename (str): The name of the file to save the list.
    """
    with open(filename, "w") as file:
        for item in lst:
            file.write(f"{item}\n")
    print(f"List saved to {filename} as text.")

def load_list_from_text_file(filename):
    lst=[]
    """
    Load a list from a text file, one item per line.

    Parameters:
        filename (str): The name of the file to load the list from.

    Returns:
        list: The loaded list.
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                lst.append(int(line.strip()))
        print(f"List loaded from {filename} as text.")
        return lst
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []
List=[] 
while True:
    try:
        
        n = int(input("Enter a number: "))
        
    except ValueError: 
        print("Input must be an integer.")
        exit()
    
    List.append(n)
    if(n==0):
        exit()
    print("current list: ",List)
    Sort=List.copy()
    Sort.sort()
    print("sorted list: ",Sort)
    re=Sort.copy()
    re.sort(reverse=True)
    print("reversed list: ",re)
    save_list_to_text_file(List,"test.txt")