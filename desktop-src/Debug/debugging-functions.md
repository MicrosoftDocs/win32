---
description: The following functions are used with debugging.
ms.assetid: 95a838a2-f138-4682-b733-3f363b6c4a4b
title: Debugging Functions
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Functions

The following functions are used with debugging.



| Function                                                           | Description                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**CheckRemoteDebuggerPresent**](/windows/win32/api/debugapi/nf-debugapi-checkremotedebuggerpresent)   | Determines whether the specified process is being debugged.                         |
| [**ContinueDebugEvent**](/windows/win32/api/debugapi/nf-debugapi-continuedebugevent)                   | Enables a debugger to continue a thread that previously reported a debugging event. |
| [**DebugActiveProcess**](/windows/win32/api/debugapi/nf-debugapi-debugactiveprocess)                   | Enables a debugger to attach to an active process and debug it.                     |
| [**DebugActiveProcessStop**](/windows/win32/api/debugapi/nf-debugapi-debugactiveprocessstop)           | Stops the debugger from debugging the specified process.                            |
| [**DebugBreak**](/windows/win32/api/debugapi/nf-debugapi-debugbreak)                                   | Causes a breakpoint exception to occur in the current process.                      |
| [**DebugBreakProcess**](/windows/desktop/api/WinBase/nf-winbase-debugbreakprocess)                     | Causes a breakpoint exception to occur in the specified process.                    |
| [**DebugSetProcessKillOnExit**](/windows/desktop/api/WinBase/nf-winbase-debugsetprocesskillonexit)     | Sets the action to be performed when the calling thread exits.                      |
| [**FatalExit**](/windows/desktop/api/WinBase/nf-winbase-fatalexit)                                     | Transfers execution control to the debugger.                                        |
| [**FlushInstructionCache**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-flushinstructioncache)             | Flushes the instruction cache for the specified process.                            |
| [**GetThreadContext**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadcontext)                       | Retrieves the context of the specified thread.                                      |
| [**GetThreadSelectorEntry**](/windows/desktop/api/WinBase/nf-winbase-getthreadselectorentry)           | Retrieves a descriptor table entry for the specified selector and thread.           |
| [**IsDebuggerPresent**](/windows/win32/api/debugapi/nf-debugapi-isdebuggerpresent)                     | Determines whether the calling process is being debugged by a user-mode debugger.   |
| [**OutputDebugString**](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa)                     | Sends a string to the debugger for display.                                         |
| [**ReadProcessMemory**](/windows/win32/api/memoryapi/nf-memoryapi-readprocessmemory)                     | Reads data from an area of memory in a specified process.                           |
| [**SetThreadContext**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadcontext)                       | Sets the context for the specified thread.                                          |
| [**WaitForDebugEvent**](/windows/win32/api/debugapi/nf-debugapi-waitfordebugevent)                     | Waits for a debugging event to occur in a process being debugged.                   |
| [**WaitForDebugEventEx**](/windows/win32/api/debugapi/nf-debugapi-waitfordebugeventex)                     | Waits for a debugging event to occur in a process being debugged, and enables support for Unicode strings from OutputDebugStringW.                   |
| **Wow64GetThreadContext**          | Retrieves the context of the specified WOW64 thread.                                |
| [**Wow64GetThreadSelectorEntry**](/windows/desktop/api/WinBase/nf-winbase-wow64getthreadselectorentry) | Retrieves a descriptor table entry for the specified selector and WOW64 thread.     |
| [**Wow64SetThreadContext**](/windows/desktop/api/WinBase/nf-winbase-wow64setthreadcontext)             | Sets the context of the specified WOW64 thread.                                     |
| [**WriteProcessMemory**](/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory)                   | Writes data to an area of memory in a specified process.                            |



 

 

 
