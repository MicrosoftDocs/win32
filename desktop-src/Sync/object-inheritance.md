---
Description: When you create a process with the CreateProcess function, you can specify that the process inherit handles to mutex, event, semaphore, or timer objects using the SECURITY\_ATTRIBUTES structure.
ms.assetid: 36491a5c-7599-4f69-ab76-d3a62261a151
title: Object Inheritance
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Object Inheritance

When you create a process with the [**CreateProcess**](https://msdn.microsoft.com/windows/desktop/3ef0a5b2-4d71-4c17-8188-76a4025287fc) function, you can specify that the process inherit handles to mutex, event, semaphore, or timer objects using the [**SECURITY\_ATTRIBUTES**](https://msdn.microsoft.com/windows/desktop/56b5b350-f4b7-47af-b5f8-6a35f32c1009) structure. The handle inherited by the process has the same access to the object as the original handle. The inherited handle appears in the handle table of the created process, but you must communicate the handle value to the created process. You can do this by specifying the value as a command-line argument when you call **CreateProcess**. The created process then uses the [**GetCommandLine**](https://msdn.microsoft.com/windows/desktop/08dfcab2-eb6e-49a4-80eb-87d4076c98c6) function to retrieve the command-line string and convert the handle argument into a usable handle. For more information, see [Inheritance](https://msdn.microsoft.com/windows/desktop/c530e723-2d40-4022-a259-dfc650604e44).

 

 



