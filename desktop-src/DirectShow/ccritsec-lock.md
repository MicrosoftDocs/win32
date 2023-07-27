---
description: The Lock method locks the critical section object.
ms.assetid: b08be5ec-3f02-4ed8-8791-20e4d2a0c55f
title: CCritSec.Lock method (Wxutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCritSec.Lock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CCritSec.Lock method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Lock** method locks the critical section object.

## Syntax


```C++
void Lock();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

This method calls the [**EnterCriticalSection**](/windows/desktop/api/synchapi/nf-synchapi-entercriticalsection) function.

Call the [**CCritSec::Unlock**](ccritsec-unlock.md) member function to unlock the critical section. You can make multiple calls to the **Lock** method on the same thread; be sure to call **Unlock** a corresponding number of times.

If the object is already locked by another thread, the **CCritSec::Lock** method blocks until the object is released, or until a possible-deadlock exception occurs.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

