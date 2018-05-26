---
Description: Seeking capabilities.
ms.assetid: c849db20-7567-41e0-9a57-85070a6e6a3a
title: CSourceSeekingm\_dwSeekingCaps member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSourceSeeking::m\_dwSeekingCaps member

Seeking capabilities.

## Syntax


```C++
DWORD m_dwSeekingCaps;
```



## Remarks

By default, the value is set to the bitwise combination of the following flags:

-   AM\_SEEKING\_CanSeekForwards
-   AM\_SEEKING\_CanSeekBackwards
-   AM\_SEEKING\_CanSeekAbsolute
-   AM\_SEEKING\_CanGetStopPos
-   AM\_SEEKING\_CanGetDuration

If the filter supports a different set of capabilities, override this value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceSeeking Class**](csourceseeking.md)
</dt> </dl>

 

 




