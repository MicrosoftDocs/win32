---
description: The Allocator method retrieves a pointer to the memory allocator.
ms.assetid: ac262502-eadc-482c-bc58-1e942889f0a7
title: CRendererInputPin.Allocator method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererInputPin.Allocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRendererInputPin.Allocator method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Allocator` method retrieves a pointer to the memory allocator.

## Syntax


```C++
IMemAllocator* Allocator() const;
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the allocator's [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface, or **NULL**.

## Remarks

This method returns the [**CBaseInputPin::m\_pAllocator**](cbaseinputpin-m-pallocator.md) member variable. The method does not increment the reference count on the interface. This method is strictly an accessor method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRendererInputPin Class**](crendererinputpin.md)
</dt> </dl>

 

 




