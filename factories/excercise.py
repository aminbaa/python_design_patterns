"""
You are given a class called `Person`. The person has two attributes: `id` and `name`.
Implement a personFactory that has a non_static `create_person` method that takes a person's
name and returns a person initialized with him name and id.
The id of the person should be set as 0-based index of the object created. So the first person should
have id=0, the second 1, and so on.
"""

from unittest import TestCase


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


class Evaluate(TestCase):
    def test_exercise(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)