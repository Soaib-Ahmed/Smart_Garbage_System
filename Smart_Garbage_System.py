Garbage_types = ['Biodegradeable_garbage', 'non_Biodegradeable_garbage']
Garbage_sub_types = ['recyclable', 'non_recyclable']


def garbage_type_and_amount_selection():
    print("Please select the type of garbage you want to dispose of:")
    print("1. Biodegradable")
    print("2. Non-biodegradable (Recyclable)")
    print("3. Non-biodegradable (Non-recyclable)")

    select = input("Enter the type of garbage (1/2/3): ")

    if select == '1':
        amount = int(input("Enter garbage amount: "))
        garbage_name = Garbage_types[0]
        garbage_dict = {'garbage_name': garbage_name, 'amount': amount}
        return garbage_dict

    elif select == '2':
        amount = int(input("Enter garbage amount: "))
        garbage_name = Garbage_sub_types[0]  # Recyclable
        garbage_type_name = 'non_Biodegradeable_garbage'
        garbage_dict = {'garbage_name': garbage_name, 'amount': amount, 'garbage_type': garbage_type_name}
        return garbage_dict

    elif select == '3':
        amount = int(input("Enter garbage amount: "))
        garbage_name = Garbage_sub_types[1]  # Non-recyclable
        garbage_type_name = 'non_Biodegradeable_garbage'
        garbage_dict = {'garbage_name': garbage_name, 'amount': amount, 'garbage_type': garbage_type_name}
        return garbage_dict

    else:
        print("Invalid selection.")
        return None


def billing_calculation(garbage):
    bill_list = []
    garbage_list_for_billing = []
    garbage_list_for_billing.append(garbage)

    for grbg in garbage_list_for_billing:
        grbg_name = grbg['garbage_name']
        grbg_amount = grbg['amount']
        bill = 0

        if grbg_name == 'Biodegradeable_garbage':
            bill = grbg_amount * 0

        elif grbg_name == 'recyclable':
            bill = grbg_amount * 2

        elif grbg_name == 'non_recyclable':
            bill = grbg_amount * 5

        bill_info = {'garbage_type': grbg_name, 'amount': grbg_amount, 'bill': bill}
        bill_list.append(bill_info)

    user_obj.total_bill.extend(bill_list)
    bill_list.clear()


class User:
    user_list = []

    def __init__(self, name, email, address, password):
        self.user_name = name
        self.user_address = address
        self.email = email
        self.password = password
        self.total_bill = []

        User.user_list.append(self)

    def total_bill_calculation(self):
        total_sum = sum(bill['bill'] for bill in self.total_bill)
        print("Total bill amount:", total_sum)

    @classmethod
    def user_exists(cls, email, password):
        for user in cls.user_list:
            if user.email == email and user.password == password:
                return user
        return None


class source_bin:
    source_garbage = []

    def receive_garbage(self, garbage):
        if garbage['amount'] > 10:
            print("********warning:**Sorry 10 garbage at a time****")
        else:
            self.source_garbage.append(garbage)
            billing_calculation(garbage)

    def printing_all_garbage(self):
        print("Printing garbage details in source bin --------")
        for grbg in self.source_garbage:
            print(grbg)
        print("source bin printing ends------------------------")

    def sending_garbage_to_GMP(self):
        gmp_bin_obj = GMP_Bin()
        gmp_bin_obj.receive_garbage_from_source(self.source_garbage)
        gmp_bin_obj.printing_gmp_garbage()
        gmp_bin_obj.allocation_of_garbage_to_bins()


class GMP_Bin:
    def __init__(self):
        self.GMP_garbage = []

    def receive_garbage_from_source(self, garbage_from_source):
        self.GMP_garbage.extend(garbage_from_source)

    def printing_gmp_garbage(self):
        print("****printing all garbage in gmp bins------")
        for grbg in self.GMP_garbage:
            print(grbg)
        print("gmp bin garbage prints ends---------------")

    def allocation_of_garbage_to_bins(self):
        bio_garbage_temp = []
        N_bio_garbage_temp = []
        for grbg in self.GMP_garbage:
            grbg_name = grbg['garbage_name']
            grbg_amount = grbg['amount']

            if grbg_name == 'Biodegradeable_garbage':
                bio_garbage_dictionary = {'garbage_type': grbg_name, 'amount': grbg_amount}
                bio_garbage_temp.append(bio_garbage_dictionary)

            elif grbg_name == 'non_Biodegradeable_garbage':
                N_bio_garbage_dictionary = {'garbage_type': grbg_name, 'amount': grbg_amount}
                N_bio_garbage_temp.append(N_bio_garbage_dictionary)

        bio_bin_obj.add_garbage(bio_garbage_temp)
        Non_Bio_bin_obj.add_garbage(N_bio_garbage_temp)


