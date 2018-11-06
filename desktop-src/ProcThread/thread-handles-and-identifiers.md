---
Description: When a new thread is created by the CreateThread or CreateRemoteThread function, a handle to the thread is returned.
ms.assetid: ff91fe27-9773-4185-bc1e-57e897be3821
title: Thread Handles and Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Thread Handles and Identifiers

When a new thread is created by the [**CreateThread**](https://msdn.microsoft.com/en-us/library/ms682453(v=VS.85).aspx) or [**CreateRemoteThread**](https://msdn.microsoft.com/en-us/library/ms682437(v=VS.85).aspx) function, a handle to the thread is returned. By default, this handle has full access rights, and—subject to security access checking—can be used in any of the functions that accept a thread handle. This handle can be inherited by child processes, depending on the inheritance flag specified when it is created. The handle can be duplicated by [**DuplicateHandle**](https://msdn.microsoft.com/en-us/library/ms724251(v=VS.85).aspx), which enables you to create a thread handle with a subset of the access rights. The handle is valid until closed, even after the thread it represents has been terminated.

The [**CreateThread**](https://msdn.microsoft.com/en-us/library/ms682453(v=VS.85).aspx) and [**CreateRemoteThread**](https://msdn.microsoft.com/en-us/library/ms682437(v=VS.85).aspx) functions also return an identifier that uniquely identifies the thread throughout the system. A thread can use the [**GetCurrentThreadId**](https://msdn.microsoft.com/en-us/library/ms683183(v=VS.85).aspx) function to get its own thread identifier. The identifiers are valid from the time the thread is created until the thread has been terminated. Note that no thread identifier will ever be 0.

If you have a thread identifier, you can get the thread handle by calling the [**OpenThread**](https://msdn.microsoft.com/en-us/library/ms684335(v=VS.85).aspx) function. **OpenThread** enables you to specify the handle's access rights and whether it can be inherited.

A thread can use the [**GetCurrentThread**](https://msdn.microsoft.com/en-us/library/ms683182(v=VS.85).aspx) function to retrieve a *pseudo handle* to its own thread object. This pseudo handle is valid only for the calling process; it cannot be inherited or duplicated for use by other processes. To get the real handle to the thread, given a pseudo handle, use the [**DuplicateHandle**](https://msdn.microsoft.com/en-us/library/ms724251(v=VS.85).aspx) function.

To enumerate the threads of a process, use the [**Thread32First**](https://msdn.microsoft.com/library/ms686728(v=VS.85).aspx) and [**Thread32Next**](https://msdn.microsoft.com/library/ms686731(v=VS.85).aspx) functions.

 

 



