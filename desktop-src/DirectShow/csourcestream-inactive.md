---
description: The Inactive method notifies the pin that the filter is no longer active. This method overrides the CBasePin::Inactive method. If the streaming thread is active, this method stops it and waits for the thread to exit.
ms.assetid: 82cf0f13-e563-4a0b-b2e1-25ab19f7ed78
title: CSourceStream.Inactive method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.Inactive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.Inactive method

The `Inactive` method notifies the pin that the filter is no longer active. This method overrides the [**CBasePin::Inactive**](cbasepin-inactive.md) method. If the streaming thread is active, this method stops it and waits for the thread to exit.

## Syntax


```C++
HRESULT Inactive();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or another **HRESULT** value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




