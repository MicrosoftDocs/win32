---
description: The EndOfStream method notifies the filter that no additional data is expected from the input pin.
ms.assetid: b8fc3976-e3d4-4f16-82b0-3900ad6a740c
title: CTransformFilter.EndOfStream method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.EndOfStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.EndOfStream method

The `EndOfStream` method notifies the filter that no additional data is expected from the input pin.

## Syntax


```C++
virtual HRESULT EndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

The input pin's [**CTransformInputPin::EndOfStream**](ctransforminputpin-endofstream.md) method calls this method. This method delivers the end-of-stream notification downstream. If the derived class uses a worker thread to deliver media samples, it should override this method and queue the end-of-stream notification.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




