---
description: This topic describes how to implement a custom media source in Microsoft Media Foundation.
ms.assetid: '82db6f32-ad94-4563-b8bd-8a5072c5b221'
title: Writing a Custom Media Source
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Custom Media Source

This topic describes how to implement a custom media source in Microsoft Media Foundation. It contains the following sections:

-   [Creating the Presentation Descriptor](#creating-the-presentation-descriptor)
-   [Starting the Media Source](#starting-the-media-source)
    -   [Seeking](#seeking)
-   [Pausing the Media Source](#pausing-the-media-source)
-   [Generating Source Data](#generating-source-data)
    -   [Sample Requests](#sample-requests)
    -   [Allocating Samples](#allocating-samples)
    -   [Gaps in the Stream](#gaps-in-the-stream)
-   [Shutting Down the Media Source](#shutting-down-the-media-source)
-   [Live Sources](#live-sources)
-   [Related topics](#related-topics)

## Creating the Presentation Descriptor

The [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) method returns a copy of the source's presentation descriptor. To create the presentation descriptor, you must know the number of streams in the source content, and the possible formats of each stream. For each stream, create a stream descriptor as follows:

1.  Create an array of media types. Each media type in the array represents a possible format for the stream. For more information about creating media types, see [Media Types](media-types.md).
2.  Call [**MFCreateStreamDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatestreamdescriptor) to create the stream descriptor. Pass in the array of media types. The function returns an [**IMFStreamDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfstreamdescriptor) pointer.
3.  Call [**IMFStreamDescriptor::GetMediaTypeHandler**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamdescriptor-getmediatypehandler) to get the stream descriptor's media type handler.
4.  Call [**IMFMediaTypeHandler::SetCurrentMediaType**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-setcurrentmediatype) to set the default stream format. Use one of the media types that you created in step 1. Generally, you should use the format with the highest quality.
5.  Optionally, set attributes on the stream descriptor. For a list of attributes that apply to stream descriptors, see [Stream Descriptor Attributes](stream-descriptor-attributes.md).

Now create the presentation descriptor:

1.  Call [**MFCreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepresentationdescriptor) and pass in the array of stream descriptors. The function returns an [**IMFPresentationDescriptor**](/windows/desktop/api/mfidl/nn-mfidl-imfpresentationdescriptor) pointer.
2.  Choose the default stream selection by calling [**IMFPresentationDescriptor::SelectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-selectstream) to select one or more streams. At least one stream must be selected in the default configuration.
3.  Optionally, set attributes on the presentation descriptor. For a list of attributes that apply to stream descriptors, see [Presentation Descriptor Attributes](presentation-descriptor-attributes.md).

You should create the presentation descriptor once, either at startup or after the source has parsed enough of the source data to determine the contents. The [**CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) method should return a copy of presentation descriptor. To create the copy, call [**IMFPresentationDescriptor::Clone**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-clone). Returning a copy prevents the client from modifying the state of the original presentation descriptor, such as the attributes or the stream selection. However, be aware that **Clone** creates a shallow copy, so the client can potentially modify the underlying stream descriptors.

## Starting the Media Source

The [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method starts the media source or seeks to a new position. A call to **Start** causes a *seek* when the previous state was either paused or running, and a new start time is specified. Otherwise, the **Start** method causes a *start*. When the **Start** operation completes, send the following events.

1.  Send an [MENewStream](menewstream.md) event for each new stream—that is, each stream that was previously deselected and is now selected. The event data is a pointer to the stream.
2.  Send an [MEUpdatedStream](meupdatedstream.md) event for each stream that was previously selected and is still selected. The event data is a pointer to the stream. (Do not send an event for deselected streams.)
3.  If the source is seeking, send an [MESourceSeeked](mesourceseeked.md) event. Otherwise, send an [MESourceStarted](mesourcestarted.md) event. The event data is the start time that was specified in the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method. For the MESourceStarted event, if the start time is VT\_EMPTY, set the [**MF\_EVENT\_SOURCE\_ACTUAL\_START**](mf-event-source-actual-start-attribute.md) attribute on the event. The attribute value is the actual start time.
4.  For each stream, if the source is seeking, send an [MEStreamSeeked](mestreamseeked.md) event. Otherwise, send an [MEStreamStarted](mestreamstarted.md) event. The event data is the start time. (The media source can queue an event on the stream by calling the stream's [**IMFMediaEventGenerator::QueueEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-queueevent) method.)

When a stream is deselected, shut down the stream. The stream should not queue any more events at that point.

The time format for the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method is given in the *pguidTimeFormat* parameter. The standard time format, indicated by **GUID\_NULL**, is 100-nanosecond units. A media source must support this time format.

### Seeking

When seeking, the requested start position might not fall on an exact sample boundary. Also, for compressed content, the start position might fall between key frames. A stream should deliver samples from the earliest point needed to produce an uncompressed sample at the requested start position. For video, that means starting from the previous key frame. The pipeline is responsible for dropping the extra frames from the decoder, so that playback starts at the requested time.

The starting time given in the source events ([MESourceStarted](mesourcestarted.md), [MESourceSeeked](mesourceseeked.md), [MEStreamStarted](mestreamstarted.md), and [MEStreamSeeked](mestreamseeked.md)) is the requested starting time (the value given in the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method), regardless of the actual start position.

For example, suppose the first few frames of a video stream have the following characteristics:



| Sample     | 1       | 2       | 3        | 4        |
|------------|---------|---------|----------|----------|
| Time       | 33 msec | 66 msec | 100 msec | 133 msec |
| Key frame? | Yes     | No      | No       | Yes      |



 

If the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method is called with a value of 100 milliseconds, the source needs to output video starting from frame 1, the first key frame prior to this time. The start event will still indicate 100 milliseconds in the event data.

## Pausing the Media Source

The [**IMFMediaSource::Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause) method pauses the media source.

While the source is paused, a stream can create new samples and store them on a queue, but the stream does not deliver the samples. Here are some exceptions to this rule:

-   Live sources should drop data while paused.
-   If the source gets data from a network, it might pause the server.

If the client calls [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) while the source is paused, the request is also queued until the source is started again. Requests should not be dropped.

Pausing is allowed only from the started state. Otherwise, [**Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause) should return **MF\_E\_INVALID\_STATE\_TRANSITION**.

## Generating Source Data

Media Foundation uses a *pull model*, meaning that streams generate and deliver samples in response to requests from the pipeline. A stream can deliver samples when the media source is running and the stream is selected. A stream delivers data only when the client requests a new sample.

### Sample Requests

The client requests a new sample by calling [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample). Here is the sequence of operations:

1.  The client calls [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample). The argument is a pointer to an optional *token* object that the client uses to track the request. The client implements the token. Tokens must expose the **IUnknown** interface. The client can also pass in a NULL pointer instead of a token.
2.  If the client provided a token, the media stream calls **AddRef** on the token and places the token in a first-in, first-out queue. The method returns, and the remaining steps occur asynchronously.

3.  When more data is available, the media stream creates a new sample. (This step is described in more detail in the next section.)
4.  The media stream pulls the first token from the queue.
5.  If the token is not **NULL**, the media stream sets the [**MFSampleExtension\_Token**](mfsampleextension-token-attribute.md) attribute on the media sample. The value of the attribute is a pointer to the token.
6.  The media stream sends an [MEMediaSample](memediasample.md) event. The event data is a pointer to the sample's [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface.
7.  If the client provided a token, the media stream calls **Release** on the token object.

If the media stream cannot fulfill the client's [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) request, it pulls the token from the queue and calls **Release** on the token, but does not send an [MEMediaSample](memediasample.md) event.

The client can use the token to track the status of the request. When the client receives the [MEMediaSample](memediasample.md) event, it can get the token from the sample and match it against the original request. The client can also use the token to detect if the media source dropped the request. If the token's reference count falls to zero and the media stream does not send an MEMediaSample event, it means that the request was dropped.

The steps listed here assume that [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method is implemented as an asynchronous operation. If the method is synchronous, you do not need to put the request token on a queue. However, if generating data takes any significant amount of time, an asynchronous approach is recommended—for example, if the source reads data from a byte stream.

The stream is responsible for buffering any data that accumulates between calls to [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample).

When the media stream reaches the end of the stream, it sends an [MEEndOfStream](meendofstream.md) event after the last sample. After every stream has ended, the media source sends an [MEEndOfPresentation](meendofpresentation.md) event. After a media stream sends the MEEndOfStream event, the [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method returns **MF\_E\_END\_OF\_STREAM** until the source is restarted.

### Allocating Samples

When the stream is ready to fill a pending sample request, it creates a new sample and adds one or more media buffers to the sample. For more information about creating media buffers, see [Media Buffers](media-buffers.md).

The stream must set the time stamp and the duration, if known. The time stamp is relative to the source. In most cases, the start of the content corresponds to a time stamp of zero. For example, if the source reads from a media file, the start of the file would have a time stamp of zero.

The time stamp on the sample does not necessarily equal the presentation time. The Media Session translates from source time to presentation time. For compressed data, the stream should generate data starting from the nearest key frame before the start time. This enables the decoder to deliver the frame that appears at the requested start time. (Otherwise, the decoder would need to wait until the following key frame.)

If the playback rate is faster or slower than 1.0, the pipeline adjusts the rate of the presentation clock. The source does not adjust the time stamps on samples.

The source can set additional information on the sample by setting attributes. For a list of sample attributes, see [Sample Attributes](sample-attributes.md).

### Gaps in the Stream

If a stream contains a gap of significant length, it is recommended that the stream send an [MEStreamTick](mestreamtick.md) event. This event notifies the client that a sample is missing. The event data is the time stamp of the missing sample, in 100-nanosecond units (**VT\_I8**). This event can save downstream components from waiting for samples that will not arrive. The stream can send as many MEStreamTick events as needed to span the gap in the stream.

## Shutting Down the Media Source

When the client is done using the media source, it calls [**IMFMediaSource::Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-shutdown). Inside this method, the media source should break any circular reference counts. Typically, there will be circular references between the media source and the media streams.

If you are using the event queue to implement [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator), call [**IMFMediaEventQueue::Shutdown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventqueue-shutdown) on the event queue. This method shuts down the event queue and signals any caller that is currently waiting for an event.

After shutdown, all methods on the source return **MF\_E\_SHUTDOWN**, with the exception of **IUnknown** methods.

## Live Sources

Starting in Windows 7, Media Foundation automatically supports audio and video capture devices. For video, the device must provide a kernel streaming (KS) minidriver in the video capture category. Media Foundation uses the PnP path to enumerate the device. For audio, Media Foundation uses the Windows Multimedia Device (MMDevice) API to enumerate audio endpoint devices. If the device meets these criteria, there is no need to implement a custom media source.

However, you might want to implement a custom media source for some other type of device or other live data source. There are only a few differences between a live source and other media sources:

-   In the [**IMFMediaSource::GetCharacteristics**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-getcharacteristics) method, return the **MFMEDIASOURCE\_IS\_LIVE** flag.
-   The first sample should have a time stamp of zero.
-   Events and streaming states are handled the same as media sources, with the exception of the paused state.
-   While paused, do not queue samples. Drop any data that is generated while paused.
-   Live sources typically do not support seeking, reverse play, or rate control.

## Related topics

<dl> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Tutorial: Writing a Custom Media Source](tutorial--writing-a-custom-media-source.md)
</dt> </dl>

 

 



