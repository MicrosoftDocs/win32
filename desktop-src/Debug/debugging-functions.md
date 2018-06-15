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
| [**CheckRemoteDebuggerPresent**](https://msdn.microsoft.com/en-us/library/ms679280(v=VS.85).aspx)   | Determines whether the specified process is being debugged.                         |
| [**ContinueDebugEvent**](https://msdn.microsoft.com/en-us/library/ms679285(v=VS.85).aspx)                   | Enables a debugger to continue a thread that previously reported a debugging event. |
| [**DebugActiveProcess**](https://msdn.microsoft.com/en-us/library/ms679295(v=VS.85).aspx)                   | Enables a debugger to attach to an active process and debug it.                     |
| [**DebugActiveProcessStop**](https://msdn.microsoft.com/en-us/library/ms679296(v=VS.85).aspx)           | Stops the debugger from debugging the specified process.                            |
| [**DebugBreak**](https://msdn.microsoft.com/en-us/library/ms679297(v=VS.85).aspx)                                   | Causes a breakpoint exception to occur in the current process.                      |
| [**DebugBreakProcess**](/windows/desktop/api/WinBase/nf-winbase-debugbreakprocess)                     | Causes a breakpoint exception to occur in the specified process.                    |
| [**DebugSetProcessKillOnExit**](/windows/desktop/api/WinBase/nf-winbase-debugsetprocesskillonexit)     | Sets the action to be performed when the calling thread exits.                      |
| [**FatalExit**](/windows/desktop/api/WinBase/nf-winbase-fatalexit)                                     | Transfers execution control to the debugger.                                        |
| [**FlushInstructionCache**](https://msdn.microsoft.com/en-us/library/ms679350(v=VS.85).aspx)             | Flushes the instruction cache for the specified process.                            |
| [**GetThreadContext**](https://msdn.microsoft.com/en-us/library/ms679362(v=VS.85).aspx)                       | Retrieves the context of the specified thread.                                      |
| [**GetThreadSelectorEntry**](/windows/desktop/api/WinBase/nf-winbase-getthreadselectorentry)           | Retrieves a descriptor table entry for the specified selector and thread.           |
| [**IsDebuggerPresent**](https://msdn.microsoft.com/en-us/library/ms680345(v=VS.85).aspx)                     | Determines whether the calling process is being debugged by a user-mode debugger.   |
| [**OutputDebugString**](https://msdn.microsoft.com/en-us/library/Aa363362(v=VS.85).aspx)                     | Sends a string to the debugger for display.                                         |
| [**ReadProcessMemory**](https://msdn.microsoft.com/en-us/library/ms680553(v=VS.85).aspx)                     | Reads data from an area of memory in a specified process.                           |
| [**SetThreadContext**](https://msdn.microsoft.com/en-us/library/ms680632(v=VS.85).aspx)                       | Sets the context for the specified thread.                                          |
| [**WaitForDebugEvent**](https://msdn.microsoft.com/en-us/library/ms681423(v=VS.85).aspx)                     | Waits for a debugging event to occur in a process being debugged.                   |
| [**Wow64GetThreadContext**](/windows/desktop/api/WinBase/nf-winbase-wow64getthreadcontext)             | Retrieves the context of the specified WOW64 thread.                                |
| [**Wow64GetThreadSelectorEntry**](/windows/desktop/api/WinBase/nf-winbase-wow64getthreadselectorentry) | Retrieves a descriptor table entry for the specified selector and WOW64 thread.     |
| [**Wow64SetThreadContext**](/windows/desktop/api/WinBase/nf-winbase-wow64setthreadcontext)             | Sets the context of the specified WOW64 thread.                                     |
| [**WriteProcessMemory**](https://msdn.microsoft.com/en-us/library/ms681674(v=VS.85).aspx)                   | Writes data to an area of memory in a specified process.                            |



 

 

 



