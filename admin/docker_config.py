SECRET_KEY = '__PDNS_ADMIN_SECRET_KEY__' # python3 -c 'import secrets; print(secrets.token_hex())'
PORT = 80
SQLALCHEMY_DATABASE_URI = 'postgresql://__PSQL_PDNS_ADMIN__:__PSQL_PDNS_ADMIN_PASSWORD__@__PSQL_PDNS_ADMIN_HOST__:__PSQL_PDNS_ADMIN_PORT__/__PSQL_PDNS_ADMIN_DB__?sslmode=verify-full'
