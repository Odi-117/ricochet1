from DBConnect import DBConnect 

dbUrl = {"dbname":"test3","user":"postgres","password":"5225", "host":"localhost"}

db = DBConnect(dbUrl,  "users")

print(db.req_select_db("*",""))