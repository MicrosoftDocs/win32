---
description: The DisplayPinInfo method traces a pin connection during debugging.
ms.assetid: 3c1aa5ab-7f6b-4518-abf3-b5138f6267ee
title: CBasePin.DisplayPinInfo method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.DisplayPinInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.DisplayPinInfo method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DisplayPinInfo` method traces a pin connection during debugging.

## Syntax


```C++
void DisplayPinInfo(
   IPin *pReceivePin
);
```



## Parameters

<dl> <dt>

*pReceivePin* 
</dt> <dd>

Pointer to the receiving pin.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

In debug builds, this method calls the [**DbgLog**](dbglog.md) function to trace a connection attempt. In retail builds, this method does nothing.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




