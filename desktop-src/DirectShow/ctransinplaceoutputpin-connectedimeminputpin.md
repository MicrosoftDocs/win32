---
description: The ConnectedIMemInputPin method retrieves a pointer to the downstream input pin. This method returns the CBaseOutputPin::m\_pInputPin member variable.
ms.assetid: 39a12603-7768-43c3-9558-7caaa8f55108
title: CTransInPlaceOutputPin.ConnectedIMemInputPin method (Transip.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransInPlaceOutputPin.ConnectedIMemInputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransInPlaceOutputPin.ConnectedIMemInputPin method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `ConnectedIMemInputPin` method retrieves a pointer to the downstream input pin. This method returns the [**CBaseOutputPin::m\_pInputPin**](cbaseoutputpin-m-pinputpin.md) member variable.

## Syntax


```C++
IMemInputPin* ConnectedIMemInputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the [**IMemInputPin**](/windows/desktop/api/Strmif/nn-strmif-imeminputpin) interface on the downstream input pin.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceOutputPin Class**](ctransinplaceoutputpin.md)
</dt> </dl>

 

 




