---
description: Implements an allocator that supports the IMemAllocator interface.
ms.assetid: c40eccef-d915-4bf3-81b2-b20e000718fb
title: CMemAllocator class (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMemAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMemAllocator class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![cmemallocator class hierarchy](images/filter10.png)

Implements an allocator that supports the [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) interface.

This class derives from [**CBaseAllocator**](cbaseallocator.md). For more information about allocators, refer to the documentation for [**CBaseAllocator**](cbaseallocator.md).



| Protected Member Variables                              | Description                                                              |
|---------------------------------------------------------|--------------------------------------------------------------------------|
| [**m\_pBuffer**](cmemallocator-m-pbuffer.md)           | Pointer to the memory block that contains the buffers.                   |
| Protected Methods                                       | Description                                                              |
| [**Free**](cmemallocator-free.md)                      | Placeholder method; called during a decommit operation.                  |
| [**ReallyFree**](cmemallocator-reallyfree.md)          | Releases the memory for the buffers.                                     |
| [**Alloc**](cmemallocator-alloc.md)                    | Allocates memory for the buffers.                                        |
| Public Methods                                          | Description                                                              |
| [**CMemAllocator**](cmemallocator-cmemallocator.md)    | Constructor method.                                                      |
| [**~ CMemAllocator**](cmemallocator--cmemallocator.md) | Destructor method.                                                       |
| [**CreateInstance**](cmemallocator-createinstance.md)  | Creates a new instance of the **CMemAllocator** class.                   |
| IMemAllocator Methods                                   | Description                                                              |
| [**SetProperties**](cmemallocator-setproperties.md)    | Specifies the number of buffers to allocate and the size of each buffer. |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Providing a Custom Allocator](providing-a-custom-allocator.md)
</dt> </dl>

 

 




