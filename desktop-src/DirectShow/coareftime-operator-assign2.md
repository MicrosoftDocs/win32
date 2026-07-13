---
description: "The operator assigns a new reference time and uses the 'rt [ref]' parameter."
ms.assetid: e3a005c0-95d5-41e0-80bb-e70399a50dca
title: COARefTime.operator= method (Ctlutil.h) - rt [ref] parameter
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COARefTime.operator=
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# COARefTime.operator= method (Ctlutil.h) - rt [ref] parameter

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This operator assigns a new reference time.

## Syntax


```C++
COARefTime& operator=(
  [ref] const REFERENCE_TIME &rt
);
```



## Parameters

<dl> <dt>

*rt* \[ref\]
</dt> <dd>

Reference to a [**REFERENCE\_TIME**](reference-time.md) value that specifies the new reference time in 100-nanosecond units.

</dd> </dl>

## Return value

Returns a reference to the object.

## Requirements

| Requirement                    | Value                                                                                                                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header  | Ctlutil.h (include Streams.h)                                                                                   |
| Library | Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**COARefTime Class**](coareftime.md)
</dt> </dl>

 

 




