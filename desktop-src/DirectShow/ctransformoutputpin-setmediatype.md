---
description: CTransformOutputPin.SetMediaType method - The SetMediaType method sets the media type for the connection.
ms.assetid: 1d6569c1-e27b-4e96-af5a-64a78b762afd
title: CTransformOutputPin.SetMediaType method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformOutputPin.SetMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformOutputPin.SetMediaType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetMediaType` method sets the media type for the connection.

## Syntax


```C++
HRESULT SetMediaType(
   const CMediaType *mt
);
```



## Parameters

<dl> <dt>

*mt* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object that specifies the media type.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method overrides the [**CBasePin::SetMediaType**](cbasepin-setmediatype.md) method. It calls the filter's [**CTransformFilter::SetMediaType**](ctransformfilter-setmediatype.md) method to inform the filter.

The pin must verify that the media type is acceptable before calling this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




