#Importacion de librerías
import datetime
import hashlib
import json
from flask		 import Flask, jsonify
from flask_ngrok import run_with_ngrok

class Blockchain:

	def __init__(self):
		""" Constructor de la clase Blockchain"""

		self.chain = []
		self.create_block(proof = 1, previous_hash = '0') # Como antes no hay ningun bloque lo inicializamos nosotros

	def create_block(self, proof, previous_hash):
		""" Creación de un nuevo bloque
			Arguments:
				- proof: Hash del bloque actual (proof != hash)
				- previous_hash: Nonce del bloque previo
				
			Returns:
				- block: Nuevo bloque creado
		 """
		block = { 'index' : len(self.chain)+1,
				  'timestamp': str(datetime.datetime.now()),
				  'proof': proof,
				  'previous_hash': previous_hash}
		self.chain.append(block) # Con append añadimos el bloque a la cadena 
		return block
	
	def get_previous_block(self):
		""" Obtención del bloque previo de la Blockchain
		
			Returns:
				- Obtencion del utlimo bloque de la blockchain
		"""
		return self.chain[-1] # Con el -1 indicamos que es el ultimo elemento de la cadena
	
	def proof_of_work(self,previous_proof):
		""" Protocolo de concenso Proof of Work(PoW)
			
			Arguments:
				- previous_proof: Nonce del bloque previos
			
			Returns:
				- new_proof: Devolución del nuevo hash obtenido con PoW
		"""
		new_proof = 1 # Será el nonce que vamos a utilizar, valor que dichos mineros van a calcular 
		check_proof = False
		while check_proof is False:
			hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest() # Usaremos el algoritmo de cifrado hash256 que es el que usa bitcoin actualmente
			if hash_operation[:4] == '0000':
				check_proof = True
			else:
				new_proof += 1
		return new_proof
	
	def hash(self,block):
		"""Cálculo del hash de un bloque.
		
			Arguments:  
				-block: Identifica a un bloque de la Blockchain
			
			Returns:
				-hash_block: Devuelve el hash del bloque
		"""
		encoded_block = json.dumps(block, sort_keys=True).encode() # Usamos el modulo json que recibe el bloque y sort_keys = true para que lo ponga en el formato correcto
		hash_block = hashlib.sha256(encoded_block).hexdigest() #cifrados el json(Str)
		return hash_block

	def is_chain_valid(self, chain):
		"""Determina si la Blockchain es valida
		
			Arguments: 
				- chain: Cadena de bloques que contiene toda la información de las transacciones
				
			Returns:
				- True/False: Devuelve un booleano en funcion de la validez de la Blockchain. (True = valida, False = invalida)
			"""
		previous_block = chain[0] # inicializamos para empezar en el primer bloque de la cadena
		block_index = 1
		while block_index < len(chain): # Vamos del inicio al final
			block = chain[block_index] # Una vez tenemos el primer campo analizamos el primer bloque
			# Bloque 200 (hash, hash_previo) -> Bloque 201 (hash, hash_previo), el hash del bloque 200 tiene que ser igual al hash_previo del 201
			if block['previous_hash'] != self.hash(previous_block): # cogemos el previous_hash del bloque actual que tiene que ser igual hash del bloque anterior
				return False
			previous_block = previous_block['proof']
			proof = block['proof']
			hash_operation = hashlib.sha256(str(proof**2 - previous_block**2).encode()).hexdigest()
			if hash_operation[:4] != '0000':
				return False
			previous_block = block
			block_index += 1
		return True







