---
Description: The Active method notifies the pin that the filter is now active. This method overrides the CBasePinActive method.
ms.assetid: e98ca947-df2f-41a7-9785-b35bd1dde1e6
title: CRenderedInputPin.Active method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CRenderedInputPin.Active method

The `Active` method notifies the pin that the filter is now active. This method overrides the [**CBasePin::Active**](cbasepin-active.md) method.

## Syntax


```C++
HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an error code otherwise.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amextra.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRenderedInputPin Class**](crenderedinputpin.md)
</dt> </dl>

 

 




