---
Description: Number of streaming threads using this pin.
ms.assetid: f8650a17-edab-4d69-91da-78107c3c60b9
title: CDynamicOutputPinm\_dwNumOutstandingOutputPinUsers member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDynamicOutputPin::m\_dwNumOutstandingOutputPinUsers member

Number of streaming threads using this pin.

## Syntax


```C++
DWORD m_dwNumOutstandingOutputPinUsers;
```



## Remarks

The [**CDynamicOutputPin::StartUsingOutputPin**](cdynamicoutputpin-startusingoutputpin.md) method increments this variable, and the [**CDynamicOutputPin::StopUsingOutputPin**](cdynamicoutputpin-stopusingoutputpin.md) method decrements it. When the value is greater than zero, some thread is using this pin to stream data or to change the connection type. The pin cannot be blocked while this is the case.

Before accessing this variable, hold the [**CDynamicOutputPin::m\_BlockStateLock**](cdynamicoutputpin-m-blockstatelock.md) critical section.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> <dt>

[**CDynamicOutputPin::StreamingThreadUsingOutputPin**](cdynamicoutputpin-streamingthreadusingoutputpin.md)
</dt> </dl>

 

 




