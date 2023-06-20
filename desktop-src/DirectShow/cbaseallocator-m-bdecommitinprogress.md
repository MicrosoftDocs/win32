---
description: Flag indicating whether a decommit operation is in progress.
ms.assetid: aa008be1-8faa-4dc1-9641-37dcc59ce6c7
title: CBaseAllocator::m_bDecommitInProgress member (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bDecommitInProgress
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseAllocator::m\_bDecommitInProgress member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Flag indicating whether a decommit operation is in progress. The value is **TRUE** after the [**CBaseAllocator::Decommit**](cbaseallocator-decommit.md) method is called, but before all the buffers have been released. If the value is **TRUE**, the [**CBaseAllocator::GetBuffer**](cbaseallocator-getbuffer.md) method fails. Also, the allocator should not deleted itself while the value is **TRUE**.

## Syntax


```C++
BOOL m_bDecommitInProgress;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseAllocator Class**](cbaseallocator.md)
</dt> </dl>

 

 




