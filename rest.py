import pymongo

connection = pymongo.MongoClient( 'homer.stuy.edu' )

db = connection.test

collection = db.restaurants

def borough( b ) :
    return collection.find( {'borough' : b } )

def zipcode( z ) :
    return collection.find( { 'address.zipcode' : z } )

def qualityZip ( z, grade ) :
    return collection.find( { 'addres.zipcode' : z , 'grades.grade' : grade } )

def lowScore ( z, score ) :
    return collection.find( { 'address.zipcode' : z , 'grades.score' : { '$lt' : score } } )


test = zipcode( '10451' )
for restaurant in test:
    print restaurant

'''testB = borough( 'Bronx' )
for restaurant in testB:
    print restaurant'''
