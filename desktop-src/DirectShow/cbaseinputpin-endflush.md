---
description: The EndFlush method ends a flush operation. Implements the IPin::EndFlush method.
ms.assetid: d4110eb4-26c5-4312-b33f-4af31e1bf2ae
title: CBaseInputPin.EndFlush method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseInputPin.EndFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseInputPin.EndFlush method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `EndFlush` method ends a flush operation. Implements the [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) method.

## Syntax


```C++
HRESULT EndFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method sets the [**CBaseInputPin::m\_bFlushing**](cbaseinputpin-m-bflushing.md) flag to **TRUE**, which enables the [**CBaseInputPin::Receive**](cbaseinputpin-receive.md) method to accept samples.

The derived class must override this method and perform the following steps:

1.  Free any buffered data and wait for all queued samples to be discarded.
2.  Clear any pending [**EC\_COMPLETE**](ec-complete.md) notifications.
3.  Call the base class method.
4.  Call [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) on downstream input pins. If the pin has not yet delivered any media samples downstream, you can skip this step. If your output pins derive from the [**CBaseOutputPin**](cbaseoutputpin.md) class, you can call the [**CBaseOutputPin::DeliverEndFlush**](cbaseoutputpin-deliverendflush.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseInputPin Class**](cbaseinputpin.md)
</dt> </dl>

 

 




