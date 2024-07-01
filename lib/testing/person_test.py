# lib/person_test.py

import pytest
from lib.person import Person

class TestPerson:
    def test_is_class(self):
        '''is a class with the name "Person"'''
        john = Person(name="John")
        assert isinstance(john, Person)
        assert john.name == "John"

    def test_talk_method(self):
        '''Person class has a talk method'''
        john = Person(name="John")
        assert hasattr(john, 'talk')
        john.talk()

    def test_walk_method(self):
        '''Person class has a walk method'''
        john = Person(name="John")
        assert hasattr(john, 'walk')
        john.walk()
