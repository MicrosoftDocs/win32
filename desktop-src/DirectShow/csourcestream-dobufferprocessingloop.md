---
description: The DoBufferProcessingLoop method generates media data and delivers it to the downstream input pin.
ms.assetid: a8dce761-eed6-402d-9115-e21822d7a853
title: CSourceStream.DoBufferProcessingLoop method (Source.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourceStream.DoBufferProcessingLoop
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSourceStream.DoBufferProcessingLoop method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `DoBufferProcessingLoop` method generates media data and delivers it to the downstream input pin.

## Syntax


```C++
virtual HRESULT DoBufferProcessingLoop();
```



## Parameters

This method has no parameters.

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                                                             |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Thread received a stop request.<br/>                              |
| <dl> <dt>**S\_OK**</dt> </dl>    | Stream ended, or downstream filter is not accepting samples.<br/> |



 

## Remarks

This method implements the main loop that processes data and delivers it downstream. Each time through the loop, the method retrieves an empty media sample from the allocator. It passes the sample to the [**CSourceStream::FillBuffer**](csourcestream-fillbuffer.md) method. The **FillBuffer** method, which the derived class must implement, generates media data and places it in the sample buffer.

The loop ends when any of the following occurs:

-   The input pin's [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method rejects a sample.
-   The **FillBuffer** method returns S\_FALSE, indicating the end of the stream, or returns an error code.
-   The thread receives a [**CSourceStream::Stop**](csourcestream-stop.md) request.

The `DoBufferProcessingLoop` method handles the end-of-stream notification. If an error occurs, it sends an [**EC\_ERRORABORT**](ec-errorabort.md) event to the filter graph manager.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSourceStream Class**](csourcestream.md)
</dt> </dl>

 

 




