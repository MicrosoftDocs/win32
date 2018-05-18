---
Description: System Reference Clock
ms.assetid: '0247dcb9-64ee-4562-944a-44bcfae80f2d'
title: System Reference Clock
---

# System Reference Clock

The System Reference Clock object implements a reference clock that returns the system time. If none of the filters in the graph provides a reference clock, the filter graph manager uses this component to synchronize the graph. Create this object by calling **CoCreateInstance**.



|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class Identifier | CLSID\_SystemClock                                                                                                                                       |
| Interfaces       | [**IAMClockAdjust**](iamclockadjust.md), [**IReferenceClock**](ireferenceclock.md), [**IReferenceClockTimerControl**](ireferenceclocktimercontrol.md) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Reference Clocks](reference-clocks.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



