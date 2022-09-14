---
description: Uncompressed Video Media Types
ms.assetid: 50bf2947-27ee-4092-9d3a-a1c13ee80e95
title: Uncompressed Video Media Types
ms.topic: article
ms.date: 05/31/2018
---

# Uncompressed Video Media Types

This topic describes how to create a media type that describes an uncompressed video format. For more information about media types generally, see [About Media Types](about-media-types.md).

To create a complete uncompressed video type, set the following attributes on the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface pointer.



| Attribute                                                                            | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_MT\_MAJOR\_TYPE**](mf-mt-major-type-attribute.md)                            | Major type. Set to **MFMediaType\_Video**.                                                                                                                                                                                          |
| [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)                                   | Subtype. See [Video Subtype GUIDs](video-subtype-guids.md).                                                                                                                                                                        |
| [**MF\_MT\_DEFAULT\_STRIDE**](mf-mt-default-stride-attribute.md)                    | Surface stride. The *stride* is the number of bytes needed to go from one row of pixels to the next. Set this attribute if the stride in bytes is not the same as the video width in bytes. Otherwise, you can omit this attribute. |
| [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md)                            | Frame rate.                                                                                                                                                                                                                         |
| [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md)                            | Frame size.                                                                                                                                                                                                                         |
| [**MF\_MT\_INTERLACE\_MODE**](mf-mt-interlace-mode-attribute.md)                    | Interlacing mode.                                                                                                                                                                                                                   |
| [**MF\_MT\_ALL\_SAMPLES\_INDEPENDENT**](mf-mt-all-samples-independent-attribute.md) | Specifies whether each sample is independent. Set to **TRUE** for uncompressed formats.                                                                                                                                             |
| [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md)           | Pixel aspect ratio.                                                                                                                                                                                                                 |



 

In addition, set the following attributes if you know the correct values. (Otherwise, omit these attributes.)



| Attribute                                                                    | Description        |
|------------------------------------------------------------------------------|--------------------|
| [**MF\_MT\_VIDEO\_PRIMARIES**](mf-mt-video-primaries-attribute.md)          | Color primaries.   |
| [**MF\_MT\_TRANSFER\_FUNCTION**](mf-mt-transfer-function-attribute.md)      | Transfer function. |
| [**MF\_MT\_YUV\_MATRIX**](mf-mt-yuv-matrix-attribute.md)                    | Transfer matrix.   |
| [**MF\_MT\_VIDEO\_CHROMA\_SITING**](mf-mt-video-chroma-siting-attribute.md) | Chroma siting.     |
| [**MF\_MT\_VIDEO\_NOMINAL\_RANGE**](mf-mt-video-nominal-range-attribute.md) | Nominal range.     |



 

For more information, see [Extended Color Information](extended-color-information.md). For example, if you create a media type that describes a video standard, and the standard defines the chroma siting, add this information to the media type. Doing so helps to preserve color fidelity throughout the pipeline.

The following functions might be useful when creating a video media type.



| Function                                                                     | Description                                                                                                                                                                          |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MFAverageTimePerFrameToFrameRate**](/windows/desktop/api/mfapi/nf-mfapi-mfaveragetimeperframetoframerate) | Calculates the frame rate, given the average frame duration.                                                                                                                         |
| [**MFCalculateImageSize**](/windows/desktop/api/mfapi/nf-mfapi-mfcalculateimagesize)                         | Calculates the image size for an uncompressed video format.                                                                                                                          |
| [**MFFrameRateToAverageTimePerFrame**](/windows/desktop/api/mfapi/nf-mfapi-mfframeratetoaveragetimeperframe) | Calculates the average duration of a video frame, given the frame rate.                                                                                                              |
| [**MFGetStrideForBitmapInfoHeader**](/windows/desktop/api/mfapi/nf-mfapi-mfgetstrideforbitmapinfoheader)     | Returns the minimum surface stride for a video format. For more information, see [Image Stride](image-stride.md).                                                                   |
| [**MFInitVideoFormat**](/windows/desktop/api/mfapi/nf-mfapi-mfinitvideoformat)                               | Initializes an [**MFVIDEOFORMAT**](/windows/desktop/api/mfobjects/ns-mfobjects-mfvideoformat) structure for some standard video formats, such as NTSC television. You can then use the structure to initialize a media type. |
| [**MFIsFormatYUV**](/windows/desktop/api/mfapi/nf-mfapi-mfisformatyuv)                                       | Queries whether a video format is a YUV format.                                                                                                                                      |



 

## Examples

