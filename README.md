## Mi Primera Blockchain con Python
### Curso udemy "Curso Completo de Blockchain de cero a experto"
### Pasos a seguir para ejecutar el servidor
1. Compilamos y arrancamos con py servidor-web.py, nos saldra algo asi:

		ngrok by @inconshreveable (Ctrl+C to quit)

		Session Status 				online  
		* Running on 					http://5d1f-79-154-128-208.ngrok.io    
		* Traffic stats available on 			http://127.0.0.1:4040
		Web Interface  				http://127.0.0.1:4040 
		Forwarding     				http://5d1f-79-154-128-208.ngrok.io -> http://localhost:5000
		Forwarding     				https://5d1f-79-154-128-208.ngrok.io -> http://localhost:5000

	    Connections     ttl     opn     rt1     rt5     p50     p90
			   	 0       0       0.00    0.00    0.00    0.00 
	
2. Abrimos postman(por ejemplo) e introducimos en una peticion GET la url que esta seguida de "Running on"
3. Seguidamente en postman una vez pegada la url anterior "http://5d1f-79-154-128-208.ngrok.io" le añadimos el metodo que queramos realizar
4. Si quisieramos crear bloques lo hariamos con
	##### **[GET]** ~/http://5d1f-79-154-128-208.ngrok.io/mine_block (Obtener ultimo bloque minado)
	![GET http://5d1f-79-154-128-208.ngrok.io/mine_block](https://i.ibb.co/pWjyHyp/mine-block.jpg)
5. Si quisieramos obtener la cadena de bloques lo hariamos con
	##### **[GET]** ~/http://5d1f-79-154-128-208.ngrok.io/get_chain (Obtener toda la cadena de bloques)
	![GET http://5d1f-79-154-128-208.ngrok.io/mine_block](https://i.ibb.co/tmGNsQh/get-chain.jpg)
6. Si quisieramos verificar que la cadena es valida lo hariamos con ç
	##### **[GET]** ~/http://5d1f-79-154-128-208.ngrok.io/is_valid (Obtener si el bloque es valido)
	![GET http://5d1f-79-154-128-208.ngrok.io/mine_block](https://i.ibb.co/DDYvqFZ/is-valid.jpg)