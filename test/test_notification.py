import unittest

from notification_service.Notification import Notification


class NotificationTest(unittest.TestCase):
    def testNotificationWithUnsupportedType(self):
        self.assertRaises(
            AttributeError,
            Notification,
            "unknown",
            "content"
        )
