---
description: The following functions are the entry points for expert DLLs and for calls from the operating system and Network Monitor.
ms.assetid: 1c0dcf6f-7f80-424b-9e6a-5a8b6a5b176f
title: Expert DLL Export Functions
ms.topic: article
ms.date: 05/31/2018
---

# Expert DLL Export Functions

The following functions are the entry points for expert DLLs and for calls from the operating system and Network Monitor.



| Function                                   | Description                                                                                                                                                              |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DllMain Expert**](dllmain-expert.md)   | Indicates that the expert DLL has been loaded or unloaded. When a process loads or unloads the DLL, the operating system calls the [**DllMain**](/windows/desktop/Dlls/dllmain) function. |
| [**Register Expert**](register-expert.md) | Determines basic information about the expert within the DLL. Network Monitor calls the **Register** function.                                                           |
| [**Configure**](configure.md)             | Configures the expert within the DLL. Network Monitor calls the [**Configure**](configure.md) function.                                                                 |
| [**Run**](run.md)                         | Starts the expert within the DLL. Network Monitor calls the [**Run**](run.md) function.                                                                                 |



 

Network Monitor also provides structures, enumerations, and helper functions that the expert can call.



| For information about                                      | See                                                                          |
|------------------------------------------------------------|------------------------------------------------------------------------------|
| Helper functions that can be called by experts and parsers | [Expert and Parser Common Functions](expert-and-parser-common-functions.md) |
| Helper functions that are called only by experts           | [Expert Functions](expert-functions.md)                                     |
| Structures that are used by expert functions               | [Expert Structures](expert-structures.md)                                   |
| Enumerations used by expert structures and functions       | [Expert Enumerations](expert-enumerations.md)                               |



 

 

 
