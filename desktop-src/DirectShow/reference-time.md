---
Description: The REFERENCE\_TIME data type defines the units for reference times in DirectShow. Each unit of reference time is 100 nanoseconds.
ms.assetid: ac77ca0d-f3d1-4258-bf2e-d7e8a33eb68e
title: REFERENCE\_TIME
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# REFERENCE\_TIME

The **REFERENCE\_TIME** data type defines the units for reference times in DirectShow. Each unit of reference time is 100 nanoseconds.


```C++
typedef LONGLONG REFERENCE_TIME;
```



## Remarks

The **REFERENCE\_TIME** data type is a 64-bit integer.

Reference times are usually measured from one of the following baselines:

-   An absolute clock time. In this case, the baseline will depend on the implementation of the clock. For more information, see [Reference Clocks](reference-clocks.md).
-   Relative to the start of playback.

For more information about reference times, see [Time and Clocks in DirectShow](time-and-clocks-in-directshow.md).

## Requirements



|                   |                                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Strmif.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Data Types](directshow-data-types.md)
</dt> </dl>

 

 




