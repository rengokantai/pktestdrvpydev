__author__ = 'Hernan Y.Ke'
import smtplib
import unittest
from unittest import mock

from ..action import PrintAction
@mock.patch("builtins.print")
class PrintActionTest(unittest.TestCase):
    def test_executing_action_prints_message(self, mock_print):
        action = PrintAction()
        action.execute("test")
        mock_print.assert_called_with("test")