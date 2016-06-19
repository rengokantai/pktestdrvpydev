__author__ = 'Hernan Y.Ke'
import unittest
from ..event import Event
class EventTest(unittest.TestCase):
    def test_listener_when_is_raised(self):
        called = False
        def listener():
            nonlocal called
            called =True
        event = Event()
        event.connect(listener)
        event.fire()
        self.assertTrue(called)
