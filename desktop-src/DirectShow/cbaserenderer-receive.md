---
description: The Receive method receives the next media sample in the stream.
ms.assetid: b340f76c-2305-444f-bc00-1ef5acdea329
title: CBaseRenderer.Receive method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.Receive
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.Receive method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Receive` method receives the next media sample in the stream.

## Syntax


```C++
virtual Receive(
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

Returns S\_OK if successful, or an **HRESULT** value indicating the cause of the error.

## Remarks

The input pin calls this method when it receives a sample from the upstream filter.

If the filter is running, this method performs the following steps:

1.  Schedules the sample for rendering ([**CBaseRenderer::PrepareReceive**](cbaserenderer-preparereceive.md)).
2.  Waits for the scheduled time ([**CBaseRenderer::WaitForRenderTime**](cbaserenderer-waitforrendertime.md)).
3.  Renders the sample ([**CBaseRenderer::Render**](cbaserenderer-render.md)).
4.  Releases the sample ([**CBaseRenderer::ClearPendingSample**](cbaserenderer-clearpendingsample.md)).

If the filter is paused, the method performs the following steps:

1.  Notifies the derived class that a sample is available ([**CBaseRenderer::OnReceiveFirstSample**](cbaserenderer-onreceivefirstsample.md)).
2.  Waits for the scheduled time.
3.  Renders the sample.
4.  Releases the sample.

While paused, the method waits in step 2 until the filter switches to a running state. At that point, the filter schedules the sample.

In the base class, the **OnReceiveFirstSample** method does nothing. The derived class can override it. For example, when a video renderer is paused, it displays the first sample as a still image.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




