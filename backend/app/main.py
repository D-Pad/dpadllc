from db_connection import UserManager 

from app_server import start_server
from sys import argv


def test_fn():
    pass


def main():
    args = argv[1:]
   
    if len(args) > 0:
        
        if args[0] == "invite":
            um = UserManager()
            um.generate_invite_codes()
            return
        
        elif args[0] == "test":
            test_fn()

    else:
        start_server()


if __name__ == "__main__":
    main() 

