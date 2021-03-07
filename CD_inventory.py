#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# MPOST, 1200-MAR-04, Troubleshot object O programming
# MPOST, 1400-MAR-04, Created Aux program for proof of concept
# MPOST, 1430-MAR-04, Tested Succesfull
# MPOST, 1500-MAR-04, Added code to week 8's psuedocode 
# MPOST, 0900-MAR-07, Added getter/Setters updated docstring
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstTbl = []

import pickle
class CD:
    """Stores data about a CD:

    properties:
        self.id = cd_id
        self.title = cd_title
        self.artist = cd_artist
    
    Getter and setter for each property setup below 

    """
    def __init__(self, cd_id, cd_title, cd_artist): 
        """__Init__ method creats pointers for program values ID Title and Artist 
            
        """
        self.id = cd_id
        self.title = cd_title
        self.artist = cd_artist
        
    @property  
    def ID(self):
       return self.id
   
    @ID.setter
    def ID(self,value):
      if type(value) == int:
          self.id = value   
   
    @property
    def TITLE(self):
       return self.title
      
    @TITLE.setter   
    def TITLE(self,value):
        if type(value) == str:
          self.title = value
   
    @property
    def ARTIST(self):
        return self.artist

    @ARTIST.setter     
    def ARTIST(self,value): 
        if type(value) == str:
            self.artist = value    

    pass

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by object

        Args:
            file_name (string): name of file used to read the data from
        

        Returns:
            None.
        """

        try:
           table.clear()  # this clears existing data and allows to load data from file
           with open(file_name, "rb+") as objFile:
            table = pickle.load(objFile)
            return table
            
        except:
                   print("\n\n\n***CDInventory.dat not found***\n\n\n")

    @staticmethod
    def write_file(strFileName, lstTbl): 
        """ Additional file proccesing function to save file to .txt
        
        Function saves objects to file using pickle method"""

           
        with open(strFileName, "wb+") as objFile: #Pickle to save objects to file
            pickle.dump(lstTbl, objFile)

    pass

# -- PRESENTATION (Input/Output) -- #
class IO:

    """Handling Input / Output"""
  

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for item in lstTbl:
            print(item.id, item.title, item.artist)
        print('======================================')
        
    @staticmethod
    def input_user():
        """User input taken then assigned to strID, strTitle, and stArtist

        
        Args:
            lstTbl.append(CDobject)
            
        Returns:
           
            lstTbl
        
        """
        while True:
            try:
               CDobject = CD((int(input('Enter ID: ').strip())), (input('What is the CD\'s title? ').strip()), (input('What is the Artist\'s name? ').strip()))
               lstTbl.append(CDobject)
               return lstTbl
               break
            except ValueError:
                print("Invalid entry. ID must be integer")    
    pass

while True:
   
    IO.print_menu()
    strChoice = IO.menu_choice()
    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstTbl = FileIO.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top (No Change)
    elif strChoice == 'a':  
        IO.input_user()
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    elif strChoice == 'i':
        IO.show_inventory(lstTbl) ## Calls for show function dispalying user inventory
        continue  # start loop back at top.
    elif strChoice == 's':
        IO.show_inventory(lstTbl) ## Calls for show function dispalying user inventory
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo.lower() in ['yes', 'y']:
            FileIO.write_file(strFileName, lstTbl) ## Calls for to save inventory to target .txt file 
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    ### catch-all should not be possible, as user choice gets vetted in IO, but to be save (no change):
    else:
        print('General Error') 


