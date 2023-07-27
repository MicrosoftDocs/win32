---
description: Learn about media types in DirectShow. The media type is a universal and extensible way to describe digital media formats.
ms.assetid: 9984ba36-4e43-4886-a073-34b330274c9c
title: About Media Types (DirectShow)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Media Types (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Because DirectShow is modular, it requires a way to describe the format of the data at each point in the filter graph. For example, consider AVI playback. Data enters the graph as a stream of RIFF chunks. These are parsed into video and audio streams. The video stream consists of video frames, which are probably compressed. After decoding, the video stream is a series of uncompressed bitmaps. The audio stream goes through a similar process.

Media Types: How DirectShow Represents Formats

The *media type* is a universal and extensible way to describe digital media formats. When two filters connect, they agree on a media type. The media type identifies what kind of data the upstream filter will deliver to the downstream filter, and the physical layout of the data. If two filters cannot agree on a media type, they will not connect.

For some applications, you will never have to worry about media types. In file playback, for example, DirectShow handles all of the details. Other kinds of applications may need to work directly with media types.

Media types are defined using the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. This structure contains the following information:

-   **Major type**: The major type is a GUID that defines the overall category of the data. Major types include video, audio, unparsed byte stream, MIDI data, and so forth.
-   **Subtype**: The subtype is another GUID, which further defines the format. For example, within the video major type, there are subtypes for RGB-24, RGB-32, UYVY, and so forth. Within audio, there is PCM audio, MPEG-1 payload, and others. The subtype provides more information than the major type, but it does not define everything about the format. For example, video subtypes do not define the image size or the frame rate. These are defined by the format block, described below.
-   **Format block**: The format block is a block of data that describes the format in detail. The format block is allocated separately from the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure. The **pbFormat** member of the **AM\_MEDIA\_TYPE** structure points to the format block.

    The **pbFormat** member is typed **void\*** because the layout of the format block changes depending on the media type. For example, PCM audio uses a [**WAVEFORMATEX**](/previous-versions/dd757713(v=vs.85)) structure. Video uses various structures, including [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) and [**VIDEOINFOHEADER2**](/previous-versions/windows/desktop/api/dvdmedia/ns-dvdmedia-videoinfoheader2). The **formattype** member of the [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure is a GUID that specifies which structure is contained in the format block. Each format structure is assigned a GUID. The **cbFormat** member specifies the size of the format block. Always check these values before dereferencing the **pbFormat** pointer.

If the format block is filled in, then the major type and subtype contain redundant information. The major type and subtype, however, provide a convenient way to identify formats without a complete format block. For example, you can specify a generic 24-bit RGB format (MEDIASUBTYPE\_RGB24), without knowing all of the information required by the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure, such as image size and frame rate.

For example, a filter might use the following code to check a media type:


```C++
HRESULT CheckMediaType(AM_MEDIA_TYPE *pmt)
{
    if (pmt == NULL) return E_POINTER;

    // Check the major type. We're looking for video.
    if (pmt->majortype != MEDIATYPE_Video)
    {
        return VFW_E_INVALIDMEDIATYPE;
    }

    // Check the subtype. We're looking for 24-bit RGB.
    if (pmt->subtype != MEDIASUBTYPE_RGB24)
    {
        return VFW_E_INVALIDMEDIATYPE;
    }

    // Check the format type and the size of the format block.
    if ((pmt->formattype == FORMAT_VideoInfo) &&
         (pmt->cbFormat >= sizeof(VIDEOINFOHEADER) &&
         (pmt->pbFormat != NULL))
    {
        // Now it's safe to coerce the format block pointer to the
        // correct structure, as defined by the formattype GUID.
        VIDEOINFOHEADER *pVIH = (VIDEOINFOHEADER*)pmt->pbFormat;
    
        // Examine pVIH (not shown). If it looks OK, return S_OK.
        return S_OK;
    }

    return VFW_E_INVALIDMEDIATYPE;
}
```



The [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure also contains some optional fields. These can be used to provide additional information, but filters are not required to use them:

-   **lSampleSize**. If this field is non-zero, it defines the size of each sample. If it is zero, it indicates that the sample size may change from sample to sample.
-   **bFixedSizeSamples**. If this Boolean flag is **TRUE**, it means the value in **lSampleSize** is valid. Otherwise, you should ignore **lSampleSize**.
-   **bTemporalCompression**. If this Boolean flag is **FALSE**, it means that all frames are key frames.

## Related topics

<dl> <dt>

[The Filter Graph and Its Components](the-filter-graph-and-its-components.md)
</dt> </dl>

 

 
