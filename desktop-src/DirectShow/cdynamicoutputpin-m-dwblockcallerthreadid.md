---
Description: The identifier of the thread that last called the IPinFlowControlBlock method on this pin. This member variable is only valid while the pin is blocked.
ms.assetid: 7f8429c5-7e58-49a1-9f36-01088379a193
title: CDynamicOutputPinm\_dwBlockCallerThreadID member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDynamicOutputPin::m\_dwBlockCallerThreadID member

The identifier of the thread that last called the [**IPinFlowControl::Block**](/windows/win32/Strmif/nf-strmif-ipinflowcontrol-block?branch=master) method on this pin. This member variable is only valid while the pin is blocked.

## Syntax


```C++
DWORD m_dwBlockCallerThreadID;
```



## Remarks

Before accessing this variable, hold the [**CDynamicOutputPin::m\_BlockStateLock**](cdynamicoutputpin-m-blockstatelock.md) critical section.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




