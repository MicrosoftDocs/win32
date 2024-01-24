---
description: The Commit method allocates the memory for the buffers. This method implements the IMemAllocator::Commit method.
ms.assetid: e8c36276-0229-428f-b030-978651ab7534
title: CBaseAllocator.Commit method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseAllocator.Commit
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseAllocator.Commit method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Commit` method allocates the memory for the buffers. This method implements the [**IMemAllocator::Commit**](/windows/desktop/api/Strmif/nf-strmif-imemallocator-commit) method.

## Syntax


```C++
HRESULT Commit();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those in the following list.



| Return code                                                                                       | Description                                        |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | Success.<br/>                                |
| <dl> <dt>**VFW\_E\_SIZENOTSET**</dt> </dl> | Buffer requirements were not specified.<br/> |



 

## Remarks

Before calling this method, call the [**CBaseAllocator::SetProperties**](cbaseallocator-setproperties.md) method to specify the buffer requirements.

This method calls the virtual method [**CBaseAllocator::Alloc**](cbaseallocator-alloc.md) to allocate the memory for the buffers. Derived classes can override **Alloc**. If a decommit operation is pending, it is canceled.

You must call this method before calling the [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




