#!/usr/bin/python3
#
# Created by Ihor Pleshchuk <ihor.pleshchuk@gmail.com>
# If you have any questions related to this script you can ask to Ihor Pleshchuk <ihor.pleshchuk@gmail.com>

import smtplib

class Smtp():
  def __init__(self, server, port = 25):
    self.server = server
    self.port = port

  def set_sender(self, sender):
    self.sender = sender

  def set_recipients(self, recipients):
    self.recipients = recipients

  def set_server(self, server):
    self.server = server

  def set_port(self, port):
    self.port = port

  def set_subject(self, subject):
    self.subject = subject

  def get_sender(self):
    return self.sender

  def get_recipients(self):
    return self.recipients
