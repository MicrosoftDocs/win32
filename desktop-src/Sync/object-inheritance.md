---
Description: When you create a process with the CreateProcess function, you can specify that the process inherit handles to mutex, event, semaphore, or timer objects using the SECURITY\_ATTRIBUTES structure.
ms.assetid: 36491a5c-7599-4f69-ab76-d3a62261a151
title: Object Inheritance
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Object Inheritance

When you create a process with the [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function, you can specify that the process inherit handles to mutex, event, semaphore, or timer objects using the [**SECURITY\_ATTRIBUTES**](https://msdn.microsoft.com/en-us/library/Aa379560(v=VS.85).aspx) structure. The handle inherited by the process has the same access to the object as the original handle. The inherited handle appears in the handle table of the created process, but you must communicate the handle value to the created process. You can do this by specifying the value as a command-line argument when you call **CreateProcess**. The created process then uses the [**GetCommandLine**](https://msdn.microsoft.com/en-us/library/ms683156(v=VS.85).aspx) function to retrieve the command-line string and convert the handle argument into a usable handle. For more information, see [Inheritance](https://msdn.microsoft.com/en-us/library/ms683463(v=VS.85).aspx).

 

 



