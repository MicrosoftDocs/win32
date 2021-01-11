---
description: Should an expert fail during run time, if you use Network Monitor functions for memory management, Network Monitor will free allocated memory.
ms.assetid: b6f5749b-161e-47a7-82cf-d85ad3703ecd
title: Managing Memory
ms.topic: article
ms.date: 05/31/2018
---

# Managing Memory

Should an expert fail during run time, if you use Network Monitor functions for memory management, Network Monitor will free allocated memory. However, when you write an expert, it might be necessary to acquire system resources and data structure information. For example, the Network Monitor Protocol Coalesce Expert acquires a file handle to build a new capture. Each expert must build its own **try/catch** handling so that the expert can free resources it acquired.

When memory is allocated, use the following existing memory functions:

-   [**ExpertAllocMemory**](expertallocmemory.md)
-   [**ExpertReallocMemory**](expertreallocmemory.md)

 

 



