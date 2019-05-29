from mongoengine import connect

# connect(host='mongodb://admin:admin123@ds263146.mlab.com:63146/gigs')

connect('gigs', host='mongodb://admin:admin123@ds263146.mlab.com:63146', alias='default')

