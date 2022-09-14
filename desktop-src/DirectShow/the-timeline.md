---
description: The Timeline
ms.assetid: a3b8bff2-8593-483c-af49-a975ab2dc330
title: The Timeline
ms.topic: article
ms.date: 05/31/2018
---

# The Timeline

\[This API is not supported and may be altered or unavailable in the future.\]

The timeline exposes the [**IAMTimeline**](iamtimeline.md) interface. This interface contains methods for setting properties on the timeline; for adding groups to the timeline; and for creating timeline objects, such as groups, tracks, and sources. To create a new timeline, call the standard **CoCreateInstance** function as follows:


```C++
IAMTimeline *pTL = NULL;
hr = CoCreateInstance(CLSID_AMTimeline, NULL, CLSCTX_INPROC_SERVER, 
        IID_IAMTimeline, (void**)&pTL);
```



The new timeline is empty. At this point you can either load an existing project file (see [Loading and Previewing a Project](loading-and-previewing-a-project.md)), or build up the timeline by creating and inserting new objects (see [Constructing a Timeline](constructing-a-timeline.md)).

## Related topics

<dl> <dt>

[Overview of the Timeline Components](overview-of-the-timeline-components.md)
</dt> </dl>

 

 



