---
description: The CanReconnectWhenActive method queries whether the pin supports dynamic reconnections.
ms.assetid: a2679987-7897-4b18-b06b-9ab8f2f3b9f5
title: CBasePin.CanReconnectWhenActive method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CanReconnectWhenActive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.CanReconnectWhenActive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CanReconnectWhenActive` method queries whether the pin supports dynamic reconnections.

## Syntax


```C++
bool CanReconnectWhenActive();
```



## Parameters

This method has no parameters.

## Return value

Returns a Boolean value that specifies whether the pin can dynamically reconnect. If **TRUE**, the pin can dynamically reconnect.

## Remarks

By default, you must stop a filter before reconnecting any of its pins. If a pin supports dynamic reconnection, however, it can reconnect while the filter is active. For more information, see [Dynamic Graph Building](dynamic-graph-building.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




