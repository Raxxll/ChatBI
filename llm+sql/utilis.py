import mysql.connector

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Exception as e:
        print(f"The error '{e}' occurred")
    
    return connection

def get_schema(connection):
    cursor = connection.cursor()
    query = """
    SELECT table_name, column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = DATABASE();
    """
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    
    # Formatting the output into a single string
    schema_dict = {}
    for row in results:
        table_name = row[0]
        column_name = row[1]
        data_type = row[2]
        
        # 如果 table_name 不在字典中，初始化一个空字典
        if table_name not in schema_dict:
            schema_dict[table_name] = {}
        
        # 将 column_name 和 data_type 添加到相应的 table_name 字典中
        schema_dict[table_name][column_name] = data_type

    return schema_dict


def run_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

def get_comments(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        # 执行SQL查询
        sql = "SELECT * FROM notation"
        cursor.execute(sql)
        result = cursor.fetchall()
        
        # 将结果格式化为字符串
        comments = "\n".join([f"{row['table_name']} | {row['mapping']}" for row in result])
        cursor.close()
        return comments
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_sql(x):
    return x.split("```sql")[1].split("```")[0]

