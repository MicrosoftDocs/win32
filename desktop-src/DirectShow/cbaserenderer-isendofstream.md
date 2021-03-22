---
description: The IsEndOfStream method queries whether the end-of-stream notification was received.
ms.assetid: 44f9b740-ff7d-4387-9c2c-a5b6b90f3295
title: CBaseRenderer.IsEndOfStream method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.IsEndOfStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.IsEndOfStream method

The `IsEndOfStream` method queries whether the end-of-stream notification was received.

## Syntax


```C++
BOOL IsEndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseRenderer::m\_bEOS**](cbaserenderer-m-beos.md) flag.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




