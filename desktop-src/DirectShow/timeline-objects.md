---
description: Timeline Objects
ms.assetid: 'da426964-d5bd-45ca-a914-c19062f3564b'
title: Timeline Objects
ms.topic: article
ms.date: 05/31/2018
---

# Timeline Objects

\[This API is not supported and may be altered or unavailable in the future.\]

Each type of object in the timeline—source, track, effect, and so forth—is a distinct COM object. However, an application does not create them using the **CoCreateInstance** function. Instead, it calls the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method. This method creates an object of the requested type, initializes it, and returns a pointer to the object. For details, see [Constructing a Timeline](constructing-a-timeline.md).

Every timeline object exposes the [**IAMTimelineObj**](iamtimelineobj.md) interface. In addition, the various object types support their own specialized interfaces:

-   Source: [**IAMTimelineSrc**](iamtimelinesrc.md)
-   Track: [**IAMTimelineTrack**](iamtimelinetrack.md)
-   Composition: [**IAMTimelineComp**](iamtimelinecomp.md)
-   Group: [**IAMTimelineComp**](iamtimelinecomp.md), [**IAMTimelineGroup**](iamtimelinegroup.md)
-   Effect: [**IAMTimelineEffect**](iamtimelineeffect.md)
-   Transition: [**IAMTimelineTrans**](iamtimelinetrans.md)

Note that groups are a type of composition, so they support [**IAMTimelineComp**](iamtimelinecomp.md), as well as their own [**IAMTimelineGroup**](iamtimelinegroup.md) interface.

In addition to the interfaces listed previously, timeline objects expose other, secondary interfaces. These interfaces determine the relationships between the object types.



| Interface                                                  | Meaning                                                                                                       | Exposed By                        |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------|
| [**IAMTimelineVirtualTrack**](iamtimelinevirtualtrack.md) | The object is a virtual track. Virtual tracks can reside inside compositions and hold other timeline objects. | Composition, Track                |
| [**IAMTimelineEffectable**](iamtimelineeffectable.md)     | The object can have effects.                                                                                  | Composition, Track, Source        |
| [**IAMTimelineTransable**](iamtimelinetransable.md)       | The object can have transitions.                                                                              | Composition, Track                |
| [**IAMTimelineSplittable**](iamtimelinesplittable.md)     | The object can be split into two objects.                                                                     | Track, Source, Effect, Transition |



 

## Related topics

<dl> <dt>

[Overview of the Timeline Components](overview-of-the-timeline-components.md)
</dt> </dl>

 

 



