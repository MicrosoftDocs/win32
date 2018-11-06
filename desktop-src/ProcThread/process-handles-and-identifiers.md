---
Description: When a new process is created by the CreateProcess function, handles of the new process and its primary thread are returned.
ms.assetid: cf6b80de-de02-4222-a414-e940ffaed8fe
title: Process Handles and Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Process Handles and Identifiers

When a new process is created by the [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function, handles of the new process and its primary thread are returned. These handles are created with full access rights, and — subject to security access checking — can be used in any of the functions that accept thread or process handles. These handles can be inherited by child processes, depending on the inheritance flag specified when they are created. The handles are valid until closed, even after the process or thread they represent has been terminated.

The [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function also returns an identifier that uniquely identifies the process throughout the system. A process can use the [**GetCurrentProcessId**](https://msdn.microsoft.com/en-us/library/ms683180(v=VS.85).aspx) function to get its own process identifier (also known as the process ID or PID). The identifier is valid from the time the process is created until the process has been terminated. A process can use the [**Process32First**](https://msdn.microsoft.com/library/ms684834(v=VS.85).aspx) function to obtain the process identifier of its parent process.

If you have a process identifier, you can get the process handle by calling the [**OpenProcess**](https://msdn.microsoft.com/en-us/library/ms684320(v=VS.85).aspx) function. **OpenProcess** enables you to specify the handle's access rights and whether it can be inherited.

A process can use the [**GetCurrentProcess**](https://msdn.microsoft.com/en-us/library/ms683179(v=VS.85).aspx) function to retrieve a pseudo handle to its own process object. This pseudo handle is valid only for the calling process; it cannot be inherited or duplicated for use by other processes. To get the real handle to the process, call the [**DuplicateHandle**](https://msdn.microsoft.com/en-us/library/ms724251(v=VS.85).aspx) function.

 

 



