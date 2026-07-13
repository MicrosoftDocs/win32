---
description: The BeginFlush method begins a flush operation. This method implements the IPin::BeginFlush method.
ms.assetid: 7c76ca06-dc3c-4f9a-9761-32aea7db4c7e
title: CTransformInputPin.BeginFlush method (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin.BeginFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformInputPin.BeginFlush method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `BeginFlush` method begins a flush operation. This method implements the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) method.

## Syntax


```C++
HRESULT BeginFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                                           | Description                             |
|-------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                     |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | Output pin is not connected.<br/> |



 

## Remarks

This method calls the pin's [**CBaseInputPin::BeginFlush**](cbaseinputpin-beginflush.md) method. Then it calls the filter's [**CTransformFilter::BeginFlush**](ctransformfilter-beginflush.md) method to deliver the call downstream.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




