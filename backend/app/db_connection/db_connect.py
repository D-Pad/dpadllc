import mariadb 
from os import environ


TABLE_SCHEMAS = {
    "visitor_counter": """
    CREATE TABLE visitor_counter (
        id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        ip_address INET6,
        last_visit TIMESTAMP 
          DEFAULT CURRENT_TIMESTAMP
          ON UPDATE CURRENT_TIMESTAMP,
        UNIQUE KEY uniq_ip (ip_address)
    ) ENGINE=InnoDB;
    """,
    
    "user_login": """
    CREATE TABLE IF NOT EXISTS user_login (
        id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

        username VARCHAR(50) NOT NULL,
        password_hash VARCHAR(255) NOT NULL,

        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP NULL DEFAULT NULL,

        UNIQUE KEY uq_username (username)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
} 


log = print


class DatabaseConnector:

    _instance = None 
    _initialized = False 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
        return cls._instance 

    def __init__(self) -> None:

        if self._initialized:
            return

        self.db_name = "dpad_llc"
        self.host = environ.get("DB_HOST_NAME") 
        self.user_name = environ.get("DB_USER_NAME") 
        self.password = environ.get("DB_PASSWORD") 

        if not all([self.host, self.user_name, self.password]):
            raise ValueError("Must provide DB host, user, and password")

        conn = self.get_connection()
        databases = self.execute_query(conn, "SHOW DATABASES")
      
        if self.db_name not in databases:
            q_string = f"CREATE DATABASE IF NOT EXISTS {self.db_name};"
            self.execute_query(conn, q_string, False)
            self.execute_query(conn, f"USE {self.db_name};", False)

        self.execute_query(conn, f"USE {self.db_name};", False)
        tables = self.execute_query(conn, "SHOW TABLES;")
        
        for table_name, schema in TABLE_SCHEMAS.items():
            if table_name not in tables:
                self.execute_query(conn, schema, False)

        conn.close()
        self._initialized = True

    def execute_query(self,
                      connection,
                      query_string: str,
                      fetching=True,
                      params=None) -> list[list] | list:
        """
        Execute a query string if it's valid
        """
        if query_string[-1] != ';':
            query_string += ';'

        try:
            cur = connection.cursor()
            if params:
                cur.execute(query_string, params)
            else:
                cur.execute(query_string)
            
            if fetching:
                data = [[j for j in i] for i in cur]
                cur.close()
                if len(data) > 0 and len(data[0]) == 1:
                    return [i[0] for i in data]
                else:
                    return data

        except mariadb.ProgrammingError as e:
            log(f"PROGRAMMING ERROR:")
            log(f"{e}")
            log(f"Attempted query: {query_string[:300]}")
            raise ValueError('FAILED')

        except mariadb.OperationalError as e:
            log(f"OPERATIONAL ERROR: {e}")
            log(f"Attempted query: {query_string[:300]}")
            exit()

    def get_connection(self, db=None) -> None:
        """
        Connect to the database
        """
        # Connect to the database
        conn = mariadb.connect(
            user=self.user_name, 
            password=self.password, 
            host=self.host,
            database=db,
            autocommit=True 
        )
        return conn

    def get_visitors(self) -> list[list]:
        query = "SELECT * FROM visitor_counter;"
        conn = self.get_connection(self.db_name)
        return self.execute_query(conn, query)

    def update_visitor_count(self, user_ip: str):
        query = """INSERT INTO visitor_counter (ip_address) 
                    VALUES (?)
                    ON DUPLICATE KEY 
                      UPDATE last_visit = CURRENT_TIMESTAMP;"""
        conn = self.get_connection(self.db_name)
        self.execute_query(conn, query, False, (user_ip,))
        conn.close()


