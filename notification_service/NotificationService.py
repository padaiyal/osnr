from abc import abstractmethod
from dataclasses import dataclass

from typing import Tuple

from email_validator import validate_email

from notification_service.Notification import Notification
from notification_service.NotificationType import NotificationType


@dataclass
class NotificationService:
    """
    Template to abstract the necessary logic to send notifications via a service.
    """

    def __init__(self, notification_service: str, credentials: dict, supported_notification_types: set) -> None:
        """
        Initialize the notification service.
        :param notification_service: Notification service name.
        :param credentials: Credentials for the notification service.
        :param supported_notification_types: Types of notifications supported by this service.
        """
        self.notification_service: str = notification_service
        self.credentials: dict = credentials.copy()
        self.validate_credentials()
        if not supported_notification_types.issubset(NotificationType.NOTIFICATION_TYPES):
            raise AttributeError(
                f"For {notification_service} notification service, supported notification types "
                f"{supported_notification_types}) contains invalid values. Valid values are: "
                f"{NotificationType.NOTIFICATION_TYPES}"
            )
        self.supported_notification_types: set = supported_notification_types.copy()

    @abstractmethod
    def validate_credentials(self) -> None:  # pragma: nocover
        """
        Validates the credentials for this notification service. Throws an exception if it's invalid.
        """
        pass

    @abstractmethod
    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:  # pragma: nocover
        """
        Notifies the desired recipients through this service.
        :param recipients: Recipients to notify.
        :param notification: Notification to send.
        """
        pass


@dataclass
class Email(NotificationService):

    def __init__(self, credentials: dict):
        super().__init__(
            notification_service=str(self.__class__).lower(),
            credentials=credentials,
            supported_notification_types={NotificationType.TEXT}
        )

    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:
        # TODO:
        all(validate_email(recipient) for recipient in recipients)
        pass

    def validate_credentials(self) -> None:
        validate_email(self.credentials['email'])


class Mobile(NotificationService):

    def __init__(self, credentials: dict):
        super().__init__(
            notification_service=str(self.__class__).lower(),
            credentials=credentials,
            supported_notification_types={NotificationType.TEXT}
        )

    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:
        # TODO:
        pass

    def validate_credentials(self) -> None:
        # TODO:
        pass


class Slack(NotificationService):

    def __init__(self, credentials: dict):
        super().__init__(
            notification_service=str(self.__class__).lower(),
            credentials=credentials,
            supported_notification_types={NotificationType.TEXT}
        )

    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:
        # TODO:
        pass

    def validate_credentials(self) -> None:
        # TODO:
        pass


class Teams(NotificationService):

    def __init__(self, credentials: dict):
        super().__init__(
            notification_service=str(self.__class__).lower(),
            credentials=credentials,
            supported_notification_types={NotificationType.TEXT}
        )

    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:
        # TODO:
        pass

    def validate_credentials(self) -> None:
        # TODO:
        pass


class Zoom(NotificationService):

    def __init__(self, credentials: dict):
        super().__init__(
            notification_service=str(self.__class__).lower(),
            credentials=credentials,
            supported_notification_types={NotificationType.TEXT}
        )

    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:
        # TODO:
        pass

    def validate_credentials(self) -> None:
        # TODO:
        pass
