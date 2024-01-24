---
description: Use this example to understand how the RLE encoder might implement the method as part of writing a transform filter.
ms.assetid: b7d878ab-523f-4b52-b98d-c9d4fa18ce8a
title: Step 5. Transform the Image
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 5. Transform the Image

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is step 5 of the tutorial [Writing Transform Filters](writing-transform-filters.md).

The upstream filter delivers media samples to the transform filter by calling the [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive) method on the transform filter's input pin. To process the data, the transform filter calls the **Transform** method, which is pure virtual. The **CTransformFilter** and **CTransInPlaceFilter** classes use two different versions of this method:

-   [**CTransformFilter::Transform**](ctransformfilter-transform.md) takes a pointer to the input sample and a pointer to the output sample. Before the filter calls the method, it copies the sample properties from the input sample to the output sample, including the time stamps.
-   [**CTransInPlaceFilter::Transform**](ctransinplacefilter-transform.md) takes a pointer to the input sample. The filter modifies the data in place.

If the **Transform** method returns S\_OK, the filter delivers the sample downstream. To skip a frame, return S\_FALSE. If there is a streaming error, return a failure code.

The following example shows how the RLE encoder might implement this method. Your own implementation might differ considerably, depending on what your filter does.


```C++
HRESULT CRleFilter::Transform(IMediaSample *pSource, IMediaSample *pDest)
{
    // Get pointers to the underlying buffers.
    BYTE *pBufferIn, *pBufferOut;
    hr = pSource->GetPointer(&pBufferIn);
    if (FAILED(hr))
    {
        return hr;
    }
    hr = pDest->GetPointer(&pBufferOut);
    if (FAILED(hr))
    {
        return hr;
    }
    // Process the data.
    DWORD cbDest = EncodeFrame(pBufferIn, pBufferOut);
    KASSERT((long)cbDest <= pDest->GetSize());

    pDest->SetActualDataLength(cbDest);
    pDest->SetSyncPoint(TRUE);
    return S_OK;
}
```



This example assumes that EncodeFrame is a private method that implements the RLE encoding. The encoding algorithm itself is not described here; for details, see the topic "Bitmap Compression" in the Platform SDK documentation.

First, the example calls [**IMediaSample::GetPointer**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getpointer) to retrieve the addresses of the underlying buffers. It passes these to the private EncoderFrame method. Then it calls [**IMediaSample::SetActualDataLength**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setactualdatalength) to specify the length of the encoded data. The downstream filter needs this information so that it can manage the buffer properly. Finally, the method calls [**IMediaSample::SetSyncPoint**](/windows/desktop/api/Strmif/nf-strmif-imediasample-setsyncpoint) to set the key frame flag to **TRUE**. Run-length encoding does not use any delta frames, so every frame is a key frame. For delta frames, set the value to **FALSE**.

Other issues that you must consider include:

-   Time stamps. The **CTransformFilter** class timestamps the output sample before calling the **Transform** method. It copies the time stamp values from the input sample, without modifying them. If your filter needs to change the time stamps, call [**IMediaSample::SetTime**](/windows/desktop/api/Strmif/nf-strmif-imediasample-settime) on the output sample.
-   Format changes. The upstream filter can change formats mid-stream by attaching a media type to the sample. Before doing so, it calls [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) on your filter's input pin. In the **CTransformFilter** class, this results in a call to **CheckInputType** followed by **CheckTransform**. The downstream filter can also change media types, using the same mechanism. In your own filter, there are two things to watch for:

    -   Make sure that **QueryAccept** does not return false acceptances.
    -   If your filter does accept format changes, check for them inside the **Transform** method by calling [**IMediaSample::GetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatype). If that method returns S\_OK, your filter must respond to the format change.

    For more information, see [Dynamic Format Changes](dynamic-format-changes.md).

-   Threads. In both **CTransformFilter** and **CTransInPlaceFilter**, the transform filter delivers output samples synchronously inside the **Receive** method. The filter does not create any worker threads to process the data. Typically, there is no reason for a transform filter to create worker threads.

Next: [Step 6. Add Support for COM](step-6--add-support-for-com.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



