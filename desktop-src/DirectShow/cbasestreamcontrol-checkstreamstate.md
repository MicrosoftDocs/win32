---
description: The CheckStreamState method determines whether a media sample should be delivered or discarded.
ms.assetid: 1533f4b9-e13e-458b-9614-96d733cef4ed
title: CBaseStreamControl.CheckStreamState method (Strmctl.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseStreamControl.CheckStreamState
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseStreamControl.CheckStreamState method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `CheckStreamState` method determines whether a media sample should be delivered or discarded.

## Syntax


```C++
enum CheckStreamState(
   IMediaSample *pSample
);
```



## Parameters

<dl> <dt>

*pSample* 
</dt> <dd>

Pointer to the sample's [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                       | Description                     |
|---------------------------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>**STREAM\_DISCARDING**</dt> </dl> | Discard this sample.<br/> |
| <dl> <dt>**STREAM\_FLOWING**</dt> </dl>    | Deliver this sample.<br/> |



 

## Remarks

Call this method when your pin receives a sample. Deliver the sample only if the return value is STREAM\_FLOWING. If the return value is STREAM\_DISCARDING, discard the sample.

If the pin discards any samples, it should mark the next sample that it delivers as a discontinuity, by calling the [**IMediaSample::SetDiscontinuity**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setdiscontinuity) method.

If your filter implements the [**IAMDroppedFrames**](/windows/desktop/api/Strmif/nn-strmif-iamdroppedframes) interface to count how many frames it drops, do not count a discarded frame as a dropped frame.

When the return value is STREAM\_DISCARDING, the method blocks until the reference time reaches the sample's start time. This prevents your pin from discarding samples too quickly. If the filter is paused, the wait time is infinite, until the filter runs, stops, or flushes data. (Filter state changes and streaming happen on separate threads, so this does not cause any deadlock.)

The **CBaseStreamControl::StreamControlState** enumeration is defined as follows:


```C++
enum StreamControlState{ 
    STREAM_FLOWING = 0x1000,
    STREAM_DISCARDING
};
```



## Examples

The following example assumes that the pin uses a member variable named m\_fLastSampleDiscarded to keep track of discontinuities.


```C++
CMyPin::Receive(IMediaSample *pSample)
{
    if (!pSample) return E_POINTER;

    int iStreamState = CheckStreamState(pSample);
    if (iStreamState == STREAM_FLOWING) 
    {
        if (m_fLastSampleDiscarded)
            pSample->SetDiscontinuity(TRUE);
        m_fLastSampleDiscarded = FALSE;
        /* Deliver the sample. */
    } 
    else 
    {
        m_fLastSampleDiscarded = TRUE;  
       // Discard this sample. Do not deliver it.
    }
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




