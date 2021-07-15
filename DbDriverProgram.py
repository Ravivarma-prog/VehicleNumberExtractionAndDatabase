import Database as db

obj = db.connectdb("testdb")

db.insertdata(obj , 141 , 'Ravivarma')
# db.selectquery(obj)

db.deleterow(obj,141)
db.deleterow(obj,132)
db.deleterow(obj,104)
db.deleterow(obj,108)
db.deleterow(obj,106)
db.deleterow(obj,116)

# db.selectquery(obj)

db.insertdata(obj , 141 , 'Ravivarma')
db.insertdata(obj , 106 , 'Balamurugan')
db.insertdata(obj , 108 , 'Chandru')
db.insertdata(obj , 116 , 'Habibullah')
db.insertdata(obj , 132 , 'Nishanth')
db.insertdata(obj , 104 , 'Arun Prakash')

# db.selectAsc(obj)

db.selectquery(obj)