---
title: Heap Extents
description: Heap Extents
ms.assetid: '4ddf2be0-61a5-44ff-b73e-cdc7cf37e626'
---

# Heap Extents

The Heap Extents graph presents the system view of the heap usage in terms of committed memory pages and represents the true cost of the heap allocations of the process. The committed memory pages include all of the data structures used to maintain the heap, the 8 bytes of control data preceding every heap allocation, and free space within the heap itself, as shown in the following screen shot.

![screen shot of a graph showing heap extents](images/he-img27.png)

The following view also gives an indication of how transient spikes in outstanding heap size or large transient allocations impact memory usage long after they are released. Note how the outstanding heap usage decreases several times in but the heap does not contract until much later in the trace.

![heap extent vs. heap allocations](images/he-img28.png)

 

 




