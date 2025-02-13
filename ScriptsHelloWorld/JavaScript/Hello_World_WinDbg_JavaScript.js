// WinDbg JavaScript sample
// Says Hello World!

// Code at root will be run with .scriptrun and .scriptload
host.diagnostics.debugLog("***> Hello World! \n");

function sayHi()
{
	//Say Hi 
	host.diagnostics.debugLog("Hi from JavaScript! \n");
}