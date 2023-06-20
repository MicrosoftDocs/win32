---
description: The REFERENCE\_TIME data type defines the units for reference times in DirectShow. Each unit of reference time is 100 nanoseconds.
ms.assetid: '862c95bc-2e0a-42c0-b907-45f64f27bd41'
title: REFERENCE_TIME (Strmif.h)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# REFERENCE\_TIME

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




