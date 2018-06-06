---
Description: To debug a process that is already running, the debugger should use DebugActiveProcess with the process identifier. To retrieve a list of process identifiers, use either the EnumProcesses or Process32First function.
ms.assetid: 2662411f-a69a-442b-a177-a27ea025bb01
title: Debugging a Running Process
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Debugging a Running Process

To debug a process that is already running, the debugger should use [**DebugActiveProcess**](/windows/desktop/api/WinBase/) with the process identifier. To retrieve a list of process identifiers, use either the [**EnumProcesses**](https://www.bing.com/search?q=**EnumProcesses**) or [**Process32First**](https://www.bing.com/search?q=**Process32First**) function.

[**DebugActiveProcess**](/windows/desktop/api/WinBase/) attaches the debugger to the active process. In this case, only the active process can be debugged; its child processes cannot. The debugger must have appropriate access to the executing process to use **DebugActiveProcess**. For more information about access rights, see [Access Control](https://msdn.microsoft.com/d9ce4ec5-5c09-4b33-93a1-39638a925986).

After the debugger has either created or attached itself to the process it intends to debug, the system notifies the debugger of all debugging events that occur in the process, and, if specified, in any child processes. For more information about debugging events, see [Debugging Events](debugging-events.md).

To detach from the process being debugged, the debugger should use the [**DebugActiveProcessStop**](/windows/desktop/api/WinBase/) function.

 

 



