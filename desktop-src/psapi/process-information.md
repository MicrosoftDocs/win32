---
title: Process Information
description: The system maintains a list of running processes. You can retrieve the identifiers for these processes by calling the EnumProcesses function. This function fills an array of DWORD values with the identifiers of all processes in the system.
ms.assetid: 229c661e-9c33-47a3-9441-558cfe2a800d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Process Information

The system maintains a list of running processes. You can retrieve the identifiers for these processes by calling the [**EnumProcesses**](/windows/win32/Psapi/nf-psapi-enumprocesses?branch=master) function. This function fills an array of **DWORD** values with the identifiers of all processes in the system.

Many functions in PSAPI require a process handle. To obtain a process handle for a running process, pass its process identifier (obtained from [**EnumProcesses**](/windows/win32/Psapi/nf-psapi-enumprocesses?branch=master)) to the [**OpenProcess**](https://msdn.microsoft.com/library/windows/desktop/ms684320) function. Remember to call the [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) function when you are finished with the process handle.

 

 




