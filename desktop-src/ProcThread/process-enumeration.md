---
Description: All users have read access to the list of processes in the system and there are a number of different functions that enumerate the active processes. The function you should use will depend on factors such as desired platform support.
ms.assetid: 4c73fb10-7ee8-4d8a-9cdb-a2ae59aef5bd
title: Process Enumeration
ms.topic: article
ms.date: 05/31/2018
---

# Process Enumeration

All users have read access to the list of processes in the system and there are a number of different functions that enumerate the active processes. The function you should use will depend on factors such as desired platform support.

The following functions are used to enumerate processes.



| Function                                                    | Description                                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**EnumProcesses**](https://msdn.microsoft.com/library/ms682629(v=VS.85).aspx)                     | Retrieves the process identifier for each process object in the system.            |
| [**Process32First**](https://msdn.microsoft.com/library/ms684834(v=VS.85).aspx)                   | Retrieves information about the first process encountered in a system snapshot.    |
| [**Process32Next**](https://msdn.microsoft.com/library/ms684836(v=VS.85).aspx)                     | Retrieves information about the next process recorded in a system snapshot.        |
| [**WTSEnumerateProcesses**](https://msdn.microsoft.com/library/Aa383831(v=VS.85).aspx) | Retrieves information about the active processes on the specified terminal server. |



 

The toolhelp functions and [**EnumProcesses**](https://msdn.microsoft.com/library/ms682629(v=VS.85).aspx) enumerate all process. To list the processes that are running in a specific user account, use [**WTSEnumerateProcesses**](https://msdn.microsoft.com/library/Aa383831(v=VS.85).aspx) and filter on the user SID. You can filter on the session ID to hide processes running in other terminal server sessions.

You can also filter processes by user account, regardless of the enumeration function, by calling [**OpenProcess**](https://msdn.microsoft.com/library/ms684320(v=VS.85).aspx), [**OpenProcessToken**](https://msdn.microsoft.com/library/Aa379295(v=VS.85).aspx), and [**GetTokenInformation**](https://msdn.microsoft.com/library/Aa446671(v=VS.85).aspx) with **TokenUser**. However, you cannot open a process that is protected by a security descriptor unless you have been granted access.

 

 



