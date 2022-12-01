from app import db

def check_login(data: dict) -> int:
    length = len(data)

    conn = db.connect()
    query = 'Select password from User WHERE userID = "{}";'.format(data['userid'])
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

    query = 'Insert Into User VALUES ("{}", "{}");'.format(data['userid'], data['password'])
    conn.execute(query)
    conn.close()



def fetch_product() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product Limit 100;")
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


def fetch_ram() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product NATURAL JOIN RAM;")
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
    print(ptype)

    if ptype != None:
        ptype = ptype.upper()
    else:
        ptype = 'None'


    if ptype == 'CPU':
        query = 'Delete From CPU where ProductId={};'.format(product_id)
        conn.execute(query)
    elif ptype == 'GPU':
        query = 'Delete From GPU where ProductId={};'.format(product_id)
        conn.execute(query)
    elif ptype == 'RAM':
        query = 'Delete From RAM where ProductId={};'.format(product_id)
        conn.execute(query)
    elif ptype == 'MOTHERBOARD' or ptype == 'MOTHER BOARD':
        query = 'Delete From MotherBoard where ProductId={};'.format(product_id)
        conn.execute(query)


    query1 = 'Delete From Product where ProductId={};'.format(product_id)
    conn.execute(query1)
    conn.close()

    return ptype


def insert_new_task(data: dict) -> str:
    length = len(data)

    ptype = ''
    if length == 13:
        query1 = 'Insert Into Product VALUES ("{}", "{}", "{}","{}");'.format(data['1'], data['2'], data['3'], 'CPU')
        query2 = 'Insert Into CPU VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'], data['8'], data['9'], data['10'], data['11'], data['12'], data['13'])
        ptype = 'CPU'
    elif length == 9:
        query1 = 'Insert Into Product VALUES ("{}", "{}", "{}","{}");'.format(data['1'], data['2'], data['3'], 'GPU')
        query2 = 'Insert Into GPU VALUES ("{}", "{}", "{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'], data['8'], data['9'])
        ptype = 'GPU'
    elif length == 7:
        query1 = 'Insert Into Product VALUES ("{}", "{}", "{}","{}");'.format(data['1'], data['2'], data['3'], 'MotherBoard')
        query2 = 'Insert Into MotherBoard VALUES ("{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'])
        ptype = 'MotherBoard'
    elif length == 8:
        query1 = 'Insert Into Product VALUES ("{}", "{}", "{}","{}");'.format(data['1'], data['2'], data['3'], 'RAM')
        query2 = 'Insert Into RAM VALUES ("{}", "{}", "{}", "{}", "{}");'.format(data['1'], data['5'], data['6'], data['7'], data['8'])
        ptype = 'RAM'
    elif length == 4:
        pass

    conn = db.connect()

    conn.execute(query1)
    print(query2)
    conn.execute(query2)
    conn.close()

    return ptype




def update_attributes(data: dict) -> str:
    length = len(data)
    conn = db.connect()

    findType = 'Select ProductType from Product where ProductId={};'.format(data['1'])
    ResultType = conn.execute(findType)
    productType = ResultType.fetchone()
    ptype = productType[0]
    ptype = ptype.upper()

    if length == 13:
        query = 'UPDATE Product NATURAL JOIN CPU SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", CPU.CodeName = "{}", CPU.Cores= "{}", CPU.Clock = "{}", CPU.CPUSocket = "{}",CPU.CPUProcess = "{}", CPU.L3_Cache = "{}", CPU.TDP= "{}", CPU.ReleaseYear = {}, CPU.ReleaseTime = "{}" WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['9'], data['10'], data['11'], data['12'], data['13'], data['1'])
        print(query)
    elif length == 9:
        query = 'UPDATE Product NATURAL JOIN GPU SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", GPU.GPU_Chip = "{}", GPU.ReleaseYear = "{}", GPU.GPU_Memory = "{}", GPU.GPU_Clock = "{}",GPU.Memory_Clock = "{}" WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['9'], data['1'])
        print(query)
    elif length == 7:
        query = 'UPDATE Product NATURAL JOIN MotherBoard SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", MotherBoard.Socket = "{}", MotherBoard.Chipset = "{}", MotherBoard.SupportMemoryType = "{}" WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['1'])
        print(query)
    elif length == 8:
        query = 'UPDATE Product NATURAL JOIN RAM SET Product.BrandName = "{}", Product.ProductName = "{}", Product.ProductType = "{}", RAM.MemoryType = "{}", RAM.MemorySize = "{}", RAM.Frequency = "{}", RAM.ReleaseYear = {} WHERE ProductId = {};'.format(
            data['2'], data['3'], data['4'], data['5'], data['6'], data['7'], data['8'], data['1'])
        print(query)
    elif length == 4:
        query = 'UPDATE Product SET Product.BrandName = "{}", Product.ProductName = "{}" WHERE ProductId = {};'.format(
            data['2'], data['3'], data['1'])
        print(query)

    print(ptype)
    conn.execute(query)
    conn.close()
    return ptype


