from dataclasses import dataclass


@dataclass
class NotificationType:
    """
    Contains the types of notifications supported by this project.
    """

    TEXT = 'text'
    AUDIO = 'audio'
    NOTIFICATION_TYPES = {TEXT, AUDIO}
