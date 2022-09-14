---
description: Step 3A.
ms.assetid: 774fcb12-8928-4667-8ef6-dce86717cc29
title: Step 3A. Implement the CheckInputType Method
ms.topic: article
ms.date: 05/31/2018
---

# Step 3A. Implement the CheckInputType Method

This is step 3A of the tutorial [Writing Transform Filters](writing-transform-filters.md).

The [**CTransformFilter::CheckInputType**](ctransformfilter-checkinputtype.md) method is called when the upstream filter proposes a media type to the transform filter. This method takes a pointer to a [**CMediaType**](cmediatype.md) object, which is a thin wrapper for the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. In this method, you should examine every relevant field of the **AM\_MEDIA\_TYPE** structure, including the fields in the format block. You can use the accessor methods defined in **CMediaType**, or reference the structure members directly. If any field is not valid, return VFW\_E\_TYPE\_NOT\_ACCEPTED. If the entire media type is valid, return S\_OK.

For example, in the RLE encoder filter, the input type must be 8-bit or 4-bit uncompressed RGB video. There is no reason to support other input formats, such as 16- or 24-bit RGB, because the filter would have to convert them to a lower bit depth, and DirectShow already provides a [Color Space Converter](color-space-converter-filter.md) filter for that purpose. The following example assumes that the encoder supports 8-bit video but not 4-bit video:


```C++
HRESULT CRleFilter::CheckInputType(const CMediaType *mtIn)
{
    if ((mtIn->majortype != MEDIATYPE_Video) ||
        (mtIn->subtype != MEDIASUBTYPE_RGB8) ||
        (mtIn->formattype != FORMAT_VideoInfo) || 
        (mtIn->cbFormat < sizeof(VIDEOINFOHEADER)))
    {
        return VFW_E_TYPE_NOT_ACCEPTED;
    }

    VIDEOINFOHEADER *pVih = 
        reinterpret_cast<VIDEOINFOHEADER*>(mtIn->pbFormat);
    if ((pVih->bmiHeader.biBitCount != 8) ||
        (pVih->bmiHeader.biCompression != BI_RGB))
    {
        return VFW_E_TYPE_NOT_ACCEPTED;
    }

    // Check the palette table.
    if (pVih->bmiHeader.biClrUsed > PALETTE_ENTRIES(pVih))
    {
        return VFW_E_TYPE_NOT_ACCEPTED;
    }
    DWORD cbPalette = pVih->bmiHeader.biClrUsed * sizeof(RGBQUAD);
    if (mtIn->cbFormat < sizeof(VIDEOINFOHEADER) + cbPalette)
    {
        return VFW_E_TYPE_NOT_ACCEPTED;
    }

    // Everything is good.
    return S_OK;
}
```



In this example, the method first checks the major type and subtype. Then it checks the format type, to make sure the format block is a [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure. The filter could also support [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2), but in this case there would be no real benefit. The **VIDEOINFOHEADER2** structure adds support for interlacing and non-square pixels, which are not likely to be relevant in 8-bit video.

If the format type is correct, the example checks the **biBitCount** and **biCompression** members of the **VIDEOINFOHEADER** structure, to verify that the format is 8-bit uncompressed RGB. As this example shows, you must coerce the


```C++
pbFormat
```



pointer to the correct structure, based on the format type. Always check the format type GUID (**formattype**) and the size of the format block (**cbFormat**) before casting the pointer.

The example also verifies that the number of palette entries is compatible with the bit depth and the format block is large enough to hold the palette entries. If all of this information is correct, the method returns S\_OK.

Next: [Step 3B. Implement the GetMediaType Method](step-3b--implement-the-getmediatype-method.md).

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



