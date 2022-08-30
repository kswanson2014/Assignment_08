# ------------------------------------------#
# Title: Assignment08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# KSwanson, 2022-Aug-26, completed TODOs
# ------------------------------------------#

# -- Data -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data for a CD
    
    Properties:
        cd_id (int): CD ID
        cd_title (str): title of the CD
        cd_artist (str): artist of the CD
        
    Methods:    
        None.
    """
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = cd_id
        self.cd_title= cd_title
        self.cd_artist = cd_artist

    @property
    def getcd_id(self):
        return self.cd_id
    
    @property
    def getcd_title(self):
        return self.cd_title
    
    @property
    def getcd_artist(self):
        return self.cd_artist

    @staticmethod
    def add_cd(lst_Inventory, cd_id, cd_title, cd_artist):
        """Add new CD
        
        Args:
            lstOfCDObjects (list of lists): 2D data structure that holds the data during runtime
            strID (str): ID of CD
            strTitle (str): Title of CD
            strArtist (str): Artist for CD 
            
        Returns:
            None.
            """
        intID = int(float(cd_id))
        dicRow = {'ID': intID, 'Title': cd_title, 'Artist': cd_artist}
        lst_Inventory.append(dicRow)
        IO.show_inventory(lst_Inventory)
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file
    
    Properties:
        None.
        
    Methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name,lst_Inventory): -> (a list of CD objects)
    """
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """ Converts data from a list of objects to a file
        
        Arguments:
            file_name (str): name of file the data is saved to
            lst_Inventory (list of objects): 2D structure, list of objects, holding uses input during script running
            
        Returns:
            None.
        """
        objFile = open(strFileName, 'w')
        for row in lstOfCDObjects:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """ Converts data from a file to a list of object
        
        Arguments:
            file_name (str): name of file the data is read to
            lst_Inventory (list of objects): 2D structure holding user input during script run
            
        Returns:
            None
        """
        try:
            lst_Inventory.clear()  # this clears existing data and allows to load data from file
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                lst_Inventory.append(dicRow)
            objFile.close()
        except FileNotFoundError:
            print('Existing inventory file not found.\n')


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output
    Properties:
        None.
        
    Methods:
        print_menu(): -> None
        menu_choice(): -> (menu choice)
        show_inventory(lst_Inventory): -> None
        new_cd(): -> (new CD Inventory item)
    """

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        
        Args:
            None.
            
        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory\n[d] Delete CD\n[s] Save Inventory to File\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        
        Args:
            None.
            
        Returns:
            choice (str): a lower case sting of the users input out of the choices l, a, i, d, s or x
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table
        
        Args:
            lstOfCDObjects (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
            
        Returns:
            None.
        """
        print()  # Add extra space for layout
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print('{}\t{} (by: {})'.format(*row.values()))
        print('======================================')
        print()  # Add extra space for layout
    
    @staticmethod
    def new_cd():
        """Get user input for a new CD
        
        Args:
            None.
        
        Returns:
            None.
        """
        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID = (int(float(strID)))
                break
            except ValueError:
                print('Please enter a valid integer\n')
        strTitle = input('Enter CD Title: ').strip()
        strArtist = input('Enter CD Artist: ').strip()
        CD.add_cd(lstOfCDObjects, intID, strTitle, strArtist)
        
    @staticmethod
    def Delete_CD(lst_Inventory):
        """Function to remove a CD from the table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstOfCDObjects:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstOfCDObjects[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        IO.show_inventory(lstOfCDObjects)  

# -- Main Body of Script -- #
# Read in the currently saved Inventory
FileIO.load_inventory(strFileName, lstOfCDObjects)

# Start main loop
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

# Process menu selection
    # Process exit
    if strChoice == 'x':
        break
        
    # Process to load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'y\' to continue and reload from file. Otherwise reload will be canceled\n')
        if strYesNo.lower() == 'y':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue
        
    # Process to add a CD
    elif strChoice == 'a':
        IO.new_cd()
        continue
        
    # Process to display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    
    # Process to delete CD
    elif strChoice == 'd':
        IO.show_inventory(lstOfCDObjects)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        IO.Delete_CD(lstOfCDObjects)
        continue
        
    # Process to save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
           FileIO.save_inventory(strFileName, lstOfCDObjects)
           pass
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
        
    # Catch-all should not be possible, as user choice gets vetted in I/O, but to be safe:
    else:
        print('General Error')