#!/usr/bin/env python3
import bcrypt

class User:

  def __init__(self, username: str, password: str, cookie = None):
    self.username = username
    self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    self.cookie = cookie

  def checkPassword(self, pw: str):
    return bcrypt.checkpw(pw.encode('utf-8'), self.password)
    
  def __str__(self):
    return "Username: {0}\nHashed Passsword: {1}\nCookie Exists: {2}".format(self.username, self.password, bool(self.cookie))

  def __repr__(self):
    return str(self)
