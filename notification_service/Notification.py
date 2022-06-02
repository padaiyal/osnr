from dataclasses import dataclass

from notification_service.NotificationType import NotificationType


@dataclass
class Notification:
    """
    Abstracts the notification to be sent.
    """

    def __init__(self, notification_type: str, content: str):
        """
        Initializes the notification.
        :param notification_type: Type of notification.
        :param content: Content of the notification.
        """
        if notification_type not in NotificationType.NOTIFICATION_TYPES:
            raise AttributeError(f"Unsupported notification type ({notification_type}). "
                                 f"The supported notification types are: "
                                 f"{NotificationType.NOTIFICATION_TYPES}")
        self.type = notification_type
        self.content = content
