---
description: The PrepareReceive method prepares the filter to render a sample.
ms.assetid: 873b6b3b-623e-4cec-91ea-fa628618348d
title: CBaseRenderer.PrepareReceive method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.PrepareReceive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.PrepareReceive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `PrepareReceive` method prepares the filter to render a sample.

## Syntax


```C++
virtual HRESULT PrepareReceive(
   IMediaSample *pMediaSample
);
```



## Parameters

<dl> <dt>

*pMediaSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                             | Description                                |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Failed.<br/>                         |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl>            | Unexpected error.<br/>               |
| <dl> <dt>**VFW\_E\_SAMPLE\_REJECTED**</dt> </dl> | Filter is dropping this sample.<br/> |



 

## Remarks

The filter calls this method from inside the [**CBaseRenderer::Receive**](cbaserenderer-receive.md) method, before it renders a sample. If the filter is running, this method schedules the sample for rendering.

If the filter already has a pending sample, or if the end-of-stream was already reached, the method returns E\_UNEXPECTED. Possibly the upstream filter is not serializing its streaming calls correctly.

If the scheduling algorithm determines that the sample should be dropped (see [**CBaseRenderer::ScheduleSample**](cbaserenderer-schedulesample.md)), the method returns VFW\_E\_SAMPLE\_REJECTED. However, the input pin's [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method does not pass this error code to the upstream filter, because dropping a sample is not an error.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




