---
Description: A synchronization object is an object whose handle can be specified in one of the wait functions to coordinate the execution of multiple threads.
ms.assetid: 11558ae9-1056-48bf-96f5-94a051df41c3
title: Synchronization Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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
| Change notification          | Created by the [**FindFirstChangeNotification**](https://www.bing.com/search?q=**FindFirstChangeNotification**) function, its state is set to signaled when a specified type of change occurs within a specified directory or directory tree. For more information, see [Obtaining Directory Change Notifications](https://www.bing.com/search?q=Obtaining Directory Change Notifications).                                                                                                                                   |
| Console input                | Created when a console is created. The handle to console input is returned by the [**CreateFile**](https://www.bing.com/search?q=**CreateFile**) function when CONIN$ is specified, or by the [**GetStdHandle**](https://www.bing.com/search?q=**GetStdHandle**) function. Its state is set to signaled when there is unread input in the console's input buffer, and set to nonsignaled when the input buffer is empty. For more information about consoles, see [Character-Mode Applications](https://www.bing.com/search?q=Character-Mode Applications) |
| Job                          | Created by calling the [**CreateJobObject**](https://msdn.microsoft.com/windows/desktop/ca6a044f-67ed-4a9c-9aeb-69dd77652854) function. The state of a job object is set to signaled when all its processes are terminated because the specified end-of-job time limit has been exceeded. For more information about job objects, see [Job Objects](https://msdn.microsoft.com/windows/desktop/59296384-5e78-44dd-8019-f1df6668928b).                                                                                                                                                             |
| Memory resource notification | Created by the [**CreateMemoryResourceNotification**](https://msdn.microsoft.com/windows/desktop/e4d794ca-4abb-4933-bd07-793e78c52881) function. Its state is set to signaled when a specified type of change occurs within physical memory. For more information about memory, see [Memory Management](https://msdn.microsoft.com/windows/desktop/14cff39d-2692-466b-8f2c-de2eb9384e91).                                                                                                                                                                                  |
| Process                      | Created by calling the [**CreateProcess**](https://msdn.microsoft.com/windows/desktop/3ef0a5b2-4d71-4c17-8188-76a4025287fc) function. Its state is set to nonsignaled while the process is running, and set to signaled when the process terminates. For more information about processes, see [Processes and Threads](https://msdn.microsoft.com/windows/desktop/6bff848c-0c55-41e7-aff1-84c6b21a1b8d).                                                                                                                                                                                  |
| Thread                       | Created when a new thread is created by calling the [**CreateProcess**](https://msdn.microsoft.com/windows/desktop/3ef0a5b2-4d71-4c17-8188-76a4025287fc), [**CreateThread**](https://msdn.microsoft.com/windows/desktop/202a4b42-513a-45de-894a-72e56c706a58), or [**CreateRemoteThread**](https://msdn.microsoft.com/windows/desktop/f5257f78-b20f-4db5-b63e-3bb4e41a4b19) function. Its state is set to nonsignaled while the thread is running, and set to signaled when the thread terminates. For more information about threads, see [Processes and Threads](https://msdn.microsoft.com/windows/desktop/6bff848c-0c55-41e7-aff1-84c6b21a1b8d).                                                            |



 

In some circumstances, you can also use a file, named pipe, or communications device as a synchronization object; however, their use for this purpose is discouraged. Instead, use asynchronous I/O and wait on the event object set in the [**OVERLAPPED**](/windows/desktop/api/WinBase/ns-minwinbase-_overlapped) structure. It is safer to use the event object because of the confusion that can occur when multiple simultaneous overlapped operations are performed on the same file, named pipe, or communications device. In this situation, there is no way to know which operation caused the object's state to be signaled.

For additional information about I/O operations on files, named pipes, or communications, see [Synchronization and Overlapped Input and Output](synchronization-and-overlapped-input-and-output.md).

 

 



