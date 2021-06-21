---
description: CRenderedInputPin.Active method - The Active method notifies the pin that the filter is now active. This method overrides the CBasePin::Active method.
ms.assetid: e98ca947-df2f-41a7-9785-b35bd1dde1e6
title: CRenderedInputPin.Active method (Amextra.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRenderedInputPin.Active
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amextra.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRenderedInputPin Class**](crenderedinputpin.md)
</dt> </dl>

 

 




