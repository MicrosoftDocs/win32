---
description: The OnThreadStartPlay method is called at the start of the CSourceStream::DoBufferProcessingLoop method.
ms.assetid: 16d3b28f-bfae-49af-b8e4-8cc8cb15ecab
title: CSourceStream.OnThreadStartPlay method (Source.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.OnThreadStartPlay
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSourceStream.OnThreadStartPlay method

The `OnThreadStartPlay` method is called at the start of the [**CSourceStream::DoBufferProcessingLoop**](csourcestream-dobufferprocessingloop.md) method.

## Syntax


```C++
virtual HRESULT OnThreadStartPlay();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method does nothing in the base class; it is available for the derived class to override.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




