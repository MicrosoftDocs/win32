---
Description: The following functions are used with debugging.
ms.assetid: 95a838a2-f138-4682-b733-3f363b6c4a4b
title: Debugging Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Functions

The following functions are used with debugging.



| Function                                                           | Description                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**CheckRemoteDebuggerPresent**](/windows/desktop/api/WinBase/)   | Determines whether the specified process is being debugged.                         |
| [**ContinueDebugEvent**](/windows/desktop/api/WinBase/)                   | Enables a debugger to continue a thread that previously reported a debugging event. |
| [**DebugActiveProcess**](/windows/desktop/api/WinBase/)                   | Enables a debugger to attach to an active process and debug it.                     |
| [**DebugActiveProcessStop**](/windows/desktop/api/WinBase/)           | Stops the debugger from debugging the specified process.                            |
| [**DebugBreak**](/windows/desktop/api/WinBase/)                                   | Causes a breakpoint exception to occur in the current process.                      |
| [**DebugBreakProcess**](/windows/desktop/api/WinBase/nf-winbase-debugbreakprocess)                     | Causes a breakpoint exception to occur in the specified process.                    |
| [**DebugSetProcessKillOnExit**](/windows/desktop/api/WinBase/nf-winbase-debugsetprocesskillonexit)     | Sets the action to be performed when the calling thread exits.                      |
| [**FatalExit**](/windows/desktop/api/WinBase/nf-winbase-fatalexit)                                     | Transfers execution control to the debugger.                                        |
| [**FlushInstructionCache**](https://www.bing.com/search?q=**FlushInstructionCache**)             | Flushes the instruction cache for the specified process.                            |
| [**GetThreadContext**](/windows/desktop/api/WinBase/nf-dbgeng-idebugadvanced4-getthreadcontext)                       | Retrieves the context of the specified thread.                                      |
| [**GetThreadSelectorEntry**](/windows/desktop/api/WinBase/nf-winbase-getthreadselectorentry)           | Retrieves a descriptor table entry for the specified selector and thread.           |
| [**IsDebuggerPresent**](/windows/desktop/api/WinBase/)                     | Determines whether the calling process is being debugged by a user-mode debugger.   |
| [**OutputDebugString**](/windows/desktop/api/WinBase/)                     | Sends a string to the debugger for display.                                         |
| [**ReadProcessMemory**](https://www.bing.com/search?q=**ReadProcessMemory**)                     | Reads data from an area of memory in a specified process.                           |
| [**SetThreadContext**](/windows/desktop/api/WinBase/nf-dbgeng-idebugadvanced4-setthreadcontext)                       | Sets the context for the specified thread.                                          |
| [**WaitForDebugEvent**](/windows/desktop/api/WinBase/)                     | Waits for a debugging event to occur in a process being debugged.                   |
| [**Wow64GetThreadContext**](/windows/desktop/api/WinBase/nf-winbase-wow64getthreadcontext)             | Retrieves the context of the specified WOW64 thread.                                |
| [**Wow64GetThreadSelectorEntry**](/windows/desktop/api/WinBase/nf-winbase-wow64getthreadselectorentry) | Retrieves a descriptor table entry for the specified selector and WOW64 thread.     |
| [**Wow64SetThreadContext**](/windows/desktop/api/WinBase/nf-winbase-wow64setthreadcontext)             | Sets the context of the specified WOW64 thread.                                     |
| [**WriteProcessMemory**](https://www.bing.com/search?q=**WriteProcessMemory**)                   | Writes data to an area of memory in a specified process.                            |



 

 

 



