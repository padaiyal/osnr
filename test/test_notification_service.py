import unittest
from typing import Dict, Tuple

from email_validator import EmailSyntaxError

from notification_service.Notification import Notification
# noinspection PyUnresolvedReferences
from notification_service.NotificationService \
    import Email, Mobile, NotificationService, Slack, Teams, Zoom  # noqa: F401
from notification_service.NotificationType import NotificationType


class NotificationServiceTest(unittest.TestCase):
    notification_services = dict()
    tests: Tuple[dict] = ()

    @staticmethod
    def get_notification_service(expected_name: str, credentials: Dict[str, str]) -> NotificationService:
        for notification_service_cls in NotificationService.__subclasses__():
            name: str = notification_service_cls.__name__.lower()
            if expected_name == name:
                # noinspection PyArgumentList
                return notification_service_cls(credentials)

    @staticmethod
    def setUpClass(**kwargs) -> None:
        credentials: Dict[str, dict] = {  # TODO: Add credentials.
            'email': {
                'email': 'abc@gmail.com',
            },  # https://docs.python.org/3/library/email.examples.html
            'mobile': {},  # https://www.twilio.com/docs/libraries/python
            'slack': {},  # https://slack.dev/python-slack-sdk/
            'teams': {},
            'zoom': {}  # https://marketplace.zoom.us/docs/api-reference/using-zoom-apis
        }
        invalid_credentials: Dict[str, dict] = {  # TODO: Add invalid credentials.
            'email': {
                'email': 'abc#gmail.com',
            },
            'mobile': {},
            'slack': {},
            'teams': {},
            'zoom': {}
        }
        for notification_service_cls in NotificationService.__subclasses__():
            name: str = notification_service_cls.__name__.lower()
            # noinspection PyArgumentList
            NotificationServiceTest.notification_services[name] = notification_service_cls(credentials[name])

        NotificationServiceTest.tests = (
            {
                'name': 'Email notification - Valid scenarios',
                'notification_service_name': 'email',
                'recipients': ('sender@mail.com',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': credentials['email'],
                'expected_init_exception': None,
                'expected_notify_exception': None,
            },
            # TODO: Add all scenarios
            {
                'name': 'Email notification - Invalid recipient',
                'notification_service_name': 'email',
                'recipients': ('sender#mail.com',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': credentials['email'],
                'expected_init_exception': None,
                'expected_notify_exception': EmailSyntaxError,
            },
            {
                'name': 'Email notification - Invalid credentials',
                'notification_service_name': 'email',
                'recipients': ('sender@mail.com',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': invalid_credentials['email'],
                'expected_init_exception': EmailSyntaxError,
                'expected_notify_exception': None,
            },
            # {
            #     'name': 'Email notification - Unsupported notification types',
            #     'notification_service_name': 'email',
            #     'recipients': ('',),
            #     'notification': Notification('unknown', 'content'),
            #     'expected_init_exception': None,
            #     'expected_notify_exception': AttributeError,
            # },
            {
                'name': 'Slack notification - Valid scenarios',
                'notification_service_name': 'slack',
                'recipients': ('',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': credentials['slack'],
                'expected_init_exception': None,
                'expected_notify_exception': None,
            },
            # {
            #     'name': 'Slack notification - Invalid recipient',
            # },
            # {
            #     'name': 'Slack notification - Unsupported notification types',
            # },
            {
                'name': 'Zoom notification - Valid scenarios',
                'notification_service_name': 'zoom',
                'recipients': ('',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': credentials['zoom'],
                'expected_init_exception': None,
                'expected_notify_exception': None,
            },
            # {
            #     'name': 'Zoom notification - Invalid recipient',
            # },
            # {
            #     'name': 'Zoom notification - Unsupported notification types',
            # },
            {
                'name': 'Teams notification - Valid scenarios',
                'notification_service_name': 'teams',
                'recipients': ('',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': credentials['teams'],
                'expected_init_exception': None,
                'expected_notify_exception': None,
            },
            # {
            #     'name': 'Teams notification - Invalid recipient',
            # },
            # {
            #     'name': 'Teams notification - Unsupported notification types',
            # },
            {
                'name': 'Mobile notification - Valid scenarios',
                'notification_service_name': 'mobile',
                'recipients': ('',),
                'notification': Notification(NotificationType.TEXT, "This message is like Schrodinger's cat"),
                'credentials': credentials['mobile'],
                'expected_init_exception': None,
                'expected_notify_exception': None,
            },
            # {
            #     'name': 'Mobile notification - Invalid recipient',
            # },
            # {
            #     'name': 'Mobile notification - Unsupported notification types',
            # },
        )

    def testNotify(self):
        for test in NotificationServiceTest.tests:
            notification_service_name: str = test['notification_service_name']
            if test['expected_init_exception']:
                self.assertRaises(
                    test['expected_init_exception'],
                    self.get_notification_service,
                    notification_service_name,
                    test['credentials']
                )
            else:
                notification_service: NotificationService = self.get_notification_service(
                    notification_service_name,
                    test['credentials']
                )
                if test['expected_notify_exception']:
                    self.assertRaises(
                        test['expected_notify_exception'],
                        notification_service.notify,
                        test['recipients'],
                        test['notification'],
                    )
                else:
                    self.assertIsNone(
                        notification_service.notify(
                            test['recipients'],
                            test['notification'],
                        )
                    )

    def testNotificationServiceWithInvalidNotificationType(self):
        class NewNotificationService(NotificationService):
            def __init__(self, credentials: dict):
                super(NewNotificationService, self).__init__("new_notification_service", credentials, {"invalid"})

            def validate_credentials(self) -> None:
                pass

            def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:  # pragma: nocover
                pass

        self.assertRaises(
            AttributeError,
            NewNotificationService,
            {}
        )
