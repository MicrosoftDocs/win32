---
description: The SetMediaType method sets the media type for the connection. This method overrides the CBasePin::SetMediaType method.
ms.assetid: b2668bb1-0739-413c-bea8-ec5541acfb3e
title: CRendererInputPin.SetMediaType method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererInputPin.SetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererInputPin.SetMediaType method

The `SetMediaType` method sets the media type for the connection. This method overrides the [**CBasePin::SetMediaType**](cbasepin-setmediatype.md) method.

## Syntax


```C++
HRESULT SetMediaType(
   const CMediaType *pmt
);
```



## Parameters

<dl> <dt>

*pmt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the media type.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




