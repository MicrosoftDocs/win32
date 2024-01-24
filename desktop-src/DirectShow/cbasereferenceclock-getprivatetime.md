---
description: The GetPrivateTime method retrieves the real time from the clock.
ms.assetid: ce9832cb-4b5a-49a1-9a69-d2fb90b3ed2e
title: CBaseReferenceClock.GetPrivateTime method (Refclock.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseReferenceClock.GetPrivateTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseReferenceClock.GetPrivateTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetPrivateTime` method retrieves the real time from the clock.

## Syntax


```C++
virtual REFERENCE_TIME GetPrivateTime();
```



## Parameters

This method has no parameters.

## Return value

Returns the current clock time, in 100-nanosecond units.

## Remarks

This method returns the real time reported by the clock. External callers use the [**CBaseReferenceClock::GetTime**](cbasereferenceclock-gettime.md) method, which calls this method. Unlike the **GetTime** method, the internal clock is allowed to go backward. If that happens, the **GetTime** method continues to return the last time that it reported, until the `GetPrivateTime` method catches up.

This method returns the system time. Override this method if your clock gets the time from another source.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Refclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> </dl>

 

 




