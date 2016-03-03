# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division


class Enviroment(object):
    """Base Enviroment class

    Attributes
    ----------
    observe : callable
        Get observation of the Enviroment's state
    update : callable
        Update Enviroment's state from a given action

    """
    def __init__(self):
        raise NotImplementedError

    def observe(self):
        raise NotImplementedError

    def update(self, action):
        raise NotImplementedError


class Agent(object):
    """Base Agent class

    Parameters
    ----------
    model : :obj:`Model`
        A learning model. Ex: neural network or table
    memory : :obj:`Memory`
        Model's memory for storing experiences for replay and such.

    Attributes
    ----------
    model : :obj:`Model`
        A learning model. Ex: neural network or table
    memory : :obj:`Memory`
        Model's memory for storing experiences for replay and such.
    act : callable
        Get Agent's action given an Enviroment observation
    train : callable
        Train :class:`Enviroment.model` on a batch calculated from
        :class:`Enviroment.memory`

    """
    def __init__(self, model, memory):
        raise NotImplementedError

    def act(self, observation):
        raise NotImplementedError

    def train(self):
        raise NotImplementedError
