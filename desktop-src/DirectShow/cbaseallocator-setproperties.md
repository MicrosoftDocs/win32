---
description: The SetProperties method specifies the number of buffers to allocate and the size of each buffer. This method implements the IMemAllocator::SetProperties method.
ms.assetid: f53c22a4-c01d-4d2f-81f0-bedf8f2ae5f0
title: CBaseAllocator.SetProperties method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.SetProperties
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseAllocator.SetProperties method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetProperties` method specifies the number of buffers to allocate and the size of each buffer. This method implements the [**IMemAllocator::SetProperties**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-setproperties) method.

## Syntax


```C++
HRESULT SetProperties(
   ALLOCATOR_PROPERTIES *pRequest,
   ALLOCATOR_PROPERTIES *pActual
);
```



## Parameters

<dl> <dt>

*pRequest* 
</dt> <dd>

Pointer to an [**ALLOCATOR\_PROPERTIES**](/windows/win32/api/strmif/ns-strmif-allocator_properties) structure that contains the buffer requirements.

</dd> <dt>

*pActual* 
</dt> <dd>

Pointer to an **ALLOCATOR\_PROPERTIES** structure that receives the actual buffer properties.

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                                 | Description                                                           |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success.<br/>                                                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>                   | **NULL** pointer argument.<br/>                                 |
| <dl> <dt>**VFW\_E\_ALREADY\_COMMITTED**</dt> </dl>   | Cannot change allocated memory while the filter is active.<br/> |
| <dl> <dt>**VFW\_E\_BADALIGN**</dt> </dl>             | An invalid alignment was specified.<br/>                        |
| <dl> <dt>**VFW\_E\_BUFFERS\_OUTSTANDING**</dt> </dl> | One or more buffers are still active.<br/>                      |



 

## Remarks

This method specifies the buffer requirements, but does not allocate any buffers. Call the [**CBaseAllocator::Commit**](cbaseallocator-commit.md) method to allocate buffers.

The caller allocates two ALLOCATOR\_PROPERTIES structures. The *pRequest* parameter contains the caller's buffer requirements, including the number of buffers and the size of each buffer. When the method returns, the *pActual* parameter contains the actual buffer properties, as set by the allocator. In the base class, assuming that the method succeeds, the actual properties always match the requested properties. Derived classes might override this behavior.

The allocator must not be committed, and must not have outstanding buffers. In the base class, the alignment must equal 1. The [**CMemAllocator**](cmemallocator.md) class overrides this requirement.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




