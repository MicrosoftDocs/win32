---
description: The put\_Rate method sets the playback rate. This method implements the IMediaPosition::put\_Rate method.
ms.assetid: c077f344-de34-4f8a-8e08-6d7086a5a4f1
title: CPosPassThru.put_Rate method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CPosPassThru.put_Rate
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CPosPassThru.put\_Rate method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `put_Rate` method sets the playback rate. This method implements the [**IMediaPosition::put\_Rate**](/windows/desktop/api/Control/nf-control-imediaposition-put_rate) method.

## Syntax


```C++
HRESULT put_Rate(
   double dRate
);
```



## Parameters

<dl> <dt>

*dRate* 
</dt> <dd>

Playback rate. Must not be zero.

</dd> </dl>

## Return value

Returns E\_INVALIDARG if *dRate* is zero. Otherwise, returns the **HRESULT** value from the connected pin.

## Remarks

Negative rates indicate reverse play. Not all media will support reverse play.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPosPassThru Class**](cpospassthru.md)
</dt> </dl>

 

 




