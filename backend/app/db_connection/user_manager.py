from db_connection import DatabaseConnector 

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError 


class UserManager:
 
    _instance = None 
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
        return cls._instance 

    def __init__(self) -> None:
      
        if self._initialized: 
            return 
        
        self.db = DatabaseConnector()
        self.initialized = True

    def add_new_user(self, username: str, password: str) -> bool:
        """ 
        Returns True if a new user was added
        """

        conn = self.db.get_connection(db="dpad_llc")

        if self.user_exists(username, conn):
            return False

        hashed_password = PasswordHasher().hash(password) 
        
        query = """ 
        INSERT INTO user_login (username, password_hash)
        VALUES (?, ?)
        """
        self.db.execute_query(conn, 
                              query, 
                              False, 
                              params=(username, hashed_password))
        return True

    def user_exists(self, username: str, conn=None) -> bool:
       
        if conn is None:
            conn = db.get_connection(db="dpad_llc")
        
        existing = self.db.execute_query(conn, 
                                         "SELECT username FROM user_login;",
                                         True) 
        if username in existing:
            return True 
        return False

    def verify_password(self, username: str, password: str) -> bool:
        conn = self.db.get_connection(db="dpad_llc")
        data = self.db.execute_query(
            conn, 
            "SELECT password_hash FROM user_login WHERE username = ?",
            params=(username,)
        )

        if len(data) > 0:
            user_password_hash = data[0]
          
            try: 
                valid = PasswordHasher().verify(user_password_hash, password)
            except VerifyMismatchError:
                valid = False
            return valid


