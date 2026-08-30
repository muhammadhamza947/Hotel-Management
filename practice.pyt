class Hotel:
    def __init__(self, room):
        self.room = room
        self.is_booked = False

    def show_room(self):
        if self.is_booked:
            print("Room", self.room, "Booked.")
        else:
            print("Room", self.room, "Available")
          

Rooms = []
while True:
    print("====== Hotel Management ======")
    print("1. Add Rooms: ")
    print("2. Show Rooms: ")
    print("3. Booked Room: ")


    print()
    choice = input("Select your choice: ")
    print()
    if choice == "1":
        no = input("Enter Room by number: ")
        find = False 
        for room in Rooms:
            if room.room == no:
                print("Room", no, "already added.")
                print("-------")
                find = True
                break
        if find == False:
            Room = Hotel(no)
            Rooms.append(Room)
            print("Room", no, "added successfully.")
            print("--------")

    elif choice == "2":
        if len(Rooms) == 0:
            print("Rooms not available.")
        else:
            for room in Rooms:
                room.show_room()

    elif choice == "3":
        for room in Rooms:
             room.show_room()
        no = input("Enter Room number for booking: ")
        find = False
        for room in Rooms:
            if room.room == no:
                if room.is_booked == False:
                    print("Room", no, "booked successfully.")
                    room.is_booked = True
                    print("--------")
                    find = True
                    break
                else:
                 print("Room", no, "booked already.")
                 print("--------")
                 find = True
                 break
        if find == False:
                print("Room is not available.")
                print("---------")

            