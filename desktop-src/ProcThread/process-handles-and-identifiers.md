---
description: When a new process is created by the CreateProcess function, handles of the new process and its primary thread are returned.
ms.assetid: cf6b80de-de02-4222-a414-e940ffaed8fe
title: Process Handles and Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Process Handles and Identifiers

When a new process is created by the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function, handles of the new process and its primary thread are returned. These handles are created with full access rights, and — subject to security access checking — can be used in any of the functions that accept thread or process handles. These handles can be inherited by child processes, depending on the inheritance flag specified when they are created. The handles are valid until closed, even after the process or thread they represent has been terminated.

The [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function also returns an identifier that uniquely identifies the process throughout the system. A process can use the [**GetCurrentProcessId**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocessid) function to get its own process identifier (also known as the process ID or PID). The identifier is valid from the time the process is created until the process has been terminated. A process can use the [**Process32First**](/windows/win32/api/tlhelp32/nf-tlhelp32-process32first) function to obtain the process identifier of its parent process.

If you have a process identifier, you can get the process handle by calling the [**OpenProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess) function. **OpenProcess** enables you to specify the handle's access rights and whether it can be inherited.

A process can use the [**GetCurrentProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) function to retrieve a pseudo handle to its own process object. This pseudo handle is valid only for the calling process; it cannot be inherited or duplicated for use by other processes. To get the real handle to the process, call the [**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle) function.

 

 
