---
description: The BeginFlush method begins a flush operation.
ms.assetid: dc652394-c24e-4cea-ac28-30a1e6de205f
title: CBaseRenderer.BeginFlush method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.BeginFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.BeginFlush method

The `BeginFlush` method begins a flush operation.

## Syntax


```C++
virtual HRESULT BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The filter's input pin calls this method when it receives a call to the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method. The filter releases the streaming thread, and releases any sample that it was holding for rendering.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




