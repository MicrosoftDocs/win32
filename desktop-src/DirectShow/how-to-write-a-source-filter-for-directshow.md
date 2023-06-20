---
description: This topic describes how to write a custom source filter for DirectShow.
ms.assetid: 032f7624-2237-41cd-844a-18ed4a2e420d
title: How to Write a Source Filter for DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How to Write a Source Filter for DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic describes how to write a custom source filter for DirectShow.

> [!Note]  
> This topic describes push sources only; it does not describe pull sources, such as the Async Reader Filter, or splitter filters that connect to pull sources. For the distinction between *push* and *pull* sources, see [Data Flow for Filter Developers](data-flow-for-filter-developers.md).

 

## The DirectShow Streaming Model

When you write a source filter, it is important to understand that a push source is not the same thing as a live source. A live source gets data from some external source, such as a camera or a network stream. Generally, a live source cannot control the incoming rate of data. If the downstream filters do not consume the data fast enough, the source will need to drop samples.

But a push source does not have to be a live source. For example, a push source can read data from a local file. In that case, the downstream renderer filters determine how fast they consume the data from the source, based on the reference clock and the sample time stamps. The source filter delivers samples as quickly as possible, but the actual data flow is gated limited by the renderers. The mechanisms for gating the data flow are described in [Data Flow for Filter Developers](data-flow-for-filter-developers.md).

Each output pin on the source filter creates a thread called a *streaming thread*. The pin delivers samples on the streaming thread. Typically, all of the decoding, processing, and rendering happens on this thread, although some downstream filters might create additional threads to queue their output samples.

The streaming thread runs a loop with the following structure:

``` syntax
until (stopped)
  1. Get a media sample from the allocator.
  2. Fill the sample with data.
  3. Time stamp the sample. 
  4. Deliver the sample downstream.
```

If no samples are available, step 1 blocks until a sample becomes available. Step 4 can also block; for example, it can block while the graph is paused.

The loop runs as quickly as possible, but is limited by how quickly the renderer filter renders each sample. Assuming the filter graph has a reference clock, the rate is determined by the presentation times on the samples. If there is no reference clock, the renderer consumes samples as quickly as possible.

## Using CSource and CSourceStream

The DirectShow base classes include two classes that support push sources: [**CSource**](csource.md) and [**CSourceStream**](csourcestream.md).

-   [**CSource**](csource.md) is the base class for the filter and implements the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface.
-   [**CSourceStream**](csourcestream.md) is the base class for the output pins, and implements the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface.

### Output Pins

A source filter can have more than one output pin. In your filter's constructor method, create one or more pins derived from [**CSourceStream**](csourcestream.md) (one pin per output stream). You don't need to store pointers to the pins; the pins automatically add themselves to the filter when they are created.

### Output Formats

The output pin handles format negotiation with the following [**CSourceStream**](csourcestream.md) methods:



| Method                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetMediaType**](csourcestream-getmediatype.md)     | Gets a media type from the output pin. <br/> The pin must propose at least one media type, because the downstream filter might not propose any types. In most cases, the downstream filter will be a decoder or a renderer, depending on whether the source filter delivers compressed or uncompressed data. A renderer filter usually requires a complete media type, containing all of the format information needed to render the stream. For a decoder, the amount of information that is required in the media type depends very much on the encoding format.<br/> |
| [**CheckMediaType**](csourcestream-checkmediatype.md) | Checks if the output pin accepts a given media type. Overriding this method is optional, depending on how you implement [**GetMediaType**](csourcestream-getmediatype.md).                                                                                                                                                                                                                                                                                                                                                                                                         |



 

The [**GetMediaType**](csourcestream-getmediatype.md) method is overloaded:

-   [**GetMediaType**](csourcestream-getmediatype.md) (1) takes a single parameter, a pointer to a [**CMediaType**](cmediatype.md) object.
-   [**GetMediaType**](csourcestream-getmediatype2.md) (2) takes an index variable and a pointer to a [**CMediaType**](cmediatype.md) object.

If the source filter's output pin supports exactly one media format, you should override (1) to initialize the [**CMediaType**](cmediatype.md) object with that format. Leave the default implementation of (2) and also leave the default implementation of [**CheckMediaType**](csourcestream-checkmediatype.md).

If the pin supports more than one format, override (2). Initialize the [**CMediaType**](cmediatype.md) object according to the value of the index variable. The pin should return the formats as an ordered list. In this case, you must also override the [**CheckMediaType**](csourcestream-checkmediatype.md) to check the media type against your list of formats.

