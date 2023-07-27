---
description: The SetClockDelta method adjusts the clock time. This method implements the IAMClockAdjust::SetClockDelta method.
ms.assetid: 2bb9266f-3866-4b2e-92a8-cde31a501047
title: CSystemClock.SetClockDelta method (Sysclock.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSystemClock.SetClockDelta
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSystemClock.SetClockDelta method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetClockDelta` method adjusts the clock time. This method implements the [**IAMClockAdjust::SetClockDelta**](/windows/desktop/api/Strmif/nf-strmif-iamclockadjust-setclockdelta) method.

## Syntax


```C++
HRESULT SetClockDelta(
   REFERENCE_TIME rtDelta
);
```



## Parameters

<dl> <dt>

*rtDelta* 
</dt> <dd>

Specifies the amount by which to adjust the clock, as a [**REFERENCE\_TIME**](reference-time.md) value. A positive value moves the clock forward, and a negative value moves the clock backward.

</dd> </dl>

## Return value

Returns S\_OK or an **HRESULT** error code.

## Remarks

This method simply calls [**CBaseReferenceClock::SetTimeDelta**](cbasereferenceclock-settimedelta.md).

The time values returned by [**IReferenceClock::GetTime**](/windows/desktop/api/Strmif/nf-strmif-ireferenceclock-gettime) are monotonically increasing. If you set the clock back, **GetTime** continues to report the old time until the internal clock catches up.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | CSystemClock Class<br/>                                                                                                                                                              |
| Header<br/>  | <dl> <dt>Sysclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




