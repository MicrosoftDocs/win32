---
Description: All users have read access to the list of processes in the system and there are a number of different functions that enumerate the active processes. The function you should use will depend on factors such as desired platform support.
ms.assetid: 4c73fb10-7ee8-4d8a-9cdb-a2ae59aef5bd
title: Process Enumeration
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Process Enumeration

All users have read access to the list of processes in the system and there are a number of different functions that enumerate the active processes. The function you should use will depend on factors such as desired platform support.

The following functions are used to enumerate processes.



| Function                                                    | Description                                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**EnumProcesses**](base.enumprocesses)                     | Retrieves the process identifier for each process object in the system.            |
| [**Process32First**](base.process32first)                   | Retrieves information about the first process encountered in a system snapshot.    |
| [**Process32Next**](base.process32next)                     | Retrieves information about the next process recorded in a system snapshot.        |
| [**WTSEnumerateProcesses**](termserv.wtsenumerateprocesses) | Retrieves information about the active processes on the specified terminal server. |



 

The toolhelp functions and [**EnumProcesses**](base.enumprocesses) enumerate all process. To list the processes that are running in a specific user account, use [**WTSEnumerateProcesses**](termserv.wtsenumerateprocesses) and filter on the user SID. You can filter on the session ID to hide processes running in other terminal server sessions.

You can also filter processes by user account, regardless of the enumeration function, by calling [**OpenProcess**](/windows/win32/WinBase/nf-processthreadsapi-openprocess?branch=master), [**OpenProcessToken**](security.openprocesstoken), and [**GetTokenInformation**](security.gettokeninformation) with **TokenUser**. However, you cannot open a process that is protected by a security descriptor unless you have been granted access.

 

 



