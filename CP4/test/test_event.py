__author__ = 'Hernan Y.Ke'
import unittest
from ..event import Event

class Mock:
    def __init__(self):
        self.called = False
        self.params = ()
    def __call__(self, *args, **kwargs):
        self.called=True
        self.params=(args,kwargs)
class EventTest(unittest.TestCase):
    def test_listener_when_is_raised(self):
        listener = Mock()
        event = Event()
        event.connect(listener)
        event.fire()
        self.assertTrue(listener.called)

    def test_listener_params(self):
        listener = Mock()
        event = Event()
        event.connect(listener)
        event.fire(1,b='b')
        self.assertEqual(((1,),{'b':'b'}),listener.params)
