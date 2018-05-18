---
Description: 'Media sinks are the pipeline objects that receive media data.'
ms.assetid: '65bb8822-5eb0-46a3-ab9e-c55ae466e982'
title: Media Sinks
---

# Media Sinks

*Media sinks* are the pipeline objects that receive media data. A media sink is the destination for one or more media streams. Media sinks fall into two general categories:

-   A *renderer* is a media sink that presents data for playback. The enhanced video renderer (EVR) displays video frames, and the audio renderer plays audio streams through the sound card or other audio device.

-   An *archive sink* is a media sink that writes data to a file or other storage.

The main difference between them is that an archive sink does not consume the data at a fixed playback rate. Instead, it writes the data that it receives as quickly as possible.

Media sinks expose the [**IMFMediaSink**](imfmediasink.md) interface. Each media sink contains one or more *stream sinks*. Each stream sink receives the data from one stream. Stream sinks expose the [**IMFStreamSink**](imfstreamsink.md) interface. Typically an application does not create media sinks directly. Instead, the application creates one or more activation objects, which the Media Session uses to create the sink. All other operations on the sink are handled by the Media Session, and the application does not call any methods on the media sink or any of the stream sinks. For more information about activation objects, see [Activation Objects](activation-objects.md).

You should read the remainder of this topic if you are writing a custom media sink, or if you want to use a media sink directly without the Media Session.

