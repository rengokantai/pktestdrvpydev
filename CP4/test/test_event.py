__author__ = 'Hernan Y.Ke'
import unittest
from unittest import mock
from ..event import Event

# class Mock:
#     def __init__(self):
#         self.called = False
#         self.params = ()
#     def __call__(self, *args, **kwargs):
#         self.called=True
#         self.params=(args,kwargs)
class EventTest(unittest.TestCase):
    def test_listener_when_is_raised(self):
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire()
        self.assertTrue(listener.called)

    def test_listener_params(self):
        listener = mock.Mock()
        event = Event()
        event.connect(listener)
        event.fire(1,b='b')
        listener.assert_called_with(1,b='b')
        listener.assert_has_calls([mock.call(1,b='b')])
        listener.assert_any_call(1,b='b')