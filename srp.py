# SRP or SOC
# Anti Pattern: GOD object

class Journal:
    """
    This class is used to record, remove, and print, daily journals
    """
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)

    # def save(self, filepath):  # Contradicts SRP
    #     pass
    #
    # def load_from_file(self, filepath):  # Contradicts SRP
    #     pass
    #
    # def load_from_web(self, uri):  # Contradicts SRP
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()


j1 = Journal()

j1.add_entry('I cried today')
j1.add_entry('I ate a bug')
print(j1)

filename = 'j1.txt'
PersistenceManager.save_to_file(j1, filename)