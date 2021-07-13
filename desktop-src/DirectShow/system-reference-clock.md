---
description: System Reference Clock
ms.assetid: 0247dcb9-64ee-4562-944a-44bcfae80f2d
title: System Reference Clock
ms.topic: article
ms.date: 05/31/2018
---

# System Reference Clock

The System Reference Clock object implements a reference clock that returns the system time. If none of the filters in the graph provides a reference clock, the filter graph manager uses this component to synchronize the graph. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class Identifier | CLSID\_SystemClock                                                                                                                                       |
| Interfaces       | [**IAMClockAdjust**](/windows/desktop/api/Strmif/nn-strmif-iamclockadjust), [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock), [**IReferenceClockTimerControl**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclocktimercontrol) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Reference Clocks](reference-clocks.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



