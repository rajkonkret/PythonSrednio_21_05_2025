# klasy mixin

class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_document(self):
        print("Skanowanie dokumentu...")
        return "Zawartość dokumentu"


class MultiDevice(Printer, Scanner):
    def photo_copy(self):
        content = self.scan_document()
        self.print_message(content)


device = MultiDevice()
device.photo_copy()
