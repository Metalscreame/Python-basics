class Camera:
    def camera_method(self):
        print("Это родительский метод из класса Camera")


# def radio_method(self): # there will be no exception. will be used first as 'Camera' is extends first
#    print("Это родительский метод из класса Camera")


class Radio:
    def radio_method(self):
        print("Это родительский метод из класса Radio")


class CellPhone(Camera, Radio):
    def cell_phone_method(self):
        print("Это дочерний метод из класса CellPhone")

    def call_using_radio(self):
        super().radio_method()

    def take_a_photo(self):
        super().camera_method()


c = CellPhone()

c.cell_phone_method()
c.call_using_radio()
c.take_a_photo()
