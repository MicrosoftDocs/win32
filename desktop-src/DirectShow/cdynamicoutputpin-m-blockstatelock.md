---
description: Critical section that protects the blocking state.
ms.assetid: 6d20cf4c-2c27-41e6-8d01-6cb5e3876a38
title: CDynamicOutputPin::m_BlockStateLock member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_BlockStateLock
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin::m\_BlockStateLock member

Critical section that protects the blocking state.

## Syntax


```C++
CCritSec m_BlockStateLock;
```



## Remarks

Hold this critical section before using any of the following member variables:

-   [**CDynamicOutputPin::m\_BlockState**](cdynamicoutputpin-m-blockstate.md)
-   [**CDynamicOutputPin::m\_dwBlockCallerThreadID**](cdynamicoutputpin-m-dwblockcallerthreadid.md)
-   [**CDynamicOutputPin::m\_dwNumOutstandingOutputPinUsers**](cdynamicoutputpin-m-dwnumoutstandingoutputpinusers.md)
-   [**CDynamicOutputPin::m\_hNotifyCallerPinBlockedEvent**](cdynamicoutputpin-m-hnotifycallerpinblockedevent.md)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