class Bio_bin:
    bio_main_garbage_collection = []

    def add_garbage(self, garbage):
        self.bio_main_garbage_collection.extend(garbage)


class Non_Bio_bin:
    def __init__(self):
        self.Non_bio_bin_garbage_collection = []

    def add_garbage(self, garbage):
        self.Non_bio_bin_garbage_collection.extend(garbage)

    def allocation_of_garbage(self):
        r_garbage_temp = []
        nr_garbage_temp = []
        for grbg in self.Non_bio_bin_garbage_collection:
            grbg_name = grbg['garbage_name']
            grbg_amount = grbg['amount']
            if grbg_name == "recyclable":
                r_garbage_dictionary = {'garbage_type': grbg_name, 'amount': grbg_amount}
                r_garbage_temp.append(r_garbage_dictionary)
                r_bin_obj.add_garbage(r_garbage_temp)
            elif grbg_name == "non_recyclable":
                nr_garbage_dictionary = {'garbage_type': grbg_name, 'amount': grbg_amount}
                nr_garbage_temp.append(nr_garbage_dictionary)
                nr_bin_obj.add_garbage(nr_garbage_temp)

                # Non-recyclable billing
                bill = grbg_amount * 5
                bill_info = {'garbage_type': grbg_name, 'amount': grbg_amount, 'bill': bill}
                user_obj.total_bill.append(bill_info)

    def printing_garbage(self):
        if not self.Non_bio_bin_garbage_collection:
            print("Non-Bio bin is empty.")
        else:
            print("Printing non-bio bin all garbage--------")
            for grbg in self.Non_bio_bin_garbage_collection:
                print(grbg)
            print("Non-Bio bin garbage print ends............")



class Recyclable_bin:
    r_garbage_collection = []

    def add_garbage(self, garbage):
        self.r_garbage_collection.extend(garbage)


class Non_Recyclable_bin:
    nr_garbage_collection = []

    def add_garbage(self, garbage):
        self.nr_garbage_collection.extend(garbage)


bio_bin_obj = Bio_bin()
Non_Bio_bin_obj = Non_Bio_bin()
r_bin_obj = Recyclable_bin()
nr_bin_obj = Non_Recyclable_bin()

user_obj = None

while True:
    print("Welcome to the Smart Garbage Collection System!")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        name = input('Name: ')
        email = input('Email: ')
        address = input('Address: ')
        password = input('Password: ')
        user_obj = User(name, email, address, password)
        print("Registration successful")

    elif choice == '2':
        email = input('Email: ')
        password = input('Password: ')
        user_obj = User.user_exists(email, password)
        if user_obj is None:
            print("Account doesn't exist.")
        else:
            print("Login successful")

            while True:
                print("\n----- Select an option -----")
                print("1. Check user details")
                print("2. Enter garbage to source bin")
                print("3. Print all garbage in bio bin")
                print("4. Print non-bio bin")
                print("5. Logout")

                user_choice = input("Choose an option (1/2/3/4/5): ")

                if user_choice == '1':
                    print("User name:", user_obj.user_name)
                    user_obj.total_bill_calculation()

                elif user_choice == '2':
                    garbage_type_selection_and_amount_dict = garbage_type_and_amount_selection()
                    if garbage_type_selection_and_amount_dict:
                        source_bin_obj = source_bin()
                        source_bin_obj.receive_garbage(garbage_type_selection_and_amount_dict)
                        source_bin_obj.printing_all_garbage()
                        source_bin_obj.sending_garbage_to_GMP()

                elif user_choice == '3':
                    print("Bio bin garbage print starts............")
                    for grbg in bio_bin_obj.bio_main_garbage_collection:
                        print(grbg)
                    print("Bio bin garbage print ends..............")

                elif user_choice == '4':
                    print("Printing non-bio bin all garbage--------")
                    Non_Bio_bin_obj.printing_garbage()
                    print("Non-Bio bin garbage print ends............")

                elif user_choice == '5':
                    print("Logging out ------")
                    user_obj = None
                    break

    elif choice == '3':
        print("Exiting the Smart Garbage Collection System.")
        break

    else:
        print("Invalid choice. Please choose again.")
