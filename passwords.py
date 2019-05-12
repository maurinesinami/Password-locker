class User:
"""
Class that generate new instances of a user
"""
    user_list =[]
    def __init__(self,username,account,password):
        self.username = username
        self.account = account
        self.password = password