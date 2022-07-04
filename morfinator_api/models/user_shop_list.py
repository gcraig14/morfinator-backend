# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from morfinator_api.models.base_model_ import Model
from morfinator_api.models.ingredient import Ingredient
from morfinator_api import util


class UserShopList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, user_id: int=None, ingredient: Ingredient=None, in_stock: bool=None):  # noqa: E501
        """UserShopList - a model defined in Swagger

        :param user_id: The user_id of this UserShopList.  # noqa: E501
        :type user_id: int
        :param ingredient: The ingredient of this UserShopList.  # noqa: E501
        :type ingredient: Ingredient
        :param in_stock: The in_stock of this UserShopList.  # noqa: E501
        :type in_stock: bool
        """
        self.swagger_types = {
            'user_id': int,
            'ingredient': Ingredient,
            'in_stock': bool
        }

        self.attribute_map = {
            'user_id': 'user_id',
            'ingredient': 'ingredient',
            'in_stock': 'in_stock'
        }

        self._user_id = user_id
        self._ingredient = ingredient
        self._in_stock = in_stock

    @classmethod
    def from_dict(cls, dikt) -> 'UserShopList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UserShopList of this UserShopList.  # noqa: E501
        :rtype: UserShopList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user_id(self) -> int:
        """Gets the user_id of this UserShopList.


        :return: The user_id of this UserShopList.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this UserShopList.


        :param user_id: The user_id of this UserShopList.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def ingredient(self) -> Ingredient:
        """Gets the ingredient of this UserShopList.


        :return: The ingredient of this UserShopList.
        :rtype: Ingredient
        """
        return self._ingredient

    @ingredient.setter
    def ingredient(self, ingredient: Ingredient):
        """Sets the ingredient of this UserShopList.


        :param ingredient: The ingredient of this UserShopList.
        :type ingredient: Ingredient
        """

        self._ingredient = ingredient

    @property
    def in_stock(self) -> bool:
        """Gets the in_stock of this UserShopList.


        :return: The in_stock of this UserShopList.
        :rtype: bool
        """
        return self._in_stock

    @in_stock.setter
    def in_stock(self, in_stock: bool):
        """Sets the in_stock of this UserShopList.


        :param in_stock: The in_stock of this UserShopList.
        :type in_stock: bool
        """

        self._in_stock = in_stock