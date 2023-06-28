---
description: CTransformOutputPin.DecideBufferSize method - The DecideBufferSize method sets the buffer requirements.
ms.assetid: cdf9e384-623e-46a6-b123-d881fe21fb09
title: CTransformOutputPin.DecideBufferSize method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformOutputPin.DecideBufferSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformOutputPin.DecideBufferSize method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DecideBufferSize` method sets the buffer requirements.

## Syntax


```C++
HRESULT DecideBufferSize(
   IMemAllocator        *pAlloc,
   ALLOCATOR_PROPERTIES *ppropInputRequest
);
```



## Parameters

<dl> <dt>

*pAlloc* 
</dt> <dd>

Pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

</dd> <dt>

*ppropInputRequest* 
</dt> <dd>

Pointer an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure that contains the input pin's buffer requirements.

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This method overrides the [**CBaseOutputPin::DecideBufferSize**](cbaseoutputpin-decidebuffersize.md) method. It calls the filter's pure virtual [**CTransformFilter::DecideBufferSize**](ctransformfilter-decidebuffersize.md) method, which the filter's derived class must implement.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




