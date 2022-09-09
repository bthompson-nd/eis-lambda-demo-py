"""The main Lambda module"""
import json
import cx_Oracle  # type: ignore

# import snowflake.connector # type: ignore
from lambda_types import LambdaDict, LambdaContext


def lambda_handler(event: LambdaDict, context: LambdaContext) -> LambdaDict:
    """The main Lambda handler. The entry point for your logic."""
    print("Event: {} | Context: {} | Starting...".format(str(event), str(context)))
    lib_dir = "/opt/instantclient_21_7"
    try:
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
        print("Oracle initialized")
    except Exception as oracle_exception:
        print("Oracle already initialized. " + str(oracle_exception))
    connection = cx_Oracle.connect(
        user=event["user"], password=event["password"], dsn=event["dsn"]
    )
    print("Connection made")
    cursor = connection.cursor()
    print("Cursor created")
    cursor.execute("""select firstname,lastname,age from PEOPLE order by age desc""")
    print("Query executed")
    rows = []
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        print(row)
        rows.append(row)
    print("Rows parsed")

    return {"statusCode": 200, "body": json.dumps(rows)}
