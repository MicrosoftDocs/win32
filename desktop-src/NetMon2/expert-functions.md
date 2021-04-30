---
description: The following helper functions can only be called by experts that export the Run or Configure function.
ms.assetid: 6890087c-7c94-41ff-bb5c-4bf88a4e07cc
title: Expert Functions
ms.topic: article
ms.date: 05/31/2018
---

# Expert Functions

The following helper functions can only be called by experts that export the [Run](run.md) or [Configure](configure.md) function.



| Function                                         | Description                                                                             |
|--------------------------------------------------|-----------------------------------------------------------------------------------------|
| [ExpertGetFrame](expertgetframe.md)             | Retrieves a given frame from the capture.                                               |
| [ExpertIndicateStatus](expertindicatestatus.md) | Indicates the percentage of completion of the expert's analysis of capture.             |
| [ExpertGetStartupInfo](expertgetstartupinfo.md) | Retrieves the startup information for the expert.                                       |
| [ExpertMemorySize](expertmemorysize.md)         | Retrieves the size of memory allocated by a call to the **ExpertAllocMemory** function. |
| [ExpertSubmitEvent](expertsubmitevent.md)       | Indicates a problem and retrieves information about the problem if one exists.          |
| [ExpertAllocMemory](expertallocmemory.md)       | Allocates memory for the expert.                                                        |
| [ExpertReallocMemory](expertreallocmemory.md)   | Changes the size of the memory allocated by the **ExpertAllocMemory** function.         |
| [ExpertFreeMemory](expertfreememory.md)         | Frees memory allocated by the expert.                                                   |



 

For information about export functions, helper functions that can be called by experts and parsers, structures, and enumerations, see the following topics:



| For information about                                             | See                                                                          |
|-------------------------------------------------------------------|------------------------------------------------------------------------------|
| Functions that are exported by experts                            | [Expert DLL Export Functions](expert-dll-export-functions.md)               |
| Structures that are used by expert functions                      | [Expert Structures](expert-structures.md)                                   |
| Enumerations used by expert structures and functions              | [Expert Enumerations](expert-enumerations.md)                               |
| Common helper functions that can be called by experts and parsers | [Expert and Parser Common Functions](expert-and-parser-common-functions.md) |



 

 

 



