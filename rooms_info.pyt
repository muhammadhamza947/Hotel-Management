class Hotel:
    def __init__(self, room):
        self.room = room
        self.is_booked = False

    def show_room(self):
         if self.is_booked:
          print("Room", self.room, "= Booked.")
         else:
             print("Room", self.room, "= Available.")


Rooms = []
while True:
    print("====== Hotel Management System =====")
    print("1. Add Rooms: ")
    print("2. Show Rooms: ")
    print("3. Book Room: ")
    print("4. Search Room: ")
    print("5. Exit: ")
    print()

    choice = input("Select your choice: ")
    print()

    # ------------- Add Rooms --------------

    if choice == "1":
        no = input("Enter room by numbers: ")
        find = False
        for room in Rooms:
            if room.room == no:
                find = True
                break
        if find == True:
            print("Room already added.")
        else:
            room = Hotel(no)
            Rooms.append(room)
            print("Room", room.room, "added successfully.")
            print("--------")

    # ------------ Show Rooms ---------------

    elif choice == "2":
        if len(Rooms) == 0:
            print("Rooms are not available.")
            print("--------")
        else: 
            for room in Rooms:
                room.show_room()

    # ------------- Booked Room -----------

    elif choice == "3":
        for room in Rooms:
               room.show_room()
        no = input("Enter room number for booking: ")
        find = False
        for room in Rooms:
            if room.room == no:
                if room.is_booked == False:
                    print("Room", no, "booked successfully.")
                    room.is_booked = True
                    print("---------")
                    find = True
                    break
        if find == False:
                print("Room", no, "already booked.")

    #  ------------- Search Room -------------

    elif choice == "4":
        no = input("Enter room number: ")
        find = False
        for room in Rooms: 
            if room.room == no:
                if room.is_booked == False:
                    print("Room", no, "available.")
                    print("--------")
                    find = True
                else: 
                    print("Room", no, "already booked.")
                    find = True
                    break
        if find == False:
            print("Room is not find.")

    # --------------- Exit --------------
    
    elif choice == "5":
        print("Program has been ended.")
        break
    else:
        print("Invalid choice.")
               
         
        