-   [Stream Sinks](#stream-sinks)
-   [Presentation Clock](#presentation-clock)
-   [Stream Formats](#stream-formats)
-   [Data Flow](#data-flow)
-   [Markers](#markers)
-   [State Changes](#state-changes)
-   [Finalizing](#finalizing)
-   [Shutting Down](#shutting-down)
-   [Media Sink Interfaces](#media-sink-interfaces)
-   [Stream Sink Interfaces](#stream-sink-interfaces)
-   [Stream Sink Events](#stream-sink-events)
-   [Related topics](#related-topics)

## Stream Sinks

A media sink can have a fixed number of stream sinks, or it can support adding and removing stream sinks. If it has a fixed number of stream sinks, the [**IMFMediaSink::GetCharacteristics**](imfmediasink-getcharacteristics.md) method returns the MEDIASINK\_FIXED\_STREAMS flag. Otherwise, you can add and remove stream sinks. To add a new stream sink, call [**IMFMediaSink::AddStreamSink**](imfmediasink-addstreamsink.md). To remove a stream sink, call [**IMFMediaSink::RemoveStreamSink**](imfmediasink-removestreamsink.md). The MEDIASINK\_FIXED\_STREAMS flag indicates that the media sink does not support these two methods. (It might support some other way to configure the number of streams, for example by setting initialization parameters when the sink is created.) The list of stream sinks is ordered. To enumerate them by index value, call the [**IMFMediaSink::GetStreamSinkByIndex**](imfmediasink-getstreamsinkbyindex.md) method.

Stream sinks also have identifiers. Stream identifiers are unique within the media sink, but do not have to be consecutive. Depending on the media sink, the stream identifiers might have some meaning that is related to the content. For example, an archive sink might write the stream identifiers into the file header. Otherwise, they are arbitrary. To get a stream sink by its identifier, call [**IMFMediaSink::GetStreamSinkById**](imfmediasink-getstreamsinkbyid.md).

## Presentation Clock

The rate at which a media sink consumes samples is controlled by the [Presentation Clock](presentation-clock.md). The Media Session selects the presentation clock and sets it on the media sink by calling the media sink's [**IMFMediaSink::SetPresentationClock**](imfmediasink-setpresentationclock.md) method. The presentation clock must be set on the media sink before streaming can begin. Every media sink requires a presentation clock to run. The media sink uses the presentation clock for two purposes:

-   To receive notifications when streaming starts or stops. The media sink receives these notifications through the [**IMFClockStateSink**](imfclockstatesink.md) interface, which all media sinks must implement.

-   To determine when it should render samples. When the media sink receives a new sample, it gets the time stamp from the sample and tries to render the sample at that presentation time.

The presentation clock derives its clock times from another object called the *presentation time source*. Presentation time sources expose the [**IMFPresentationTimeSource**](imfpresentationtimesource.md) interface. Some media sinks have access to an accurate clock, so they expose this interface. This means that a media sink might schedule samples against a time provided by its own clock. However, the media sink cannot assume this to be the case. It must always use the time from the presentation clock, regardless of whether the presentation clock is driven by the media sink itself, or by some other clock.

If a media sink cannot match rates with a clock other than its own, the [**GetCharacteristics**](imfmediasink-getcharacteristics.md) method returns the MEDIASINK\_CANNOT\_MATCH\_CLOCK flag. If this flag is present and the presentation clock uses a different presentation time source, the media sink is likely to perform poorly. For example, it might glitch during playback.

A *rateless* sink is a media sink that ignores the time stamps on samples and consumes data as soon as each sample arrives. A rateless media sink returns the MEDIASINK\_RATELESS flag from the [**GetCharacteristics**](imfmediasink-getcharacteristics.md) method. Typically this flag applies to archive sinks. If every media sink in the pipeline is rateless, the Media Session uses a special rateless presentation clock. This clock runs as quickly as the sinks consume samples.

## Stream Formats

Before the media sink can receive samples, the client must set the media type on the stream sinks. To set the media type, call the stream sink's [**IMFStreamSink::GetMediaTypeHandler**](imfstreamsink-getmediatypehandler.md) method. This method returns a pointer to the [**IMFMediaTypeHandler**](imfmediatypehandler.md) interface. Use this interface to get the list of preferred media types, get the current media type, and set the media type.

To get the list of preferred media types, call [**IMFMediaTypeHandler::GetMediaTypeByIndex**](imfmediatypehandler-getmediatypebyindex.md). The preferred types should be taken as a hint to the client. The list might be incomplete or include partial media types. A partial media type is one that does not have all of the attributes needed to describe a valid format. For example, a partial video type might specify the color space and bit depth but not the image width or height. A partial audio type might specify the compression format and the sample rate but not the number of audio channels.

To get the stream sink's current media type, call [**IMFMediaTypeHandler::GetCurrentMediaType**](imfmediatypehandler-getcurrentmediatype.md). When a stream sink is first created, it might have a default media type already set, or it might have no media type until the client sets one.

To set the media type, call [**IMFMediaTypeHandler::SetCurrentMediaType**](imfmediatypehandler-setcurrentmediatype.md). Some stream sinks might not support changing the type after is has been set. Therefore, it useful to test media types before setting them. To test whether the media sink will accept a media type, (without setting the type), call [**IMFMediaTypeHandler::IsMediaTypeSupported**](imfmediatypehandler-ismediatypesupported.md).

## Data Flow

Media sinks use a *pull model*, which means that the stream sinks request data as they need it. The client should respond in a timely manner to avoid any glitching.

Some media sinks support *prerolling*. Prerolling is the process of giving data to the media sink before the presentation clock starts. If a media sink supports prerolling, the media sink exposes the [**IMFMediaSinkPreroll**](imfmediasinkpreroll.md) interface, and the [**GetCharacteristics**](imfmediasink-getcharacteristics.md) method returns the MEDIASINK\_CAN\_PREROLL flag. Prerolling ensures that the media sink is ready to present the first sample when the presentation clock starts. It is recommended that the client always preroll if the media sink supports it, because it can prevent glitching or gaps during playback.

Data flow to a media sink works as follows:

1.  The client sets the media types and the presentation clock. The media sink registers itself with the presentation clock to receive notifications about clock state changes.
2.  Optionally, the client queries for [**IMFMediaSinkPreroll**](imfmediasinkpreroll.md). If the media sink exposes this interface, the client calls [**IMFMediaSinkPreroll::NotifyPreroll**](imfmediasinkpreroll-notifypreroll.md). Otherwise, the client skips to step 5.
3.  Each stream sink sends one or more [MEStreamSinkRequestSample](mestreamsinkrequestsample.md) events. In response to each of these events, the client gets the next sample of data for that stream and calls [**IMFStreamSink::ProcessSample**](imfstreamsink-processsample.md).
4.  When each stream sink receives enough preroll data, it sends an [MEStreamSinkPrerolled](mestreamsinkprerolled.md) event.
5.  The client calls [**IMFPresentationClock::Start**](imfpresentationclock-start.md) to start the presentation clock.
6.  The presentation clock notifies the media sink that the clock is starting, by calling [**IMFClockStateSink::OnClockStart**](imfclockstatesink-onclockstart.md).
7.  To get more data, each stream sink sends [MEStreamSinkRequestSample](mestreamsinkrequestsample.md) events. In response to each of these events, the client gets the next sample and calls [**ProcessSample**](imfstreamsink-processsample.md). This step is repeated until the presentation ends.

Most media sinks process samples asynchronously, so the stream sinks can send out more than one sample request at a time.

During streaming, the client can call [**IMFStreamSink::PlaceMarker**](imfstreamsink-placemarker.md) and [**IMFStreamSink::Flush**](imfstreamsink-flush.md) at any time. Markers are described in the next section. Flushing causes the stream sink to drop any samples that it has queued but not rendered yet.

## Markers

Markers provide a way for the client to indicate specific points in the stream. A marker consists of the following information:

-   The marker type, defined as a member of the [**MFSTREAMSINK\_MARKER\_TYPE**](mfstreamsink-marker-type.md) enumeration.
-   Data associated with the marker. The meaning of the data depends on the marker type. Some marker types do not have data.
-   Optional data for the client's own use.

To place a marker, the client calls [**IMFStreamSink::PlaceMarker**](imfstreamsink-placemarker.md). The stream sink finishes processing any samples that it received before the **PlaceMarker** call, and then sends an [MEStreamSinkMarker](mestreamsinkmarker.md) event.

Most media sinks keep a queue of pending samples, which they process asynchronously. Marker events must be serialized with sample processing, so the media sink should place the markers in the same queue. For example, suppose the client makes the following method calls:

1.  [**ProcessSample**](imfstreamsink-processsample.md) (Sample \#1)
2.  [**ProcessSample**](imfstreamsink-processsample.md) (Sample \#2)
3.  [**PlaceMarker**](imfstreamsink-placemarker.md) (Marker \#1)
4.  [**ProcessSample**](imfstreamsink-processsample.md) (Sample \#3)
5.  [**PlaceMarker**](imfstreamsink-placemarker.md) (Marker \#2)

In this example, the stream sink must send the [MEStreamSinkMarker](mestreamsinkmarker.md) event for marker \#1 after it processes sample \#2, and the event for marker \#2 after it processes sample \#3.

If the client flushes a stream sink, the stream sink immediately processes any markers that were in the queue. It sets the status code to E\_ABORT on these events.

Some markers contain information that is relevant to the media sink:

-   **MFSTREAMSINK\_MARKER\_TICK**: Indicates there is a gap in the stream. The next sample will be a discontinuity.
-   **MFSTREAMSINK\_MARKER\_ENDOFSEGMENT**: Indicates the end of a segment or the end of a stream. The next sample (if any) might be a discontinuity.
-   **MFSTREAMSINK\_MARKER\_EVENT**: Contains an event. Depending on the event type and the implementation of the media sink, the media sink might handle the event or ignore it.

## State Changes

A media sink is notified of state changes in the presentation clock through the media sink's [**IMFClockStateSink**](imfclockstatesink.md) interface. When the client sets the presentation clock, the media sink calls [**IMFPresentationClock::AddClockStateSink**](imfpresentationclock-addclockstatesink.md) to register itself for notifications from the clock. The following table summarizes how a media sink behaves in response to clock state changes.



| Clock state change                                         | Sample processing                                                                                                                                                                                                                                             | Marker processing                                                                                                                                                                                   |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnClockStart**](imfclockstatesink-onclockstart.md)     | Process samples whose time stamp is equal to or later than the clock start time.                                                                                                                                                                              | Send the [MEStreamSinkMarker](mestreamsinkmarker.md) event when all of the samples received before the marker have been processed.                                                                 |
| [**OnClockPause**](imfclockstatesink-onclockpause.md)     | The media sink can fail [**ProcessSample**](imfstreamsink-processsample.md) while paused.<br/> If the media sink accepts samples while paused, it must queue them until the clock restarts. Do not process any queued samples while paused.<br/> | If there are queued samples, put markers onto the same queue. Send the marker event when the clock restarts.<br/> Otherwise, send the marker event immediately.<br/>                    |
| [**OnClockRestart**](imfclockstatesink-onclockrestart.md) | Process any samples that were queued while paused, and then treat the same as [**OnClockStart**](imfclockstatesink-onclockstart.md).                                                                                                                         | Send [MEStreamSinkMarker](mestreamsinkmarker.md) events for queued markers (serialized with sample processing), and then treat the same as [**OnClockStart**](imfclockstatesink-onclockstart.md). |
| [**OnClockStop**](imfclockstatesink-onclockstop.md)       | Drop all queued samples. Further calls to [**ProcessSample**](imfstreamsink-processsample.md) can fail.                                                                                                                                                      | Send queued marker events. On subsequent calls to [**PlaceMarker**](imfstreamsink-placemarker.md), send the marker event immediately.                                                              |



 

In addition, stream sinks must send the following events when they have completed the state transitions:

-   [**OnClockStart**](imfclockstatesink-onclockstart.md), [**OnClockRestart**](imfclockstatesink-onclockrestart.md): [MEStreamSinkStarted](mestreamsinkstarted.md) event
-   [**OnClockPause**](imfclockstatesink-onclockpause.md): [MEStreamSinkPaused](mestreamsinkpaused.md) event
-   [**OnClockStop**](imfclockstatesink-onclockstop.md): [MEStreamSinkStopped](mestreamsinkstopped.md) event

## Finalizing

Some media sinks require an extra processing step after the last sample is delivered. Typically this requirement applies to archive sinks, which must write headers or indexes into the file. If a media sink requires any final processing, it exposes the [**IMFFinalizableMediaSink**](imffinalizablemediasink.md) interface.

After the client delivers the last sample, the client queries for this interface. If the media sink supports the interface, the client calls [**IMFFinalizableMediaSink::BeginFinalize**](imffinalizablemediasink-beginfinalize.md) to perform the final processing asynchronously. This method follows the standard Media Foundation asynchronous model, described in [Asynchronous Callback Methods](asynchronous-callback-methods.md). The media sink can assume that the client will call **BeginFinalize**. Failure to call **BeginFinalize** can result in an incorrectly authored file.

## Shutting Down

When the client is done using the media sink, the client calls [**IMFMediaSink::Shutdown**](imfmediasink-shutdown.md). Inside this method, the media sink should break any circular reference counts. Typically, there will be circular references between the media sink and the stream sinks.

If you are using the event queue helper object to implement [**IMFMediaEventGenerator**](imfmediaeventgenerator.md), call [**IMFMediaEventQueue::Shutdown**](imfmediaeventqueue-shutdown.md) on the event queue. This method shuts down the event queue and signals any caller that is currently waiting for an event.

After shutdown, all methods on the media sink return MF\_E\_SHUTDOWN, with the exception of **IUnknown** methods.

## Media Sink Interfaces

The following table lists the standard interfaces that media sinks can expose through **QueryInterface**. Media sinks can also expose custom interfaces.



| Interface                                                      | Description                                                                                   |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| [**IMFMediaSink**](imfmediasink.md)                           | The primary interface for media sinks. (Required.)                                            |
| [**IMFClockStateSink**](imfclockstatesink.md)                 | Used to notify the media sink when presentation clock changes state. (Required.)              |
| [**IMFFinalizableMediaSink**](imffinalizablemediasink.md)     | Implement if the media sink must perform a final processing step. (Optional.)                 |
| [**IMFGetService**](imfgetservice.md)                         | Implement if the media sink exposes any service interfaces. (Optional.)                       |
| [**IMFMediaEventGenerator**](imfmediaeventgenerator.md)       | Implement if the media sink sends any events. (Optional.)                                     |
| [**IMFMediaSinkPreroll**](imfmediasinkpreroll.md)             | Implement if the media sink supports preroll. (Optional.)                                     |
| [**IMFPresentationTimeSource**](imfpresentationtimesource.md) | Implement if the media sink can provide a time source for the presentation clock. (Optional.) |
| [**IMFQualityAdvise**](imfqualityadvise.md)                   | Implement if the media sink can adjust playback quality. (Optional.)                          |



 

Optionally, a media sink can implement the following interface as a service.



| Service interface                        | Description                                    |
|------------------------------------------|------------------------------------------------|
| [**IMFRateSupport**](imfratesupport.md) | Reports the range of supported playback rates. |



 

For more information about service interfaces and [**IMFGetService**](imfgetservice.md), see [Service Interfaces](service-interfaces.md).

## Stream Sink Interfaces

Stream sinks must expose the following interfaces through **QueryInterface**.



| Interface                                                | Description                                                                                              |
|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**IMFStreamSink**](imfstreamsink.md)                   | The primary interface for stream sinks. (Required.)                                                      |
| [**IMFMediaEventGenerator**](imfmediaeventgenerator.md) | Queues events. The [**IMFStreamSink**](imfstreamsink.md) interface inherits this interface. (Required.) |



 

Currently no service interfaces are defined for stream sinks.

## Stream Sink Events

The following table lists the events that are defined for generic stream sinks. Stream sinks can also send custom events not listed here.



| Event                                                                  | Description                                                  |
|------------------------------------------------------------------------|--------------------------------------------------------------|
| [MEStreamSinkFormatChanged](mestreamsinkformatchanged.md)             | The stream sink's media type is no longer valid. (Optional.) |
| [MEStreamSinkMarker](mestreamsinkmarker.md)                           | A marker was processed. (Required.)                          |
| [MEStreamSinkPaused](mestreamsinkpaused.md)                           | The stream sink has paused. (Required.)                      |
| [MEStreamSinkPrerolled](mestreamsinkprerolled.md)                     | Preroll is complete. (Optional.)                             |
| [MEStreamSinkRateChanged](mestreamsinkratechanged.md)                 | The stream sink has changed playback rate. (Optional.)       |
| [MEStreamSinkRequestSample](mestreamsinkrequestsample.md)             | A new sample is requested. (Required.)                       |
| [MEStreamSinkScrubSampleComplete](mestreamsinkscrubsamplecomplete.md) | A scrub request was completed. (Optional.)                   |
| [MEStreamSinkStarted](mestreamsinkstarted.md)                         | The stream sink has started. (Required.)                     |
| [MEStreamSinkStopped](mestreamsinkstopped.md)                         | The stream sink has stopped. (Required.)                     |



 

Currently no general-purpose events are defined for media sinks. Some media sinks might send custom events.

## Related topics

<dl> <dt>

[Media Foundation Pipeline](media-foundation-pipeline.md)
</dt> <dt>

[Media Foundation Architecture](media-foundation-architecture.md)
</dt> </dl>

 

 




