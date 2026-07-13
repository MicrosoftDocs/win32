---
description: The EOS method updates the cached time stamps after an end-of-stream notification.
ms.assetid: 7fb2f964-ec15-47f5-902b-29b9b121e876
title: CRendererPosPassThru.EOS method (Ctlutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererPosPassThru.EOS
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRendererPosPassThru.EOS method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `EOS` method updates the cached time stamps after an end-of-stream notification.

## Syntax


```C++
HRESULT EOS();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those listed in the following table.



| Return code                                                                            | Description                                               |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Failure. Possibly the filter is not streaming.<br/> |



 

## Remarks

The filter should call this method when it receives an end-of-stream notification ([**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream)). The method sets both cached time stamps equal to the stop position, ensuring that the [**IMediaSeeking:: GetCurrentPosition**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getcurrentposition) method returns the correct values at the end of the stream.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




