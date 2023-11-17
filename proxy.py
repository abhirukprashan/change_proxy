import os
while True:
	address = str(input("enter proxy address: ")) ##input address
	port = str(input("enter port: ")) ## input port

	#commands
	github_proxy = "cmd /k git config --global http.proxy http://" + address + ":" + port
	npm_proxy1 = "cmd /k npm config set proxy http://" + address + ":" + port
	npm_proxy2 = "cmd /k npm config set https-proxy http://" + address + ":"+ port

	try:
		print("all set !!!!!!")
		os.system(github_proxy)
		os.system(npm_proxy1)
		os.system(npm_proxy2)
		


	except:
		print("error")