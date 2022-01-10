import mysql.connector
import dbconfig as cfg

# Class object for Database Access Object (DAO)
class sportsclubDao:
   db=""

   def __init__(self):
      self.db = mysql.connector.connect(
          host=cfg.mysql['host'],
          user=cfg.mysql['user'],
          password=cfg.mysql['password'],
          database=cfg.mysql['database']
      )

   def getAllLoc(self):      
      cursor = self.db.cursor()
      sql = 'select * from location'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []      
      for result in results:
         resultAsDict = self.convertLocToDict(result)
         returnArray.append(resultAsDict)
      return returnArray


   def getAllMem(self):      
      cursor = self.db.cursor()
      sql = 'select * from members'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []      
      for result in results:
         resultAsDict = self.convertMemToDict(result)
         returnArray.append(resultAsDict)
      return returnArray

   def getAllStock(self):      
      cursor = self.db.cursor()
      sql = 'select * from stock'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []      
      for result in results:
         resultAsDict = self.convertStockToDict(result)
         returnArray.append(resultAsDict)
      return returnArray


   def getAllAdmin(self):      
      cursor = self.db.cursor()
      sql = 'select * from admin'
      cursor.execute(sql)
      results = cursor.fetchall()
      returnArray = []      
      for result in results:
         resultAsDict = self.convertAdminToDict(result)
         returnArray.append(resultAsDict)
      return returnArray













   # Create department, returns deptID of new department
   def createLoc(self, location):
      cursor = self.db.cursor()
      sql = "insert into location (location) values (%s)"
      values = [
         # dept['deptID'], - auto-increment
         location['location'],         
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   def createMem(self, mem):
      cursor = self.db.cursor()
      sql = "insert into members (name, age, gender, locId) values (%s, %s, %s, %s)"
      values = [
         # dept['deptID'], - auto-increment
         mem['name'],    
         mem['age'], 
         mem['gender'],  
         mem['locId']    
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   def createAdmin(self, admin):
      cursor = self.db.cursor()
      sql = "insert into admin (name, password) values (%s, %s)"
      values = [
         # admin['adminId'], - auto-increment
         admin['name'],    
         admin['password']       
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   def createStock(self, stock):
      cursor = self.db.cursor()
      sql = "insert into stock (name, description, price) values (%s, %s, %s)"
      values = [
         # stock['stockId'], - auto-increment
         stock['name'],    
         stock['description'],   
         stock['price']      
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid



























   def findByLocId(self, locId):
      cursor = self.db.cursor()
      sql = "select * from location where locId = %s"      
      values = [locId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      l = self.convertLocToDict(results)     
      return l


   def getAllMemByLoc(self, locId):
      cursor = self.db.cursor()
      sql = 'select * from members where locId = %s;'
      values = [locId]
      cursor.execute(sql, values)
      results = cursor.fetchall()
      m = self.convertMemToDict(results)     
      return m


   def findByMemId(self, memberId):
      cursor = self.db.cursor()
      sql = "select * from members where memberId = %s"      
      values = [memberId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      mm = self.convertMemToDict(results)     
      return mm


   def findByStockId(self, stockId):
      cursor = self.db.cursor()
      sql = "select * from stock where stockId = %s"      
      values = [stockId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      s = self.convertStockToDict(results)     
      return s

   def findByAdminId(self, adminId):
      cursor = self.db.cursor()
      sql = "select * from admin where adminId = %s"      
      values = [adminId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      a = self.convertAdminToDict(results)     
      return a













   def updateLoc(self, location):
      cursor = self.db.cursor()
      sql = "update location set location = %s where locId = %s"
      values = [
         location['location'],
         location['locId']
      ]
      cursor.execute(sql, values)
      self.db.commit()


   def updateMem(self, mem):
      cursor = self.db.cursor()
      sql = "update members set name = %s, age = %s, gender = %s where memberId = %s"
      values = [
         mem['name'],
         mem['age'],
         mem['gender'],
         mem['memberId']
      ]
      cursor.execute(sql, values)
      self.db.commit()
      
   def updateStock(self, stock):
      cursor = self.db.cursor()
      sql = "update stock set name = %s, description = %s, price = %s where stockId = %s"
      values = [
         stock['name'],
         stock['description'],
         stock['price'],
         stock['stockId']
      ]
      cursor.execute(sql, values)
      self.db.commit()

   def updateAdmin(self, admin):
      cursor = self.db.cursor()
      sql = "update admin set name = %s, password = %s where adminId = %s"
      values = [
         admin['name'],
         admin['password'],
         admin['adminId']         
      ]
      cursor.execute(sql, values)
      self.db.commit()







   def deleteLoc(self, locId):      
      cursor = self.db.cursor()
      sql = 'delete from location where locId = %s'
      values = [locId]
      cursor.execute(sql, values)
      self.db.commit()

   def deleteMem(self, memberId):      
      cursor = self.db.cursor()
      sql = 'delete from members where memberId = %s'
      values = [memberId]
      cursor.execute(sql, values)
      self.db.commit()

   def deleteStock(self, stockId):      
      cursor = self.db.cursor()
      sql = 'delete from stock where stockId = %s'
      values = [stockId]
      cursor.execute(sql, values)
      self.db.commit()
  
   def deleteAdmin(self, adminId):      
      cursor = self.db.cursor()
      sql = 'delete from admin where adminId = %s'
      values = [adminId]
      cursor.execute(sql, values)
      self.db.commit()


















   # Function to convert department into Dictionary/JSON
   def convertLocToDict(self, result):
      colnames = ['locId', 'location']
      loc = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            loc[colName] = value
      return loc

   # Function to convert employee into Dictionary/JSON
   def convertMemToDict(self, result):
      colnames = ['memberId', 'name', 'age', 'gender', 'locId']
      mem = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            mem[colName] = value
      return mem

   # Function to convert user into Dictionary/JSON
   def convertStockToDict(self, result):
      colnames = ['stockId', 'name', 'description', 'price']
      u = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            u[colName] = value
      return u

   # Function to convert user into Dictionary/JSON
   def convertAdminToDict(self, result):
      colnames = ['adminId', 'name', 'password']
      u = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            u[colName] = value
      return u
















sportsclubDao = sportsclubDao()