def search_task_by_ProductName(keyword, current) -> dict:
    conn = db.connect()
    if current == 'CPU':
        query = 'Select * from Product NATURAL JOIN CPU WHERE ProductName LIKE "%%{}%%" or BrandName LIKE "%%{}%%" or CodeName LIKE "%%{}%%" or Cores LIKE "%%{}%%" or Clock LIKE "%%{}%%" or CPUSocket LIKE "%%{}%%" or CPUProcess LIKE "%%{}%%" or L3_Cache LIKE "%%{}%%" or TDP LIKE "%%{}%%" or ReleaseYear LIKE "%%{}%%" or ReleaseTime LIKE "%%{}%%" or ProductId LIKE "%%{}%%";'.format(keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword, keyword)
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
        query = 'Select * from Product NATURAL JOIN RAM WHERE ProductName LIKE "%%{}%%" or BrandName LIKE "%%{}%%" or MemoryType LIKE "%%{}%%" or MemorySize LIKE "%%{}%%" or Frequency LIKE "%%{}%%" or ReleaseYear LIKE "%%{}%%" or ProductId LIKE "%%{}%%";'.format(
            keyword, keyword, keyword, keyword, keyword, keyword, keyword)
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




def search_adquery(keyword) -> dict:
    conn = db.connect()
    query = 'Select * from MotherBoard m NATURAL JOIN Product p WHERE Socket in (SELECT c.CPUSocket from CPU c natural join Product p where ProductName LIKE "%%{}%%");'.format(keyword)
    query_results = conn.execute(query)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    query_list = []
    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        query_list.append(item)

    return query_list, keys


def search_adquery_sp(keyword) -> dict:
    conn = db.connect()
    query1 = 'DROP PROCEDURE IF EXISTS result;'
    query = 'CREATE PROCEDURE result() ' \
            'BEGIN ' \
            'DECLARE varId REAL; ' \
            'DECLARE varSocket varchar(30); ' \
            'DECLARE varChipset varchar(30); ' \
            'DECLARE varSupportMemoryType varchar(30); ' \
            'DECLARE varBrandName varchar(30); ' \
            'DECLARE varProductName varchar(30); ' \
            'DECLARE varProductType varchar(30); ' \
            'DECLARE varStatus varchar(30); ' \
            'DECLARE exit_loop BOOLEAN ' \
            'DEFAULT FALSE; ' \
            'DECLARE cusCur CURSOR FOR ' \
            '( Select * from MotherBoard m NATURAL JOIN Product p WHERE Socket IN (SELECT c.CPUSocket from CPU c natural join Product p where ProductName LIKE "%%{}%%")); ' \
            'DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_loop = TRUE;' \
            'DROP TABLE IF EXISTS NewTable;' \
            'CREATE TABLE NewTable( ' \
            'ProductId REAL,' \
            'ssocket varchar(30),' \
            'Chipset varchar(30),' \
            'SupportMemoryType varchar(30),' \
            'BrandName varchar(30),' \
            'ProductName varchar(30),' \
            'ProductType varchar(30),' \
            'ProductStatus varchar(30)' \
            ');' \
            'OPEN cusCur; ' \
            'cloop: LOOP ' \
            'FETCH cusCur INTO varId, varSocket, varChipset,varSupportMemoryType, varBrandName, varProductName, varProductType;' \
            'IF(exit_loop) THEN ' \
            'LEAVE cloop;' \
            'END IF; ' \
            'IF (varSupportMemoryType LIKE "%%DDR5%%") THEN ' \
            'SET varStatus = "Advanced";' \
            'ELSEIF (varSupportMemoryType LIKE "%%DDR4%%") THEN ' \
            'SET varStatus = "Medium";' \
            'ELSE ' \
            'SET varStatus = "Low";' \
            'END IF;' \
            'INSERT INTO NewTable VALUES' \
            '(varId, varSocket, varChipset,varSupportMemoryType, varBrandName,varProductName, varProductType, varStatus);' \
            'END LOOP cloop;' \
            'CLOSE cusCur;' \
            'SELECT * FROM NewTable;' \
            'END'.format(keyword)
    print(query)
    query2 = 'CALL result();'

    conn.execute(query1)
    conn.execute(query)
    query_results = conn.execute(query2)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    query_list = []
    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        query_list.append(item)

    return query_list, keys




