---
description: CTransInPlaceOutputPin.PeekAllocator method - The PeekAllocator method returns a pointer to the pin's allocator. The method does not increment the reference count on the interface.
ms.assetid: 3653d472-059c-426c-8e81-4f7cbd1a8ec3
title: CTransInPlaceOutputPin.PeekAllocator method (Transip.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceOutputPin.PeekAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransInPlaceOutputPin.PeekAllocator method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `PeekAllocator` method returns a pointer to the pin's allocator. The method does not increment the reference count on the interface.

## Syntax


```C++
IMemAllocator* PeekAllocator();
```



## Parameters

This method has no parameters.

## Return value

Returns the [**CBaseOutputPin::m\_pAllocator**](cbaseoutputpin-m-pallocator.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceOutputPin Class**](ctransinplaceoutputpin.md)
</dt> </dl>

 

 




