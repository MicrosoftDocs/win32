---
Description: The EndOfStream method notifies the pin that no additional data is expected. This method implements the IPinEndOfStream method. Call this method only on input pins.
ms.assetid: 52a71c30-bd68-4152-8901-71ef2e65913a
title: CBasePin.EndOfStream method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.EndOfStream method

The `EndOfStream` method notifies the pin that no additional data is expected. This method implements the [**IPin::EndOfStream**](/windows/win32/Strmif/nf-strmif-ipin-endofstream?branch=master) method. Call this method only on input pins.

## Syntax


```C++
HRESULT EndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The filter should pass end-of-stream notifications downstream, to the input pins of connected filters. If the filter is a renderer, it should post an [**EC\_COMPLETE**](ec-complete.md) event notification to the filter graph manager. For more information, see [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md).

In the base class, this method does nothing. Derived classes should override this method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




