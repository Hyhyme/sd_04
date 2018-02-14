import pymongo

connection = pymongo.MongoClient( 'homer.stuy.edu' )

db = connection.test

collection = db.restaurants

def borough( b ) :
    return collection.find( {'borough' : b } )

def zipcode( z ) :
    return collection.find( { 'address.zipcode' : z } } )

test = zipcode( '10451' )
for restaurant in test:
    print restaurant

'''testB = borough( 'Bronx' )
for restaurant in testB:
    print restaurant'''
