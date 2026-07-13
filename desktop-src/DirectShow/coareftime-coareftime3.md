---
description: "Learn about the COARefTime.COARefTime constructor (Ctlutil.h) method. This method uses the 't' parameter."
ms.assetid: 1f3b5c63-edaa-42c1-8892-d6681c81ae4d
title: COARefTime.COARefTime constructor (Ctlutil.h) - t parameter
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COARefTime.COARefTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COARefTime.COARefTime constructor (Ctlutil.h) - t parameter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
COARefTime(
   REFERENCE_TIME t
);
```



## Parameters

<dl> <dt>

*t* 
</dt> <dd>

[**REFERENCE\_TIME**](reference-time.md) value that specifies the reference time in 100-nanosecond units.

</dd> </dl>

## Requirements

| Requirement                   | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Ctlutil.h (include Streams.h)                                                                                   |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




