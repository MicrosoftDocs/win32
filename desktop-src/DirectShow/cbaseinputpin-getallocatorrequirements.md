---
description: The GetAllocatorRequirements method retrieves the allocator properties requested by the input pin.
ms.assetid: 81564924-6d5b-4b2a-b549-e3f358f18371
title: CBaseInputPin.GetAllocatorRequirements method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.GetAllocatorRequirements
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseInputPin.GetAllocatorRequirements method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetAllocatorRequirements` method retrieves the allocator properties requested by the input pin.

## Syntax


```C++
HRESULT GetAllocatorRequirements(
   ALLOCATOR_PROPERTIES *pProps
);
```



## Parameters

<dl> <dt>

*pProps* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure, which is filled in with the requirements.

</dd> </dl>

## Return value

Returns E\_NOTIMPL.

## Remarks

When an output pin initializes a memory allocator, it can call this method to determine whether the input pin has any buffer requirements. For more information, see [**CBaseOutputPin::DecideAllocator**](cbaseoutputpin-decideallocator.md).

Implementing this method is optional. If the filter has specific alignment or prefix requirements, override this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




