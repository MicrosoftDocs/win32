---
description: A video capture device might support several capture formats. Formats typically differ by compression type, color space (YUV or RGB), frame size, or frame rate.
ms.assetid: 479abaea-f310-4139-9967-f24b03c34558
title: How to Set the Video Capture Format
ms.topic: article
ms.date: 05/31/2018
---

# How to Set the Video Capture Format

A video capture device might support several capture formats. Formats typically differ by compression type, color space (YUV or RGB), frame size, or frame rate.

The list of supported formats is contained in the *presentation descriptor*. For more information, see [Presentation Descriptors](presentation-descriptors.md).

To enumerate the supported formats:

1.  Create the media source for the capture device. See [Enumerating Video Capture Devices](enumerating-video-capture-devices.md).
2.  Call [**IMFMediaSource::CreatePresentationDescriptor**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasource-createpresentationdescriptor) on the media source to get the presentation descriptor.
3.  Call [**IMFPresentationDescriptor::GetStreamDescriptorByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfpresentationdescriptor-getstreamdescriptorbyindex) to get the stream descriptor for the video stream.
4.  Call [**IMFStreamDescriptor::GetMediaTypeHandler**](/windows/desktop/api/mfidl/nf-mfidl-imfstreamdescriptor-getmediatypehandler) on the stream descriptor.
5.  Call [**IMFMediaTypeHandler::GetMediaTypeCount**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-getmediatypecount) to get the number of supported formats.
6.  In a loop, call [**IMFMediaTypeHandler::GetMediaTypeByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-getmediatypebyindex) to get each format. The format is represented by a *media type*. For more information, see [Video Media Types](video-media-types.md).

The following example enumerates the capture formats for a device:


```C++
HRESULT EnumerateCaptureFormats(IMFMediaSource *pSource)
{
    IMFPresentationDescriptor *pPD = NULL;
    IMFStreamDescriptor *pSD = NULL;
    IMFMediaTypeHandler *pHandler = NULL;
    IMFMediaType *pType = NULL;

    HRESULT hr = pSource->CreatePresentationDescriptor(&pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    BOOL fSelected;
    hr = pPD->GetStreamDescriptorByIndex(0, &fSelected, &pSD);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSD->GetMediaTypeHandler(&pHandler);
    if (FAILED(hr))
    {
        goto done;
    }

    DWORD cTypes = 0;
    hr = pHandler->GetMediaTypeCount(&cTypes);
    if (FAILED(hr))
    {
        goto done;
    }

    for (DWORD i = 0; i < cTypes; i++)
    {
        hr = pHandler->GetMediaTypeByIndex(i, &pType);
        if (FAILED(hr))
        {
            goto done;
        }

        LogMediaType(pType);
        OutputDebugString(L"\n");

        SafeRelease(&pType);
    }

done:
    SafeRelease(&pPD);
    SafeRelease(&pSD);
    SafeRelease(&pHandler);
    SafeRelease(&pType);
    return hr;
}
```



The `LogMediaType` function used in this example is listed in the topic [Media Type Debugging Code](media-type-debugging-code.md).

To set the capture format:

1.  Get a pointer to the [**IMFMediaTypeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfmediatypehandler) interface, as shown in the previous example.
2.  Call [**IMFMediaTypeHandler::GetMediaTypeByIndex**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-getmediatypebyindex) to get the desired format, specified by index.
3.  Call [**IMFMediaTypeHandler::SetCurrentMediaType**](/windows/desktop/api/mfidl/nf-mfidl-imfmediatypehandler-setcurrentmediatype) to set the format.

If you do not set the capture format, the device will use its default format.

The following example sets the capture format:


```C++
HRESULT SetDeviceFormat(IMFMediaSource *pSource, DWORD dwFormatIndex)
{
    IMFPresentationDescriptor *pPD = NULL;
    IMFStreamDescriptor *pSD = NULL;
    IMFMediaTypeHandler *pHandler = NULL;
    IMFMediaType *pType = NULL;

    HRESULT hr = pSource->CreatePresentationDescriptor(&pPD);
    if (FAILED(hr))
    {
        goto done;
    }

    BOOL fSelected;
    hr = pPD->GetStreamDescriptorByIndex(0, &fSelected, &pSD);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pSD->GetMediaTypeHandler(&pHandler);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pHandler->GetMediaTypeByIndex(dwFormatIndex, &pType);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pHandler->SetCurrentMediaType(pType);

done:
    SafeRelease(&pPD);
    SafeRelease(&pSD);
    SafeRelease(&pHandler);
    SafeRelease(&pType);
    return hr;
}
```



The order in which formats are returned depends on the device. Typically, they are grouped first by compression type or color space; and then from smallest frame size to largest frame size within each group.

The frame rate is handled slightly differently than the other format attributes. For more information, see [How to Set the Video Capture Frame Rate](how-to-set-the-video-capture-frame-rate.md).

> [!Note]  
> In some devices, the format list will contain a duplicate entry for each format. For example, if the device supports 15 distinct capture formats, the list will contain 30 entries. Within each pair, one of the media types will have the attribute [**MF\_MT\_AM\_FORMAT\_TYPE**](mf-mt-am-format-type-attribute.md) equal to **FORMAT\_VideoInfo**, and the other will have **MF\_MT\_AM\_FORMAT\_TYPE** equal to **FORMAT\_VideoInfo2**. (These two values are defined in the header file uuids.h.) The second type might also contain additional color information ([Extended Color Information](extended-color-information.md)) or show a different value for interlacing ([**MF\_MT\_INTERLACE\_MODE**](mf-mt-interlace-mode-attribute.md)). These duplicate types exist to support older DirectShow applications. In a Media Foundation application, you should ignore the **FORMAT\_VideoInfo** type whenever a duplicate **FORMAT\_VideoInfo2** type is listed.

 

## Related topics

<dl> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



