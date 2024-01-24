---
description: A child process can inherit handles from its parent process. An inherited handle is valid only in the context of the child process. To enable a child process to inherit open handles from its parent process, use the following steps.
ms.assetid: 957cd369-bebf-4e04-9f7e-a936e2e97887
title: Handle Inheritance
ms.topic: article
ms.date: 05/31/2018
---

# Handle Inheritance

A child process can inherit handles from its parent process. An inherited handle is valid only in the context of the child process. To enable a child process to inherit open handles from its parent process, use the following steps.

1.  Create the handle with the **bInheritHandle** member of the [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure set to **TRUE**.
2.  Create the child process using the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) function, with the *bInheritHandles* parameter set to **TRUE**.

The [**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle) function duplicates a handle to be used in the current process or in another process. If an application duplicates one of its handles for another process, the duplicated handle is valid only in the context of the other process.

A duplicated or inherited handle is a unique value, but it refers to the same object as the original handle. Processes can inherit or duplicate handles to the following types of objects:

-   Access Token
-   Communications device
-   Console input
-   Console screen buffer
-   Desktop
-   Directory
-   Event
-   File
-   File mapping
-   Job
-   Mailslot
-   Mutex
-   Pipe
-   Process
-   Registry key
-   Semaphore
-   Socket
-   Thread
-   Timer
-   Window station

All other objects are private to the process that created them; their object handles cannot be duplicated or inherited.

For more information, see [Inheritance](/windows/desktop/ProcThread/inheritance).

 

 
