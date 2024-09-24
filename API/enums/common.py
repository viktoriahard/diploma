from enum import Enum


class Status(Enum):
    """
    Pet Statuses
    """
    Available: str = 'available'
    NotAvailable: str = 'not-available'


