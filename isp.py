# Integration Segregation Principle
"""
In the field of software engineering, the interface-segregation principle (ISP) states
that no client should be forced to depend on methods it does not use.
ISP is intended to keep a system decoupled and thus easier to refactor, change, and redeploy.
"""
from abc import abstractmethod


class Machine:

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):

    def print(self, document):
        return 'Printing Document'

    def fax(self, document):
        return 'Faxing Document'

    def scan(self, document):
        return 'Scanning Document'


class SingleFunctionPrinter(Machine):  # Not a good idea

    def print(self, document):
        return 'Printing Document'

    def fax(self, document):
        raise NotImplementedError('This is a single function printer and does not fax')

    def scan(self, document):
        raise NotImplementedError('This is a single function printer and does not scan')

# Alternative


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        return 'Printing Document'


class MyPrinterScanner(Printer, Scanner):
    def print(self, document):
        return 'Printing Document'

    def scan(self, document):
        return 'Scanning Document'

