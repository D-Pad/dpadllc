from db_connection import UserManager, DatabaseConnector

from app_server import start_server
from sys import argv


def test_fn():
    db = DatabaseConnector()
    with open("ips.txt", "r") as file:
        ips = [i.split(',')[0] for i in file.readlines()]
   
    for ip in ips:
        db.update_visitor_count(ip)


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

