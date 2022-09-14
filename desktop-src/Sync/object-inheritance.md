---
description: When you create a process with the CreateProcess function, you can specify that the process inherit handles to mutex, event, semaphore, or timer objects using the SECURITY\_ATTRIBUTES structure.
ms.assetid: 36491a5c-7599-4f69-ab76-d3a62261a151
title: Object Inheritance
ms.topic: article
ms.date: 05/31/2018
---

# Object Inheritance

When you create a process with the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function, you can specify that the process inherit handles to mutex, event, semaphore, or timer objects using the [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure. The handle inherited by the process has the same access to the object as the original handle. The inherited handle appears in the handle table of the created process, but you must communicate the handle value to the created process. You can do this by specifying the value as a command-line argument when you call **CreateProcess**. The created process then uses the [**GetCommandLine**](/windows/win32/api/processenv/nf-processenv-getcommandlinea) function to retrieve the command-line string and convert the handle argument into a usable handle. For more information, see [Inheritance](../procthread/inheritance.md).

 

 