def search_adquery2(keyword) -> dict:
    conn = db.connect()
    query = 'select Count(*), c.CPUProcess from CPU c NATURAL JOIN Product p where CPUSocket in (select m.Socket from MotherBoard m natural join Product p where ProductName like "%%{}%%") group by c.CPUProcess'.format(keyword)
    query_results = conn.execute(query)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    query_list = []
    for result in results:
        item = {
            "Count(*)": result[0],
            "CPUProcess": result[1],
        }
        query_list.append(item)

    return query_list, keys


def search_adquery2_sp(keyword) -> dict:
    conn = db.connect()
    query1 = 'DROP PROCEDURE IF EXISTS result2;'
    query = 'CREATE PROCEDURE result2()' \
            'BEGIN ' \
            'DECLARE varCnt INT;' \
            'DECLARE varProcess varchar(30);' \
            'DECLARE varLevel varchar(30);' \
            'DECLARE exit_loop BOOLEAN DEFAULT FALSE;' \
            'DECLARE cusCur CURSOR FOR ' \
            '(select Count(*), c.CPUProcess from CPU c NATURAL JOIN Product p ' \
            'where CPUSocket IN (select m.Socket from MotherBoard m natural join Product p ' \
            'where ProductName like "%%{}%%") ' \
            'group by c.CPUProcess);' \
            'DECLARE CONTINUE HANDLER FOR NOT FOUND SET exit_loop = TRUE;' \
            'DROP TABLE IF EXISTS NewTable;' \
            'CREATE TABLE NewTable(' \
            'Number_CPU INT, ' \
            'CPUProcess varchar(30) PRIMARY KEY, ' \
            'ProcessLevel varchar(30));' \
            'OPEN cusCur;' \
            'cloop: LOOP ' \
            'FETCH cusCur INTO varCnt, varProcess; ' \
            'IF(exit_loop) THEN ' \
            'LEAVE cloop;' \
            'END IF; ' \
            'IF(varProcess="5 nm" OR varProcess = "6 nm") THEN ' \
            'SET varLevel = "A+"; ' \
            'ELSEIF (varProcess = "7 nm" OR varProcess = "10 nm") THEN ' \
            'SET varLevel = "A"; ' \
            'ELSEIF (varProcess LIKE "%%12%%") THEN ' \
            'SET varLevel = "B";' \
            'ELSEIF(varProcess LIKE "%%14%%") THEN ' \
            'SET varLevel = "C";' \
            'else ' \
            'SET varLevel = "D";' \
            'END IF;' \
            'INSERT INTO NewTable VALUES ' \
            '(varCnt, varProcess, varLevel);' \
            'END LOOP cloop;' \
            'CLOSE cusCur;' \
            'SELECT * FROM NewTable;' \
            'END'.format(keyword)
    print(keyword)
    query2 = 'CALL result2();'

    conn.execute(query1)
    conn.execute(query)
    query_results = conn.execute(query2)
    results = query_results.fetchall()
    keys = query_results.keys()
    conn.close()
    query_list = []
    for result in results:
        i = 0
        item = {}
        for key in keys:
            item[key] = result[i]
            i += 1
        query_list.append(item)

    return query_list, keys