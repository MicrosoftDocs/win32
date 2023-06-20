---
description: Step 3B.
ms.assetid: 0ec57083-b192-404a-938f-bc6bb1cf0ddb
title: Step 3B. Implement the GetMediaType Method
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 3B. Implement the GetMediaType Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is step 3B of the tutorial [Writing Transform Filters](writing-transform-filters.md).

> [!Note]  
> This step is not required for filters that derive from **CTransInPlaceFilter**.

 

The [**CTransformFilter::GetMediaType**](ctransformfilter-getmediatype.md) method returns one of the filter's preferred output types, referenced by index number. This method is never called unless the filter's input pin is already connected. Therefore, you can use the media type from the upstream connection to determine the preferred output types.

An encoder typically offers a single preferred type, representing the target format. Decoders generally support a range of output formats, and offer them in order of descending quality or efficiency. For example, the list might be UYVY, Y211, RGB-24, RGB-565, RGB-555, and RGB-8, in that order. Effect filters may require an exact match between the output format and the input format.

The following example returns a single output type, which is constructed by modifying the input type to specify RLE8 compression:


```C++
HRESULT CRleFilter::GetMediaType(int iPosition, CMediaType *pMediaType)
{
    ASSERT(m_pInput->IsConnected());
    if (iPosition < 0)
    {
        return E_INVALIDARG;
    }
    if (iPosition == 0)
    {
        HRESULT hr = m_pInput->ConnectionMediaType(pMediaType);
        if (FAILED(hr))
        {
            return hr;
        }
        FOURCCMap fccMap = FCC('MRLE'); 
        pMediaType->subtype = static_cast<GUID>(fccMap);
        pMediaType->SetVariableSize();
        pMediaType->SetTemporalCompression(FALSE);

        ASSERT(pMediaType->formattype == FORMAT_VideoInfo);
        VIDEOINFOHEADER *pVih =
            reinterpret_cast<VIDEOINFOHEADER*>(pMediaType->pbFormat);
        pVih->bmiHeader.biCompression = BI_RLE8;
        pVih->bmiHeader.biSizeImage = DIBSIZE(pVih->bmiHeader); 
        return S_OK;
    }
    // else
    return VFW_S_NO_MORE_ITEMS;
}
```



In this example, the method calls [**IPin::ConnectionMediaType**](/windows/desktop/api/Strmif/nf-strmif-ipin-connectionmediatype) to get the input type from the input pin. Then it changes some of the fields to indicate the compression format, as follows:

-   It assigns a new subtype GUID, which is constructed from the FOURCC code 'MRLE', using the [**FOURCCMap**](fourccmap.md) class.
-   It calls the [**CMediaType::SetVariableSize**](cmediatype-setvariablesize.md) method, which sets the **bFixedSizeSamples** flag to **FALSE** and the **lSampleSize** member to zero, indicating variable-sized samples.
-   It calls the [**CMediaType::SetTemporalCompression**](cmediatype-settemporalcompression.md) method with the value **FALSE**, indicating that every frame is a key frame. (This field is informational only, so you could safely ignore it.)
-   It sets the **biCompression** field to BI\_RLE8.
-   It sets the **biSizeImage** field to the image size.

Next: [Step 3C. Implement the CheckTransform Method](step-3c--implement-the-checktransform-method.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



