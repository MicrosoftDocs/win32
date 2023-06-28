---
description: Flag that indicates whether the filter has sent an end-of-stream notification.
ms.assetid: 93f897de-04bb-4de4-a612-39b27c7d6f6c
title: CTransformFilter::m_bEOSDelivered member (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_bEOSDelivered
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformFilter::m\_bEOSDelivered member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Flag that indicates whether the filter has sent an end-of-stream notification.

## Syntax


```C++
BOOL m_bEOSDelivered;
```



## Remarks

If the filter pauses when it does not have an input connection, it sends an end-of-stream notification downstream and sets this flag to **TRUE**. The end-of-stream notification ensures that the downstream filter does not wait for samples. Note that the filter's [**EndOfStream**](ctransformfilter-endofstream.md) method does not set this flag.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




