---
description: The SetReconnectWhenActive method specifies whether the pin supports dynamic reconnections.
ms.assetid: 64776008-5d1b-461c-a446-8cd6124276c0
title: CBasePin.SetReconnectWhenActive method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.SetReconnectWhenActive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.SetReconnectWhenActive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetReconnectWhenActive` method specifies whether the pin supports dynamic reconnections.

## Syntax


```C++
void SetReconnectWhenActive(
   bool bCanReconnect
);
```



## Parameters

<dl> <dt>

*bCanReconnect* 
</dt> <dd>

Boolean value that specifies whether the pin can dynamically reconnect. If **TRUE**, the pin can dynamically reconnect.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

By default, you must stop a filter before reconnecting any of its pins. If the pin can reconnect while the filter is active, call this method with a value of **TRUE**. For more information, see [Dynamic Graph Building](dynamic-graph-building.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




