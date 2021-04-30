---
description: CMSPCallMultiGraph Members
ms.assetid: 49451585-3084-4426-8617-79b60eb77518
title: CMSPCallMultiGraph Members
ms.topic: article
ms.date: 05/31/2018
---

# CMSPCallMultiGraph Members

``` syntax
CMSPArray <THREADPOOLWAITBLOCK>     m_ThreadPoolWaitBlocks;
```

The wait blocks store the information about the wait registered to the thread pool. It includes the wait handles returned by the [**RegisterWaitForSingleObject**](/windows/desktop/api/winbase/nf-winbase-registerwaitforsingleobject) call and a pointer to the context structure. Each block in the array is for a graph in one of the stream objects. The offset of a block in this array is the same as the offset of the stream that owns the graph.

 

 
