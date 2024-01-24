---
description: The CheckStreaming method determines whether the pin can accept samples.
ms.assetid: fa063966-4c72-466e-933c-def6a6818621
title: CTransformInputPin.CheckStreaming method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.CheckStreaming
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformInputPin.CheckStreaming method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckStreaming` method determines whether the pin can accept samples.

## Syntax


```C++
HRESULT CheckStreaming();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values listed in the following table.



| Return code                                                                                           | Description                                 |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                         |
| <dl> <dt>**S\_FALSE**</dt> </dl>               | Pin is currently flushing.<br/>       |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | The output pin is not connected.<br/> |
| <dl> <dt>**VFW\_E\_RUNTIME\_ERROR**</dt> </dl> | A run-time error occurred.<br/>       |
| <dl> <dt>**VFW\_E\_WRONG\_STATE**</dt> </dl>   | The pin is stopped.<br/>              |



 

## Remarks

This method overrides the [**CBaseInputPin::CheckStreaming**](cbaseinputpin-checkstreaming.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




