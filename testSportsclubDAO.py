from sportsclubDAO import sportsclubDao

location1 = {
    'location':'belfast',   
}

location2 = {
    'location':'cavan', 
}

location3 = {
    'locId':2,
    'location':'sligo'
}


member1 = {
    'name':'ronan', 
    'age':'24',  
    'email' : 'ronan@galway.com', 
    'gender':'M',  
    'locId' : '3'
}

member2 = {
    'name':'darren', 
    'age':'35',  
    'email' : 'darren@galway.com', 
    'gender':'M',  
    'locId' : '3'
}

member3 = {
    'name':'Cat', 
    'age':'40',  
    'email' : 'cat@cork.com', 
    'gender':'F',  
    'locId' : '2'
}

member4 = {
    'memberId': '2', 
    'name':'Clare', 
    'age':'32',      
    'gender':'F'
 
}

stock1 = {
   'name':'jersey',
   'description': 'blue and white, size 16',
   'price': 9.99
}

stock2 = {
   'name':'tracksuit',
   'description': 'away kit, size 8',
   'price':29.99
}

stock3 = {
   'name':'football',
   'description': 'childrens, size 4',
   'price':15.00,
   'stockId': 2
}



admin1 = {
   'name':'admin',
   'password':'admin',
}

admin2 = {
   'name':'jim',
   'password':'1234',
}

admin3 = {
   'name':'frances',
   'password':'0000',
   'adminId' : 2
}


# Insert table contents
returnValue = sportsclubDao.createLoc(location1)
print(returnValue)
returnValue = sportsclubDao.createLoc(location2)
print(returnValue)
returnValue = sportsclubDao.createMem(member1)
print(returnValue)
returnValue = sportsclubDao.createMem(member2)
print(returnValue)
returnValue = sportsclubDao.createMem(member3)
print(returnValue)
returnValue = sportsclubDao.createStock(stock1)
print(returnValue)
returnValue = sportsclubDao.createStock(stock2)
print(returnValue)
returnValue = sportsclubDao.createAdmin(admin1)
print(returnValue)
returnValue = sportsclubDao.createAdmin(admin2)
print(returnValue)


# Get all table contents
returnValue = sportsclubDao.getAllLoc()
print(returnValue)
returnValue = sportsclubDao.getAllMem()
print(returnValue)
returnValue = sportsclubDao.getAllStock()
print(returnValue)
returnValue = sportsclubDao.getAllAdmin()
print(returnValue)

# Get table contents by ID
returnValue = sportsclubDao.findByLocId(2)
print(returnValue)
returnValue = sportsclubDao.getAllMemByLoc(3)
print(returnValue)
returnValue = sportsclubDao.findByStockId(1)
print(returnValue)
returnValue = sportsclubDao.findByAdminName('frances')
print(returnValue)

# # Update table contents
returnValue = sportsclubDao.updateMem(member4)
print(returnValue)
returnValue = sportsclubDao.updateLoc(location3)
print(returnValue)
returnValue = sportsclubDao.updateStock(stock3)
print(returnValue)
returnValue = sportsclubDao.updateAdmin(admin3)
print(returnValue)


# # Delete table contents
returnValue = sportsclubDao.deleteLoc(1)
print(returnValue)
returnValue = sportsclubDao.deleteMem(1)
print(returnValue)
returnValue = sportsclubDao.deleteStock(1)
print(returnValue)
returnValue = sportsclubDao.deleteAdmin(1)
print(returnValue)
