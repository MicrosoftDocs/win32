---
description: The GetBuffer method retrieves a media sample that contains a buffer. This method implements the IMemAllocator::GetBuffer method.
ms.assetid: 81694b9c-b325-47c8-94e4-f54d1329a684
title: CBaseAllocator.GetBuffer method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.GetBuffer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseAllocator.GetBuffer method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetBuffer` method retrieves a media sample that contains a buffer. This method implements the [**IMemAllocator::GetBuffer**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-getbuffer) method.

## Syntax


```C++
HRESULT GetBuffer(
   IMediaSample   **ppBuffer,
   REFERENCE_TIME *pStartTime,
   REFERENCE_TIME *pEndTime,
   DWORD          dwFlags
);
```



## Parameters

<dl> <dt>

*ppBuffer* 
</dt> <dd>

Receives a pointer to the buffer's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface. The caller must release the interface.

</dd> <dt>

*pStartTime* 
</dt> <dd>

Pointer to the start time of the sample.

</dd> <dt>

*pEndTime* 
</dt> <dd>

Pointer to the end time of the sample.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Bitwise combination of zero or more flags. The base class supports the following flag.



| Value                                                                                                                                                          | Meaning                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <span id="AM_GBF_NOWAIT"></span><span id="am_gbf_nowait"></span><dl> <dt>**AM\_GBF\_NOWAIT**</dt> </dl> | Do not wait for a buffer to become available. <br/> |



 

</dd> </dl>

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                           | Description                             |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                     |
| <dl> <dt>**VFW\_E\_NOT\_COMMITTED**</dt> </dl> | Allocator was not committed.<br/> |
| <dl> <dt>**VFW\_E\_TIMEOUT**</dt> </dl>        | Timed out.<br/>                   |



 

## Remarks

Unless the caller specifies the **AM\_GBF\_NOWAIT** flag in *dwFlags*, this method blocks until the next sample is available.

The retrieved media sample has a valid pointer to the allocated buffer. The caller is responsible for setting any other properties on the sample, such as the time stamps, the media times, or the sync-point property. For more information, see [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample).

In the base class, the *pStartTime* and *pEndTime* parameters are ignored. Derived classes can use these values. For example, the allocator for the [Video Renderer](video-renderer-filter.md) filter uses these values to synchronize switching between DirectDraw surfaces.

If the method needs to wait on a sample, it increments the count of waiting objects ([**CBaseAllocator::m\_lCount**](cbaseallocator-m-lcount.md)) and the calls [**WaitForSingleObject**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobject) function on the semaphore ([**CBaseAllocator::m\_hSem**](cbaseallocator-m-hsem.md)). When a sample becomes available, it calls the [**CBaseAllocator::ReleaseBuffer**](cbaseallocator-releasebuffer.md) method on the allocator, which increases the semaphore count by **m\_lCount** (thereby releasing the waiting threads) and sets **m\_lCount** back to zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