For uncompressed video formats, remember that the downstream filter can propose formats with various stride values. Your filter should accept any valid stride value. For more information, see [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader).

You must also override the pure-virtual [**CBaseOutputPin::DecideBufferSize**](cbaseoutputpin-decidebuffersize.md) method. Use this method to set the size of the sample buffers.

### Streaming

The [**CSourceStream**](csourcestream.md) class creates the streaming thread for the pin. The thread procedure is implemented in the [**CSourceStream::DoBufferProcessingLoop**](csourcestream-dobufferprocessingloop.md) method. This method calls the pure-virtual [**CSourceStream::FillBuffer**](csourcestream-fillbuffer.md) method, which the derived class must override. This method is where the pin fills the buffer with data. For example, if your filter delivers uncompressed video, this is where you would draw the video frames.

The base class automatically starts and stops the thread loop at the right times, when the filter pauses or stops. When this happens, the [**CSourceStream**](csourcestream.md) class calls some methods to notify your derived class:

-   [**CSourceStream::OnThreadCreate**](csourcestream-onthreadcreate.md)
-   [**CSourceStream::OnThreadDestroy**](csourcestream-onthreaddestroy.md)
-   [**CSourceStream::OnThreadStartPlay**](csourcestream-onthreadstartplay.md)

You can override these methods if you need to add any special handling. Otherwise, the default implementations simply return **S\_OK**.

## Seeking

If you have a source filter with one output pin, you can use the [**CSourceSeeking**](csourceseeking.md) class as a starting point for implementing seeking. Inherit your pin class from both [**CSourceStream**](csourcestream.md) and **CSourceSeeking**.

> [!Note]  
> [**CSourceSeeking**](csourceseeking.md) is not recommended for a filter with more than one output pin. The main issue is that only one pin should respond to seeking requests. Typically this requires communication among the pins and the filter.

 

The [**CSourceSeeking**](csourceseeking.md) class manages the playback rate, start time, stop time, and duration. Your derived class should set the initial stop time and duration. Whenever one of these values changes, the [**CSourceSeeking::ChangeRate**](csourceseeking-changerate.md), [**CSourceSeeking::ChangeStart**](csourceseeking-changestart.md), or [**CSourceSeeking::ChangeStop**](csourceseeking-changestop.md) method is called, as appropriate. The methods are all pure virtual methods. The derived pin class overrides these methods to do the following:

1.  Call [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) on the downstream pin. This causes downstream filters to release samples they are holding and reject new samples.
2.  Call [**CSourceStream::Stop**](csourcestream-stop.md) to stop the streaming thread. The source filter suspends producing new data.
3.  Call [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) on the downstream pin. This signals the downstream filters to accept new data.
4.  Call [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment) with the new start and stop times and rate.
5.  Set the discontinuity property on the next sample.

For more information, see [Supporting Seeking in a Source Filter](supporting-seeking-in-a-source-filter.md).

If your filter supports seeking, the stream position is now independent of the presentation time. After a seek, time stamps reset to zero. The general formula for time stamps is:

-   sample start time = time elapsed / playback rate
-   sample end time = sample start time + (time per frame / playback rate)

where *time elapsed* is the time that has elapsed since the filter started running or since the last seek command.

### Time Formats for Seeking

By default, seek commands are in units of 100-nanoseconds. Your source filter can support additional time formats, such as seeking by frame number. Each time format is identified by a GUID; see [**Time Format GUIDs**](time-format-guids.md).

To support additional time formats, you must implement the following methods on your output pin:

-   [**IMediaSeeking::ConvertTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-converttimeformat)
-   [**IMediaSeeking::GetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-gettimeformat)
-   [**IMediaSeeking::IsFormatSupported**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-isformatsupported)
-   [**IMediaSeeking::IsUsingTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-isusingtimeformat)
-   [**IMediaSeeking::QueryPreferredFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-querypreferredformat)
-   [**IMediaSeeking::SetTimeFormat**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-settimeformat)

If the application sets a new time format, all of the position parameters in the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) methods are interpreted in terms of the new time format. For example, if the time format is frames, the [**IMediaSeeking::GetDuration**](/windows/desktop/api/Strmif/nf-strmif-imediaseeking-getduration) method must return the duration in frames.

In practice, few DirectShow filters support additional time formats, and as a result, few DirectShow applications make use of this capability.

## Related topics

<dl> <dt>

[Writing Source Filters](writing-source-filters.md)
</dt> </dl>

 

 




