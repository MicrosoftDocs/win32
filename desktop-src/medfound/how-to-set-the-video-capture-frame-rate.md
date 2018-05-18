---
Description: 'A video capture device might support a range of frame rates.'
ms.assetid: '9578e60d-0339-4382-b798-2d31d2ddbe76'
title: How to Set the Video Capture Frame Rate
---

# How to Set the Video Capture Frame Rate

A video capture device might support a range of frame rates. If this information is available, the minimum and maximum frame rates are stored as media type attributes:



| Attribute                                                         | Description         |
|-------------------------------------------------------------------|---------------------|
| [MF\_MT\_FRAME\_RATE\_RANGE\_MAX](mf-mt-frame-rate-range-max.md) | Maximum frame rate. |
| [MF\_MT\_FRAME\_RATE\_RANGE\_MIN](mf-mt-frame-rate-range-min.md) | Minimum frame rate. |



 

The range can vary depending on the capture format. For example, at larger frame sizes, the maximum frame rate might be reduced.

To set the frame rate:

1.  Create the media source for the capture device. See [Enumerating Video Capture Devices](enumerating-video-capture-devices.md).
2.  Call [**IMFMediaSource::CreatePresentationDescriptor**](imfmediasource-createpresentationdescriptor.md) on the media source to get the presentation descriptor.
3.  Call [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](imfpresentationdescriptor-getstreamdescriptorbyindex.md) to get the stream descriptor for the video stream.
4.  Call [**IMFStreamDescriptor::GetMediaTypeHandler**](imfstreamdescriptor-getmediatypehandler.md) on the stream descriptor.
5.  Enumerate the capture formats, as described in [How to Set the Video Capture Format](how-to-set-the-video-capture-format.md).
6.  Select the desired output format from the list.
7.  Query the media type for the [MF\_MT\_FRAME\_RATE\_RANGE\_MAX](mf-mt-frame-rate-range-max.md) and [MF\_MT\_FRAME\_RATE\_RANGE\_MIN](mf-mt-frame-rate-range-min.md) attributes. This values give the range of supported frame rates. The device might support other frame rates within this range.
8.  Set the [**MF\_MT\_FRAME**](mf-mt-frame-rate-attribute.md) attribute on the media type to specify the desired frame rate.
9.  Call [**IMFMediaTypeHandler::SetCurrentMediaType**](imfmediatypehandler-setcurrentmediatype.md) with the modified media type.

The following example sets the frame rate equal to the maximum frame rate that the device supports:


```C++
HRESULT SetMaxFrameRate(IMFMediaSource *pSource, DWORD dwTypeIndex)
{
    IMFPresentationDescriptor *pPD = NULL;
    IMFStreamDescriptor *pSD = NULL;
    IMFMediaTypeHandler *pHandler = NULL;
    IMFMediaType *pType = NULL;

    HRESULT hr = pSource->CreatePresentationDescriptor(&amp;pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    BOOL fSelected;
    hr = pPD->GetStreamDescriptorByIndex(dwTypeIndex, &amp;fSelected, &amp;pSD);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSD->GetMediaTypeHandler(&amp;pHandler);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pHandler->GetCurrentMediaType(&amp;pType);
    if (FAILED(hr))
    {
        goto done;
    }

    // Get the maximum frame rate for the selected capture format.

    // Note: To get the minimum frame rate, use the 
    // MF_MT_FRAME_RATE_RANGE_MIN attribute instead.

    PROPVARIANT var;
    if (SUCCEEDED(pType->GetItem(MF_MT_FRAME_RATE_RANGE_MAX, &amp;var)))
    {
        hr = pType->SetItem(MF_MT_FRAME_RATE, var);

        PropVariantClear(&amp;var);

        if (FAILED(hr))
        {
            goto done;
        }

        hr = pHandler->SetCurrentMediaType(pType);
    }

done:
    SafeRelease(&amp;pPD);
    SafeRelease(&amp;pSD);
    SafeRelease(&amp;pHandler);
    SafeRelease(&amp;pType);
    return hr;
}
```



## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



