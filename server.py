# Data Representation 
# Orla Higgins G00364860
# application server to be run in virtual environment 

# import flask and dependencies 
from flask import Flask, url_for, request, redirect, abort, jsonify, session, abort, render_template
# import a new instance of the sportsclubDao class from the sportsclubDAO file
from sportsclubDAO import sportsclubDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')



@app.route("/")
def index():      
    
    return "hello"


# Get all data from location table
@app.route('/location')
def getAllLoc():  
   app.logger.info('Get all locations')
   return jsonify(sportsclubDao.getAllLoc())

# Get all data from members table
@app.route('/members')
def getAllMem():
   app.logger.info('Get all members')
   return jsonify(sportsclubDao.getAllMem())

# Get all data from admin table
@app.route('/admin')
def getAllAdmin():
   app.logger.info('Get all admins')
   return jsonify(sportsclubDao.getAllAdmin())

# Get all data from stock table
@app.route('/stock')
def getAllStock():
   app.logger.info('Get all stock')
   return jsonify(sportsclubDao.getAllStock())



# Find by id - location tables
@app.route('/location/<int:locId>')
def findByLocId(locId):
   app.logger.info('Get dept with locId %s', locId)
   return jsonify(sportsclubDao.findByLocId(locId))

# Find by id - members tables
@app.route('/members/<int:memberId>')
def findByMemId(memberId):
   app.logger.info('Get members with memberId %s', memberId)
   return jsonify(sportsclubDao.findByMemId(memberId))

# Find by id - admin tables
@app.route('/admin/<int:adminId>')
def findByAdminId(adminId):
   app.logger.info('Get admin %s', adminId)
   return jsonify(sportsclubDao.findByAdminId(adminId))

# Find by id - all members by location tables
@app.route('/members/location/<int:locId>')
def getAllMemByLoc(locId):
   app.logger.info('Get all members in %s', locId)
   return jsonify(sportsclubDao.getAllMemByLoc(locId))




# Create a new location in location table
#curl  -i -H "Content-Type:application/json" -X POST -d "{\"location\":\"sligo\"}" http://127.0.0.1:5000/location
@app.route('/location', methods=['POST'])
def createLoc():
   location = {
      "location": request.json["location"],
   }
   app.logger.info('Created location %s', location)
   return jsonify(sportsclubDao.createLoc(location))

# Create a new member in members table
@app.route('/members', methods=['POST'])
def createMem():  
   locId = request.json["locId"]
   checkLoc = sportsclubDao.findByLocId(locId)
   if checkLoc == {}:
      app.logger.info('Location, %s, not found', checkLoc.locId)
      return jsonify({})
   mem = {
      "name": request.json["name"],
      "age": request.json["age"],
      "gender":request.json["gender"],
      "locId": request.json["locId"]
   }
   app.logger.info('Created member %s', mem)
   return jsonify(sportsclubDao.createMem(mem))

# Create a new admin in admin table
@app.route('/admin', methods=['POST'])
def createAdmin():   
   admin = {
      "name": request.json["name"],
      "password": request.json["password"]
   }
   app.logger.info('Created admin %s', admin)
   return jsonify(sportsclubDao.createAdmin(admin))

# Create new stock in stock table
# curl  -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"hello\",\"description\":\"someone\",\"price\":20}" http://127.0.0.1:5000/stock
@app.route('/stock', methods=['POST'])
def createStock(): 
   stock = {
      "name": request.json["name"],
      "description": request.json["description"], 
      "price": request.json["price"]
   }
   app.logger.info('Created stock %s', stock)
   return jsonify(sportsclubDao.createStock(stock))






# update location in location table
# curl -X PUT -d "{\"location\":\"heaven\"}" -H "content-type:application/json" http://127.0.0.1:5000/location/3
@app.route('/location/<int:locId>', methods=['PUT'])
def updateLoc(locId):
   foundLoc = sportsclubDao.findByLocId(locId)
   if foundLoc == {}:
      app.logger.info('Location, %s, not found', locId)
      return jsonify({}), 404
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   currentLoc = foundLoc
   if 'location' in request.json: 
       currentLoc['location'] = request.json['location']
   sportsclubDao.updateLoc(currentLoc)
   app.logger.info('Updated location %s', currentLoc)
   return jsonify(currentLoc)

