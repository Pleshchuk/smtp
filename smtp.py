#!/usr/bin/python3
#
# Created by Ihor Pleshchuk <ihor.pleshchuk@gmail.com>
# If you have any questions related to this script you can ask to Ihor Pleshchuk <ihor.pleshchuk@gmail.com>

import smtplib

class Smtp():
  def __init__(self, server, port = 25):
    self.server = server
    self.port = port