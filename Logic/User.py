class User:
  def __init__(self, email: str, username: str, password: str):
    self.email: str = email
    self.username: str = username
    self.password: str = password
  
  def PasswordSize(self) -> int:
    return len(self.password)

  def __str__(self):
    userString = ""
    
    userString += f"Email: {self.email}\n"
    userString += f"Username: {self.username}\n"
    userString += f"Password: "

    passwordSize = self.PasswordSize()
    for character in range(passwordSize):
      userString += "*"

    return userString