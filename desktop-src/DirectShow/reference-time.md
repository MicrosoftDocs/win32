---
description: The REFERENCE\_TIME data type defines the units for reference times in DirectShow. Each unit of reference time is 100 nanoseconds.
ms.assetid: '862c95bc-2e0a-42c0-b907-45f64f27bd41'
title: REFERENCE_TIME (Strmif.h)
ms.topic: article
ms.date: 05/31/2018
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



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Strmif.h (include Dshow.h)</dt> </dl> |



## See also

<dl> <dt>

[DirectShow Data Types](directshow-data-types.md)
</dt> </dl>

 

 




