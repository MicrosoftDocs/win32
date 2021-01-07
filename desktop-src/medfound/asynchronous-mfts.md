---
description: This topic describes asynchronous data processing for Media Foundation transforms (MFTs).
ms.assetid: d438ffae-fc50-454f-8ce4-2d6676500fff
title: Asynchronous MFTs
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous MFTs

This topic describes asynchronous data processing for Media Foundation transforms (MFTs).

> [!Note]  
> This topic applies to Windows 7 or later.

 

-   [About Asynchronous MFTs](#about-asynchronous-mfts)
-   [General Requirements](#general-requirements)
-   [Events](#events)
-   [ProcessInput](#processinput)
-   [ProcessOutput](#processoutput)
-   [Draining](#draining)
-   [Flushing](#flushing)
-   [Markers](#markers)
-   [Format Changes](#format-changes)
-   [Attributes](#attributes)
-   [Unlocking Asynchronous MFTs](#unlocking-asynchronous-mfts)
-   [Shutting Down the MFT](#shutting-down-the-mft)
-   [Registration and Enumeration](#registration-and-enumeration)
-   [Related topics](#related-topics)

## About Asynchronous MFTs

When MFTs were introduced in Windows Vista, the API was designed for *synchronous* data processing. In that model, the MFT is always either waiting to get input, or waiting to produce output.

Consider a typical video decoder. To get a decoded frame, the client calls [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput). If the decoder has enough data to decode a frame, **ProcessOutput** blocks while the MFT decodes the frame. Otherwise, **ProcessOutput** returns **MF_E_TRANSFORM_NEED_MORE_INPUT**, indicating that the client should call [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput).

This model works well if the decoder performs all of its decoding operations on one thread. But suppose the decoder uses several threads to decode frames in parallel. For the best performance, the decoder should receive new input whenever a decoding thread becomes idle. But the rate at which threads complete decoding operations will not align exactly with the client's calls to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) and [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput), resulting in threads waiting for work.

Windows 7 introduces event-driven, *asynchronous* processing for MFTs. In this model, whenever the MFT needs input or has output, it sends an event to the client.

## General Requirements

This topic describes how asynchronous MFTs differ from synchronous MFT. Except where noted in this topic, the two processing models are the same. (In particular, format negotiation is the same.)

An asynchronous MFT must implement the following interfaces:

-   [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)
-   [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator)
-   [**IMFShutdown**](/windows/desktop/api/mfidl/nn-mfidl-imfshutdown)

## Events

An asynchronous MFT uses the following events to signal its data-processing status:



| Event                                                    | Description                                                       |
|----------------------------------------------------------|-------------------------------------------------------------------|
| [METransformNeedInput](metransformneedinput.md)         | Sent when the MFT can accept more input.                          |
| [METransformHaveOutput](metransformhaveoutput.md)       | Sent when the MFT has output.                                     |
| [METransformDrainComplete](metransformdraincomplete.md) | Sent when a drain operation completes. See [Draining](#draining). |
| [METransformMarker](metransformmarker.md)               | Sent when a marker is process. See [Markers](#markers).           |



 

These events are sent out-of-band. It is important to understand the difference between in-band and out-of-band events in the context of an MFT.

The original MFT design supports *in-band* events. An in-band event contains information about the data stream, such as information about a format change. The client sends in-band events to the MFT by calling [**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent). The MFT can send in-band events back to the client in the [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method. (Specifically, events are conveyed in the **pEvents** member of the [**MFT_OUTPUT_DATA_BUFFER**](/windows/desktop/api/mftransform/ns-mftransform-mft_output_data_buffer) structure.)

An MFT sends out-of-band events through the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface as follows:

1.  The MFT implements the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface, as described in [Media Event Generators](media-event-generators.md).
2.  The client calls **IUnknown::QueryInterface** on the MFT for the [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. An asynchronous MFT must expose this interface. Synchronous MFTs should not expose this interface.
3.  The client calls [**IMFMediaEventGenerator::BeginGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-begingetevent) and [**IMFMediaEventGenerator::EndGetEvent**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventgenerator-endgetevent) to receive out-of-band events from the MFT.

## ProcessInput

The [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) method is modified as follows:

1.  When streaming starts, the client sends the [**MFT_MESSAGE_NOTIFY_START_OF_STREAM**](mft-message-notify-start-of-stream.md) message.
2.  During streaming, the MFT requests data by sending an [METransformNeedInput](metransformneedinput.md) event. The event data is the stream identifier.
3.  For each [METransformNeedInput](metransformneedinput.md) event, the client calls [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) for the specified stream.
4.  At the end of streaming, the client may call [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT_MESSAGE_NOTIFY_END_OF_STREAM**](mft-message-notify-end-of-stream.md) message.

Implementation notes:

-   The MFT must not send any [METransformNeedInput](metransformneedinput.md) events until it receives the [**MFT_MESSAGE_NOTIFY_START_OF_STREAM**](mft-message-notify-start-of-stream.md) message.
-   During streaming, the MFT may send [METransformNeedInput](metransformneedinput.md) events at any time.
-   The MFT should maintain a count of pending [METransformNeedInput](metransformneedinput.md) events. Any call to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) that does not correspond to an METransformNeedInput event must return **MF_E_NOTACCEPTING**.
-   When the MFT receives the [**MFT_MESSAGE_NOTIFY_END_OF_STREAM**](mft-message-notify-end-of-stream.md) message, it resets the count of pending [METransformNeedInput](metransformneedinput.md) events to zero.
-   The MFT must not send any [METransformNeedInput](metransformneedinput.md) events after it receives the [**MFT_MESSAGE_NOTIFY_END_OF_STREAM**](mft-message-notify-end-of-stream.md) message.
-   If [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) is called before [**MFT_MESSAGE_NOTIFY_START_OF_STREAM**](mft-message-notify-start-of-stream.md) or after [**MFT_MESSAGE_NOTIFY_END_OF_STREAM**](mft-message-notify-end-of-stream.md), the method must return **MF_E_NOTACCEPTING**.

## ProcessOutput

The [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method is modified as follows:

1.  Whenever the MFT has output, it sends an [METransformHaveOutput](metransformhaveoutput.md) event.
2.  For each [METransformHaveOutput](metransformhaveoutput.md) event, the client calls [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput).

Implementation notes:

-   If the client calls [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) at any other time, the method returns **E_UNEXPECTED**.
-   An asynchronous MFT should never return **MF_E_TRANSFORM_NEED_MORE_INPUT** from the [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method. If the MFT requires more input, it sends an [METransformNeedInput](metransformneedinput.md) event.

## Draining

Draining an MFT causes the MFT to produce as much output as it can from whatever input data has already been sent. Draining an asynchronous MFT works as follows:

1.  The client sends the [**MFT_MESSAGE_COMMAND_DRAIN**](mft-message-command-drain.md) message.
2.  The MFT continues to send [METransformHaveOutput](metransformhaveoutput.md) events until it has no more data to process. It does not send [METransformNeedInput](metransformneedinput.md) events during this time.
3.  After the MFT sends the last [METransformHaveOutput](metransformhaveoutput.md) event, it sends an [METransformDrainComplete](metransformdraincomplete.md) event.

After draining is complete, the MFT does not send another [METransformNeedInput](metransformneedinput.md) event until it receives an [**MFT_MESSAGE_NOTIFY_START_OF_STREAM**](mft-message-notify-start-of-stream.md) message from the client.

## Flushing

The client can flush the MFT by sending the [**MFT_MESSAGE_COMMAND_FLUSH**](mft-message-command-flush.md) message. The MFT drops all of the input and output samples it is holding.

The MFT does not send another [METransformNeedInput](metransformneedinput.md) event until it receives an [**MFT_MESSAGE_NOTIFY_START_OF_STREAM**](mft-message-notify-start-of-stream.md) message from the client.

## Markers

The client can mark a point in the stream by sending the [**MFT_MESSAGE_COMMAND_MARKER**](mft-message-command-marker.md) message. The MFT responds as follows:

1.  The MFT generates as many output samples as it can from the existing input data, sending an [METransformHaveOutput](metransformhaveoutput.md) event for each output sample.
2.  After all of the output is generated, the MFT sends an [METransformMarker](metransformmarker.md) event. This event must be sent after all of the [METransformHaveOutput](metransformhaveoutput.md) events.

For example, suppose that a decoder has enough input data to produce four output samples. If the client sends the [**MFT_MESSAGE_COMMAND_MARKER**](mft-message-command-marker.md) message, the MFT will queue four [METransformHaveOutput](metransformhaveoutput.md) events (one per output sample), followed by an [METransformMarker](metransformmarker.md) event.

The marker message is similar to the drain message. However, a drain is considered a break in the stream, whereas a marker is not. Draining and markers have the following differences.

Draining:

-   While draining, the MFT does not send [METransformNeedInput](metransformneedinput.md) events.
-   The MFT discards any input data that cannot be used to create an output sample.
-   Some MFTs produce a "tail" at the end of the data. For example, audio effects such as reverb or echo produce extra data after the input data has stopped. An MFT that generates a tail should do so at the end of a drain operation.
-   After the MFT has finished draining, it marks the next output sample with the [**MFSampleExtension_Discontinuity**](mfsampleextension-discontinuity-attribute.md) attribute, to indicate a discontinuity in the stream.

Marker:

-   The MFT continues to send [METransformNeedInput](metransformneedinput.md) events before sending the marker event.
-   The MFT does not discard any input data. If there is partial data, it should be processed after the marker point.
-   The MFT does not produce a tail at the marker point.
-   The MFT does not set the discontinuity flag after the marker point.

## Format Changes

An asynchronous MFT must support dynamic format changes, as described in [Handling Stream Changes](handling-stream-changes.md).

## Attributes

An asynchronous MFT must implement the [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) method to return a valid attribute store. The following attributes apply to asynchronous MFTs:



| Attribute                                                                                    | Description                                                                                                                       |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [MF_TRANSFORM_ASYNC](mf-transform-async.md)                                               | The MFT must set this attribute to **TRUE** (1). The client can query this attribute to discover whether the MFT is asynchronous. |
| [MF_TRANSFORM_ASYNC_UNLOCK](mf-transform-async-unlock.md)                                |                                                                                                                                   |
| [**MFT_SUPPORT_DYNAMIC_FORMAT_CHANGE**](mft-support-dynamic-format-change-attribute.md) | The MFT must set this attribute to **TRUE** (1). The client can assume that this attribute is set.                                |



 

## Unlocking Asynchronous MFTs

Asynchronous MFTs are not compatible with the original MFT data processing model. To prevent asynchronous MFTs from breaking existing applications, the following mechanism is defined:

<dl> The client calls <a href="/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes">IMFTransform::GetAttributes</a> on the MFT.  
The client queries the for this <a href="mf-transform-async.md">MF_TRANSFORM_ASYNC</a> attribute. For an asynchronous MFT, the value of this attribute is **TRUE**.  
To unlock the MFT, the client must sets the <a href="mf-transform-async-unlock.md">MF_TRANSFORM_ASYNC_UNLOCK</a> attribute to **TRUE**.  
</dl>

Until the client unlocks the MFT, all [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) methods should return **MF_E_TRANSFORM_ASYNC_LOCKED**, with the following exceptions:

-   [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes) (all asynchronous MFTs)
-   [**IMFTransform::GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype) (all asynchronous MFTs)
-   [**IMFTransform::GetOutputCurrentType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputcurrenttype) (encoders only)
-   [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) (encoders only)
-   [**IMFTransform::GetStreamCount**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamcount) (all asynchronous MFTs)
-   [**IMFTransform::GetStreamIDs**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamids) (all asynchronous MFTs)

The following code shows how to unlock an asynchronous MFT:


```C++
HRESULT UnlockAsyncMFT(IMFTransform *pMFT)
{
    IMFAttributes *pAttributes = NULL;

    HRESULT hr = hr = pMFT->GetAttributes(&pAttributes);

    if (SUCCEEDED(hr))
    {
        hr = pAttributes->SetUINT32(MF_TRANSFORM_ASYNC_UNLOCK, TRUE);
        pAttributes->Release();
    }
    
    return hr;
}
```



## Shutting Down the MFT

Asynchronous MFTs must implement the [**IMFShutdown**](/windows/desktop/api/mfidl/nn-mfidl-imfshutdown) interface.

-   [**Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfshutdown-shutdown): The MFT must shut down its event queue. If using the standard event queue, call [**IMFMediaEventQueue::Shutdown**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediaeventqueue-shutdown). Optionally, the MFT may release other resources. The client must not use the MFT after calling **Shutdown**.
-   [**GetShutdownStatus**](/windows/desktop/api/mfidl/nf-mfidl-imfshutdown-getshutdownstatus): After [**Shutdown**](/windows/desktop/api/mfidl/nf-mfidl-imfshutdown-shutdown) has been called, the MFT should return the value **MFSHUTDOWN_COMPLETED** in the *pStatus* parameter. It should not return the value **MFSHUTDOWN_INITIATED**.

## Registration and Enumeration

To register an asynchronous MFT, call the [**MFTRegister**](/windows/desktop/api/mfapi/nf-mfapi-mftregister) function and set the **MFT_ENUM_FLAG_ASYNCMFT** flag in the *Flags* parameter. (Previously this flag was reserved.)

To enumerate asynchronous MFTs, call the [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function and set the **MFT_ENUM_FLAG_ASYNCMFT** flag in the *Flags* parameter. For backward compatibility, the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) function does not enumerate asynchronous MFTs. Otherwise, installing an asynchronous MFT on the user's computer could break existing applications.

## Related topics

<dl> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 



