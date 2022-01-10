from flask import Flask, url_for, request, redirect, abort, jsonify, session, abort, render_template
from sportsclubDAO import sportsclubDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')



@app.route("/")
def index():      
    
    return "hello"



@app.route('/location')
def getAllLoc():  
   app.logger.info('Get all locations')
   return jsonify(sportsclubDao.getAllLoc())

@app.route('/members')
def getAllMem():
   app.logger.info('Get all members')
   return jsonify(sportsclubDao.getAllMem())

@app.route('/admin')
def getAllAdmin():
   app.logger.info('Get all admins')
   return jsonify(sportsclubDao.getAllAdmin())

@app.route('/stock')
def getAllStock():
   app.logger.info('Get all stock')
   return jsonify(sportsclubDao.getAllStock())




@app.route('/location/<int:locId>')
def findByLocId(locId):
   app.logger.info('Get dept with locId %s', locId)
   return jsonify(sportsclubDao.findByLocId(locId))

@app.route('/members/<int:memberId>')
def findByMemId(memberId):
   app.logger.info('Get members with memberId %s', memberId)
   return jsonify(sportsclubDao.findByMemId(memberId))

@app.route('/admin/<int:adminId>')
def findByAdminId(adminId):
   app.logger.info('Get admin %s', adminId)
   return jsonify(sportsclubDao.findByAdminId(adminId))

@app.route('/members/location/<int:locId>')
def getAllMemByLoc(locId):
   app.logger.info('Get all members in %s', locId)
   return jsonify(sportsclubDao.getAllMemByLoc(locId))





@app.route('/location', methods=['POST'])
def createLoc():
   location = {
      "location": request.json["location"],
   }
   app.logger.info('Created location %s', location)
   return jsonify(sportsclubDao.createLoc(location))

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

@app.route('/admin', methods=['POST'])
def createAdmin():   
   admin = {
      "name": request.json["name"],
      "password": request.json["password"]
   }
   app.logger.info('Created admin %s', admin)
   return jsonify(sportsclubDao.createAdmin(admin))


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



#curl -X DELETE http://127.0.0.1:5000/location/4
@app.route('/location/<int:locId>', methods=['DELETE'])
def deleteLoc(locId):
    sportsclubDao.deleteLoc(locId)
    return jsonify({"done":True})

#curl -X DELETE http://127.0.0.1:5000/location/4
@app.route('/members/<int:memberId>', methods=['DELETE'])
def deleteMem(memberId):
    sportsclubDao.deleteMem(memberId)
    return jsonify({"done":True})

#curl -X DELETE http://127.0.0.1:5000/location/4
@app.route('/admin/<int:adminId>', methods=['DELETE'])
def deleteAdmin(adminId):
    sportsclubDao.deleteAdmin(adminId)
    return jsonify({"done":True})

#curl -X DELETE http://127.0.0.1:5000/location/4
@app.route('/stock/<int:stockId>', methods=['DELETE'])
def deleteStock(stockId):
    sportsclubDao.deleteStock(stockId)
    return jsonify({"done":True})

# initialise server app
if __name__ == "__main__":
   app.run(debug=True)
   #app.run()