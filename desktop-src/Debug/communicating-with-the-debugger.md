---
Description: 'The OutputDebugString function sends a string from the process being debugged to the debugger by generating an OUTPUT\_DEBUG\_STRING\_EVENT debugging event. A process can detect whether it is being debugged by calling the IsDebuggerPresent function.'
ms.assetid: 'd9e1d565-fb76-4d91-8aa7-4ff0ff31f71f'
title: Communicating with the Debugger
---

# Communicating with the Debugger

The [**OutputDebugString**](outputdebugstring.md) function sends a string from the process being debugged to the debugger by generating an OUTPUT\_DEBUG\_STRING\_EVENT debugging event. A process can detect whether it is being debugged by calling the [**IsDebuggerPresent**](isdebuggerpresent.md) function.

The [**DebugBreak**](debugbreak.md) function causes a breakpoint exception in the current process. A breakpoint is a location in a program where execution is stopped to allow the developer to examine the program's code, variables, and register values and, as necessary, to make changes, continue execution, or terminate execution.

The [**FatalExit**](fatalexit.md) function terminates the current process and gives execution control to the debugger, but unlike [**DebugBreak**](debugbreak.md), it does not generate an exception. This function should only be used as a last resort, because it does not always free the process's memory or close its files.

 

 



