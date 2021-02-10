---
description: This topic takes an in-depth look at the MPEG-1 Media Source SDK Sample.
ms.assetid: d392f30c-c963-4eb3-add2-1bb986919c0b
title: 'Case Study: MPEG-1 Media Source'
ms.topic: article
ms.date: 05/31/2018
---

# Case Study: MPEG-1 Media Source

In Microsoft Media Foundation, the object that introduces media data into the data pipeline is called a *media source*. This topic takes an in-depth look at the [MPEG-1 Media Source](mpeg1source-sample.md) SDK Sample.

-   [Prerequisites](#prerequisites)
-   [C++ Classes Used in the MPEG-1 Source](#c-classes-used-in-the-mpeg-1-source)
-   [Byte-Stream Handler](#byte-stream-handler)
-   [Presentation Descriptor](#presentation-descriptor)
-   [Streaming States](#streaming-states)
    -   [Start](#start)
    -   [Pause](#pause)
    -   [Stop](#stop)
-   [Sample Requests](#sample-requests)
-   [End of Stream](#end-of-stream)
-   [Asynchronous Operations](#asynchronous-operations)
    -   [Operation Queue](#operation-queue)
-   [Related topics](#related-topics)

## Prerequisites

Before reading this topic you should understand the following Media Foundation concepts:

-   [Media Source Object Model](media-source-object-model.md)
-   [Asynchronous Callback Methods](asynchronous-callback-methods.md).
-   [Work Queues](work-queues.md)
-   [Media Event Generators](media-event-generators.md)
-   [Media Buffers](media-buffers.md)
-   [Media Samples](media-samples.md)
-   [Media Types](media-types.md)

You should also have a basic understanding of the Media Foundation architecture, particularly the role of media sources in the pipeline. (For more information, see [Media Sources](media-sources.md).)

In addition, you may want to read the topic [Writing a Custom Media Source](writing-a-custom-media-source.md), which gives a more general overview of the steps described here.

This topic does not reproduce all of the code from the SDK sample, because the sample is fairly large.

## C++ Classes Used in the MPEG-1 Source

The sample MPEG-1 source is implemented with the following C++ classes:

-   `MPEG1ByteStreamHandler`. Implements the byte-stream handler for the media source. Given a byte stream, the byte-stream handler creates an instance of the source.
-   `MPEG1Source`. Implements the media source.
-   `MPEG1Stream`. Implements the media stream objects. The media source creates one `MPEG1Stream` object for every audio or video stream in the MPEG-1 bitstream.
-   `Parser`. Parses the MPEG-1 bitstream. For the most part, the details of this class are not relevant to the Media Foundation APIs.
-   SourceOp, OpQueue: These two classes manage asynchronous operations in the media source. (See [Asynchronous Operations](#asynchronous-operations)).

Other miscellaneous helper classes are described later in the topic.

## Byte-Stream Handler

The *byte-stream* handler is the object that creates the media source. The byte-stream handler is created by the source resolver; applications do not interact directly with the byte-stream handler. The source resolver discovers the byte-stream handler by looking in the registry. Handler are registered by file name extension or MIME type. For the MPEG-1 source, the byte-stream handler is registered for the ".mpg" file name extension.

> [!Note]  
> If you want to support custom URL schemes, you can also write a *scheme handler*. The MPEG-1 source is designed for local files, and Media Foundation already provides a scheme handler for "file://" URLs.

 

The byte-stream handler implements the [**IMFByteStreamHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamhandler) interface. This interface has two most important methods that must be implemented:

-   [**BeginCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-begincreateobject). Starts an asynchronous operation to create the media source.
-   [**EndCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-endcreateobject). Completes the asynchronous call.

Two other methods are optional and not implemented in the SDK sample:

-   [**CancelObjectCreation**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-cancelobjectcreation). Cancels the [**BeginCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-begincreateobject) method. This method is useful for a network source that might have a high latency at startup.
-   [**GetMaxNumberOfBytesRequiredForResolution**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-getmaxnumberofbytesrequiredforresolution). Gets the maximum number of bytes that the handler will read from the source stream. Implement this method if you know how much data the byte-stream handler before it can create the media source. Otherwise, simply return **E\_NOTIMPL**.

Here is the implementation of the [**BeginCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-begincreateobject) method:


```C++
HRESULT MPEG1ByteStreamHandler::BeginCreateObject(
        /* [in] */ IMFByteStream *pByteStream,
        /* [in] */ LPCWSTR pwszURL,
        /* [in] */ DWORD dwFlags,
        /* [in] */ IPropertyStore *pProps,
        /* [out] */ IUnknown **ppIUnknownCancelCookie,  // Can be NULL
        /* [in] */ IMFAsyncCallback *pCallback,
        /* [in] */ IUnknown *punkState                  // Can be NULL
        )
{
    if (pByteStream == NULL)
    {
        return E_POINTER;
    }

    if (pCallback == NULL)
    {
        return E_POINTER;
    }

    if ((dwFlags & MF_RESOLUTION_MEDIASOURCE) == 0)
    {
        return E_INVALIDARG;
    }

    HRESULT hr = S_OK;

    IMFAsyncResult *pResult = NULL;
    MPEG1Source    *pSource = NULL;

    // Create an instance of the media source.
    hr = MPEG1Source::CreateInstance(&pSource);

    // Create a result object for the caller's async callback.
    if (SUCCEEDED(hr))
    {
        hr = MFCreateAsyncResult(NULL, pCallback, punkState, &pResult);
    }

    // Start opening the source. This is an async operation.
    // When it completes, the source will invoke our callback
    // and then we will invoke the caller's callback.
    if (SUCCEEDED(hr))
    {
        hr = pSource->BeginOpen(pByteStream, this, NULL);
    }

    if (SUCCEEDED(hr))
    {
        if (ppIUnknownCancelCookie)
        {
            *ppIUnknownCancelCookie = NULL;
        }

        m_pSource = pSource;
        m_pSource->AddRef();

        m_pResult = pResult;
        m_pResult->AddRef();
    }

// cleanup
    SafeRelease(&pSource);
    SafeRelease(&pResult);
    return hr;
}
```



The method performs the following steps:

1.  Creates a new instance of the `MPEG1Source` object.
2.  Create an asynchronous result object. This object is used later to invoke the source resolver's callback method.
3.  Calls `MPEG1Source::BeginOpen`, an asynchronous method defined in the `MPEG1Source` class.
4.  Sets *ppIUnknownCancelCookie* to **NULL**, which informs the caller that [**CancelObjectCreation**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-cancelobjectcreation) is not supported.

The `MPEG1Source::BeginOpen` method does the actual work of reading the byte stream and initializing the `MPEG1Source` object. This method is not part of the public API. You can define any mechanism between the handler and the media source that suits your needs. Putting most of the logic into the media source keeps the byte-stream handler relatively simple.

Briefly, `BeginOpen` does the following:

1.  Calls [**IMFByteStream::GetCapabilities**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-getcapabilities) to verify that the source byte stream is both readable and seekable.
2.  Calls [**IMFByteStream::BeginRead**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-beginread) to start an asynchronous I/O request.

The rest of the initialization occurs asynchronously. The media source reads enough data from the stream to parse the MPEG-1 sequence headers. Then it creates a *presentation descriptor*, which is the object used to describe the audio and video streams in the file. (For more information, see [Presentation Descriptor](#presentation-descriptor).) When the `BeginOpen` operation completes, the byte-stream handler invokes the source resolver's callback method. At that point, the source resolver calls [**IMFByteStreamHandler::EndCreateObject**](/windows/desktop/api/mfidl/nf-mfidl-imfbytestreamhandler-endcreateobject). The **EndCreateObject** method returns the status of the operation.


```C++
HRESULT MPEG1ByteStreamHandler::EndCreateObject(
        /* [in] */ IMFAsyncResult *pResult,
        /* [out] */ MF_OBJECT_TYPE *pObjectType,
        /* [out] */ IUnknown **ppObject)
{
    if (pResult == NULL || pObjectType == NULL || ppObject == NULL)
    {
        return E_POINTER;
    }

    HRESULT hr = S_OK;

    *pObjectType = MF_OBJECT_INVALID;
    *ppObject = NULL;

    hr = pResult->GetStatus();

    if (SUCCEEDED(hr))
    {
        *pObjectType = MF_OBJECT_MEDIASOURCE;

        assert(m_pSource != NULL);

        hr = m_pSource->QueryInterface(IID_PPV_ARGS(ppObject));
    }

    SafeRelease(&m_pSource);
    SafeRelease(&m_pResult);
    return hr;
}
```



If an error occurs at any time during this process, the callback is invoked with an error status code.

## Presentation Descriptor

The presentation descriptor describes the contents of the MPEG-1 file, including the following information:

-   The number of the streams.
-   The format of each stream.
-   Stream identifiers.
-   The selection status of each stream (selected or deselected).

In terms of the Media Foundation architecture, the presentation descriptor contains one or more *stream descriptors*. Each stream descriptor contains a *media type handler*, which is used to get or set media types on the stream. Media Foundation provides stock implementations for the presentation descriptor and stream descriptor; these are suitable for most media sources.

To create a presentation descriptor, perform the following steps:

1.  For each stream:
    1.  Provide a stream ID and an array of possible media types. If the stream supports more than one media type, order the list of media types by preference, if any. (Put the optimal type first, and the least optimal type last.)
    2.  Call [**MFCreateStreamDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatestreamdescriptor) to create the stream descriptor.
    3.  Call [**IMFStreamDescriptor::GetMediaTypeHandler**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamdescriptor-getmediatypehandler) on the newly created stream descriptor.
    4.  Call [**IMFMediaTypeHandler::SetCurrentMediaType**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-setcurrentmediatype) to set the default format for the stream. If there is more than one media type, you should generally set the first type in the list.
2.  Call [**MFCreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepresentationdescriptor) and pass in the array of stream descriptor pointers.
3.  For each stream, call [**IMFPresentationDescriptor::SelectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-selectstream) or [**DeselectStream**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-deselectstream) to set the default selection state. If there is more than one stream of the same type (audio or video), only one should be selected by default.

The `MPEG1Source` object creates the presentation descriptor in its `InitPresentationDescriptor` method:


```C++
HRESULT MPEG1Source::InitPresentationDescriptor()
{
    HRESULT hr = S_OK;
    DWORD cStreams = 0;

    assert(m_pPresentationDescriptor == NULL);
    assert(m_state == STATE_OPENING);

    if (m_pHeader == NULL)
    {
        return E_FAIL;
    }

    // Get the number of streams, as declared in the MPEG-1 header, skipping
    // any streams with an unsupported format.
    for (DWORD i = 0; i < m_pHeader->cStreams; i++)
    {
        if (IsStreamTypeSupported(m_pHeader->streams[i].type))
        {
            cStreams++;
        }
    }

    // How many streams do we actually have?
    if (cStreams > m_streams.GetCount())
    {
        // Keep reading data until we have seen a packet for each stream.
        return S_OK;
    }

    // We should never create a stream we don't support.
    assert(cStreams == m_streams.GetCount());

    // Ready to create the presentation descriptor.

    // Create an array of IMFStreamDescriptor pointers.
    IMFStreamDescriptor **ppSD =
            new (std::nothrow) IMFStreamDescriptor*[cStreams];

    if (ppSD == NULL)
    {
        hr = E_OUTOFMEMORY;
        goto done;
    }

    ZeroMemory(ppSD, cStreams * sizeof(IMFStreamDescriptor*));

    // Fill the array by getting the stream descriptors from the streams.
    for (DWORD i = 0; i < cStreams; i++)
    {
        hr = m_streams[i]->GetStreamDescriptor(&ppSD[i]);
        if (FAILED(hr))
        {
            goto done;
        }
    }

    // Create the presentation descriptor.
    hr = MFCreatePresentationDescriptor(cStreams, ppSD,
        &m_pPresentationDescriptor);

    if (FAILED(hr))
    {
        goto done;
    }

    // Select the first video stream (if any).
    for (DWORD i = 0; i < cStreams; i++)
    {
        GUID majorType = GUID_NULL;

        hr = GetStreamMajorType(ppSD[i], &majorType);
        if (FAILED(hr))
        {
            goto done;
        }

        if (majorType == MFMediaType_Video)
        {
            hr = m_pPresentationDescriptor->SelectStream(i);
            if (FAILED(hr))
            {
                goto done;
            }
            break;
        }
    }

    // Switch state from "opening" to stopped.
    m_state = STATE_STOPPED;

    // Invoke the async callback to complete the BeginOpen operation.
    hr = CompleteOpen(S_OK);

done:
    // clean up:
    if (ppSD)
    {
        for (DWORD i = 0; i < cStreams; i++)
        {
            SafeRelease(&ppSD[i]);
        }
        delete [] ppSD;
    }
    return hr;
}
```



The application gets the presentation descriptor by calling [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor). This method creates a shallow copy of the presentation descriptor by calling [**IMFPresentationDescriptor::Clone**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-clone). (The copy contains pointers to the original stream descriptors.) The application can use the presentation descriptor to set the media type, select a stream, or deselect a stream.

Optionally, presentation descriptors and stream descriptors can contain attributes that give additional information about the source. For a list such attributes, see the following topics:

-   [Presentation Descriptor Attributes](presentation-descriptor-attributes.md)
-   [Stream Descriptor Attributes](stream-descriptor-attributes.md)

One attribute deserves special mention: The [**MF\_PD\_DURATION**](mf-pd-duration-attribute.md) attribute contains the total duration of the source. Set this attribute if you know the duration up front; for example, the duration might be specified in the file headers, depending on the file format. The application might display this value, or use it to set a progress bar or seek bar.

## Streaming States

A media source defines the following states:



| State    | Description                                                                                                     |
|----------|-----------------------------------------------------------------------------------------------------------------|
| Started  | The source accepts and processes sample requests.                                                               |
| Paused   | The source accepts sample requests, but does not process them. Requests are queued until the source is started. |
| Stopped. | The source rejects sample requests.                                                                             |



 

### Start

The [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method starts the media source. It takes the following parameters:

-   A presentation descriptor.
-   A time-format GUID.
-   A start position.

The application must obtain the presentation descriptor by calling [**CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepresentationdescriptor) on the source. There is no defined mechanism for validating a presentation descriptor. If the application specifies the wrong presentation descriptor, the results are undefined.

The time-format GUID specifies how to interpret the starting position. The standard format is 100-nanosecond (ns) units, indicated by GUID\_NULL. Every media source must support 100-ns units. Optionally, a source can support other units of time, such as frame number or time code. However, there is no standard way to query a media source for the list of time formats it supports.

The start position is given as a **PROPVARIANT**, allowing for different data types depending on the time format. For 100-ns, the **PROPVARIANT** type is either **VT\_I8** or **VT\_EMPTY**. If **VT\_I8**, the **PROPVARIANT** contains the start position in 100-ns units. The value **VT\_EMPTY** has the special meaning "start at the current position."

Implement the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method as follows:

1.  Validate parameters and state:
    -   Check for **NULL** parameters.
    -   Check the time-format GUID. If the value is invalid, return **MF\_E\_UNSUPPORTED\_TIME\_FORMAT**.
    -   Check the data type of the **PROPVARIANT** that holds the start position.
    -   Validate the start position. If invalid, return **MF\_E\_INVALIDREQUEST**.
    -   If the source has been shut down, return **MF\_E\_SHUTDOWN**.
2.  If no error occurs in step 1, queue an asynchronous operation. Everything after this step occurs on a work-queue thread.
3.  For each stream:
    1.  Check if the stream is already active from a previous [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) request.
    2.  Call [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex) to check whether the application selected or deselected the stream.
    3.  If a previously selected stream is now deselected, flush any undelivered samples for that stream.
    4.  If the stream is active, the media source (not the stream) sends one of the following events:
        -   It sends [MEUpdatedStream](meupdatedstream.md) if the stream was previously active.
        -   Otherwise, it sends [MENewStream](menewstream.md).

        For both events, the event data is the [**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream) pointer for the stream.
    5.  If the source is restarting from the paused state, there might be pending sample requests. If so, deliver these now.
    6.  If the source is seeking to a new position, each stream object sends an [MEStreamSeeked](mestreamseeked.md) event. Otherwise, each stream sends an [MEStreamStarted](mestreamstarted.md) event.
4.  If the source is seeking to a new position, the media source sends an [MESourceSeeked](mesourceseeked.md) event. Otherwise, it sends an [MESourceStarted](mesourcestarted.md) event.

If an error occurs at any time after step 2, the source sends an [MESourceStarted](mesourcestarted.md) event with an error code. This alerts the application that the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) method failed asynchronously.

The following code shows steps 1–2:


```C++
HRESULT MPEG1Source::Start(
        IMFPresentationDescriptor* pPresentationDescriptor,
        const GUID* pguidTimeFormat,
        const PROPVARIANT* pvarStartPos
    )
{

    HRESULT hr = S_OK;
    SourceOp *pAsyncOp = NULL;

    // Check parameters.

    // Start position and presentation descriptor cannot be NULL.
    if (pvarStartPos == NULL || pPresentationDescriptor == NULL)
    {
        return E_INVALIDARG;
    }

    // Check the time format.
    if ((pguidTimeFormat != NULL) && (*pguidTimeFormat != GUID_NULL))
    {
        // Unrecognized time format GUID.
        return MF_E_UNSUPPORTED_TIME_FORMAT;
    }

    // Check the data type of the start position.
    if ((pvarStartPos->vt != VT_I8) && (pvarStartPos->vt != VT_EMPTY))
    {
        return MF_E_UNSUPPORTED_TIME_FORMAT;
    }

    EnterCriticalSection(&m_critSec);

    // Check if this is a seek request. This sample does not support seeking.

    if (pvarStartPos->vt == VT_I8)
    {
        // If the current state is STOPPED, then position 0 is valid.
        // Otherwise, the start position must be VT_EMPTY (current position).

        if ((m_state != STATE_STOPPED) || (pvarStartPos->hVal.QuadPart != 0))
        {
            hr = MF_E_INVALIDREQUEST;
            goto done;
        }
    }

    // Fail if the source is shut down.
    hr = CheckShutdown();
    if (FAILED(hr))
    {
        goto done;
    }

    // Fail if the source was not initialized yet.
    hr = IsInitialized();
    if (FAILED(hr))
    {
        goto done;
    }

    // Perform a basic check on the caller's presentation descriptor.
    hr = ValidatePresentationDescriptor(pPresentationDescriptor);
    if (FAILED(hr))
    {
        goto done;
    }

    // The operation looks OK. Complete the operation asynchronously.
    hr = SourceOp::CreateStartOp(pPresentationDescriptor, &pAsyncOp);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pAsyncOp->SetData(*pvarStartPos);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = QueueOperation(pAsyncOp);

done:
    SafeRelease(&pAsyncOp);
    LeaveCriticalSection(&m_critSec);
    return hr;
}
```



The remaining steps are shown in the next example:


```C++
HRESULT MPEG1Source::DoStart(StartOp *pOp)
{
    assert(pOp->Op() == SourceOp::OP_START);

    IMFPresentationDescriptor *pPD = NULL;
    IMFMediaEvent  *pEvent = NULL;

    HRESULT     hr = S_OK;
    LONGLONG    llStartOffset = 0;
    BOOL        bRestartFromCurrentPosition = FALSE;
    BOOL        bSentEvents = FALSE;

    hr = BeginAsyncOp(pOp);

    // Get the presentation descriptor from the SourceOp object.
    // This is the PD that the caller passed into the Start() method.
    // The PD has already been validated.
    if (SUCCEEDED(hr))
    {
        hr = pOp->GetPresentationDescriptor(&pPD);
    }

    // Because this sample does not support seeking, the start
    // position must be 0 (from stopped) or "current position."

    // If the sample supported seeking, we would need to get the
    // start position from the PROPVARIANT data contained in pOp.

    if (SUCCEEDED(hr))
    {
        // Select/deselect streams, based on what the caller set in the PD.
        // This method also sends the MENewStream/MEUpdatedStream events.
        hr = SelectStreams(pPD, pOp->Data());
    }

    if (SUCCEEDED(hr))
    {
        m_state = STATE_STARTED;

        // Queue the "started" event. The event data is the start position.
        hr = m_pEventQueue->QueueEventParamVar(
            MESourceStarted,
            GUID_NULL,
            S_OK,
            &pOp->Data()
            );
    }

    if (FAILED(hr))
    {
        // Failure. Send the error code to the application.

        // Note: It's possible that QueueEvent itself failed, in which case it
        // is likely to fail again. But there is no good way to recover in
        // that case.

        (void)m_pEventQueue->QueueEventParamVar(
            MESourceStarted, GUID_NULL, hr, NULL);
    }

    CompleteAsyncOp(pOp);

    SafeRelease(&pEvent);
    SafeRelease(&pPD);
    return hr;
}
```



### Pause

The [**IMFMediaSource::Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-pause) method pauses the media source. Implement this method as follows:

1.  Queue an asynchronous operation.
2.  Each active stream sends an [MEStreamPaused](mestreampaused.md) event.
3.  The media source sends an [MESourcePaused](mesourcepaused.md) event.

While paused, the source queues sample requests without processing them. (See [Sample Requests](#sample-requests).)

### Stop

The [**IMFMediaSource::Stop**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-stop) method stops the media source. Implement this method as follows:

1.  Queue an asynchronous operation.
2.  Each active stream sends an [MEStreamStopped](mestreamstopped.md) event.
3.  Clear all queued samples and sample requests.
4.  The media source sends an [MESourceStopped](mesourcestopped.md) event.

While stopped, the source rejects all requests for samples.

If the source is stopped while an I/O request is in progress, the I/O request might complete after the source enters the stopped state. In that case, the source should discard the result of that I/O request.

## Sample Requests

Media Foundation use a *pull* model, in which the pipeline requests samples from the media source. This differs from the model used by DirectShow, in which the sources "pushes" samples.

To request a new sample, the Media Foundation pipeline calls [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample). This method takes an **IUnknown** pointer that represents a *token* object. The implementation of the token object is up to the caller; it simply provides a way for the caller to track sample requests. The token parameter can also be **NULL**.

Assuming the source uses asynchronous I/O requests to read data, sample generation will not be synchronized with sample requests. To synchronize sample requests with sample generation, a media source does the following:

1.  Request tokens are placed on a queue.
2.  As samples are generated, they are placed on a second queue.
3.  The media source completes a sample request by pulling a request token from the first queue and a sample from the second queue.
4.  The media source sends an MEMediaSample event. The event contains a pointer to the sample, and the sample contains a pointer to the token.

The following diagram shows the relationship between the [MEMediaSample](memediasample.md) event, the sample, and the request token.

![diagram showing memediasample and a sample queue pointing to imfsample; imfsample and the request queue point to iunknown](images/mediasourceimpl01.png)

The example MPEG-1 source implements this process as follows:

1.  The [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method puts the request on a FIFO queue.
2.  As I/O requests are completed, the media source creates new samples and puts them on a second FIFO queue. (This queue has a maximum size, to prevent the source from reading too far ahead.)
3.  Whenever both of these queues have at least one item (one request and one sample), the media source completes the first request from the request queue by sending out the first sample from the sample queue.
4.  To deliver a sample, the stream object (not the source object) sends an [MEMediaSample](memediasample.md) event.
    -   The event data is a pointer to the sample's [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface.
    -   If the request included a token, attach the token to the sample by setting the [**MFSampleExtension\_Token**](mfsampleextension-token-attribute.md) attribute on the sample.

At this point, there are three possibilities:

-   There is another sample in the sample queue, but no matching request.
-   There is a request, but no sample.
-   Both queues are empty; there are no samples and no requests.

If the sample queue is empty, the source checks for the end of the stream (see [End of Stream](#end-of-stream)). Otherwise, it starts another I/O request for data. If any error occurs during this process, the stream sends an [MEError](meerror.md) event.

The following code implements the [**IMFMediaStream::RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method:


```C++
HRESULT MPEG1Stream::RequestSample(IUnknown* pToken)
{
    HRESULT hr = S_OK;
    IMFMediaSource *pSource = NULL;

    // Hold the media source object's critical section.
    SourceLock lock(m_pSource);

    hr = CheckShutdown();
    if (FAILED(hr))
    {
        goto done;
    }

    if (m_state == STATE_STOPPED)
    {
        hr = MF_E_INVALIDREQUEST;
        goto done;
    }

    if (!m_bActive)
    {
        // If the stream is not active, it should not get sample requests.
        hr = MF_E_INVALIDREQUEST;
        goto done;
    }

    if (m_bEOS && m_Samples.IsEmpty())
    {
        // This stream has already reached the end of the stream, and the
        // sample queue is empty.
        hr = MF_E_END_OF_STREAM;
        goto done;
    }

    hr = m_Requests.InsertBack(pToken);
    if (FAILED(hr))
    {
        goto done;
    }

    // Dispatch the request.
    hr = DispatchSamples();
    if (FAILED(hr))
    {
        goto done;
    }

done:
    if (FAILED(hr) && (m_state != STATE_SHUTDOWN))
    {
        // An error occurred. Send an MEError even from the source,
        // unless the source is already shut down.
        hr = m_pSource->QueueEvent(MEError, GUID_NULL, hr, NULL);
    }
    return hr;
}
```



The `DispatchSamples` method pulls samples from the sample queue, matches them with pending sample requests, and queues [MEMediaSample](memediasample.md) events:


```C++
HRESULT MPEG1Stream::DispatchSamples()
{
    HRESULT hr = S_OK;
    BOOL bNeedData = FALSE;
    BOOL bEOS = FALSE;

    SourceLock lock(m_pSource);

    // An I/O request can complete after the source is paused, stopped, or
    // shut down. Do not deliver samples unless the source is running.
    if (m_state != STATE_STARTED)
    {
        return S_OK;
    }

    IMFSample *pSample = NULL;
    IUnknown  *pToken = NULL;

    // Deliver as many samples as we can.
    while (!m_Samples.IsEmpty() && !m_Requests.IsEmpty())
    {
        // Pull the next sample from the queue.
        hr = m_Samples.RemoveFront(&pSample);
        if (FAILED(hr))
        {
            goto done;
        }

        // Pull the next request token from the queue. Tokens can be NULL.
        hr = m_Requests.RemoveFront(&pToken);
        if (FAILED(hr))
        {
            goto done;
        }

        if (pToken)
        {
            // Set the token on the sample.
            hr = pSample->SetUnknown(MFSampleExtension_Token, pToken);
            if (FAILED(hr))
            {
                goto done;
            }
        }

        // Send an MEMediaSample event with the sample.
        hr = m_pEventQueue->QueueEventParamUnk(
            MEMediaSample, GUID_NULL, S_OK, pSample);

        if (FAILED(hr))
        {
            goto done;
        }

        SafeRelease(&pSample);
        SafeRelease(&pToken);
    }

    if (m_Samples.IsEmpty() && m_bEOS)
    {
        // The sample queue is empty AND we have reached the end of the source
        // stream. Notify the pipeline by sending the end-of-stream event.

        hr = m_pEventQueue->QueueEventParamVar(
            MEEndOfStream, GUID_NULL, S_OK, NULL);

        if (FAILED(hr))
        {
            goto done;
        }

        // Notify the source. It will send the end-of-presentation event.
        hr = m_pSource->QueueAsyncOperation(SourceOp::OP_END_OF_STREAM);
        if (FAILED(hr))
        {
            goto done;
        }
    }
    else if (NeedsData())
    {
        // The sample queue is empty; the request queue is not empty; and we
        // have not reached the end of the stream. Ask for more data.
        hr = m_pSource->QueueAsyncOperation(SourceOp::OP_REQUEST_DATA);
        if (FAILED(hr))
        {
            goto done;
        }
    }

done:
    if (FAILED(hr) && (m_state != STATE_SHUTDOWN))
    {
        // An error occurred. Send an MEError even from the source,
        // unless the source is already shut down.
        m_pSource->QueueEvent(MEError, GUID_NULL, hr, NULL);
    }

    SafeRelease(&pSample);
    SafeRelease(&pToken);
    return S_OK;
}
```



The `DispatchSamples` method is called in the following circumstances:

-   Inside the [**RequestSample**](/windows/desktop/api/mfidl/nf-mfidl-imfmediastream-requestsample) method.
-   When the media source restarts from the paused state.
-   When an I/O request completes.

## End of Stream

When a stream has no more data, and all of the samples for that stream have been delivered, the stream objects sends an [MEEndOfStream](meendofstream.md) event.

When all of the active streams are done, the media source sends an [MEEndOfPresentation](meendofpresentation.md) event.

## Asynchronous Operations

Perhaps the hardest part of writing a media source is understanding the Media Foundation asynchronous model.

All of the methods on a media source that control streaming are asynchronous. In each case, the method does some initial validation, such as checking parameters. The source then dispatches the rest of the work to a work queue. After the operation completes, the media source sends an event back to the caller, through the media source's [**IMFMediaEventGenerator**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) interface. It is therefore important to understand work queues.

To put an item on a work queue, you can call either [**MFPutWorkItem**](/windows/desktop/api/mfapi/nf-mfapi-mfputworkitem) or [**MFPutWorkItemEx**](/windows/desktop/api/mfapi/nf-mfapi-mfputworkitemex). The MPEG-1 source happens to use **MFPutWorkItem**, but the two functions do the same thing. The **MFPutWorkItem** function takes the following parameters:

-   A **DWORD** value that identifies the work queue. You can create a private work queue or use **MFASYNC\_CALLBACK\_QUEUE\_STANDARD**.
-   A pointer to the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface. This callback interface is invoked to perform the work.
-   An optional state object, which must implement **IUnknown**.

The work queue is serviced by one or more worker threads that continuously pull the next work item from the queue and invoke the [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method of the callback interface.

Work items are not guaranteed to execute in the same order that you put them on the queue. Remember that more than one thread can service the same work queue, so [**Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) calls can overlap or occur out of order. Therefore, it is up to the media source to maintain the correct internal state, by submitting work queue items in the right order. Only when the previous operation is complete does the source start the next operation.

To represent pending operations, the MPEG-1 source defines a class named `SourceOp`:


```C++
// Represents a request for an asynchronous operation.

class SourceOp : public IUnknown
{
public:

    enum Operation
    {
        OP_START,
        OP_PAUSE,
        OP_STOP,
        OP_REQUEST_DATA,
        OP_END_OF_STREAM
    };

    static HRESULT CreateOp(Operation op, SourceOp **ppOp);
    static HRESULT CreateStartOp(IMFPresentationDescriptor *pPD, SourceOp **ppOp);

    // IUnknown
    STDMETHODIMP QueryInterface(REFIID iid, void** ppv);
    STDMETHODIMP_(ULONG) AddRef();
    STDMETHODIMP_(ULONG) Release();

    SourceOp(Operation op);
    virtual ~SourceOp();

    HRESULT SetData(const PROPVARIANT& var);

    Operation Op() const { return m_op; }
    const PROPVARIANT& Data() { return m_data;}

protected:
    long        m_cRef;     // Reference count.
    Operation   m_op;
    PROPVARIANT m_data;     // Data for the operation.
};
```



The `Operation` enumeration identifies which operation is pending. The class also contains a **PROPVARIANT** to convey any additional data for the operation.

### Operation Queue

To serialize operations, the media source maintains a queue of `SourceOp` objects. It uses a helper class to manage the queue:


```C++
template <class OP_TYPE>
class OpQueue : public IUnknown
{
public:

    typedef ComPtrList<OP_TYPE>   OpList;

    HRESULT QueueOperation(OP_TYPE *pOp);

protected:

    HRESULT ProcessQueue();
    HRESULT ProcessQueueAsync(IMFAsyncResult *pResult);

    virtual HRESULT DispatchOperation(OP_TYPE *pOp) = 0;
    virtual HRESULT ValidateOperation(OP_TYPE *pOp) = 0;

    OpQueue(CRITICAL_SECTION& critsec)
        : m_OnProcessQueue(this, &OpQueue::ProcessQueueAsync),
          m_critsec(critsec)
    {
    }

    virtual ~OpQueue()
    {
    }

protected:
    OpList                  m_OpQueue;         // Queue of operations.
    CRITICAL_SECTION&       m_critsec;         // Protects the queue state.
    AsyncCallback<OpQueue>  m_OnProcessQueue;  // ProcessQueueAsync callback.
};
```



The `OpQueue` class is designed to be inherited by the component that performs asynchronous work items. The *OP\_TYPE* template parameter is the object type used to represent work items in the queue—in this case, *OP\_TYPE* will be `SourceOp`. The `OpQueue` class implements the following methods:

-   `QueueOperation` puts a new item on the queue.
-   `ProcessQueue` dispatches the next operation from the queue. This method is asynchronous.
-   `ProcessQueueAsync` completes the asynchronous `ProcessQueue` method.

Another two methods must be implemented by the derived class:

-   `ValidateOperation` checks whether it is valid to perform a specified operation, given the current state of the media source.
-   `DispatchOperation` carries out the asynchronous work item.

The operation queue is used as follows:

1.  The Media Foundation pipeline calls an asynchronous method on the media source, such as [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start).
2.  The asynchronous method calls `QueueOperation`, which puts the [**Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start) operation on the queue and calls `ProcessQueue` (in the form of a `SourceOp` object).
3.  `ProcessQueue` calls [**MFPutWorkItem**](/windows/desktop/api/mfapi/nf-mfapi-mfputworkitem).
4.  The work-queue thread calls `ProcessQueueAsync`.
5.  The `ProcessQueueAsync` method calls `ValidateOperation` and `DispatchOperation`.

The following code queues a new operation on the MPEG-1 source:


```C++
template <class OP_TYPE>
HRESULT OpQueue<OP_TYPE>::QueueOperation(OP_TYPE *pOp)
{
    HRESULT hr = S_OK;

    EnterCriticalSection(&m_critsec);

    hr = m_OpQueue.InsertBack(pOp);
    if (SUCCEEDED(hr))
    {
        hr = ProcessQueue();
    }

    LeaveCriticalSection(&m_critsec);
    return hr;
}
```



The following code processes the queue:


```C++
template <class OP_TYPE>
HRESULT OpQueue<OP_TYPE>::ProcessQueue()
{
    HRESULT hr = S_OK;
    if (m_OpQueue.GetCount() > 0)
    {
        hr = MFPutWorkItem(
            MFASYNC_CALLBACK_QUEUE_STANDARD,    // Use the standard work queue.
            &m_OnProcessQueue,                  // Callback method.
            NULL                                // State object.
            );
    }
    return hr;
}
```



The `ValidateOperation` method checks whether the MPEG-1 source can dispatch the next operation in the queue. If another operation is in progress, `ValidateOperation` returns **MF\_E\_NOTACCEPTING**. This ensures that `DispatchOperation` is not called while there is another operation pending.


```C++
HRESULT MPEG1Source::ValidateOperation(SourceOp *pOp)
{
    if (m_pCurrentOp != NULL)
    {
        return MF_E_NOTACCEPTING;
    }
    return S_OK;
}
```



The DispatchOperation method switches on the operation type:


```C++
//-------------------------------------------------------------------
// DispatchOperation
//
// Performs the asynchronous operation indicated by pOp.
//
// NOTE:
// This method implements the pure-virtual OpQueue::DispatchOperation
// method. It is always called from a work-queue thread.
//-------------------------------------------------------------------

HRESULT MPEG1Source::DispatchOperation(SourceOp *pOp)
{
    EnterCriticalSection(&m_critSec);

    HRESULT hr = S_OK;

    if (m_state == STATE_SHUTDOWN)
    {
        LeaveCriticalSection(&m_critSec);

        return S_OK; // Already shut down, ignore the request.
    }

    switch (pOp->Op())
    {

    // IMFMediaSource methods:

    case SourceOp::OP_START:
        hr = DoStart((StartOp*)pOp);
        break;

    case SourceOp::OP_STOP:
        hr = DoStop(pOp);
        break;

    case SourceOp::OP_PAUSE:
        hr = DoPause(pOp);
        break;

    // Operations requested by the streams:

    case SourceOp::OP_REQUEST_DATA:
        hr = OnStreamRequestSample(pOp);
        break;

    case SourceOp::OP_END_OF_STREAM:
        hr = OnEndOfStream(pOp);
        break;

    default:
        hr = E_UNEXPECTED;
    }

    if (FAILED(hr))
    {
        StreamingError(hr);
    }

    LeaveCriticalSection(&m_critSec);
    return hr;
}
```



To summarize:

1.  The pipeline calls an asynchronous method, such as [**IMFMediaSource::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-start).
2.  The asynchronous method calls `OpQueue::QueueOperation`, passing in a pointer to a `SourceOp` object.
3.  The `QueueOperation` method puts the operation on the *m\_OpQueue* queue and calls `OpQueue::ProcessQueue`.
4.  The `ProcessQueue` method calls [**MFPutWorkItem**](/windows/desktop/api/mfapi/nf-mfapi-mfputworkitem). From this point, everything happens on a Media Foundation work-queue thread. The asynchronous method returns to the caller.
5.  The work-queue thread calls the `OpQueue::ProcessQueueAsync` method.
6.  The `ProcessQueueAsync` method calls `MPEG1Source:ValidateOperation` to validate the operation.
7.  The `ProcessQueueAsync` method calls `MPEG1Source::DispatchOperation` to process the operation.

There are several benefits to this design:

-   Methods are asynchronous, so they do not block the calling application's thread.
-   Operations are dispatched on a Media Foundation work-queue thread, which is shared among pipeline components. Therefore, the media source does not create its own thread, reducing the total number of threads that are created.
-   The media source does not block while waiting for operations to complete. This reduces the chance that a media source will accidentally cause a deadlock, and helps to reduce context switching.
-   The media source can use asynchronous I/O to read the source file (by calling [**IMFByteStream::BeginRead**](/windows/desktop/api/mfobjects/nf-mfobjects-imfbytestream-beginread)). The media source does not need to block while waiting for I/O routine complete.

If you follow the pattern shown in the SDK sample, you can focus on the particular details of your media source.

## Related topics

<dl> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Writing a Custom Media Source](writing-a-custom-media-source.md)
</dt> </dl>

 

 



