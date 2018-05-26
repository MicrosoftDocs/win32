---
Description: System Reference Clock
ms.assetid: 0247dcb9-64ee-4562-944a-44bcfae80f2d
title: System Reference Clock
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System Reference Clock

The System Reference Clock object implements a reference clock that returns the system time. If none of the filters in the graph provides a reference clock, the filter graph manager uses this component to synchronize the graph. Create this object by calling **CoCreateInstance**.



|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class Identifier | CLSID\_SystemClock                                                                                                                                       |
| Interfaces       | [**IAMClockAdjust**](/windows/win32/Strmif/nn-strmif-iamclockadjust?branch=master), [**IReferenceClock**](/windows/win32/Strmif/nn-strmif-ireferenceclock?branch=master), [**IReferenceClockTimerControl**](/windows/win32/Strmif/nn-strmif-ireferenceclocktimercontrol?branch=master) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Reference Clocks](reference-clocks.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



