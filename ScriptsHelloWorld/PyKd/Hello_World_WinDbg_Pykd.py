import pykd

def main():
	# Print "Hello World" to the Python console
	print("Hello World")
	
	# Execute the WinDbg command !process 0 0 and get the output
	result = pykd.dbgCommand("!process 0 0")
	
	# Print the result of the command to the Python console
	print(result)

if __name__ == "__main__":
	main()