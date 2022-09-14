---
title: Process Information
description: The system maintains a list of running processes. You can retrieve the identifiers for these processes by calling the EnumProcesses function. This function fills an array of DWORD values with the identifiers of all processes in the system.
ms.assetid: 229c661e-9c33-47a3-9441-558cfe2a800d
ms.topic: article
ms.date: 05/31/2018
---

# Process Information

The system maintains a list of running processes. You can retrieve the identifiers for these processes by calling the [**EnumProcesses**](/windows/desktop/api/Psapi/nf-psapi-enumprocesses) function. This function fills an array of **DWORD** values with the identifiers of all processes in the system.

Many functions in PSAPI require a process handle. To obtain a process handle for a running process, pass its process identifier (obtained from [**EnumProcesses**](/windows/desktop/api/Psapi/nf-psapi-enumprocesses)) to the [**OpenProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-openprocess) function. Remember to call the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function when you are finished with the process handle.

 

 