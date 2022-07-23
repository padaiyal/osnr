from abc import abstractmethod
from dataclasses import dataclass
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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
        # Validates the email of each recipient.
        all(validate_email(recipient) for recipient in recipients)
        # Sends the message to each recipient.
        for recipient in recipients:
            # Sets the variables for the message.
            message: Mail = Mail(from_email=self.credentials['email'],
                                 to_emails=recipient,
                                 subject=notification.content,
                                 plain_text_content=notification.content)
            # Initializes the api with the ssh_key.
            sg = SendGridAPIClient(self.credentials['ssh_key'])
            # Sends the message to the recipient.
            sg.send(message)

    def validate_credentials(self) -> bool:
        # Check if a sender's email has been given in the credentials.
        if 'email' not in self.credentials.keys():
            raise AttributeError('Email has to be given in credentials.')
        # Check if the email given in the credentials is none.
        elif self.credentials['email'] is None:
            raise AttributeError("The given email can't be none.")
        # Check if the email format is valid.
        validate_email(self.credentials['email'])
        # Check if an ssh_key as been given in the credentials.
        if 'ssh_key' not in self.credentials.keys():
            raise AttributeError('The sendgrid ssh key has to be given in the credentials dictionary.')
        # Check if the ssh_key given in the credentials is none.
        elif self.credentials['ssh_key'] is None:
            raise AttributeError('The sendgrid ssh key has to be given in the credentials dictionary.')
        return True


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


class Whatsapp(NotificationService):

    def __init__(self, credentials: dict):
        super().__init__(
            notification_service=str(self.__class__).lower(),
            credentials=credentials,
            supported_notification_types={NotificationType.TEXT}
        )

    def notify(self, recipients: Tuple[str, ...], notification: Notification) -> None:  # pragma no cover
        # TODO:
        pass

    def validate_credentials(self) -> None:
        # TODO:
        pass
