---
Description: The EndOfStream method notifies the pin that no additional data is expected. This method overrides the CBasePinEndOfStream method.
ms.assetid: fb5fd8bb-47be-4df6-b837-2c5ff4347478
title: CRendererInputPin.EndOfStream method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRendererInputPin.EndOfStream method

The `EndOfStream` method notifies the pin that no additional data is expected. This method overrides the [**CBasePin::EndOfStream**](cbasepin-endofstream.md) method.

## Syntax


```C++
HRESULT EndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




