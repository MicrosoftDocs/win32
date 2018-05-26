---
Description: The DeliverEndFlush method requests the connected input pin to end a flush operation.
ms.assetid: e37bf06a-6cdc-4f14-bf2e-7a7d7004cff6
title: CDynamicOutputPin.DeliverEndFlush method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDynamicOutputPin.DeliverEndFlush method

The `DeliverEndFlush` method requests the connected input pin to end a flush operation.

## Syntax


```C++
HRESULT DeliverEndFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the failure.

## Remarks

This method overrides the [**CBaseOutputPin::DeliverEndFlush**](cbaseoutputpin-deliverendflush.md) method. It resets the [**CDynamicOutputPin::m\_hStopEvent**](cdynamicoutputpin-m-hstopevent.md) event.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




