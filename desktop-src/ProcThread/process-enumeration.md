---
Description: All users have read access to the list of processes in the system and there are a number of different functions that enumerate the active processes. The function you should use will depend on factors such as desired platform support.
ms.assetid: 4c73fb10-7ee8-4d8a-9cdb-a2ae59aef5bd
title: Process Enumeration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Process Enumeration

All users have read access to the list of processes in the system and there are a number of different functions that enumerate the active processes. The function you should use will depend on factors such as desired platform support.

The following functions are used to enumerate processes.



| Function                                                    | Description                                                                        |
|-------------------------------------------------------------|------------------------------------------------------------------------------------|
| [**EnumProcesses**](https://www.bing.com/search?q=**EnumProcesses**)                     | Retrieves the process identifier for each process object in the system.            |
| [**Process32First**](https://www.bing.com/search?q=**Process32First**)                   | Retrieves information about the first process encountered in a system snapshot.    |
| [**Process32Next**](https://www.bing.com/search?q=**Process32Next**)                     | Retrieves information about the next process recorded in a system snapshot.        |
| [**WTSEnumerateProcesses**](https://msdn.microsoft.com/windows/desktop/ddfae294-2e7c-416e-b328-76d011b4af39) | Retrieves information about the active processes on the specified terminal server. |



 

The toolhelp functions and [**EnumProcesses**](https://www.bing.com/search?q=**EnumProcesses**) enumerate all process. To list the processes that are running in a specific user account, use [**WTSEnumerateProcesses**](https://msdn.microsoft.com/windows/desktop/ddfae294-2e7c-416e-b328-76d011b4af39) and filter on the user SID. You can filter on the session ID to hide processes running in other terminal server sessions.

You can also filter processes by user account, regardless of the enumeration function, by calling [**OpenProcess**](/windows/desktop/api/WinBase/nf-processthreadsapi-openprocess), [**OpenProcessToken**](https://msdn.microsoft.com/windows/desktop/1e760ad8-7e46-4748-8c45-36ad8efe936a), and [**GetTokenInformation**](https://msdn.microsoft.com/windows/desktop/e94de19c-de12-40fb-a72c-060f7ad12f75) with **TokenUser**. However, you cannot open a process that is protected by a security descriptor unless you have been granted access.

 

 



