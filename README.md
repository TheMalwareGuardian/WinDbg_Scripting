# 🕵️‍♂️ Hello WinDbg Scripting

This repository serves as a starting point for scripting in WinDbg, covering WinDbg native scripting, JavaScript, and PyKD (Python).

<p align="center">
	<img src="Images/Logos/Logo_WinDbg_Scripting.png">
</p>


---
---
---


## 📑 Table of Contents

* [What You'll Find Here](#what-youll-find-here)
* [WinDbg Commands Reference](#windbg-commands-reference)
* [More WinDbg Commands & Information](#more-windbg-commands-and-information)


---
---
---


<div id='what-youll-find-here'/>

## 📋 What You'll Find Here
- **Basic Hello World scripts** for getting started with WinDbg scripting.
- **WinDbg Native Scripting** examples to automate debugging tasks.
- **JavaScript and Python (pykd)** samples for extending WinDbg capabilities.
- **Complete pykd package** including DLLs and required files to ensure it functions correctly.
- **A copy of the official WinDbg documentation** for quick reference.
-  **A collection of essential WinDbg commands** to navigate and operate efficiently.
- **Links to additional Windows Kernel debugging resources** for deeper exploration.


---
---
---


<div id='windbg-commands-reference'/>

## 📜 WinDbg Commands Reference  

A categorized list of essential WinDbg commands for debugging, reverse engineering, and malware analysis.

---

| **Category** | **Command** | **Description** | **Example Usage** |
|-------------|------------|-----------------|--------------------|
| 🔹 **Help & Documentation** | | | |
|  | `.help` | Show help menu for commands | `.help` |
|  | `.hh` | Open the WinDbg help documentation for a specific command | `.hh lm` |
|  | `!help` | Show help for extension commands | `!help` |
| 🔹 **Debugger State & Scripting** | | | |
|  | `dx Debugger.State` | Show debugger state | `dx Debugger.State` |
|  | `dx -r2 Debugger.State.Scripts` | Show loaded scripts | `dx -r2 Debugger.State.Scripts` |
|  | `.scriptrun <script.js>` | Run a JavaScript script | `.scriptrun myscript.js` |
|  | `.scriptload <script.js>` | Load a JavaScript script into the debugger | `.scriptload myscript.js` |
|  | `.scriptunload <script.js>` | Unload a loaded script | `.scriptunload myscript.js` |
|  | `.scriptlist` | List all loaded scripts | `.scriptlist` |
| 🔹 **Logging & Output Management** | | | |
|  | `.logopen <file>` | Open a log file to store session output | `.logopen C:\debug.log` |
|  | `.logfile` | Display the path of the currently active log file | `.logfile` |
|  | `.logclose` | Stop logging debug output | `.logclose` |
| 🔹 **General Commands** | | | |
|  | `? expression` | Evaluate an expression | `? 0x100 + 0x200` |
|  | `.chain` | Show loaded extension DLLs | `.chain` |
|  | `.time` | Show debugging session timestamps | `.time` |
|  | `.cls` | Clear screen | `.cls` |
| 🔹 **Execution Control** | | | |
|  | `g` | Continue execution of the target process | `g` |
|  | `gh` | Continue execution but break on the next hard-coded breakpoint | `gh` |
|  | `gn` | Continue execution, ignoring the next exception | `gn` |
|  | `gu` | Continue execution until the function returns | `gu` |
|  | `t` | Step into | `t` |
|  | `p` | Step over | `p` |
| 🔹 **Breakpoints** | | | |
|  | `bp <address>` | Set a breakpoint at a memory address | `bp fffff80079966b90` |
|  | `bp <module>!<function>` | Set a breakpoint on a function | `bp nt!NtCreateFile` |
|  | `bm <module>!*` | Breakpoints on all functions | `bm nt!*` |
|  | `bl` | List all breakpoints | `bl` |
|  | `bc <n>` | Clear a specific breakpoint | `bc 1` |
|  | `bc *` | Clear all breakpoints | `bc *` |
| 🔹 **Modules & Symbols** | | | |
|  | `lm` | List all loaded modules | `lm` |
|  | `lm m <module>` | Show details for a module | `lm m nt` |
|  | `x <module>!*` | List all symbols in a module | `x nt!*` |
|  | `x <module>!<symbol>` | Find a function or symbol | `x nt!ExAllocatePoolWithTag` |
|  | `!sym` | Show symbol loading status | `!sym` |
|  | `.reload` | Reload all symbols | `.reload` |
|  | `.symfix` | Reset symbol path | `.symfix` |
| 🔹 **Process & Thread Management** | | | |
|  | `!process 0 0` | List all processes with details | `!process 0 0` |
|  | `!process <Address> 1` | Show detailed process information | `!process ffffab0c5a691040 1` |
|  | `.process <Address>` | Switch to a specific process | `.process ffffab0c60a9e080` |
|  | `dt _EPROCESS` | Show process structure | `dt _EPROCESS` |
|  | `!handle -p` | Show process handles | `!handle -p` |
|  | `!token` | Show access tokens | `!token` |
|  | `!peb` | Show Process Environment Block (PEB) | `!peb` |
|  | `!thread` | Show details of the current thread | `!thread` |
|  | `!teb` | Show Thread Environment Block (TEB) | `!teb` |
|  | `!running` | Show all running threads in the system | `!running` |
|  | `!stacks` | Show call stacks of all threads | `!stacks` |
| 🔹 **Memory Analysis** | | | |
|  | `!address` | Show memory usage stats | `!address` |
|  | `!vad` | Show virtual address descriptor (VAD) tree | `!vad` |
|  | `!pte <address>` | Show Page Table Entry | `!pte fffff80079a4af5c` |
|  | `dq <address>` | Dump memory in **QWORDs** | `dq ffffbe8e8c5a4080+0x1d8 L2` |
|  | `dd <address>` | Dump memory in **DWORDs** | `dd ffffbe8e8c5a4080+0x1d8 L2` |
|  | `dw <address>` | Dump memory in **WORDS** | `dw ffffbe8e8c5a4080+0x1d8 L2` |
|  | `db <address>` | Dump memory in **bytes** | `db ffffbe8e8c5a4080+0x1d8 L2` |
|  | `dc <address>` | Dump memory as **ANSI characters** | `dc ffffbe8e8c5a4080+0x338` |
|  | `du <address>` | Dump memory as **Unicode characters** | `du ffffbe8e8c5a4080+0x338` |
| 🔹 **Code Disassembly** | | | |
|  | `u <address>` | Disassemble code at a specific address | `u fffff80079966b90` |
|  | `ub <address>` | Disassemble code backwards from an address | `ub fffff80079966b90` |
|  | `uf <function>` | Disassemble an entire function | `uf nt!NtCreateFile` |
| 🔹 **Registry Analysis** | | | |
|  | `!reg hivelist` | Display the list of registry hives in the system | `!reg hivelist` |
|  | `!reg querykey <FullKeyPath>` | Dump subkeys and values of a registry key | `!reg querykey \Registry\Machine\SYSTEM` |
| 🔹 **Objects & Device Analysis** | | | |
|  | `!drvobj <driver>` | Show driver object details | `!drvobj ntfs` |
|  | `!devobj <device>` | Show device object details | `!devobj \Device\HarddiskVolume1` |
|  | `!irpfind` | List all active IRPs in memory | `!irpfind` |
|  | `!irp <address>` | Show IRP details | `!irp fffffa8004e9b460` |


<details>
<summary> Click to expand WinDbg .help commands output</summary>

```
lkd> .help
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z All

. commands:
.allow_bp_ba_convert [0|1] - Control bp/bm/bu breakpoints to use hardware debug register support
.allow_exec_cmds [0|1] - control execution commands
.allow_image_mapping [0|1] - control on-demand image file mapping
.apply_dbp [<options>] - add current data breakpoint state to a register context
.asm [<options>] - set disassembly options
.asm- [<options>] - clear disassembly options
.attach <proc> - attach to <proc> at next execution
.block { <commands> } - brackets a set of commands for nested execution
.break - break out of the enclosing loop
.bugcheck - display the bugcheck code and parameters for a crashed system
.cache [<options>] - virtual memory cache control
.catch { <commands> } - catch failures in commands
.chain - list current extensions
.clients - list currently active clients
.codearch <address> - determine the architecture of code at the given address
.context [<address>] - set page directory base
.continue - continue the enclosing loop
.copysym [<options>] <path> - copy current symbol files to a directory
.cordll [<options>] - control CLR debug DLL
.crash - cause target to bugcheck
.create <command line> - create a new process
.createdir [<options>] [<path>] - control process creation options
.cxr <address> - dump context record at specified address k* after this gives cxr stack
.dbgdbg - attach a debugger to the current debugger
.debug_sw_wow [0|1] - allow interaction with software WOW emulation
.detach - detach from the current process/dump
.dml_file <file> - output DML content from file
.dml_flow <start> <addr> - show basic block code flow
.dml_start [<options>] - navigable overview of debugger activities
.do { <commands> } (<cond>) - execute <commands> until <cond> is zero
.drivers - This command was removed -- use 'lm' or .reload -l)
.dump [<options>] <filename> - create a dump file on the host system
.echo ["<string>"|<string>] - echo string
.echocpunum [0|1] - toggle DbgPrint processor number output
.echotime - output debugger time
.echotimestamps [0|1] - toggle timestamp output on events
.ecxr - dump context record for current exception
.excr - dump context record for current exception
.effmach [<machine>] - change current machine type
.else { <commands> } - if/then/else conditional execution
.elsif (<cond>) { <commands> } [<else clauses>] - if/then/else conditional execution
.enable_long_status [0|1] - dump LONG types in default base
.enable_unicode [0|1] - dump USHORT array/pointers and unicode strings
.endsrv <id> - disable the given engine server
.endpsrv - cause the current session's remote server to exit
.enumtag - enumerate available tagged data
.event_code - display cached event instructions
.eventlog - display log of recent events
.events - display and select available events
.eventstr - display any event strings registered by debuggee
.exepath [<dir>[;...]] - set executable search path
.exepath+ [<dir>[;...]] - append executable search path
.expr - control expression evaluator
.exptr <address> - do .exr and .cxr for EXCEPTION_POINTERS
.exr <address> - dump exception record at specified address
.extmatch [<opts>] <pattern> - display all extensions matching pattern
.extpath <opts> [<dir>[;...]] - set extension search path
.extpath+ <opts> [<dir>[;...]] - append extension search path
.f+ - set current stack frame to caller of current frame
.f- - set current stack frame to callee of current frame
.fiber <address> - sets context of fiber at address resets context if no address specified
.fiximports <pattern> - attempts to link imports for images
.fnent <address> - dump function entry for the given code address
.fnret <fnaddr> [<retval>] - display formatted return value
.for ( <init> ; <cond> ; <step> ) { <commands> } - execute <commands> and <step> until <cond> is zero
.force_chpe_effmach [0|1] - force CHPE locals to be relative to the effective machine
.force_radix_output [0|1] - dump integer types in default base
.force_system_init [<options>] - force pending systems to initialize if possible
.force_tb - forcibly allow branch tracing
.foreach [opts] ( <alias> { <tcmds> } ) { <ecmds> } - execute <ecmds> for each token in the output of <tcmds>
.fpo <options> - control override FPO information
.frame [<frame>] - set current stack frame for locals
.formats <expr> - displays expression result in many formats
.help [<options>] - display this help
.holdmem <options> [range] - hold and compare memory data
.if (<cond>) { <commands> } [<else clauses>] - if/then/else conditional execution
.ignore_missing_pages [0|1] - control kernel summary dump missing page error message
.ignore_wow_kd_context [0|1] - control WOW64 kernel debugging partial context error message
.imgscan <options> - scan memory for PE images
.jdinfo [/u] <jdi_addr> - interpret AeDebug information
.kframes <count> - set default stack trace depth
.lastevent - display the last event that occurred
.leave - exit the enclosing .catch
.lines - toggle line symbol loading
.load <name> - add this extension DLL to the extension chain
.loadby <name> <mod> - add the extension DLL in the module directory to the extension chain
.locale [<locale>] - set the current locale
.logfile - display log status
.logopen [<file>] - open new log file
.logappend [<file>] - append to log file
.logclose - close log file
.netsyms [0|1] - allow/disallow net symbol paths
.netuse [<options>] - manage net connections
.noshell - disable shell commands
.noversion - disable extension version checking
.nvlist - display the set of .NATVIS files loaded into the debugger
.nvload <name> - load a .NATVIS file
.nvunload <name> - unload a .NATVIS file
.nvunloadall - unload all .NATVIS files
.ofilter <pattern> - filter debuggee output against the given pattern
.opendump <file> - open a dump file
.outmask <mask> - set bits in the current output mask
.outmask- <mask> - clear bits in the current output mask
.pacmask [<options>] - display or override current PAC mask
.pcmd [<options>] - control per-prompt command
.pop [<options>] - pop state
.prefer_dml [0|1] - control DML mode default
.printf "<format>", <args...> - formatted output
.process [<address>] - sets implicit process resets default if no address specified
.prompt_allow [<options>] - control what information can be displayed at the prompt
.push [<options>] - push state
.quit_lock [<options>] - locks session against unexpected quit
.readmem <file> <range> - read raw memory from a file
.record_branches [0|1] - controls recording of processor branching
.reload [<image.ext>[=<address>,<size>]] - reload symbols
.restart - request a session restart
.remote <pipename> - start remote.exe server
.secure [0|1] - disallow operations dangerous for the host
.scriptdebug [<script name>] - enters the script debugger or starts debugging a script loaded into the debugger
.scriptlist - display the set of scripts loaded into the debugger
.scriptload <name> - load a script file
.scriptproviders - display the set of script providers in the debugger
.scriptrun - load a script file and execute its main function
.scriptunload <name> - unload a script file
.scriptunloadall - unload all script files
.veighton - enable the V8 JavaScript provider
.veightoff - disable the V8 JavaScript provider
.send_file <options> - send files to remote server
.server <options> - start engine server
.servers - list active remoting servers
.segmentation <opts> - overrides segmentation mode
.setdll <name> - debugger will search for extensions in this DLL first
.settings - manage settings
.shell [<command>] - execute shell command
.show_read_failures [<opts>] - control extra read failure output
.show_sym_failures [<opts>] - control extra symbol failure output
.sleep <milliseconds> - debugger sleeps for given duration useful for allowing access to a machine that's broken in on an ntsd -d
.srcfix [<path extra>] - fix source search path
.srcfix+ [<path extra>] - append fixed source search path
.srcnoisy [0|1] - control verbose source loading output
.srcpath [<dir>[;...]] - set source search path
.srcpath+ [<dir>[;...]] - append source search path
.step_filter [<opts>] ["<pattern>[;<pattern>...]"] - Set symbol patterns to skip when stepping
.symfix [<localsym>] - fix symbol search path
.symfix+ [<localsym>] - append fixed symbol search path
.symopt <flags> - set symbol options
.symopt+ <flags> - set symbol options
.symopt- <flags> - clear symbol options
.sympath [<dir>[;...]] - set symbol search path
.sympath+ [<dir>[;...]] - append symbol search path
.tagmask [<options>] - display or override current pointer tag mask
.targetloglevel <level> - sets diagnostic logging level for plug-ins
.thread [<address>] - sets context of thread at address resets default context if no address specified
.time - displays session time information
.ttime - displays thread time information
.tlist - list running processes
.trap <address> - dump a trap frame
.tss <selector> - dump a Task State Segment
.typeopt <flags> - set/clear type options
.unload <name> - remove this extension DLL from the list of extension DLLs
.unloadall - remove all extension DLLs from the list of extensions DLLs
.wake - wake up a .sleep'ing debugger
.while (<cond>) { <commands> } - execute <commands> while <cond> is non-zero
.writemem <file> <range> - write raw memory to a file
.rrestart - register current session for Application Restart
.urestart - unregister current session from Application Restart
.inline - query the state whether debuggers should query inline functions
.stackprovider - query the state whether debugger should query stack dump providers
.stkwalk_force_frame_pointer - query or set the state whether debuggers should unwind stack solely based on frame pointer
.hideinjectedcode [<on|off|help>] - Hide injected calls from stepping in source mode
.enablepackagedebug <packageFullName> - Enable debugging for UWP application.
.disablepackagedebug <packageFullName> - Disable debugging for UWP application.
.suspendpackage <packageFullName> - Suspends a UWP application.
.resumepackage <packageFullName> - Resumes a UWP application.
.querypackage <packageFullName> - Displays the state of a UWP application.
.querypackages - Lists all UWP applications and their state.
.createpackageapp <packageFullName> <appName> [<arguments>] - Enables debugging and launches a UWP application.
.terminatepackageapp <packageFullName> - Terminates all processes for UWP application.
.activatepackagebgtask <packageFullName> <bgTaskId> - Enables debugging and launches a UWP background task.
.findext <search string> - Search the help of all extensions in the extension repository.
.kdtargetmac - Display the target MAC address
.generatedoc <XmlFileName> - Generates an XML documentation file for the registered named models.
.lookupxfghash <XFG Hash> [Module] - Looks up an XFG prototype hash from symbols with a given module search pattern (default is all modules with symbols loaded).
.extensionnugetfeature [0|1] - control if an EG uses file share or the new Nuget feed). Default is 0.
.check_for_gallery_updates - Checks all Nuget or file share extension repositories for updates.
.update_ms_nuget_cred_provider [web|artifacts|help] - Updates (if available) Microsoft Nuget Credential Provider.

Use ".hh <command>" or open debugger.chm in the debuggers directory to get
detailed documentation on a command.
```
</details>


---
---
---


<div id='more-windbg-commands-and-information'/>

## 🔍 More WinDbg Commands & Information

If you have any doubts about a specific command, make sure to read the official documentation on the [WinDbg debugger](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/) and [WinDbg debugger commands](https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/)**.  

A local copy of the official WinDbg documentation is also available in this repository under the WinDbgDocumentation folder.  

📌 [WinDbg Documentation](https://github.com/TheMalwareGuardian/WinDbg_Scripting/tree/main/WinDbgDocumentation/)

Additionally, you can find more information, debugging techniques, and practical examples in the following repository:  

📌 [TheMalwareGuardian: Awesome Bootkits & Rootkits Development - Debugging Section](https://github.com/TheMalwareGuardian/Awesome-Bootkits-Rootkits-Development?tab=readme-ov-file#debugging)
