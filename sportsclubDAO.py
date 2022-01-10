# import the mysql connector module
import mysql.connector
# import the dbconfig.py file which contains my credentials to log into mysql
import dbconfig as cfg

# Class object for Database Access Object (DAO)
class sportsclubDao:
   db=""

   # function to connect to the database, 
   # initial connection to the database when a new instance of the class is created
   def __init__(self):
      self.db = mysql.connector.connect(
          host=cfg.mysql['host'],
          user=cfg.mysql['user'],
          password=cfg.mysql['password'],
          database=cfg.mysql['database']
      )

   # function to retrieve all locations from the location table in the database
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

   # function to retrieve all members from the members table in the database
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

   # function to retrieve all stock from the stock table in the database
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

   # function to retrieve all admins from the admin table in the database
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












   # function to create new location in the location database table
   def createLoc(self, location):
      cursor = self.db.cursor()
      sql = "insert into location (location) values (%s)"
      values = [
         # location['locId'], - auto-increment
         location['location'],         
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   # function to create new members in the members database table
   def createMem(self, mem):
      cursor = self.db.cursor()
      sql = "insert into members (name, age, gender, locId) values (%s, %s, %s, %s)"
      values = [
         # mem['memberId'], - auto-increment
         mem['name'],    
         mem['age'], 
         mem['gender'],  
         mem['locId']    
      ]
      cursor.execute(sql, values)
      self.db.commit()
      return cursor.lastrowid

   # function to create new admin in the admin database table
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

   # function to create new stock in the stock database table
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









   # function to find location by id
   def findByLocId(self, locId):
      cursor = self.db.cursor()
      sql = "select * from location where locId = %s"      
      values = [locId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      l = self.convertLocToDict(results)     
      return l

   # function to find all members by location id
   def getAllMemByLoc(self, locId):
      cursor = self.db.cursor()
      sql = 'select * from members where locId = %s;'
      values = [locId]
      cursor.execute(sql, values)
      results = cursor.fetchall()
      m = self.convertMemToDict(results)     
      return m

   # function to find member by id
   def findByMemId(self, memberId):
      cursor = self.db.cursor()
      sql = "select * from members where memberId = %s"      
      values = [memberId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      mm = self.convertMemToDict(results)     
      return mm

   # function to find stock by id
   def findByStockId(self, stockId):
      cursor = self.db.cursor()
      sql = "select * from stock where stockId = %s"      
      values = [stockId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      s = self.convertStockToDict(results)     
      return s

   # function to find admin by id
   def findByAdminId(self, adminId):
      cursor = self.db.cursor()
      sql = "select * from admin where adminId = %s"      
      values = [adminId]
      cursor.execute(sql, values)
      results = cursor.fetchone()
      a = self.convertAdminToDict(results)     
      return a












   # function to update existing location in the db
   def updateLoc(self, location):
      cursor = self.db.cursor()
      sql = "update location set location = %s where locId = %s"
      values = [
         location['location'],
         location['locId']
      ]
      cursor.execute(sql, values)
      self.db.commit()

   # function to update existing member in the db
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

   # function to update existing stock in the db     
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

   # function to update existing admin in the db
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






   # function to delete existing location in the db
   def deleteLoc(self, locId):      
      cursor = self.db.cursor()
      sql = 'delete from location where locId = %s'
      values = [locId]
      cursor.execute(sql, values)
      self.db.commit()

   # function to delete existing member in the db
   def deleteMem(self, memberId):      
      cursor = self.db.cursor()
      sql = 'delete from members where memberId = %s'
      values = [memberId]
      cursor.execute(sql, values)
      self.db.commit()

   # function to delete existing stock in the db
   def deleteStock(self, stockId):      
      cursor = self.db.cursor()
      sql = 'delete from stock where stockId = %s'
      values = [stockId]
      cursor.execute(sql, values)
      self.db.commit()

   # function to delete existing admin in the db 
   def deleteAdmin(self, adminId):      
      cursor = self.db.cursor()
      sql = 'delete from admin where adminId = %s'
      values = [adminId]
      cursor.execute(sql, values)
      self.db.commit()









   # function that converts the location data from the database to JSON
   def convertLocToDict(self, result):
      colnames = ['locId', 'location']
      loc = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            loc[colName] = value
      return loc

   # function that converts the members data from the database to JSON
   def convertMemToDict(self, result):
      colnames = ['memberId', 'name', 'age', 'gender', 'locId']
      mem = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            mem[colName] = value
      return mem

   # function that converts the stock data from the database to JSON
   def convertStockToDict(self, result):
      colnames = ['stockId', 'name', 'description', 'price']
      u = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            u[colName] = value
      return u

   # function that converts the admin data from the database to JSON
   def convertAdminToDict(self, result):
      colnames = ['adminId', 'name', 'password']
      u = {}
      if result:
         for i, colName in enumerate(colnames):
            value = result[i]
            u[colName] = value
      return u









# new instance of the sportsclubDAO class called 
sportsclubDao = sportsclubDao()