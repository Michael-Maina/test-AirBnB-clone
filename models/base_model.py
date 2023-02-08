#!/usr/bin/python3
"""BaseModel Module"""
from datetime import datetime
import uuid


class BaseModel:
    """
    Class BaseModel defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.strptime(kwargs["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                              "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns an informal string representation of a BaseModel instance
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary with all keys/values of __dict__ of the instance
        """
        inst_dict = self.__dict__
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def save(self):
        """
        Updates public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()
