class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=self.root_name)

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def __str__(self):
        return str(self.__root)


# if you want to build a simple HTML paragraph using a list
hello = 'hello'
parts = ['<p>', hello, '</p>']
print(''.join(parts))

# now I want an HTML list with 2 words in it
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))

print('-' * 10)

h1 = HtmlElement('p', 'It is a paragraph')
print(h1)
h2 = HtmlElement('div', text='This is a div with a paragraph:')
h2.elements = [h1]
print(h2)

print('-' * 10)

h3 = HtmlElement()
print(h3)

print('-' * 10)

builder = HtmlBuilder('ul')
builder.add_child('li', 'hello')
builder.add_child('li', 'world')
print(builder)

print('-' * 10)

builder = HtmlBuilder('ul')
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
print(builder)

print('-' * 10)

builder = HtmlElement.create('ul')
builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
print(builder)
