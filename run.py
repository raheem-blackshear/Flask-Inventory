#!flask/bin/python
from inventory import inventory

CSRF_ENABLED = True
inventory.secret_key = 'hahahahahahahah--that-was-funny'
inventory.config['UPLOAD_FOLDER'] = 'app/static/products/'
inventory.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

inventory.run(debug=True, host='127.0.0.1',port=5002) #remove host if you do not want it public
