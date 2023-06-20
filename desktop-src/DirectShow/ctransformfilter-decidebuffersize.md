---
description: CTransformFilter.DecideBufferSize method - The DecideBufferSize method sets the output pin's buffer requirements.
ms.assetid: 33e41668-b4f6-4142-b22e-2ddfb96332df
title: CTransformFilter.DecideBufferSize method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.DecideBufferSize
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformFilter.DecideBufferSize method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DecideBufferSize` method sets the output pin's buffer requirements.

## Syntax


```C++
virtual HRESULT DecideBufferSize(
   IMemAllocator        *pAlloc,
   ALLOCATOR_PROPERTIES *ppropInputRequest
) = 0;
```



## Parameters

<dl> <dt>

*pAlloc* 
</dt> <dd>

Pointer to the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface on the output pin's allocator.

</dd> <dt>

*ppropInputRequest* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure that contains buffer requirements from the downstream input pin.

</dd> </dl>

## Return value

Returns S\_OK or another **HRESULT** value.

## Remarks

The output pin's [**CTransformOutputPin::DecideBufferSize**](ctransformoutputpin-decidebuffersize.md) method calls this method. The derived class must implement this method. For more information, see [**CBaseOutputPin::DecideBufferSize**](cbaseoutputpin-decidebuffersize.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