# update members in members table
# curl -X PUT -d "{\"name\":\"it\", \"age\":200, \"gender\":\"M\", \"locId\":\"3\"}" -H "content-type:application/json" http://127.0.0.1:5000/members/2
@app.route('/members/<int:memberId>', methods=['PUT'])
def updateMem(memberId):
   foundMem = sportsclubDao.findByMemId(memberId)
   if foundMem == {}:
      app.logger.info('Member, %s, not found', memberId)
      return jsonify({}), 404
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   currentMem = foundMem
   if 'name' in request.json:
      currentMem['name'] = request.json['name']
   if 'age' in request.json:
      currentMem['age'] = request.json['age']
   if 'gender' in request.json:
      currentMem['gender'] = request.json['gender']
   if 'locId' in request.json:  
      locId = request.json['locId']
      checkLoc = sportsclubDao.findByLocId(locId)
      if checkLoc == {}:
         app.logger.info('Location %s not found', locId)
         return jsonify({}), 404
      currentMem['locId'] = locId       
   values = (currentMem['name'],currentMem['age'] , currentMem['gender'] , currentMem['locId'])
   sportsclubDao.updateMem(currentMem)
   app.logger.info('Updated member %s', currentMem)
   return jsonify(currentMem)

# update stock in stock table
# curl -X PUT -d "{\"name\":\"bike\", \"description\":\"fast moving\", \"price\":200}" -H "content-type:application/json" http://127.0.0.1:5000/stock/4
@app.route('/stock/<int:stockId>', methods=['PUT'])
def updateStock(stockId):
   foundStock = sportsclubDao.findByStockId(stockId)
   if foundStock == {}:
      app.logger.info('Stock, %s, not found', stockId)
      return jsonify({}), 404
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   currentStock = foundStock
   if 'name' in request.json: 
       currentStock['name'] = request.json['name']
   if 'description' in request.json:
      currentStock['description'] = request.json['description']
   if 'price' in request.json:
      currentStock['price'] = request.json['price']
   sportsclubDao.updateStock(currentStock)
   app.logger.info('Updated stock %s', currentStock)
   return jsonify(currentStock)

# update admin in admin table
# curl -X PUT -d "{\"name\":\"tom\", \"password\":\"1234\"}" -H "content-type:application/json" http://127.0.0.1:5000/admin/6
@app.route('/admin/<int:adminId>', methods=['PUT'])
def updateAdmin(adminId):
   foundAdmin = sportsclubDao.findByAdminId(adminId)
   if foundAdmin == {}:
      app.logger.info('Admin, %s, not found', adminId)
      return jsonify({}), 404
   if not request.json:
      app.logger.info('Request format not json')
      abort(400)
   currentAdmin = foundAdmin
   if 'name' in request.json: 
       currentAdmin['name'] = request.json['name']
   if 'password' in request.json: 
       currentAdmin['password'] = request.json['password']
   sportsclubDao.updateAdmin(currentAdmin)
   app.logger.info('Updated admin %s', currentAdmin)
   return jsonify(currentAdmin)


# delete location
#curl -X DELETE http://127.0.0.1:5000/location/4
@app.route('/location/<int:locId>', methods=['DELETE'])
def deleteLoc(locId):
    sportsclubDao.deleteLoc(locId)
    return jsonify({"done":True})

# delete members
#curl -X DELETE http://127.0.0.1:5000/members/4
@app.route('/members/<int:memberId>', methods=['DELETE'])
def deleteMem(memberId):
    sportsclubDao.deleteMem(memberId)
    return jsonify({"done":True})

# delete admins
#curl -X DELETE http://127.0.0.1:5000/admin/4
@app.route('/admin/<int:adminId>', methods=['DELETE'])
def deleteAdmin(adminId):
    sportsclubDao.deleteAdmin(adminId)
    return jsonify({"done":True})

# delete stock
#curl -X DELETE http://127.0.0.1:5000/stock/4
@app.route('/stock/<int:stockId>', methods=['DELETE'])
def deleteStock(stockId):
    sportsclubDao.deleteStock(stockId)
    return jsonify({"done":True})

# initialise server app
if __name__ == "__main__":
   app.run(debug=True)
   #app.run()