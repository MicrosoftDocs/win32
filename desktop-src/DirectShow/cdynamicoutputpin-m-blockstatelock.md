---
description: Critical section that protects the blocking state.
ms.assetid: 6d20cf4c-2c27-41e6-8d01-6cb5e3876a38
title: CDynamicOutputPin::m_BlockStateLock member (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_BlockStateLock
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDynamicOutputPin::m\_BlockStateLock member

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Critical section that protects the blocking state.

## Syntax


```C++
CCritSec m_BlockStateLock;
```



## Remarks

Hold this critical section before using any of the following member variables:

-   [**CDynamicOutputPin::m\_BlockState**](cdynamicoutputpin-m-blockstate.md)
-   [**CDynamicOutputPin::m\_dwBlockCallerThreadID**](cdynamicoutputpin-m-dwblockcallerthreadid.md)
-   [**CDynamicOutputPin::m\_dwNumOutstandingOutputPinUsers**](cdynamicoutputpin-m-dwnumoutstandingoutputpinusers.md)
-   [**CDynamicOutputPin::m\_hNotifyCallerPinBlockedEvent**](cdynamicoutputpin-m-hnotifycallerpinblockedevent.md)

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




