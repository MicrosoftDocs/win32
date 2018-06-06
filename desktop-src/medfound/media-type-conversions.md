---
Description: Media Type Conversions
ms.assetid: 6aee18b8-79b1-47fb-816f-d1c2c77b3a03
title: Media Type Conversions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Media Type Conversions

Occasionally it is necessary to convert between Media Foundation media types and the older media type structures from DirectShow or the Windows Media Format SDK.

### From a Format Structure to a Media Foundation Type

The following functions initialize a Media Foundation media type from a format structure. These functions are also useful if a data stream or a file header contains a format structure. For example, the file header for WAVE audio files contains a [**WAVEFORMATEX**](https://msdn.microsoft.com/4f3bf6fb-b15f-43b3-82f1-e7a8a3007057) structure.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Structure to Convert</th>
<th>Function</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>AM_MEDIA_TYPE</strong>](https://msdn.microsoft.com/973697d0-2897-48b5-88ca-a88a9650eb02) (DirectShow)<br/> [<strong>DMO_MEDIA_TYPE</strong>](https://msdn.microsoft.com/c545ddf7-9797-45ab-a42a-d8550b598e98) (DirectX Media Objects) <br/> [<strong>WM_MEDIA_TYPE</strong>](https://msdn.microsoft.com/37a9ac59-e152-47e1-96ee-b816cd645936) (Windows Media Format SDK) <br/>
<blockquote>
[!Note]<br />
These structures are equivalent.
</blockquote>
<br/> <br/></td>
<td>[<strong>MFInitMediaTypeFromAMMediaType</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromammediatype)</td>
</tr>
<tr class="even">
<td>[<strong>BITMAPINFOHEADER</strong>](https://msdn.microsoft.com/153c08a8-d32c-4e9d-9da9-b915eb172327)</td>
<td>[<strong>MFCreateVideoMediaTypeFromBitMapInfoHeaderEx</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfcreatevideomediatypefrombitmapinfoheaderex)</td>
</tr>
<tr class="odd">
<td>[<strong>MFVIDEOFORMAT</strong>](/windows/desktop/api/mfobjects/ns-mfobjects-_mfvideoformat)</td>
<td>[<strong>MFInitMediaTypeFromMFVideoFormat</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefrommfvideoformat)</td>
</tr>
<tr class="even">
<td>[<strong>MPEG1VIDEOINFO</strong>](https://msdn.microsoft.com/ae5b8825-7c1c-4a44-b665-098732e6c3bc)</td>
<td>[<strong>MFInitMediaTypeFromMPEG1VideoInfo</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefrommpeg1videoinfo)</td>
</tr>
<tr class="odd">
<td>[<strong>MPEG2VIDEOINFO</strong>](https://msdn.microsoft.com/1a6ab686-99a1-40c2-addf-7fa215e2311a)</td>
<td>[<strong>MFInitMediaTypeFromMPEG2VideoInfo</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefrommpeg2videoinfo)</td>
</tr>
<tr class="even">
<td>[<strong>VIDEOINFOHEADER2</strong>](https://msdn.microsoft.com/5e3d5bf0-435f-45da-8409-a1463b56a7ae)</td>
<td>[<strong>MFInitMediaTypeFromVideoInfoHeader2</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromvideoinfoheader2)</td>
</tr>
<tr class="odd">
<td>[<strong>VIDEOINFOHEADER</strong>](https://msdn.microsoft.com/a175592b-0dc1-4001-b52f-785407965932)</td>
<td>[<strong>MFInitMediaTypeFromVideoInfoHeader</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromvideoinfoheader)</td>
</tr>
<tr class="even">
<td>[<strong>WAVEFORMATEX</strong>](https://msdn.microsoft.com/4f3bf6fb-b15f-43b3-82f1-e7a8a3007057) or [<strong>WAVEFORMATEXTENSIBLE</strong>](https://msdn.microsoft.com/b16cdcab-fa4f-4c9a-b1f3-af459bd33245)</td>
<td>[<strong>MFInitMediaTypeFromWaveFormatEx</strong>](/windows/desktop/api/mfapi/nf-mfapi-mfinitmediatypefromwaveformatex)</td>
</tr>
</tbody>
</table>



 

### From a Media Foundation Type to a Format Structure

The following functions create or initialize a format structure from a Media Foundation media type.



| Function                                                                             | Target Structure                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMFMediaType::GetRepresentation**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediatype-getrepresentation)            | [**AM\_MEDIA\_TYPE**](https://msdn.microsoft.com/973697d0-2897-48b5-88ca-a88a9650eb02), [**MFVIDEOFORMAT**](/windows/desktop/api/mfobjects/ns-mfobjects-_mfvideoformat), [**VIDEOINFOHEADER**](https://msdn.microsoft.com/a175592b-0dc1-4001-b52f-785407965932), or [**VIDEOINFOHEADER2**](https://msdn.microsoft.com/5e3d5bf0-435f-45da-8409-a1463b56a7ae) |
| [**MFCreateAMMediaTypeFromMFMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateammediatypefrommfmediatype)     | [**AM\_MEDIA\_TYPE**](https://msdn.microsoft.com/973697d0-2897-48b5-88ca-a88a9650eb02)                                                                                                                                          |
| [**MFCreateMFVideoFormatFromMFMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatemfvideoformatfrommfmediatype) | [**MFVIDEOFORMAT**](/windows/desktop/api/mfobjects/ns-mfobjects-_mfvideoformat)                                                                                                                                              |
| [**MFCreateWaveFormatExFromMFMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatewaveformatexfrommfmediatype)   | [**WAVEFORMATEX**](https://msdn.microsoft.com/4f3bf6fb-b15f-43b3-82f1-e7a8a3007057) or [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/b16cdcab-fa4f-4c9a-b1f3-af459bd33245)                                                                                    |
| [**MFInitAMMediaTypeFromMFMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfinitammediatypefrommfmediatype)         | [**AM\_MEDIA\_TYPE**](https://msdn.microsoft.com/973697d0-2897-48b5-88ca-a88a9650eb02)                                                                                                                                          |



 

## Format Mappings

The following tables list the Media Foundation attributes that correspond to various format structures. Not all of these attributes can be translated directly. To perform conversions, you should use the functions listed in the previous section; these tables are provided mainly for reference.

### AM\_MEDIA\_TYPE



| Member                   | Attribute                                                                            |
|--------------------------|--------------------------------------------------------------------------------------|
| **bTemporalCompression** | [**MF\_MT\_ALL\_SAMPLES\_INDEPENDENT**](mf-mt-all-samples-independent-attribute.md) |
| **bFixedSizeSamples**    | [**MF\_MT\_FIXED\_SIZE\_SAMPLES**](mf-mt-fixed-size-samples-attribute.md)           |
| **lSampleSize**          | [**MF\_MT\_SAMPLE\_SIZE**](mf-mt-sample-size-attribute.md)                          |



 

### WAVEFORMATEX, WAVEFORMATEXTENSIBLE



| Member                  | Attribute                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **wFormatTag**          | [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)<br/> If **wFormatTag** is WAVE\_FORMAT\_EXTENSIBLE, the subtype is found in the **SubFormat** member.<br/> |
| **nChannels**           | [**MF\_MT\_AUDIO\_NUM\_CHANNELS**](mf-mt-audio-num-channels-attribute.md)                                                                                                |
| **nSamplesPerSec**      | [**MF\_MT\_AUDIO\_SAMPLES\_PER\_SECOND**](mf-mt-audio-samples-per-second-attribute.md)                                                                                   |
| **nAvgBytesPerSec**     | [**MF\_MT\_AUDIO\_AVG\_BYTES\_PER\_SECOND**](mf-mt-audio-avg-bytes-per-second-attribute.md)                                                                              |
| **nBlockAlign**         | [**MF\_MT\_AUDIO\_BLOCK\_ALIGNMENT**](mf-mt-audio-block-alignment-attribute.md)                                                                                          |
| **wBitsPerSample**      | [**MF\_MT\_AUDIO\_BITS\_PER\_SAMPLE**](mf-mt-audio-bits-per-sample-attribute.md)                                                                                         |
| **wValidBitsPerSample** | [**MF\_MT\_AUDIO\_VALID\_BITS\_PER\_SAMPLE**](mf-mt-audio-valid-bits-per-sample-attribute.md)                                                                            |
| **wSamplesPerBlock**    | [**MF\_MT\_AUDIO\_SAMPLES\_PER\_BLOCK**](mf-mt-audio-samples-per-block-attribute.md)                                                                                     |
| **dwChannelMask**       | [**MF\_MT\_AUDIO\_CHANNEL\_MASK**](mf-mt-audio-channel-mask-attribute.md)                                                                                                |
| **SubFormat**           | [**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)                                                                                                                        |
| Extra data              | [**MF\_MT\_USER\_DATA**](mf-mt-user-data-attribute.md)                                                                                                                   |



 

### VIDEOINFOHEADER, VIDEOINFOHEADER2



| Member                                         | Attribute                                                                                                                                                                                                                                        |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **dwBitRate**                                  | [**MF\_MT\_AVG\_BITRATE**](mf-mt-avg-bitrate-attribute.md)                                                                                                                                                                                      |
| **dwBitErrorRate**                             | [**MF\_MT\_AVG\_BIT\_ERROR\_RATE**](mf-mt-avg-bit-error-rate-attribute.md)                                                                                                                                                                      |
| **AvgTimePerFrame**                            | [**MF\_MT\_FRAME\_RATE**](mf-mt-frame-rate-attribute.md); use [**MFAverageTimePerFrameToFrameRate**](/windows/desktop/api/mfapi/nf-mfapi-mfaveragetimeperframetoframerate) to calculate this value.                                                                             |
| **dwInterlaceFlags**                           | [**MF\_MT\_INTERLACE\_MODE**](mf-mt-interlace-mode-attribute.md)                                                                                                                                                                                |
| **dwCopyProtectFlags**                         | No defined equivalent                                                                                                                                                                                                                            |
| **dwPictAspectRatioX**, **dwPictAspectRatioY** | [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md); must convert from picture aspect ratio to picture aspect ratio.                                                                                                      |
| **dwControlFlags**                             | [**MF\_MT\_PAD\_CONTROL\_FLAGS**](mf-mt-pad-control-flags-attribute.md). If the **AMCONTROL\_COLORINFO\_PRESENT** flag is present, set the extended color attributes described in [Extended Color Information](extended-color-information.md). |
| **bmiHeader.biWidth**, **bmiHeader.biHeight**  | [**MF\_MT\_FRAME\_SIZE**](mf-mt-frame-size-attribute.md)                                                                                                                                                                                        |
| **bmiHeader.biBitCount**                       | Implicit in the subtype ([**MF\_MT\_SUBTYPE**](mf-mt-subtype-attribute.md)).                                                                                                                                                                    |
| **bmiHeader.biCompression**                    | Implicit in the subtype.                                                                                                                                                                                                                         |
| **bmiHeader.biSizeImage**                      | [**MF\_MT\_SAMPLE\_SIZE**](mf-mt-sample-size-attribute.md)                                                                                                                                                                                      |
| Palette information                            | [**MF\_MT\_PALETTE**](mf-mt-palette-attribute.md)                                                                                                                                                                                               |



 

The following attributes can be inferred from the [**VIDEOINFOHEADER**](https://msdn.microsoft.com/a175592b-0dc1-4001-b52f-785407965932) or [**VIDEOINFOHEADER2**](https://msdn.microsoft.com/5e3d5bf0-435f-45da-8409-a1463b56a7ae) structure but also require some knowledge of the format details. For example, different YUV formats have different stride requirements.

-   [**MF\_MT\_DEFAULT\_STRIDE**](mf-mt-default-stride-attribute.md)
-   [**MF\_MT\_MINIMUM\_DISPLAY\_APERTURE**](mf-mt-minimum-display-aperture-attribute.md)
-   [**MF\_MT\_PAN\_SCAN\_APERTURE**](mf-mt-pan-scan-aperture-attribute.md)

### MPEG1VIDEOINFO



| Member                                   | Attribute                                                                       |
|------------------------------------------|---------------------------------------------------------------------------------|
| **dwStartTimeCode**                      | [**MF\_MT\_MPEG\_START\_TIME\_CODE**](mf-mt-mpeg-start-time-code-attribute.md) |
| **bSequenceHeader**                      | [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md)  |
| **biXPelsPerMeter**, **biYPelsPerMeter** | [**MF\_MT\_PIXEL\_ASPECT\_RATIO**](mf-mt-pixel-aspect-ratio-attribute.md)      |



 

### MPEG2VIDEOINFO



| Member               | Attribute                                                                       |
|----------------------|---------------------------------------------------------------------------------|
| **dwStartTimeCode**  | [**MF\_MT\_MPEG\_START\_TIME\_CODE**](mf-mt-mpeg-start-time-code-attribute.md) |
| **dwSequenceHeader** | [**MF\_MT\_MPEG\_SEQUENCE\_HEADER**](mf-mt-mpeg-sequence-header-attribute.md)  |
| **dwProfile**        | [**MF\_MT\_MPEG2\_PROFILE**](mf-mt-mpeg2-profile-attribute.md)                 |
| **dwLevel**          | [**MF\_MT\_MPEG2\_LEVEL**](mf-mt-mpeg2-level-attribute.md)                     |
| **dwFlags**          | [**MF\_MT\_MPEG2\_FLAGS**](mf-mt-mpeg2-flags-attribute.md)                     |



 

## Examples

The following code fills in a [**BITMAPINFOHEADER**](https://msdn.microsoft.com/153c08a8-d32c-4e9d-9da9-b915eb172327) structure from a video media type. Note that this conversions loses some of the format information (interlacing, frame rate, extended color data). However, it might be useful when saving a bitmap from a video frame, for example.


```C++
#include <dshow.h>
#include <dvdmedia.h>

// Converts a video type to a BITMAPINFO structure.
// The caller must free the structure by calling CoTaskMemFree.

// Note that this conversion loses some format information, including 
// interlacing, and frame rate.

HRESULT GetBitmapInfoHeaderFromMFMediaType(
    IMFMediaType *pType,            // Pointer to the media type.
    BITMAPINFOHEADER **ppBmih,      // Receives a pointer to the structure. 
    DWORD *pcbSize)                 // Receives the size of the structure.
{
    *ppBmih = NULL;
    *pcbSize = 0;

    GUID majorType = GUID_NULL;
    AM_MEDIA_TYPE *pmt = NULL;
    DWORD cbSize = 0;
    DWORD cbOffset = 0;
    BITMAPINFOHEADER *pBMIH = NULL;

    // Verify that this is a video type.
    HRESULT hr = pType->GetMajorType(&amp;majorType);
    if (FAILED(hr))
    {
        goto done;
    }

    if (majorType != MFMediaType_Video)
    {
        hr = MF_E_INVALIDMEDIATYPE;
        goto done;
    }

    hr = pType->GetRepresentation(AM_MEDIA_TYPE_REPRESENTATION, (void**)&amp;pmt);
    if (FAILED(hr))
    {
        goto done;
    }

    if (pmt->formattype == FORMAT_VideoInfo)
    {
        cbOffset = (FIELD_OFFSET(VIDEOINFOHEADER,bmiHeader));
    }
    else if (pmt->formattype == FORMAT_VideoInfo2)
    {
        cbOffset = (FIELD_OFFSET(VIDEOINFOHEADER2,bmiHeader));
    }
    else
    {
        hr = MF_E_INVALIDMEDIATYPE; // Unsupported format type.
        goto done;
    }

    if (pmt->cbFormat - cbOffset < sizeof(BITMAPINFOHEADER))
    {
        hr = E_UNEXPECTED; // Bad format size. 
        goto done;
    }

    cbSize = pmt->cbFormat - cbOffset;

    pBMIH = (BITMAPINFOHEADER*)CoTaskMemAlloc(cbSize);
    if (pBMIH == NULL)
    {
        hr = E_OUTOFMEMORY;
        goto done;
    }
    
    CopyMemory(pBMIH, pmt->pbFormat + cbOffset, cbSize);
    
    *ppBmih = pBMIH;
    *pcbSize = cbSize;

done:
    if (pmt)
    {
        pType->FreeRepresentation(AM_MEDIA_TYPE_REPRESENTATION, pmt);
    }
    return hr;
}
```



## Related topics

<dl> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 




