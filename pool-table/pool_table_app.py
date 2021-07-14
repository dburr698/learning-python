# You have just been hired by University of Houston as a developer. 
# Your first task is to create a pool table management app 
# which will manage the pool tables in University Center Games Room.

from pool_table_class import PoolTable

pool_tables = []

# populate the pool_tables array with 12 PoolTable objects  
for i in range(1, 13):
    pool_tables.append(PoolTable(i))


def display_tables():
    print("\nCurrent Status of Pool Hall Tables")
        # As an admin you should be able to see all the tables (12)
        # Print pool_tables with numbers 1-12
    for table in pool_tables:
        # As an admin each table in the list should show, whether the table is OCCUPIED or NOT OCCUPIED.
        if table.is_occupied == False:
            status = "Not Occupied"
            print(f"Pool Table {table.number}: {status}")
        else:
            status = "Occupied"
            print(f"Pool Table {table.number}: {status} - Start Time: {table.start_time} - Elapsed Time: {table.elapsed_time}")


print("\nWelcome to Pool Hall Manager!")

while True:

    print("\nMain Menu")
    print("1 - Check Out a Pool Table")
    print("2 - Return a Pool Table")
    print("3 - View status of Pool Tables")
    print("4 - Quit the application")

    select = input("\nSelect an option from the menu: ")

    if select == "1":
        display_tables()
        check_out = int(input("\nEnter table number that is being checked out: "))
        if pool_tables[check_out - 1].is_occupied == True:
            print("\nThis table is occupied.")
                
        else:
            pool_tables[check_out - 1].check_out()
            print(f"\nPool Table {check_out} has been checked out.")
            
                

    elif select == "2":
        display_tables()
        end = int(input("\nEnter the table number that is being returned: "))
        if pool_tables[end - 1].is_occupied == False:
            print("\nThis table has not been checked out.")
        
        else:
            pool_tables[end - 1].return_table()
            print(f"Pool Table {end} has been returned.")
            print(f"Pool Table {end} - Start Time: {pool_tables[end - 1].start_time} - End Time: {pool_tables[end - 1].end_time}")

    elif select == "3":
        display_tables()

    elif select == "4":
        print("\nExiting Pool Hall Manager.")
        print("Have a nice day!\n")
        break 
        

    