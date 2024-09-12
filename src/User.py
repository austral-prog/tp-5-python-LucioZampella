class User:
    def __init__(self, dni, name, number_of_checkouts=0, number_of_checkins=0):
        self.__dni = dni
        self.__name = name
        self.__number_of_checkouts = number_of_checkouts
        self.__number_of_checkins = number_of_checkins

    # Getters
    def get_dni(self):
        return self.__dni

    def get_name(self):
        return self.__name

    def get_number_of_checkouts(self):
        return self.__number_of_checkouts

    def get_number_of_checkins(self):
        return self.__number_of_checkins

    # Setters
    def increment_checkouts(self):
        self.__number_of_checkouts += 1

    def increment_checkins(self):
        self.__number_of_checkins += 1