This example shows a function that fills in the most common information for an uncompressed video format. The function returns an [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface pointer. You can then add additional attributes to the media type as needed.


```C++
HRESULT CreateUncompressedVideoType(
    DWORD                fccFormat,  // FOURCC or D3DFORMAT value.     
    UINT32               width, 
    UINT32               height,
    MFVideoInterlaceMode interlaceMode,
    const MFRatio&       frameRate,
    const MFRatio&       par,
    IMFMediaType         **ppType
    )
{
    if (ppType == NULL)
    {
        return E_POINTER;
    }

    GUID    subtype = MFVideoFormat_Base;
    LONG    lStride = 0;
    UINT    cbImage = 0;

    IMFMediaType *pType = NULL;

    // Set the subtype GUID from the FOURCC or D3DFORMAT value.
    subtype.Data1 = fccFormat;

    HRESULT hr = MFCreateMediaType(&pType);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pType->SetGUID(MF_MT_MAJOR_TYPE, MFMediaType_Video);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pType->SetGUID(MF_MT_SUBTYPE, subtype);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pType->SetUINT32(MF_MT_INTERLACE_MODE, interlaceMode);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = MFSetAttributeSize(pType, MF_MT_FRAME_SIZE, width, height);
    if (FAILED(hr))
    {
        goto done;
    }

    // Calculate the default stride value.
    hr = pType->SetUINT32(MF_MT_DEFAULT_STRIDE, UINT32(lStride));
    if (FAILED(hr))
    {
        goto done;
    }

    // Calculate the image size in bytes.
    hr = MFCalculateImageSize(subtype, width, height, &cbImage);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pType->SetUINT32(MF_MT_SAMPLE_SIZE, cbImage);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pType->SetUINT32(MF_MT_FIXED_SIZE_SAMPLES, TRUE);
    if (FAILED(hr))
    {
        goto done;
    }

    hr = pType->SetUINT32(MF_MT_ALL_SAMPLES_INDEPENDENT, TRUE);
    if (FAILED(hr))
    {
        goto done;
    }

    // Frame rate
    hr = MFSetAttributeRatio(pType, MF_MT_FRAME_RATE, frameRate.Numerator, 
        frameRate.Denominator);
    if (FAILED(hr))
    {
        goto done;
    }

    // Pixel aspect ratio
    hr = MFSetAttributeRatio(pType, MF_MT_PIXEL_ASPECT_RATIO, par.Numerator, 
        par.Denominator);
    if (FAILED(hr))
    {
        goto done;
    }

    // Return the pointer to the caller.
    *ppType = pType;
    (*ppType)->AddRef();

done:
    SafeRelease(&pType);
    return hr;
}
```



The next example takes an encoded video format as input, and creates a matching uncompressed video type. This type would be suitable to set on an encoder or decoder, for example.


```C++
HRESULT ConvertVideoTypeToUncompressedType(
    IMFMediaType *pType,    // Pointer to an encoded video type.
    const GUID& subtype,    // Uncompressed subtype (eg, RGB-32, AYUV)
    IMFMediaType **ppType   // Receives a matching uncompressed video type.
    )
{
    IMFMediaType *pTypeUncomp = NULL;

    HRESULT hr = S_OK;
    GUID majortype = { 0 };
    MFRatio par = { 0 };

    hr = pType->GetMajorType(&majortype);

    if (majortype != MFMediaType_Video)
    {
        return MF_E_INVALIDMEDIATYPE;
    }

    // Create a new media type and copy over all of the items.
    // This ensures that extended color information is retained.

    if (SUCCEEDED(hr))
    {
        hr = MFCreateMediaType(&pTypeUncomp);
    }

    if (SUCCEEDED(hr))
    {
        hr = pType->CopyAllItems(pTypeUncomp);
    }

    // Set the subtype.
    if (SUCCEEDED(hr))
    {
        hr = pTypeUncomp->SetGUID(MF_MT_SUBTYPE, subtype);
    }

    // Uncompressed means all samples are independent.
    if (SUCCEEDED(hr))
    {
        hr = pTypeUncomp->SetUINT32(MF_MT_ALL_SAMPLES_INDEPENDENT, TRUE);
    }

    // Fix up PAR if not set on the original type.
    if (SUCCEEDED(hr))
    {
        hr = MFGetAttributeRatio(
            pTypeUncomp, 
            MF_MT_PIXEL_ASPECT_RATIO, 
            (UINT32*)&par.Numerator, 
            (UINT32*)&par.Denominator
            );

        // Default to square pixels.
        if (FAILED(hr))
        {
            hr = MFSetAttributeRatio(
                pTypeUncomp, 
                MF_MT_PIXEL_ASPECT_RATIO, 
                1, 1
                );
        }
    }

    if (SUCCEEDED(hr))
    {
        *ppType = pTypeUncomp;
        (*ppType)->AddRef();
    }

    SafeRelease(&pTypeUncomp);
    return hr;
}
```



## Related topics

<dl> <dt>

[Extended Color Information](extended-color-information.md)
</dt> <dt>

[Image Stride](image-stride.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> <dt>

[Video Media Types](video-media-types.md)
</dt> <dt>

[Video Subtype GUIDs](video-subtype-guids.md)
</dt> </dl>

 

 



