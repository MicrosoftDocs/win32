---
description: The OutputDebugString function sends a string from the process being debugged to the debugger by generating an OUTPUT\_DEBUG\_STRING\_EVENT debugging event. A process can detect whether it is being debugged by calling the IsDebuggerPresent function.
ms.assetid: d9e1d565-fb76-4d91-8aa7-4ff0ff31f71f
title: Communicating with the Debugger
ms.topic: article
ms.date: 05/31/2018
---

# Communicating with the Debugger

The [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) function sends a string from the process being debugged to the debugger by generating an OUTPUT\_DEBUG\_STRING\_EVENT debugging event. A process can detect whether it is being debugged by calling the [**IsDebuggerPresent**](/windows/win32/api/debugapi/nf-debugapi-isdebuggerpresent) function.

The [**DebugBreak**](/windows/win32/api/debugapi/nf-debugapi-debugbreak) function causes a breakpoint exception in the current process. A breakpoint is a location in a program where execution is stopped to allow the developer to examine the program's code, variables, and register values and, as necessary, to make changes, continue execution, or terminate execution.

The [**FatalExit**](/windows/desktop/api/WinBase/nf-winbase-fatalexit) function terminates the current process and gives execution control to the debugger, but unlike [**DebugBreak**](/windows/win32/api/debugapi/nf-debugapi-debugbreak), it does not generate an exception. This function should only be used as a last resort, because it does not always free the process's memory or close its files.

 

 
