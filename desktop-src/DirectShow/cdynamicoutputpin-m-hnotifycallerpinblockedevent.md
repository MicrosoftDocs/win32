---
description: Event that is signaled when the pin successfully blocks, or the user cancels a pending block.
ms.assetid: 699bb7f7-e4f7-47c3-bbb1-0bc6556651ae
title: CDynamicOutputPin::m_hNotifyCallerPinBlockedEvent member (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_hNotifyCallerPinBlockedEvent
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDynamicOutputPin::m\_hNotifyCallerPinBlockedEvent member

Event that is signaled when the pin successfully blocks, or the user cancels a pending block.

## Syntax


```C++
HANDLE m_hNotifyCallerPinBlockedEvent;
```



## Remarks

Before accessing this variable, hold the [**CDynamicOutputPin::m\_BlockStateLock**](cdynamicoutputpin-m-blockstatelock.md) critical section.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




