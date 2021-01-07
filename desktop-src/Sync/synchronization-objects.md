---
description: A synchronization object is an object whose handle can be specified in one of the wait functions to coordinate the execution of multiple threads.
ms.assetid: 11558ae9-1056-48bf-96f5-94a051df41c3
title: Synchronization Objects
ms.topic: article
ms.date: 05/31/2018
---

# Synchronization Objects

A *synchronization object* is an object whose handle can be specified in one of the [wait functions](wait-functions.md) to coordinate the execution of multiple threads. More than one process can have a handle to the same synchronization object, making interprocess synchronization possible.

The following object types are provided exclusively for synchronization.



| Type           | Description                                                                                                                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event          | Notifies one or more waiting threads that an event has occurred. For more information, see [Event Objects](event-objects.md).                                                                                   |
| Mutex          | Can be owned by only one thread at a time, enabling threads to coordinate mutually exclusive access to a shared resource. For more information, see [Mutex Objects](mutex-objects.md).                          |
| Semaphore      | Maintains a count between zero and some maximum value, limiting the number of threads that are simultaneously accessing a shared resource. For more information, see [Semaphore Objects](semaphore-objects.md). |
| Waitable timer | Notifies one or more waiting threads that a specified time has arrived. For more information, see [Waitable Timer Objects](waitable-timer-objects.md).                                                          |



 

Though available for other uses, the following objects can also be used for synchronization.



| Object                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change notification          | Created by the [**FindFirstChangeNotification**](/windows/win32/api/fileapi/nf-fileapi-findfirstchangenotificationa) function, its state is set to signaled when a specified type of change occurs within a specified directory or directory tree. For more information, see [Obtaining Directory Change Notifications](../fileio/obtaining-directory-change-notifications.md).                                                                                                                                   |
| Console input                | Created when a console is created. The handle to console input is returned by the [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) function when CONIN$ is specified, or by the [**GetStdHandle**](/windows/console/getstdhandle) function. Its state is set to signaled when there is unread input in the console's input buffer, and set to nonsignaled when the input buffer is empty. For more information about consoles, see [Character-Mode Applications](/windows/console/character-mode-applications) |
| Job                          | Created by calling the [**CreateJobObject**](/windows/win32/api/jobapi2/nf-jobapi2-createjobobjectw) function. The state of a job object is set to signaled when all its processes are terminated because the specified end-of-job time limit has been exceeded. For more information about job objects, see [Job Objects](../procthread/job-objects.md).                                                                                                                                                             |
| Memory resource notification | Created by the [**CreateMemoryResourceNotification**](/windows/win32/api/memoryapi/nf-memoryapi-creatememoryresourcenotification) function. Its state is set to signaled when a specified type of change occurs within physical memory. For more information about memory, see [Memory Management](../memory/memory-management.md).                                                                                                                                                                                  |
| Process                      | Created by calling the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function. Its state is set to nonsignaled while the process is running, and set to signaled when the process terminates. For more information about processes, see [Processes and Threads](../procthread/processes-and-threads.md).                                                                                                                                                                                  |
| Thread                       | Created when a new thread is created by calling the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa), [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread), or [**CreateRemoteThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread) function. Its state is set to nonsignaled while the thread is running, and set to signaled when the thread terminates. For more information about threads, see [Processes and Threads](../procthread/processes-and-threads.md).                                                            |



 

In some circumstances, you can also use a file, named pipe, or communications device as a synchronization object; however, their use for this purpose is discouraged. Instead, use asynchronous I/O and wait on the event object set in the [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure. It is safer to use the event object because of the confusion that can occur when multiple simultaneous overlapped operations are performed on the same file, named pipe, or communications device. In this situation, there is no way to know which operation caused the object's state to be signaled.

For additional information about I/O operations on files, named pipes, or communications, see [Synchronization and Overlapped Input and Output](synchronization-and-overlapped-input-and-output.md).

 

 
