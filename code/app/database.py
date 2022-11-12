from app import db

def fetch_todo() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product NATURAL JOIN CPU;")
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    cpu_list = []
    for result in results:
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

    return cpu_list, keys




def remove_task_by_id(product_id: float) -> None:
    conn = db.connect()
    query = 'Delete From CPU where ProductId={};'.format(product_id)
    conn.execute(query)
    conn.close()




def insert_new_task(t1: float, t2: str, t3: str, t4: str, t5: str, t6: str, t7:str, t8: str, t9: str, t10: str, t11: int) ->  None:
    conn = db.connect()
    query1 = 'Insert Into Product VALUES ({}, "{}", "{}");'.format(t1, t2, t3)
    query2 = 'Insert Into CPU VALUES ({}, "{}", "{}", "{}", "{}", "{}", "{}", "{}", {});'.format(t1, t4, t5, t6, t7, t8, t9, t10, t11)
    conn.execute(query1)
    conn.execute(query2)
    conn.close()




def update_attributes(t1: float, t2: str, t3: str, t4: str, t5: str, t6: str, t7:str, t8: str, t9: str, t10: str, t11: int) ->  None:
    conn = db.connect()
    query1 = 'UPDATE Product NATURAL JOIN CPU SET Product.BrandName = "{}", Product.ProductName = "{}", CPU.CodeName = "{}", CPU.Cores= "{}", CPU.Clock = "{}", CPU.CPUSocket = "{}",CPU.CPUProcess = "{}", CPU.L3_Cache = "{}", CPU.TDP= "{}", CPU.ReleaseYear = {} WHERE ProductId = {};'.format(t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t1)
    conn.execute(query1)
    conn.close()




def search_task_by_ProductName(keyword) -> dict:
    conn = db.connect()
    query = 'Select * from Product NATURAL JOIN CPU WHERE ProductName LIKE "%%{}%%" or BrandName LIKE "%%{}%%" or CodeName LIKE "%%{}%%" or Cores LIKE "%%{}%%" or Clock LIKE "%%{}%%" or CPUSocket LIKE "%%{}%%" or CPUProcess LIKE "%%{}%%" or L3_Cache LIKE "%%{}%%" or TDP LIKE "%%{}%%" or ReleaseYear LIKE "%%{}%%" or ProductId LIKE "%%{}%%";'.format(keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword)
    print(query)
    query_results = conn.execute(query)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    search_list = []
    for result in results:
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
        search_list.append(item)

    return search_list, keys




def search_adquery() -> dict:
    conn = db.connect()
    query = 'Select * from MotherBoard m NATURAL JOIN Product p WHERE Socket = (SELECT c.CPUSocket from CPU c natural join Product p where ProductName LIKE "Ryzen 7 5700x%%");'
    query_results = conn.execute(query)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    query_list = []
    for result in results:
        item = {
            "ProductId": result[0],
            "BrandName": result[1],
            "ProductName": result[2],
            "CodeName": result[3],
            "Cores": result[4],
            "Clock": result[5],
        }
        query_list.append(item)

    return query_list, keys




def search_adquery2() -> dict:
    conn = db.connect()
    query = 'select Count(*), c.CPUProcess from CPU c NATURAL JOIN Product p where CPUSocket = (select m.Socket from MotherBoard m natural join Product p where ProductName like "ASUS TUF Gaming X470 ATX%%") group by c.CPUProcess'
    query_results = conn.execute(query)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    query_list = []
    for result in results:
        item = {
            "ProductId": result[0],
            "BrandName": result[1], 
            # 我不知道怎么解决,但是这样能跑
        }
        query_list.append(item)

    return query_list, keys