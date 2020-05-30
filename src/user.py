#!/usr/bin/env python3
import pickle, bcrypt, os
from requests import session

DIR = os.path.join(os.getcwd(), "data")
if not os.path.isdir(DIR):
  print("Creating data directory")
  os.makedirs(DIR)

class User:

  def __init__(self, username: str, password: str):
    self.userFilePath = os.path.join(DIR, "{0}.cookie".format(username))
    try:
      with open(self.userFilePath, "rb") as f:
        user = pickle.load(f)
      if (username == user.username and user.checkPassword(password)):
        print("User found, loading cookie...")
        self.cookie = user.cookie
        self.password = user.password
    except FileNotFoundError:
      print("User not found, creating new profile...")
      self.cookie = None
      self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    finally:
      self.username = username

  def updateCookie(self, cookie: session):
    self.cookie = cookie

  def saveUser(self):
    with open(self.userFilePath, "wb") as f:
      pickle.dump(self, f)

  def checkPassword(self, pw: str):
    return bcrypt.checkpw(pw.encode('utf-8'), self.password)

  def __str__(self):
    return "Username: {0}\nHashed Passsword: {1}\nCookie Exists: {2}".format(self.username, self.password, bool(self.cookie))

  def __repr__(self):
    return str(self)

def test():
  user = User("abc", "qwer")
  print(user)
  user.saveUser()

if __name__ == "__main__":
  test()
