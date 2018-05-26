---
Description: The following functions are used with debugging.
ms.assetid: 95a838a2-f138-4682-b733-3f363b6c4a4b
title: Debugging Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Debugging Functions

The following functions are used with debugging.



| Function                                                           | Description                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**CheckRemoteDebuggerPresent**](/windows/win32/WinBase/?branch=master)   | Determines whether the specified process is being debugged.                         |
| [**ContinueDebugEvent**](/windows/win32/WinBase/?branch=master)                   | Enables a debugger to continue a thread that previously reported a debugging event. |
| [**DebugActiveProcess**](/windows/win32/WinBase/?branch=master)                   | Enables a debugger to attach to an active process and debug it.                     |
| [**DebugActiveProcessStop**](/windows/win32/WinBase/?branch=master)           | Stops the debugger from debugging the specified process.                            |
| [**DebugBreak**](/windows/win32/WinBase/?branch=master)                                   | Causes a breakpoint exception to occur in the current process.                      |
| [**DebugBreakProcess**](/windows/win32/WinBase/nf-winbase-debugbreakprocess?branch=master)                     | Causes a breakpoint exception to occur in the specified process.                    |
| [**DebugSetProcessKillOnExit**](/windows/win32/WinBase/nf-winbase-debugsetprocesskillonexit?branch=master)     | Sets the action to be performed when the calling thread exits.                      |
| [**FatalExit**](/windows/win32/WinBase/nf-winbase-fatalexit?branch=master)                                     | Transfers execution control to the debugger.                                        |
| [**FlushInstructionCache**](flushinstructioncache.md)             | Flushes the instruction cache for the specified process.                            |
| [**GetThreadContext**](/windows/win32/WinBase/nf-dbgeng-idebugadvanced4-getthreadcontext?branch=master)                       | Retrieves the context of the specified thread.                                      |
| [**GetThreadSelectorEntry**](/windows/win32/WinBase/nf-winbase-getthreadselectorentry?branch=master)           | Retrieves a descriptor table entry for the specified selector and thread.           |
| [**IsDebuggerPresent**](/windows/win32/WinBase/?branch=master)                     | Determines whether the calling process is being debugged by a user-mode debugger.   |
| [**OutputDebugString**](/windows/win32/WinBase/?branch=master)                     | Sends a string to the debugger for display.                                         |
| [**ReadProcessMemory**](readprocessmemory.md)                     | Reads data from an area of memory in a specified process.                           |
| [**SetThreadContext**](/windows/win32/WinBase/nf-dbgeng-idebugadvanced4-setthreadcontext?branch=master)                       | Sets the context for the specified thread.                                          |
| [**WaitForDebugEvent**](/windows/win32/WinBase/?branch=master)                     | Waits for a debugging event to occur in a process being debugged.                   |
| [**Wow64GetThreadContext**](/windows/win32/WinBase/nf-winbase-wow64getthreadcontext?branch=master)             | Retrieves the context of the specified WOW64 thread.                                |
| [**Wow64GetThreadSelectorEntry**](/windows/win32/WinBase/nf-winbase-wow64getthreadselectorentry?branch=master) | Retrieves a descriptor table entry for the specified selector and WOW64 thread.     |
| [**Wow64SetThreadContext**](/windows/win32/WinBase/nf-winbase-wow64setthreadcontext?branch=master)             | Sets the context of the specified WOW64 thread.                                     |
| [**WriteProcessMemory**](writeprocessmemory.md)                   | Writes data to an area of memory in a specified process.                            |



 

 

 



