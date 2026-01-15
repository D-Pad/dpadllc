from db_connection import DatabaseConnector 

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError 

import secrets 


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

    def add_new_user(self, 
                     username: str, 
                     password: str, 
                     invite_code: str) -> (bool, str):
        """ 
        Returns True if a new user was added
        """
        conn = self.db.get_connection(db="dpad_llc")
        ph = PasswordHasher()

        print("USERNAME", username, "PASSWORD", password, "INVITE", invite_code)
        if self.user_exists(username, conn):
            return False, "Username already exists"

        # Verify the invite code first
        invite_codes = self.db.execute_query(conn, 
                                             "SELECT * FROM invite_codes;")

        valid_invite_code = False
        validated_id = None
        for row in invite_codes:
            code_id = row[0]
            code_hash = row[1]
            try: 
                ph.verify(code_hash, invite_code)
                valid_invite_code = True
                validated_id = code_id 
                break
            except VerifyMismatchError:
                pass

        if not valid_invite_code:
            return False, "Invalid invite code"

        # Security checks
        for key_word in ["select", "delete", "drop", "use"]:
            if key_word in username.lower() or " " in username:
                return False, "Invalid user name"

        if len(password) < 8:
            return False, "Password not long enough"

        if " " in password:
            return False, "Password must not contain spaces"

        # Consume the invite
        query = """ 
        DELETE FROM invite_codes WHERE id = ?;
        """
        self.db.execute_query(conn, query, False, params=(validated_id,))
      
        hashed_password = ph.hash(password) 
        query = """ 
        INSERT INTO user_login (username, password_hash)
        VALUES (?, ?)
        """
        self.db.execute_query(conn, 
                              query, 
                              False, 
                              params=(username, hashed_password))
        
        return True, "User created"

    def generate_invite_codes(self, num_codes=10):
        
        conn = self.db.get_connection("dpad_llc")
        invite_codes = []

        for _ in range(num_codes):
            code = secrets.token_urlsafe(16)
            code_hash = PasswordHasher().hash(code) 
            self.db.execute_query(
                conn,
                """
                INSERT INTO invite_codes (code_hash) 
                VALUES (?);
                """,
                False, 
                params=(code_hash,)
            )
            invite_codes.append(code)
        
        with open("invite_codes.txt", "a") as file:
            file.write("\n".join(invite_codes))

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


