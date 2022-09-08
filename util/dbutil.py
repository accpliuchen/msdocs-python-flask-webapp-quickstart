import pymysql


class AmanMySQL():
    # 初始化
    def __init__(self):
#         self.host = "127.0.0.1"
#         self.user = "root"
#         self.passwd = "Liuchen198327!"
#         self.dbName = "mydb"
#         self.port = "3306"

        self.host = "nyuhealth.mysql.database.azure.com"
        self.user = "xuejinyu"
        self.passwd = "nyuHealth2022!"
        self.dbName = "mydb"
        self.port = "3306"

    # def __init__(self, host, user, passwd, dbName):
    #     self.host = host
    #     self.user = user
    #     self.passwd = passwd
    #     self.dbName = dbName

    # 连接数据库，需要传数据库地址、用户名、密码、数据库名称，默认设置了编码信息
    def connet(self):
        try:
            #self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName, use_unicode=True, charset='utf8')
            self.db=pymysql.connect(host=self.host,user=self.user,password=self.passwd,database=self.dbName,port=3306,charset='utf8')
            self.cursor = self.db.cursor()
        except Exception as e:
            return e

    # 关闭数据库连接
    def close(self):
        try:
            self.cursor.close()
            self.db.close()
        except Exception as e:
            return e

    # 查询操作，查询单条数据
    def get_one(self, sql):
        # res = None
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except Exception:
            res = None
        return res

    def selectDb(self,sql):
        ''' 数据库查询 '''
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql) # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            data = self.cursor.fetchall() # 返回所有记录列表
            return data
        except Exception as e:
            print(e)
        finally:
            self.cursor.close()


    # 查询操作，查询多条数据
    def get_all_headers(self, sql):
        # res = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            row_headers=[x[0] for x in self.cursor.description]
            self.close()
        except Exception:
            row_headers = ()
        return row_headers

    # 查询操作，查询多条数据
    def get_all(self, sql):
        # res = ()
        try:
            self.connet()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except Exception:
            res = ()
        return res

    # 查询数据库对象
    def get_all_obj(self, sql, tableName, *args):
        resList = []
        fieldsList = []
        try:
            if (len(args) > 0):
                for item in args:
                    fieldsList.append(item)
            else:
                fieldsSql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s' and table_schema = '%s'" % (
                    tableName, self.dbName)
                fields = self.get_all(fieldsSql)
                for item in fields:
                    fieldsList.append(item[0])

            # 执行查询数据sql
            res = self.get_all(sql)
            for item in res:
                obj = {}
                count = 0
                for x in item:
                    obj[fieldsList[count]] = x
                    count += 1
                resList.append(obj)
            return resList
        except Exception as e:
            return e

    # 数据库插入、更新、删除操作
    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        # count = 0
        try:
            self.connet()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except Exception as e:
            self.db.rollback()
            count = 0
        return count