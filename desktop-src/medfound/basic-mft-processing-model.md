---
description: This topic describes how a client uses a Media Foundation transform (MFT) to process data. The client is anything that directly calls methods on the MFT. This might be the application or the Media Foundation pipeline.
ms.assetid: be977d75-999e-4e57-9672-00a89246a2c1
title: Basic MFT Processing Model
ms.topic: article
ms.date: 05/31/2018
---

# Basic MFT Processing Model

This topic describes how a client uses a Media Foundation transform (MFT) to process data. The *client* is anything that directly calls methods on the MFT. This might be the application or the Media Foundation pipeline.

Read this topic if you are:

-   Writing an application that makes direct calls to one or more MFTs.
-   Writing a custom MFT and want to understand the expected behavior of an MFT.

This topic describes a *synchronous* processing model. In this model, all data-processing methods block until they complete. MFTs can also support an *asynchronous* model, which is described in the topic [Asynchronous MFTs](asynchronous-mfts.md).

-   [Basic Processing Model](#basic-processing-model)
    -   [Create the MFT](#create-the-mft)
    -   [Get Stream Identifiers](#get-stream-identifiers)
    -   [Set Media Types](#set-media-types)
    -   [Get Buffer Requirements](#get-buffer-requirements)
    -   [Process Data](#process-data)
-   [Extensions to the Basic Model](#extensions-to-the-basic-model)
-   [IMF2DBuffer](#imf2dbuffer)
-   [Flushing an MFT](#flushing-an-mft)
-   [Draining an MFT](#draining-an-mft)
-   [Sample Attributes](#sample-attributes)
-   [Discontinuities](#discontinuities)
-   [Dynamic Format Changes](#dynamic-format-changes)
-   [Stream Events](#stream-events)
-   [Related topics](#related-topics)

## Basic Processing Model

### Create the MFT

There are several ways to create an MFT:

-   Call the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) function.
-   Call the [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function.
-   If you already know the CLSID of the MFT, simply call **CoCreateInstance**.

Some MFTs might provide other options, such as a specialized creation function.

### Get Stream Identifiers

An MFT has one or more *streams*. Input streams receive input data, and output streams generate output data. Streams are not represented as distinct objects. Instead, various MFT methods take stream identifiers as parameters.

Some MFTs allow the client to add or remove input streams. During streaming, an MFT can add or remove output streams. (The client cannot add or remove output streams.)

1.  (Optional.) Call [**IMFTransform::GetStreamLimits**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamlimits) to get the minimum and maximum number of streams that the MFT can support. If the minimum and maximum are the same, the MFT has a fixed number of streams.
2.  Call [**IMFTransform::GetStreamCount**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamcount) to get the initial number of streams.
3.  Call [**IMFTransform::GetStreamIDs**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamids) to get the stream identifiers. If this method returns E\_NOTIMPL, it means the MFT has a fixed number of streams, and the stream identifiers are consecutive starting from zero.
4.  (Optional.) If the MFT does not have a fixed number of streams, call [**IMFTransform::AddInputStreams**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-addinputstreams) to add more input streams, or [**IMFTransform::DeleteInputStream**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-deleteinputstream) to remove input streams. (You cannot add or remove output streams.)

### Set Media Types

Before an MFT can process data, the client must set a media types for each of the streams of the MFT. An MFT might require that the client set the input types before setting the output types, or might require the opposite order (output types first). Some MFTs do not have a requirement on the order.

An MFT can provide a list of preferred media types for a stream. Also, MFTs can indicate the general formats that they support by adding this information to the registry.

To set the media types, do the following:

1.  (Optional.) For each input stream, call [**IMFTransform::GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype) to get the list of preferred types for that stream.
    -   If this method returns MF\_E\_TRANSFORM\_TYPE\_NOT\_SET, you must set the output types first; skip to step 3.
    -   If the method returns E\_NOTIMPL, the MFT does not have a list of preferred input types; skip to step 2.
2.  For each input stream, call [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) to set the input type. You can use a media type from step 1, or a type that describes your input data. If any stream returns MF\_E\_TRANSFORM\_TYPE\_NOT\_SET, skip to step 3.
3.  (Optional.) For each output stream, call [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) to get a list of preferred types for that stream.
    -   If this method returns MF\_E\_TRANSFORM\_TYPE\_NOT\_SET, you must set the input types first; go back to step 1.
    -   If any stream returns E\_NOTIMPL, the MFT does not have a list of preferred output types; skip to step 4.
4.  For each output stream, call [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) to set the output type. You can use a media type from step 3, or a type that describes your required output format.
5.  If any input streams do not have a media type, go back to step 1.

### Get Buffer Requirements

After the client sets the media types, it should get the buffer requirements for each stream:

-   For each input stream, call [**IMFTransform::GetInputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreaminfo).
-   For each output stream, call [**IMFTransform::GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo).

### Process Data

An MFT is designed to be a reliable state machine. It does not make any calls back to the client.

1.  Call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING**](mft-message-notify-begin-streaming.md) message. This message requests the MFT to allocate any resources it needs during streaming.
2.  Call [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) on at least one input stream to deliver an input sample to the MFT.
3.  (Optional.) Call [**IMFTransform::GetOutputStatus**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstatus) to query whether the MFT can generate an output sample. If the method returns S\_OK, check the *pdwFlags* parameter. If *pdwFlags* contains the **MFT\_OUTPUT\_STATUS\_SAMPLE\_READY** flag, go to step 4. If *pdwFlags* is zero, go back to step 2. If the method returns E\_NOTIMPL, go to step 4.
4.  Call [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) to get output data.
    -   If the method returns **MF\_E\_TRANSFORM\_NEED\_MORE\_INPUT**, it means the MFT requires more input data; go back to step 2.
    -   If the method returns **MF\_E\_TRANSFORM\_STREAM\_CHANGE**, it means the number of output streams has changed, or the output format has changed. The client might need to query for new stream identifiers or set new media types. For more information, see the documentation for [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput).
5.  If there is still input data to process, go to step 2. If the MFT has consumed all of the available input data, proceed to step 6.
6.  Call [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_NOTIFY\_END\_OF\_STREAM**](mft-message-notify-end-of-stream.md) message.
7.  Call [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message.
8.  Call [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) to get the remaining output. Repeat this step until the method returns **MF\_E\_TRANSFORM\_NEED\_MORE\_INPUT**. This return value signals that all of the output has been drained from the MFT. (Do not treat this as an error condition.)

The sequence described here keeps as little data as possible in the MFT. After every call to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput), the client attempts to get output. Several input samples might be needed to produce one output sample, or a single input sample might generate several output samples. The optimal behavior for the client is to pull output samples from the MFT until the MFT requires more input.

However, the MFT should be able to handle a different order of method calls by the client. For example, the client might simply alternate between calls to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) and [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput). The MFT should restrict the amount of input that it gets by returning **MF\_E\_NOTACCEPTING** from **ProcessInput** whenever it has some output to produce.

The order of method calls described here is not the only valid sequence of events. For example, steps 3 and 4 assume that the client starts with the input types and then tries the output types. The client can also reverse this order and start with the output types. In either case, if the MFT requires the opposite order, it should return the error code MF\_E\_TRANSFORM\_TYPE\_NOT\_SET.

The client can call informational methods, such as [**GetInputCurrentType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputcurrenttype) and [**GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo), at any time during streaming. The client can also attempt to change the media types at any time. The MFT should return an error code if this is not a valid operation. In short, MFTs should assume very little about the order of operations, other than what is documented in the calls themselves.

The following diagram shows a flow chart of the procedures described in this topic.

![flow chart that leads from get stream identifiers through loops that set input types, get input, and process output](images/mft-processing.gif)

## Extensions to the Basic Model

Optionally, an MFT can support some extensions to the basic streaming model.

-   Lazy-read streams. If the [**IMFTransform::GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo) method returns the **MFT\_OUTPUT\_STREAM\_LAZY\_READ** flag for an output stream, the client does not have to collect data from that output stream. The MFT continues to accept input, and at some point the MFT will discard the output data from that stream. If all of the output streams have this flag, the MFT will never fail to accept input. An example might be a visualization transform, where the client gets the output only when it has spare CPU cycles to draw the visualization.
-   Discardable streams. If the [**GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo) method returns the **MFT\_OUTPUT\_STREAM\_DISCARDABLE** flag for an output stream, the client can request the MFT to discard output, but the MFT will not discard any output unless requested. When the MFT reaches its maximum input buffer, the client must either collect some output data or request the MFT to discard the output.
-   Optional streams. If the [**GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo) method returns the **MFT\_OUTPUT\_STREAM\_OPTIONAL** flag for an output stream, or the [**IMFTransform::GetInputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreaminfo) method returns the **MFT\_INPUT\_STREAM\_OPTIONAL** flag for an input stream, that stream is optional. The client does not have to set a media type on the stream. If the client does not set the type, the stream is deselected. A deselected output stream does not produce samples, and the client does not provide a buffer for the stream when it calls [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput). A deselected input stream does not accept input data. An MFT can mark all of its input and output streams as optional. However, it is expected that at least one input and one output must be selected for the MFT to work.
-   Asynchronous processing. The asynchronous processing model was introduced in Windows 7. It is described in the topic [Asynchronous MFTs](asynchronous-mfts.md).

## IMF2DBuffer

If an MFT processes uncompressed video data, it should use the [**IMF2DBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer) interface to manipulate the sample buffers. To get this interface, query the [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface on any input or output buffer. Not using this interface when it is available may result in additional buffer copies. To make proper use of this interface, the transform should not lock the buffer using the **IMFMediaBuffer** interface when **IMF2DBuffer** is available.

For more information about processing video data, see [Uncompressed Video Buffers](uncompressed-video-buffers.md).

## Flushing an MFT

*Flushing* an MFT causes the MFT to discard all of its input data. This can cause a break in the output stream. A client would typically flush an MFT before seeking to a new point in the input stream or switching to a new input stream, when the client does not care about losing data.

To flush an MFT, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_COMMAND\_FLUSH**](mft-message-command-flush.md) message.

## Draining an MFT

*Draining* an MFT causes the MFT to produce as much output as it can from whatever input data has already been sent. If the MFT cannot produce a complete output sample from the available input, it will drop input data. A client would typically drain an MFT when it reached the end of the source stream, or immediately before a format change in the source stream. To drain an MFT, do the following:

1.  Call [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message. This message notifies the MFT that it should deliver as much output data as it can from the input data that has already been sent.
2.  Call [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) to get output data, until the method returns **MF\_E\_TRANSFORM\_NEED\_MORE\_INPUT**.

While the MFT is being drained, it will not accept any more input.

## Sample Attributes

The input samples might have attributes that must be copied to the corresponding output samples.

-   If the MFT returns **VARIANT\_TRUE** for the [**MFPKEY\_EXATTRIBUTE\_SUPPORTED**](mfpkey-exattribute-supported-property.md) property, the MFT must copy the attributes.
-   If the [**MFPKEY\_EXATTRIBUTE\_SUPPORTED**](mfpkey-exattribute-supported-property.md) property is either **VARIANT\_FALSE** or is not set, the client must copy the attributes.

For an MFT with one input and one output, you can use the following general rule:

-   If each input sample produces exactly one output sample, you can let the client copy the attributes. Leave the [**MFPKEY\_EXATTRIBUTE\_SUPPORTED**](mfpkey-exattribute-supported-property.md) property unset.
-   If there is not a one-to-one correspondence between input samples and output samples, the MFT must determine the correct attributes for output samples. Set the [**MFPKEY\_EXATTRIBUTE\_SUPPORTED**](mfpkey-exattribute-supported-property.md) property to **VARIANT\_TRUE**.

## Discontinuities

A discontinuity is a break in an audio or video stream. Discontinuities can be caused by dropped packets on a network connection, corrupt file data, a switch from one source stream to another, or a wide range of other causes. Discontinuities are signaled by setting the [**MFSampleExtension\_Discontinuity**](mfsampleextension-discontinuity-attribute.md) attribute on the first sample after the discontinuity. It is not possible to signal a discontinuity in the middle of a sample. Therefore, any discontinuous data should be sent in separate samples.

Some transforms, especially those that handle uncompressed data, such as audio and video effects, should ignore discontinuities when they process input data. These MFTs are generally designed to handle continuous data, and should treat any data they receive as continuous, even after a discontinuity.

If an MFT ignores a discontinuity on input data, it should still set the discontinuity flag on the output sample, if the output sample has the same time stamp as the input sample. If the output sample has a different time stamp, however, the MFT should not propagate the discontinuity. (This would be the case in some audio resamplers, for example.) A discontinuity at the wrong place in the stream is worse than no discontinuity.

Most decoders cannot ignore discontinuities, because a discontinuity affects the interpretation of the next sample. Any encoding technology that uses inter-frame compression, such as MPEG-2, falls into this category. Some encoding schemes use only intra-frame compression, such as DV and MJPEG. These decoders can safely ignore discontinuities.

Transforms that respond to discontinuities should generally output as much of the data before the discontinuity as they can, and discard the rest. The input sample with the discontinuity flag should be processed as though it were the first sample in the stream. (This behavior matches what is specified for the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message.) However, the exact details will depend on the media format.

If a decoder does nothing to mitigate a discontinuity, it should copy the discontinuity flag to the output data. Demultiplexers and other MFTs that work entirely with compressed data must copy any discontinuities to their output streams. Otherwise, the downstream components may not be able to decode the compressed data correctly. In general, it is almost always correct to pass discontinuities downstream, unless the MFT contains explicit code to smooth out discontinuities.

## Dynamic Format Changes

Formats can change during streaming. For example, aspect ratio can change in the middle of a video stream.

For details about how stream changes are handled by an MFT, see [Handling Stream Changes](handling-stream-changes.md).

## Stream Events

To send an event to an MFT, call [**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent). If the method returns **MF\_S\_TRANSFORM\_DO\_NOT\_PROPAGATE\_EVENT**, the MFT will return the event to the caller on a subsequent call to [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput). If the method returns any other **HRESULT** value, the MFT will not return the event to the client in **ProcessOutput**. In that case, the client is responsible for propagating the event downstream to the next component in the pipeline, if applicable. For more information, see [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput).

## Related topics

<dl> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 



