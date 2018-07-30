---
Description: Kernel object handles are process specific.
ms.assetid: 3e3288dd-155a-41d0-9d43-5f49ed4c4a9d
title: Kernel Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Kernel Objects

Kernel object handles are process specific. That is, a process must either create the object or open an existing object to obtain a kernel object handle. The per-process limit on kernel handles is 2^24. However, handles are stored in the paged pool, so the actual number of handles you can create is based on available memory. The number of handles that you can create on 32-bit Windows is significantly lower than 2^24.

Any process can create a new handle to an existing kernel object (even one created by another process), provided that the process knows the name of the object and has security access to the object. Kernel object handles include access rights that indicate the actions that can be granted or denied to a process. An application specifies access rights when it creates an object or obtains an existing object handle. Each type of kernel object supports its own set of access rights. For example, event handles can have set or wait access (or both), file handles can have read or write access (or both), and so on. For more information, see [Securable Objects](https://msdn.microsoft.com/library/windows/desktop/aa379557).

In the following illustration, an application creates an event object. The [**CreateEvent**](https://msdn.microsoft.com/library/windows/desktop/ms682396) function creates the event object and returns an object handle.

![application creating an event object](images/cshob-03.png)

After the event object has been created, the application can use the event handle to set or wait on the event. The handle remains valid until the application closes the handle or terminates.

Most kernel objects support multiple handles to a single object. For example, the application in the preceding illustration could obtain additional event object handles by using the [**OpenEvent**](https://msdn.microsoft.com/library/windows/desktop/ms684305) function, as shown in the following illustration.

![application creating an event object with multiple handles](images/cshob-04.png)

This method enables an application to have handles with different access rights. For example, Handle 1 might have set and wait access to the event, and Handle 2 might have only wait access.

If another process knows the event name and has security access to the object, it can create its own event object handle by using [**OpenEvent**](https://msdn.microsoft.com/library/windows/desktop/ms684305). The creating application could also duplicate one of its handles into the same process or into another process by using the [**DuplicateHandle**](https://msdn.microsoft.com/en-us/library/ms724251(v=VS.85).aspx) function.

An object remains in memory as long as at least one object handle exists. In the following illustration, the applications use the [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx) function to close their event object handles. When there are no event handles, the system removes the object from memory, as shown in the following illustration.

![application closing event object handles to remove object from memory](images/cshob-08.png)

The system manages file objects somewhat differently from other kernel objects. File objects contain the file pointer — the pointer to the next byte to be read or written in a file. Whenever an application creates a new file handle, the system creates a new file object. Therefore, more than one file object can refer to a single file on disk, as shown in the next illustration.

![multiple file objects referring to a file on disk](images/cshob-09.png)

Only through duplication or inheritance can more than one file handle refer to the same file object, as shown in the following illustration.

![two file handles refer to same file object](images/cshob-10.png)

The following table lists each of the kernel objects, along with each object's creator and destroyer functions. The creator functions either create the object and an object handle or create a new existing object handle. The destroyer functions close the object handle. When an application closes the last handle to a kernel object, the system removes the object from memory.



| Kernel object                | Creator function                                                                                                                                                                                                                                                  | Destroyer function                                                                      |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Access token                 | [**CreateRestrictedToken**](https://msdn.microsoft.com/library/windows/desktop/aa446583), [**DuplicateToken**](https://msdn.microsoft.com/library/windows/desktop/aa446616), [**DuplicateTokenEx**](https://msdn.microsoft.com/library/windows/desktop/aa446617), [**OpenProcessToken**](https://msdn.microsoft.com/library/windows/desktop/aa379295), [**OpenThreadToken**](https://msdn.microsoft.com/library/windows/desktop/aa379296) | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Change notification          | [**FindFirstChangeNotification**](https://msdn.microsoft.com/library/windows/desktop/aa364417)                                                                                                                                                                                                 | [**FindCloseChangeNotification**](https://msdn.microsoft.com/library/windows/desktop/aa364414)                       |
| Communications device        | [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858)                                                                                                                                                                                                                                   | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Console input                | [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), with CONIN$                                                                                                                                                                                                                      | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Console screen buffer        | [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), with CONOUT$                                                                                                                                                                                                                     | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Desktop                      | [**GetThreadDesktop**](https://msdn.microsoft.com/library/windows/desktop/ms683232)                                                                                                                                                                                                                     | Applications cannot delete this object.                                                 |
| Event                        | [**CreateEvent**](https://msdn.microsoft.com/library/windows/desktop/ms682396), [**CreateEventEx**](https://msdn.microsoft.com/library/windows/desktop/ms682400), [**OpenEvent**](https://msdn.microsoft.com/library/windows/desktop/ms684305)                                                                                                                                                     | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Event log                    | [**OpenEventLog**](https://msdn.microsoft.com/library/windows/desktop/aa363672), [**RegisterEventSource**](https://msdn.microsoft.com/library/windows/desktop/aa363678), [**OpenBackupEventLog**](https://msdn.microsoft.com/library/windows/desktop/aa363671)                                                                                                                     | [**CloseEventLog**](https://msdn.microsoft.com/library/windows/desktop/aa363639)                                                 |
| File                         | [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858)                                                                                                                                                                                                                                 | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx), [**DeleteFile**](https://msdn.microsoft.com/library/windows/desktop/aa363915)                     |
| File mapping                 | [**CreateFileMapping**](https://msdn.microsoft.com/library/windows/desktop/aa366537), [**OpenFileMapping**](https://msdn.microsoft.com/library/windows/desktop/aa366791)                                                                                                                                                                          | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Find file                    | [**FindFirstFile**](https://msdn.microsoft.com/library/windows/desktop/aa364418)                                                                                                                                                                                                                             | [**FindClose**](https://msdn.microsoft.com/library/windows/desktop/aa364413)                                                           |
| Heap                         | [**HeapCreate**](https://msdn.microsoft.com/library/windows/desktop/aa366599)                                                                                                                                                                                                                                 | [**HeapDestroy**](https://msdn.microsoft.com/library/windows/desktop/aa366700)                                                     |
| I/O completion port          | [**CreateIoCompletionPort**](https://msdn.microsoft.com/library/windows/desktop/aa363862)                                                                                                                                                                                                           | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Job                          | [**CreateJobObject**](https://msdn.microsoft.com/library/windows/desktop/ms682409)                                                                                                                                                                                                                       | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Mailslot                     | [**CreateMailslot**](https://msdn.microsoft.com/library/windows/desktop/aa365147)                                                                                                                                                                                                                         | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Memory resource notification | [**CreateMemoryResourceNotification**](https://msdn.microsoft.com/library/windows/desktop/aa366541)                                                                                                                                                                                     | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Module                       | [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175), [**GetModuleHandle**](https://msdn.microsoft.com/library/windows/desktop/ms683199)                                                                                                                                                                                  | [**FreeLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms683152)                                                     |
| Mutex                        | [**CreateMutex**](https://msdn.microsoft.com/library/windows/desktop/ms682411), [**CreateMutexEx**](https://msdn.microsoft.com/library/windows/desktop/ms682418), [**OpenMutex**](https://msdn.microsoft.com/library/windows/desktop/ms684315)                                                                                                                                                     | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Pipe                         | [**CreateNamedPipe**](https://msdn.microsoft.com/library/windows/desktop/aa365150), [**CreatePipe**](https://msdn.microsoft.com/library/windows/desktop/aa365152)                                                                                                                                                                                    | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx), [**DisconnectNamedPipe**](https://msdn.microsoft.com/library/windows/desktop/aa365166) |
| Process                      | [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425), [**OpenProcess**](https://msdn.microsoft.com/library/windows/desktop/ms684320), [**GetCurrentProcess**](https://msdn.microsoft.com/library/windows/desktop/ms683179)                                                                                                                                     | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx), [**TerminateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms686714)       |
| Semaphore                    | [**CreateSemaphore**](https://msdn.microsoft.com/library/windows/desktop/ms682438), [**CreateSemaphoreEx**](https://msdn.microsoft.com/library/windows/desktop/ms682446), [**OpenSemaphore**](https://msdn.microsoft.com/library/windows/desktop/ms684326)                                                                                                                             | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Socket                       | [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506), [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526)                                                                                                                                                                                                    | [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582)                                                |
| Thread                       | [**CreateThread**](https://msdn.microsoft.com/library/windows/desktop/ms682453), [**CreateRemoteThread**](https://msdn.microsoft.com/library/windows/desktop/ms682437), [**GetCurrentThread**](https://msdn.microsoft.com/library/windows/desktop/ms683182)                                                                                                                           | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx), [**TerminateThread**](https://msdn.microsoft.com/library/windows/desktop/ms686717)         |
| Timer                        | [**CreateWaitableTimer**](https://msdn.microsoft.com/library/windows/desktop/ms682492), [**CreateWaitableTimerEx**](https://msdn.microsoft.com/library/windows/desktop/ms682494), [**OpenWaitableTimer**](https://msdn.microsoft.com/library/windows/desktop/ms684337)                                                                                                     | [**CloseHandle**](https://msdn.microsoft.com/en-us/library/ms724211(v=VS.85).aspx)                                                      |
| Update resource              | [**BeginUpdateResource**](https://msdn.microsoft.com/library/ms648030(v=VS.85).aspx)                                                                                                                                                                                                         | [**EndUpdateResource**](https://msdn.microsoft.com/library/ms648032(v=VS.85).aspx)                                   |
| Window station               | [**GetProcessWindowStation**](https://msdn.microsoft.com/library/windows/desktop/ms683225)                                                                                                                                                                                                       | Applications cannot delete this object.                                                 |



 

## Related topics

<dl> <dt>

[Kernel Object Namespaces](https://msdn.microsoft.com/library/aa382954)
</dt> </dl>

 

 



