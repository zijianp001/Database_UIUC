from app import db

def check_login(data: dict) -> int:
    length = len(data)

    conn = db.connect()
    query = 'Select password from user WHERE userID = "{}";'.format(data['userid'])
    query_results = conn.execute(query)
    results = query_results.fetchone()

    if results is None:
        correctPassWord = None
        print("Account does not exist")
        return 1
    else:
        correctPassWord = results[0]
        inputPassWord = data['password']
        if correctPassWord == inputPassWord:
            print("Correct")
            return 2
        else:
            print("Incorrect password")
            return 3


def register_account(data: dict) -> None:
    length = len(data)
    print(length)
    print(data['userid'])
    print(data['password'])
    print(data['confirmpw'])
    conn = db.connect()

    query = 'Insert Into user VALUES ("{}", "{}");'.format(data['userid'], data['password'])
    conn.execute(query)
    conn.close()



def fetch_product() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product;")
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    product_list = []

    # for result in results:
    #     item = {
    #         "ProductId": result[0],
    #         "BrandName": result[1],
    #         "ProductName": result[2],
    #         "ProductType": result[3]
    #     }
    #     product_list.append(item)
    
    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        product_list.append(item)

    return product_list, keys

def fetch_cpu() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product NATURAL JOIN CPU;")
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    cpu_list = []
    
    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        cpu_list.append(item)

    return cpu_list, keys


def fetch_gpu() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product NATURAL JOIN GPU;")
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    gpu_list = []

    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        gpu_list.append(item)

    return gpu_list, keys


def fetch_mob() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product NATURAL JOIN MotherBoard;")
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    mob_list = []

    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        mob_list.append(item)

    return mob_list, keys


def remove_task_by_id(product_id: float) -> str:
    conn = db.connect()
    print(product_id)
    findType = 'Select ProductType from Product where ProductId={};'.format(product_id)
    ResultType = conn.execute(findType)
    productType = ResultType.fetchone()
    ptype = productType[0]
    print(productType)
    ptype = ptype.upper()

    if ptype == 'CPU':
        query = 'Delete From CPU where ProductId={};'.format(product_id)
    elif ptype == 'GPU':
        query = 'Delete From GPU where ProductId={};'.format(product_id)
    elif ptype == 'RAM':
        query = 'Delete From RAM where ProductId={};'.format(product_id)
    else:
        query = 'Delete From MotherBoard where ProductId={};'.format(product_id)

    query1 = 'Delete From Product where ProductId={};'.format(product_id)
    conn.execute(query)
    conn.execute(query1)
    conn.close()

    return ptype


def insert_new_task(data: dict) -> None:
    length = len(data)
    query1 = 'Insert Into Product VALUES ("{}", "{}", "{}","{}");'.format(data['1'], data['2'], data['3'], data['4'])

    if length == 12:
        query2 = 'Insert Into CPU VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'], data['8'], data['9'], data['10'], data['11'], data['12'])
        print(query2)
    elif length == 9:
        query2 = 'Insert Into GPU VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'], data['8'], data['9'])
    elif length == 7:
        query2 = 'Insert Into MotherBoard VALUES ("{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'])
    elif length == 4:
        pass

    conn = db.connect()

    conn.execute(query1)
    conn.execute(query2)
    conn.close()




def update_attributes(data: dict) -> str:
    length = len(data)
    conn = db.connect()

    findType = 'Select ProductType from Product where ProductId={};'.format(data['1'])
    ResultType = conn.execute(findType)
    productType = ResultType.fetchone()
    ptype = productType[0]
    ptype = ptype.upper()

    if length == 12:
        query = 'UPDATE Product NATURAL JOIN CPU SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", CPU.CodeName = "{}", CPU.Cores= "{}", CPU.Clock = "{}", CPU.CPUSocket = "{}",CPU.CPUProcess = "{}", CPU.L3_Cache = "{}", CPU.TDP= "{}", CPU.ReleaseYear = {} WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['9'], data['10'], data['11'], data['12'], data['1'])
        print(query)
    elif length == 9:
        query = 'UPDATE Product NATURAL JOIN GPU SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", GPU.GPU_Chip = "{}", GPU.ReleaseYear = "{}", GPU.GPU_Memory = "{}", GPU.GPU_Clock = "{}",GPU.Memory_Clock = "{}" WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['9'], data['1'])
        print(query)
    elif length == 7:
        query = 'UPDATE Product NATURAL JOIN MotherBoard SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", MotherBoard.Socket = "{}", MotherBoard.Chipset = "{}", MotherBoard.SupportMemoryType = "{}" WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['1'])
        print(query)
    elif length == 4:
        pass



    print(ptype)

    conn.execute(query)
    conn.close()

    return ptype




def search_task_by_ProductName(keyword, current) -> dict:
    conn = db.connect()
    if current == 'CPU':
        query = 'Select * from Product NATURAL JOIN CPU WHERE ProductName LIKE "%%{}%%" or BrandName LIKE "%%{}%%" or CodeName LIKE "%%{}%%" or Cores LIKE "%%{}%%" or Clock LIKE "%%{}%%" or CPUSocket LIKE "%%{}%%" or CPUProcess LIKE "%%{}%%" or L3_Cache LIKE "%%{}%%" or TDP LIKE "%%{}%%" or ReleaseYear LIKE "%%{}%%" or ProductId LIKE "%%{}%%";'.format(keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword)
        print(query)
        query_results = conn.execute(query)
        results = query_results.fetchall()
        keys = query_results.keys()
        conn.close()
        search_list = []

        for result in results:
            i = 0
            item = {}
            for key in keys:
                item[key] = result[i]
                i += 1
            search_list.append(item)

    elif current == 'MOB':
        query = 'Select * from Product NATURAL JOIN MotherBoard WHERE ProductName LIKE "%%{}%%" or BrandName LIKE "%%{}%%" or Socket LIKE "%%{}%%" or Chipset LIKE "%%{}%%" or SupportMemoryType LIKE "%%{}%%" or ProductId LIKE "%%{}%%";'.format(keyword, keyword, keyword, keyword, keyword, keyword)
        print(query)
        query_results = conn.execute(query)
        results = query_results.fetchall()
        keys = query_results.keys()
        conn.close()
        search_list = []
        for result in results:
            i = 0
            item = {}
            for key in keys:
                item[key] = result[i]
                i += 1
            search_list.append(item)
    elif current == 'RAM':
        print()
    else:
        query = 'Select * from Product NATURAL JOIN GPU WHERE ProductName LIKE "%%{}%%" or BrandName LIKE "%%{}%%" or GPU_Chip LIKE "%%{}%%" or GPU_Memory LIKE "%%{}%%" or GPU_Clock LIKE "%%{}%%" or Memory_Clock LIKE "%%{}%%" or ReleaseYear LIKE "%%{}%%" or ProductId LIKE "%%{}%%";'.format(keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword)
        print(query)
        query_results = conn.execute(query)
        results = query_results.fetchall()
        keys = query_results.keys()
        conn.close()
        search_list = []
        for result in results:
            i = 0
            item = {}
            for key in keys:
                item[key] = result[i]
                i += 1
            search_list.append(item)
    # 再加上 ram 和 MOB

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