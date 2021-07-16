# You have just been hired by University of Houston as a developer. 
# Your first task is to create a pool table management app 
# which will manage the pool tables in University Center Games Room.

from pool_table_class import PoolTable
from datetime import date

pool_tables = []

# populate the pool_tables array with 12 PoolTable objects  
for i in range(1, 13):
    pool_tables.append(PoolTable(i))


def display_tables():
    print("\n\tCurrent Status of Pool Hall Tables:")
        # As an admin you should be able to see all the tables (12)
        # Print pool_tables with numbers 1-12
    for table in pool_tables:
        # As an admin each table in the list should show, whether the table is OCCUPIED or NOT OCCUPIED.
        if table.is_occupied == False:
            status = "Not Occupied"
            print(f"\tPool Table {table.number}: {status}")
        else:
            status = "Occupied"
            table.delta_elapsed()
            print(f"\tPool Table {table.number}: {status} - Start Time: {table.start_time} - Elapsed Time: {table.elapsed_time}")

def add_to_file():
        today = str(date.today())
        ext = ".txt"
        file_name = today + ext
        with open(file_name, "a") as file:
            file.write(f"Pool Table {table_number} - Start Time: {table.start_time} - End Time: {table.end_time} - Total Time: {table.total_time} - Final Cost: ${table.cost}\n")


print("\n------------ Welcome to Pool Hall Manager! ------------")

while True:

    print("\n\t*************** Main Menu **************")
    print("\t***** 1 - Check Out a Pool Table   *****")
    print("\t***** 2 - Return a Pool Table      *****")
    print("\t***** 3 - View Pool Tables Status  *****")
    print("\t***** q - Quit the application     *****")
    print("\t****************************************")

    select = input("\nSelect an option from the menu: ")

    if select == "1":
        display_tables()
        try:
            table_number = int(input("\nEnter table number that is being checked out: "))
            table = pool_tables[table_number - 1]
            if table.is_occupied == True:
                print("\nThis table is occupied.")
                
            else:
                table.check_out()
                print(f"\nPool Table {table_number} has been checked out.")
        
        except ValueError:
            print("\nThat was not a number. Try again.")
        except IndexError:
            print("\nThis table does not exist. Try again.")
            
                

    elif select == "2":
        display_tables()
        try:
            table_number = int(input("\nEnter the table number that is being returned: "))
            table = pool_tables[table_number - 1]
            if table.is_occupied == False:
                print("\nThis table has not been checked out.")
        
            else:
                table.return_table()
                print(f"Pool Table {table_number} has been returned.")
                table.delta_total()
                table.calculate_cost()
                print(f"Pool Table {table_number} - Start Time: {table.start_time} - End Time: {table.end_time} - Total Time: {table.total_time} - Final Cost: ${table.cost}")
                add_to_file()
        
        except ValueError:
            print("\nThat was not a number. Try again.")
        except IndexError:
            print("\nThis table does not exist. Try again.")

    elif select == "3":
        display_tables()

    elif select == "q":
        print("\n-------------- Exiting Pool Hall Manager. ----------------")
        print("-------------------- Have a nice day! --------------------\n")
        break 
        

    