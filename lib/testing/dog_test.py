# lib/dog_test.py

import pytest
from lib.dog import Dog

class TestDog:
    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog(name="Fido", breed="Labrador")
        assert isinstance(fido, Dog)
        assert fido.name == "Fido"
        assert fido.breed == "Labrador"

    def test_default_breed(self):
        '''Dog.__init__ should default breed to "Mutt"'''
        fido = Dog(name="Fido")
        assert fido.breed == "Mutt"

    def test_sit_method(self):
        '''Dog class has a sit method'''
        fido = Dog(name="Fido", breed="Labrador")
        assert hasattr(fido, 'sit')
        fido.sit()
