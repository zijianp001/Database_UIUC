"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Product NATURAL JOIN CPU;").fetchall()
    conn.close()
    cpu_list = []
    for result in query_results:
        item = {
            "ProductId": result[0],
            "BrandName": result[1],
            "ProductName": result[2],
            "CodeName": result[3],
            "Cores": result[4],
            "Clock": result[5],
            "CPUSocket": result[6],
            "CPUProcess": result[7],
            "L3_Cache": result[8],
            "TDP": result[9],
            "ReleaseYear": result[10]
        }
        cpu_list.append(item)

    return cpu_list


def search_task_by_ProductName(keyword: str) -> dict:
    conn = db.connect()
    query = "Select * from Product NATURAL JOIN CPU WHERE ProductName LIKE %s;", (keyword)
    query_results = conn.execute(query).fetchall()
    conn.close()
    list = []
    for result in query_results:
        item = {
            "ProductId": result[0],
            "BrandName": result[1],
            "ProductName": result[2],
            "CodeName": result[3],
            "Cores": result[4],
            "Clock": result[5],
            "CPUSocket": result[6],
            "CPUProcess": result[7],
            "L3_Cache": result[8],
            "TDP": result[9],
            "ReleaseYear": result[10]
        }
        list.append(item)

    return list




def remove_task_by_id(product_id: float) -> None:
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From CPU where ProductId={};'.format(product_id)
    conn.execute(query)
    conn.close()



def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """

    conn = db.connect()
    query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(t1: float, t2: str, t3: str, t4: str, t5: str, t6: str, t7:str, t8: str, t9: str, t10: str, t11: int) ->  None:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    conn = db.connect()
    query1 = 'Insert Into Product VALUES ({}, "{}", "{}");'.format(t1, t2, t3)
    query2 = 'Insert Into CPU VALUES ({}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", {});'.format(t1, t4, t5, t6, t7, t8, t9, t10, t11)
    conn.execute(query1)
    conn.execute(query2)
    conn.close()



