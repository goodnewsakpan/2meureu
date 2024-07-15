from __future__ import annotations
from libs.decorator import android_only
import socket


def get_connect(func, host="8.8.8.8", port=53, timeout=3):
    """Checks for an active Internet connection."""

    def wrapped(*args):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
                (host, port)
            )
            return func(*args)
        except Exception:
            return False

    return wrapped


class DataBase:
    """
    Your methods for working with the database should be implemented in this
    class.
    """

    name = "Firebase"

    def __init__(self):
        self.firestore = None
        self.storage = None
        self.database = None
        self.user = None
        self.auth = None
        self.android_thing()

    @android_only
    def android_thing(self):
        from sjfirebase.jclass import (
            SJFirebaseAuthEmail,
            SJFirebaseUser,
            SJFirebaseDatabase,
            SJFirebaseStorage,
            SJFirebaseFirestore
        )
        self.auth = SJFirebaseAuthEmail
        self.user = SJFirebaseUser
        self.database = SJFirebaseDatabase
        self.storage = SJFirebaseStorage
        self.firestore = SJFirebaseFirestore


