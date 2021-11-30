#Importacion de librerías
import datetime
import hashlib
import json
from flask		 import Flask, jsonify
from flask_ngrok import run_with_ngrok
from blockchain import Blockchain

# Crear una aplicacion web 
app = Flask(__name__)
run_with_ngrok(app)

# Si se obtiene error 500, actualizar Flask y ejecutar la siguiente linea
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Creacion de la Blockchain
blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET']) 						# Definimos la url 
def mine_block():
	"""Minado de un nuevo bloque """
	previous_block	= blockchain.get_previous_block() 				# obtenemos el ultimo elemento de la cadena
	previous_proof 	= previous_block['proof']		  				# obtenemos su proof(nonce)
	proof 			= blockchain.proof_of_work(previous_proof)		# obtenemos su proof of work
	previous_hash 	= blockchain.hash(previous_block)				# obtenemos su has
	block 			= blockchain.create_block(proof, previous_hash)	# obtenemos un bloque con su nonce y hash
	response = { 'message' 	 	 : '¡Enhorabuena, has minado un nuevo bloque',
				 'index'	  	 : block['index'],
				 'timestamp' 	 : block['timestamp'],
				 'proof' 	 	 : block['proof'],
				 'previous_hash' : block['previous_hash']
				}
	return jsonify(response), 200

@app.route('/get_chain', methods = ['GET']) 
def get_chain():													# Obtencion de todos los bloques que conforman la cadena
	"""Obtención de la Blockchain """
	response = { 'chain'  : blockchain.chain,
				 'length' : len(blockchain.chain)
				}
	return jsonify(response), 200

@app.route('/is_valid', methods = ['GET'])
def is_valid():														# Comprobacion de si la blockchain es valida
	"""Comprobacion de si la blockchain es valida """
	is_valid = blockchain.is_chain_valid(blockchain.chain)
	if is_valid:
		response = {'message' : '¡La cadena de bloques es válida!'}
	else:
		response = {'message' : '¡La cadena de bloques NO es válida!'}
	return jsonify(response), 200

app.run()