---
Description: Media Foundation transforms (MFTs) are an evolution of the transform model first introduced with DirectX Media Objects (DMOs).
ms.assetid: 4e8c3ec9-6ffa-4858-a4ea-8ef8ccaf9253
title: Comparison of MFTs and DMOs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Comparison of MFTs and DMOs

Media Foundation transforms (MFTs) are an evolution of the transform model first introduced with DirectX Media Objects (DMOs). This topic summarizes the main ways in which MFTs differ from DMOs. Read this topic if you are already familiar with the DMO interfaces, or if you want to convert an existing DMO into an MFT.

This topic contains the following sections:

-   [Number of Streams](#number-of-streams)
-   [Format Negotiation](#format-negotiation)
-   [Streaming](#streaming)
    -   [Allocating Resources](#allocating-resources)
    -   [Processing Data](#processing-data)
    -   [Flushing](#flushing)
    -   [Stream Discontinuities](#stream-discontinuities)
-   [Miscellaneous Differences](#miscellaneous-differences)
-   [Flags](#flags)
    -   [ProcessInput Flags](#processinput-flags)
    -   [ProcessOutput Flags](#processoutput-flags)
    -   [GetInputStatus Flags](#getinputstatus-flags)
    -   [GetOutputStatus Flags](#getoutputstatus-flags)
    -   [GetInputStreamInfo Flags](#getinputstreaminfo-flags)
    -   [GetOutputStreamInfo Flags](#getoutputstreaminfo-flags)
    -   [SetInputType/SetOutputType Flags](#setinputtypesetoutputtype-flags)
-   [Error Codes](#error-codes)
-   [Creating Hybrid DMO/MFT Objects](#creating-hybrid-dmomft-objects)
-   [Related topics](#related-topics)

## Number of Streams

A DMO has a fixed number of streams, while an MFT can support a dynamic number of streams. The client can add input streams, and the MFT can add new output streams during processing. MFTs are not required to support dynamic streams, however. An MFT can have a fixed number of streams, just like a DMO.

The following methods are used to support dynamic streams on an MFT:

-   [**IMFTransform::AddInputStreams**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-addinputstreams)
-   [**IMFTransform::DeleteInputStream**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-deleteinputstream)
-   [**IMFTransform::GetStreamIDs**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamids)
-   [**IMFTransform::GetStreamLimits**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getstreamlimits)

In addition, the [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method defines the behavior for adding or removing output streams.

Because DMOs have fixed streams, the streams on a DMO are identified using zero-based index values. MFTs, on the other hand, use stream identifiers that do not necessarily correspond to index values. This is because the number of streams on an MFT might change. For example, stream 0 might be removed, leaving stream 1 as the first stream. However, an MFT with a fixed number of streams should observe the same convention as DMOs and use index values for stream identifiers.

## Format Negotiation

MFTs use the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface to describe media types. Otherwise, format negotiation with MFTs works on the same basic principles as with DMOs. The following table lists the format negotiation methods for DMOs and the corresponding methods for MFTs.



| DMO method                                                                        | MFT method                                                                          |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [**IMediaObject::GetInputCurrentType**](https://msdn.microsoft.com/windows/desktop/81d5c1b8-086c-422d-b2d7-85728507888d)   | [**IMFTransform::GetInputCurrentType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputcurrenttype)       |
| [**IMediaObject::GetInputMaxLatency**](https://msdn.microsoft.com/windows/desktop/f8a18b4c-a59c-4e9d-aff7-62333e9ffda9)     | [**IMFTransform::GetInputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreaminfo)         |
| [**IMediaObject::GetInputSizeInfo**](https://msdn.microsoft.com/windows/desktop/cce6359a-cd6e-46c9-a1cb-553ae5f83b9c)         | [**IMFTransform::GetInputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreaminfo)         |
| [**IMediaObject::GetInputType**](https://msdn.microsoft.com/windows/desktop/22693a22-97be-487d-ad17-31a2d8ee874c)                 | [**IMFTransform::GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype)   |
| [**IMediaObject::GetOutputCurrentType**](https://msdn.microsoft.com/windows/desktop/f5ebcf96-d008-448e-852b-39bdf1f39c4b) | [**IMFTransform::GetOutputCurrentType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputcurrenttype)     |
| [**IMediaObject::GetOutputSizeInfo**](https://msdn.microsoft.com/windows/desktop/497bc88e-4e26-409f-9d42-6a214a5d56e9)       | [**IMFTransform::GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo)       |
| [**IMediaObject::GetOutputType**](https://msdn.microsoft.com/windows/desktop/a7652472-4091-4ecf-b623-5c6eb01be44a)               | [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) |



 

## Streaming

Like DMOs, MFTs process data through calls to [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) and [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) methods. Here are the major differences between DMO and MFT processes when streaming data.

### Allocating Resources

MFTs do not have the [**IMediaObject::AllocateStreamingResources**](https://msdn.microsoft.com/windows/desktop/cd608bf2-50a5-4037-aeb5-c5c380c3d6df) and [**IMediaObject::FreeStreamingResources**](https://msdn.microsoft.com/windows/desktop/c4d2dbf1-45c9-47a2-a21f-5eb04f828ec1) methods used with DMOs. To handle allocation and deallocation of resources efficiently, an MFT can respond to the following messages in the [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) method:

-   [**MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING**](mft-message-notify-begin-streaming.md)
-   [**MFT\_MESSAGE\_NOTIFY\_START\_OF\_STREAM**](mft-message-notify-start-of-stream.md)

In addition, the client can signal the start and end of a stream by calling [**ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the following messages:

-   [**MFT\_MESSAGE\_NOTIFY\_END\_OF\_STREAM**](mft-message-notify-end-of-stream.md)
-   [**MFT\_MESSAGE\_NOTIFY\_END\_STREAMING**](mft-message-notify-end-streaming.md)

These two messages have no exact DMO equivalent.

### Processing Data

MFTs use media samples to hold input and output data. Media samples expose the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface, and contain the following data:

-   Time stamp and duration.
-   Attributes that contain per-sample information. For a list of attributes, see [Sample Attributes](sample-attributes.md).
-   Zero or more media buffers. Each media buffer exposes the [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface.

The [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer) interface is similar to the DMO **IMediaBuffer** interface. To access the underlying memory buffer, call [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock). This method is roughly equivalent to [**IMediaBuffer::GetBufferAndLength**](https://msdn.microsoft.com/windows/desktop/255ef101-f004-41c8-afb8-437d21decee5) for DMOs.

For uncompressed video data, a media buffer might also support the [**IMF2DBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer) interface. An MFT that processes uncompressed video (either as input or output) should be prepared to use the **IMF2DBuffer** interface if the buffer exposes it. For more information, see [Uncompressed Video Buffers](uncompressed-video-buffers.md).

Media Foundation provides some standard implementations of [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer), so it is generally not necessary to write your own implementation. To create a DMO buffer from a Media Foundation buffer, call [**MFCreateLegacyMediaBufferOnMFMediaBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatelegacymediabufferonmfmediabuffer).

### Flushing

MFTs do not have a [**Flush**](https://msdn.microsoft.com/windows/desktop/c80001b8-5648-430a-b565-e90486c48ac5) method. To flush an MFT, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_COMMAND\_FLUSH**](mft-message-command-flush.md) message.

### Stream Discontinuities

MFTs do not have a [**Discontinuity**](https://msdn.microsoft.com/windows/desktop/1a8e51e2-5d19-423d-acd2-8f1c0a143cf3) method. To signal a discontinuity in a stream, set the [**MFSampleExtension\_Discontinuity**](mfsampleextension-discontinuity-attribute.md) attribute on the input sample.

## Miscellaneous Differences

Here are some additional minor differences between MFTs and DMOs.

-   There are no MFT equivalents for the following DMO methods:
    -   [**IMediaObject::Lock**](https://msdn.microsoft.com/windows/desktop/6923dd91-7bdb-4a0c-833d-4742973825ee)
    -   [**IMediaObject::SetInputMaxLatency**](https://msdn.microsoft.com/windows/desktop/45fb0caa-cd12-4847-a646-f6fd90c50b81)
-   MFTs are not required to support aggregation.
-   MFTs support an operation called *draining*. The purpose of draining is to process any data that remains in the MF, without providing any more input data to the MFT (for example, at the end of the stream). To drain an MFT, call [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message. For more information, see [Basic MFT Processing Model](basic-mft-processing-model.md).
-   MFTs can have attributes, including per-stream attributes. Use the following methods to get the attributes from an MFT:

    -   [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes)
    -   [**IMFTransform::GetInputStreamAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreamattributes)
    -   [**IMFTransform::GetOutputStreamAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreamattributes)

-   MFTs can process events. To send an event to an MFT, call [**IMFTransform::ProcessEvent**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processevent). An MFT can send an event to the client through the [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method. For more information, see [Basic MFT Processing Model](basic-mft-processing-model.md).

## Flags

The following tables list the various DMO flags and their MFT equivalents. Whenever a DMO flag maps directly to an MFT flag, both flags have the same numeric value. However, some DMO flags do not have exact MFT equivalents, and vice versa.

### ProcessInput Flags

DMOs: [**\_DMO\_INPUT\_DATA\_BUFFER\_FLAGS**](https://msdn.microsoft.com/windows/desktop/b0217926-ac2d-48e5-a5d0-e31be6ea20ac) enumeration.

MFTs: No equivalent enumeration.



| DMO flag                                  | MFT flag                                                                                                                                      |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **DMO\_INPUT\_DATA\_BUFFERF\_SYNCPOINT**  | No equivalent flag. Instead, set the [**MFSampleExtension\_CleanPoint**](mfsampleextension-cleanpoint-attribute.md) attribute on the sample. |
| **DMO\_INPUT\_DATA\_BUFFERF\_TIME**       | No equivalent flag. Instead, call [**IMFSample::SetSampleTime**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-setsampletime) on the sample.                                  |
| **DMO\_INPUT\_DATA\_BUFFERF\_TIMELENGTH** | No equivalent flag. Instead, call [**IMFSample::SetSampleDuration**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-setsampleduration) on the sample.                          |



 

### ProcessOutput Flags

DMOs: [**\_DMO\_PROCESS\_OUTPUT\_FLAGS**](https://msdn.microsoft.com/windows/desktop/7648f975-3753-41fe-a311-e86334ef7071) enumeration.

MFTs: [**\_MFT\_PROCESS\_OUTPUT\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_process_output_flags) enumeration.



| DMO flag                                            | MFT flag                                            |
|-----------------------------------------------------|-----------------------------------------------------|
| **DMO\_PROCESS\_OUTPUT\_DISCARD\_WHEN\_NO\_BUFFER** | **MFT\_PROCESS\_OUTPUT\_DISCARD\_WHEN\_NO\_BUFFER** |



 

DMOs: [**\_DMO\_OUTPUT\_DATA\_BUFFER\_FLAGS**](https://msdn.microsoft.com/windows/desktop/80ce44a7-4b69-4aed-8b28-10e84a658f12) enumeration.

MFTs: [**\_MFT\_OUTPUT\_DATA\_BUFFER\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_output_data_buffer_flags) enumeration.



| DMO flag                                   | MFT flag                                                                                                                                            |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **DMO\_OUTPUT\_DATA\_BUFFERF\_SYNCPOINT**  | No equivalent flag. Instead, check for the [**MFSampleExtension\_CleanPoint**](mfsampleextension-cleanpoint-attribute.md) attribute on the sample. |
| **DMO\_OUTPUT\_DATA\_BUFFERF\_TIME**       | No equivalent flag. Instead, call [**IMFSample::GetSampleTime**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getsampletime) on the sample.                                        |
| **DMO\_OUTPUT\_DATA\_BUFFERF\_TIMELENGTH** | No equivalent flag. Instead, call [**IMFSample::GetSampleDuration**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getsampleduration) on the sample.                                |
| **DMO\_OUTPUT\_DATA\_BUFFERF\_INCOMPLETE** | **MFT\_OUTPUT\_DATA\_BUFFER\_INCOMPLETE**                                                                                                           |
| No equivalent flag.                        | **MFT\_OUTPUT\_DATA\_BUFFER\_FORMAT\_CHANGE**                                                                                                       |
| No equivalent flag.                        | **MFT\_OUTPUT\_DATA\_BUFFER\_STREAM\_END**                                                                                                          |
| No equivalent flag.                        | **MFT\_OUTPUT\_DATA\_BUFFER\_NO\_SAMPLE**                                                                                                           |



 

### GetInputStatus Flags

DMOs: **\_DMO\_INPUT\_STATUS\_FLAGS** enumeration.

MFTs: [**\_MFT\_INPUT\_STATUS\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_input_status_flags) enumeration.



| DMO flag                              | MFT flag                             |
|---------------------------------------|--------------------------------------|
| **DMO\_INPUT\_STATUSF\_ACCEPT\_DATA** | **MFT\_INPUT\_STATUS\_ACCEPT\_DATA** |



 

### GetOutputStatus Flags

DMOs: No equivalent enumeration.

MFTs: [**\_MFT\_OUTPUT\_STATUS\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_output_status_flags) enumeration.



| DMO flag            | MFT flag                               |
|---------------------|----------------------------------------|
| No equivalent flag. | **MFT\_OUTPUT\_STATUS\_SAMPLE\_READY** |



 

### GetInputStreamInfo Flags

DMOs: [**\_DMO\_INPUT\_STREAM\_INFO\_FLAGS**](https://msdn.microsoft.com/windows/desktop/96e37678-0325-4569-8491-c8ef23f6c76e) enumeration.

MFTs: [**\_MFT\_INPUT\_STREAM\_INFO\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_input_stream_info_flags) enumeration.



| DMO flag                                             | MFT flag                                            |
|------------------------------------------------------|-----------------------------------------------------|
| **DMO\_INPUT\_STREAMF\_WHOLE\_SAMPLES**              | **MFT\_INPUT\_STREAM\_WHOLE\_SAMPLES**              |
| **DMO\_INPUT\_STREAMF\_SINGLE\_SAMPLE\_PER\_BUFFER** | **MFT\_INPUT\_STREAM\_SINGLE\_SAMPLE\_PER\_BUFFER** |
| **DMO\_INPUT\_STREAMF\_FIXED\_SAMPLE\_SIZE**         | **MFT\_INPUT\_STREAM\_FIXED\_SAMPLE\_SIZE**         |
| **DMO\_INPUT\_STREAMF\_HOLDS\_BUFFERS**              | **MFT\_INPUT\_STREAM\_HOLDS\_BUFFERS**              |
| No equivalent flag.                                  | **MFT\_INPUT\_STREAM\_DOES\_NOT\_ADDREF**           |
| No equivalent flag.                                  | **MFT\_INPUT\_STREAM\_REMOVABLE**                   |
| No equivalent flag.                                  | **MFT\_INPUT\_STREAM\_OPTIONAL**                    |



 

### GetOutputStreamInfo Flags

DMOs: [**\_DMO\_OUTPUT\_STREAM\_INFO\_FLAGS**](https://msdn.microsoft.com/windows/desktop/570dd009-0101-4a01-b064-4f4404fb453f) enumeration.

MFTs: [**\_MFT\_OUTPUT\_STREAM\_INFO\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_output_stream_info_flags) enumeration.



| DMO flag                                              | MFT flag                                             |
|-------------------------------------------------------|------------------------------------------------------|
| **DMO\_OUTPUT\_STREAMF\_WHOLE\_SAMPLES**              | **MFT\_OUTPUT\_STREAM\_WHOLE\_SAMPLES**              |
| **DMO\_OUTPUT\_STREAMF\_SINGLE\_SAMPLE\_PER\_BUFFER** | **MFT\_OUTPUT\_STREAM\_SINGLE\_SAMPLE\_PER\_BUFFER** |
| **DMO\_OUTPUT\_STREAMF\_FIXED\_SAMPLE\_SIZE**         | **MFT\_OUTPUT\_STREAM\_FIXED\_SAMPLE\_SIZE**         |
| **DMO\_OUTPUT\_STREAMF\_DISCARDABLE**                 | **MFT\_OUTPUT\_STREAM\_DISCARDABLE**                 |
| **DMO\_OUTPUT\_STREAMF\_OPTIONAL**                    | **MFT\_OUTPUT\_STREAM\_OPTIONAL**                    |
| No equivalent flag.                                   | **MFT\_OUTPUT\_STREAM\_PROVIDES\_SAMPLES**           |
| No equivalent flag.                                   | **MFT\_OUTPUT\_STREAM\_CAN\_PROVIDE\_SAMPLES**       |
| No equivalent flag.                                   | **MFT\_OUTPUT\_STREAM\_LAZY\_READ**                  |
| No equivalent flag.                                   | **MFT\_OUTPUT\_STREAM\_REMOVABLE**                   |



 

### SetInputType/SetOutputType Flags

DMOs: [**\_DMO\_SET\_TYPE\_FLAGS**](https://msdn.microsoft.com/windows/desktop/e0638668-bbd2-4696-8482-d72438510740) enumeration.

MFTs: [**\_MFT\_SET\_TYPE\_FLAGS**](/windows/desktop/api/mftransform/ne-mftransform-_mft_set_type_flags) enumeration.



| DMO flag                        | MFT flag                                                                             |
|---------------------------------|--------------------------------------------------------------------------------------|
| **DMO\_SET\_TYPEF\_TEST\_ONLY** | **MFT\_SET\_TYPE\_TEST\_ONLY**                                                       |
| **DMO\_SET\_TYPEF\_CLEAR**      | No equivalent flag. Instead, set the media type to **NULL** to clear the media type. |



 

## Error Codes

The following table shows how to map DMO error codes to MFT error codes. A hybrid MFT/DMO object should return the DMO error codes from [**IMediaObject**](https://msdn.microsoft.com/windows/desktop/a3fd17aa-7df2-40f4-8f2c-45bae38e4c0b) methods and the MFT error codes from [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) methods. The DMO error codes are defined in the header file MediaErr.h. The MFT error codes are defined in the header file mferror.h.



| DMO error code                  | MFT error code                       |
|---------------------------------|--------------------------------------|
| **DMO\_E\_INVALIDTYPE**         | **MF\_E\_INVALIDTYPE**               |
| **DMO\_E\_INVALIDSTREAMINDEX**  | **MF\_E\_INVALIDSTREAMNUMBER**       |
| **DMO\_E\_NOTACCEPTING**        | **MF\_E\_NOTACCEPTING**              |
| **DMO\_E\_NO\_MORE\_ITEMS**     | **MF\_E\_NO\_MORE\_TYPES**           |
| **DMO\_E\_TYPE\_NOT\_ACCEPTED** | **MF\_E\_INVALIDMEDIATYPE**          |
| **DMO\_E\_TYPE\_NOT\_SET**      | **MF\_E\_TRANSFORM\_TYPE\_NOT\_SET** |



 

## Creating Hybrid DMO/MFT Objects

The [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface is loosely based on [**IMediaObject**](https://msdn.microsoft.com/windows/desktop/a3fd17aa-7df2-40f4-8f2c-45bae38e4c0b), which is the primary interface for DirectX Media Objects (DMOs). It is possible to create objects that expose both interfaces. However, this can lead to naming collisions, because the interfaces have some methods that share the same name. You can solve this problem in one of two ways:

Solution 1: Include the following line at the top of any .cpp file that contains MFT functions:

``` syntax
#define MFT_UNIQUE_METHOD_NAMES
```

This changes the declaration of the [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform) interface so that most of the method names are prefixed with "MFT". Thus, [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) becomes **IMFTransform::MFTProcessInput**, while [**IMediaObject::ProcessInput**](https://msdn.microsoft.com/windows/desktop/f52e9586-f65d-418f-8c1a-c97c0a81d253) keeps its original name. This technique is most useful if you are converting an existing DMO to a hybrid DMO/MFT. You can add the new MFT methods without changing the DMO methods.

Solution 2: Use C++ syntax to disambiguate names that are inherited from more than one interface. For example, declare the MFT version of [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) as follows:

``` syntax
CMyHybridObject::IMFTransform::ProcessInput(...)
```

Declare the DMO version of [**ProcessInput**](https://msdn.microsoft.com/windows/desktop/f52e9586-f65d-418f-8c1a-c97c0a81d253) like this:

``` syntax
CMyHybridObject::IMediaObject::ProcessInput(...)
```

If you make an internal call to a method within the object, you can use this syntax, but doing so will override the virtual status of the method. A better way to make calls from inside the object is the following:

``` syntax
hr = ((IMediaObject*)this)->ProcessInput(...)
```

That way, if you derive another class from **CMyHybridObject** and override the CMyHybridObject::IMediaObject::ProcessInput method, the correct virtual method is called. The DMO interfaces are documented in the DirectShow SDK documentation.

## Related topics

<dl> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 



