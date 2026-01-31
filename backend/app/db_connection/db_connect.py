import psycopg2
from os import environ


TABLE_SCHEMAS = {
    "visitor_counter": """
    CREATE TABLE visitor_counter (
        id              BIGSERIAL PRIMARY KEY,
        ip_address      INET,
        last_visit      TIMESTAMPTZ 
            DEFAULT CURRENT_TIMESTAMP
            NOT NULL,

        CONSTRAINT uniq_ip UNIQUE (ip_address)
    );

    -- Optional: make sure the timestamp is always updated on row change
    CREATE OR REPLACE FUNCTION update_last_visit()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.last_visit = CURRENT_TIMESTAMP;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

    CREATE TRIGGER trg_visitor_counter_update_last_visit
        BEFORE UPDATE ON visitor_counter
        FOR EACH ROW
        EXECUTE FUNCTION update_last_visit();
    """,

    "user_login": """
    CREATE TABLE IF NOT EXISTS user_login (
        id              BIGSERIAL PRIMARY KEY,

        username        VARCHAR(50) NOT NULL,
        password_hash   VARCHAR(255) NOT NULL,

        created_at      TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
        last_login      TIMESTAMPTZ,

        CONSTRAINT uq_username UNIQUE (username)
    );
    """,

    "invite_codes": """
    CREATE TABLE IF NOT EXISTS invite_codes (
        id          BIGSERIAL PRIMARY KEY,
        code_hash   VARCHAR(255) NOT NULL
    );
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

        self.db_name = "dpad_llc_website"
        self.host = environ.get("DB_HOST_NAME") 
        self.user_name = environ.get("DB_USER_NAME") 
        self.password = environ.get("DB_PASSWORD") 
        self.port = int(environ.get("DB_PORT_NUM", 5432))

        if not all([self.host, self.user_name, self.password]):
            raise ValueError("Must provide DB host, user, and password")

        conn = self.get_connection()
        
        tables = self.execute_query(conn, 
                                    """
                                    SELECT table_name
                                    FROM information_schema.tables
                                    WHERE table_schema = 'public'
                                    """)
       
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

            else:
                connection.commit()


        except psycopg2.ProgrammingError as e:
            log(f"PROGRAMMING ERROR:")
            log(f"{e}")
            log(f"Attempted query: {query_string[:300]}")
            raise ValueError('FAILED')

        except psycopg2.OperationalError as e:
            log(f"OPERATIONAL ERROR: {e}")
            log(f"Attempted query: {query_string[:300]}")
            exit()

    def get_connection(self, db=None) -> None:
        """
        Connect to the database
        """
        # Connect to the database
        conn = psycopg2.connect(
            user=self.user_name, 
            password=self.password, 
            host=self.host,
            database=db if db is not None else self.db_name,
            port=self.port
        )
        return conn

    def get_visitors(self) -> list[list]:
        query = """
        SELECT id, ip_address, last_visit
        FROM visitor_counter; 
        """
        conn = self.get_connection(self.db_name)
        return self.execute_query(conn, query)

    def update_visitor_count(self, user_ip: str):
        query = """
        INSERT INTO visitor_counter (ip_address, last_visit)
        VALUES (%s, CURRENT_TIMESTAMP)
        ON CONFLICT ON CONSTRAINT uniq_ip
        DO UPDATE SET
            last_visit = CURRENT_TIMESTAMP;
        """
        conn = self.get_connection(self.db_name)
        self.execute_query(conn, query, False, (user_ip,))
        conn.close()


