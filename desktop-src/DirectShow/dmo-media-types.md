---
description: DMO Media Types
ms.assetid: 40958e12-09c7-4ce5-aa4d-5ed8b1f40aa3
title: DMO Media Types
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO Media Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A media type describes the format associated with a stream of media data. This article describes how DMOs handle media types. It is primarily intended for developers who are writing their own custom DMOs.

Media types are defined using the [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) structure. This structure includes the following information:

-   The *major type* is a globally unique identifier (GUID) that defines a broad category, such as audio or video.
-   The *subtype* is a GUID that defines more specific aspects of the type. For example, within video, the subtypes include 16-bit RGB, 24-bit RGB, UYVY, DV-encoded video, and so forth.
-   The *format block* is a secondary structure that fully specifies the format. The layout of the format block depends on the type of data. For example, PCM audio uses the **WAVEFORMATEX** structure. Video uses various other structures, including **VIDEOINFOHEADER** and **VIDEOINFOHEADER2**. The layout of the format block is identified by a format type GUID. For example, FORMAT\_WaveFormatEx specifies a **WAVEFORMATEX** structure.

When a DMO is first created, the streams do not have a media type. Before the DMO can process any data, the client must set a media type for each stream. This process is described from the client's perspective in [Setting Media Types on a DMO](setting-media-types-on-a-dmo.md).

**Media Types in the Registry**

A DMO can add a list of media types that it supports to the registry, by calling the [**DMORegister**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoregister) function. An application can use this information to search for DMOs that match a particular format. The information in the registry is not meant to be comprehensive. Typically, you would include only the main types that the DMO supports. The registry entry has separate keys for input and output types, but does not distinguish among individual streams.

The **DMORegister** function uses the [**DMO\_PARTIAL\_MEDIATYPE**](/previous-versions/windows/desktop/api/Dmoreg/ns-dmoreg-dmo_partial_mediatype) structure to describe media types. This structure contains a subset of the information found in the **DMO\_MEDIA\_TYPE** structure—namely the major type and the subtype. It does not include a format block, because the format block typically contains information that is too granular to include in the registry, such as the height and width of a video image.

**Preferred Media Types**

After the application has created a DMO, it can query the DMO for the media types it supports. For each stream, the DMO creates a list of media types (possibly empty), ranked in order of preference. The [**IMediaObject::GetInputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-getinputtype) and [**IMediaObject::GetOutputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-getoutputtype) methods enumerate the preferred types. A stream's preferred types can change dynamically when the application sets media types on other streams. For example, the list of preferred output types might change after the input type is set, or vice versa. However, the DMO is not required to update its preferred types dynamically. The application cannot assume that every type it receives is valid. For this reason, the [**IMediaObject::SetInputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-setinputtype) and [**IMediaObject::SetOutputType**](/previous-versions/windows/desktop/api/Mediaobj/nf-mediaobj-imediaobject-setoutputtype) methods support a flag for testing a specific type.

The **GetInputType** and **GetOutputType** methods both return a **DMO\_MEDIA\_TYPE** structure. The DMO can leave some of the information in this structure blank, to indicate a range of types. The major type or subtype can be GUID\_NULL, and the format block can be empty (zero bytes). If the format block is empty, the format type must be GUID\_NULL.

After the application sets all of a DMO's input types, the DMO should generally return at least one complete type for each output stream. A complete output type facilitates testing, and applications can use it as a reasonable default. The DMO test application relies on this behavior. (See [Using the DMOTest Application](using-the-dmotest-application.md).)

**Setting the Media Types**

Applications use the **SetInputType** and **SetOutputType** methods to test, set, or clear types on a specified stream. The application must fully specify the type. The DMO verifies whether it can accept the proposed type. The answer may depend on which types have been set on other streams. The DMO\_SET\_TYPEF\_CLEAR flag clears a stream's type, so the application can "back out" and try another combination.

**Example Scenarios**

The following examples describe some typical scenarios, to illustrate the points made in the previous sections.

-   **Video Decoders.** In a typical video decoder, the input type partly determines the output type. For example, usually both streams must have the same frame rate and image dimensions. One option is not to define any preferred output types until the input type is set. Another option is to enumerate a set of incomplete types, omitting the format block. Use the subtype to indicate the supported uncompressed types, such as 16-bit RGB, 24-bit RGB, and so forth. Also, video decoders generally do not support setting the output type before the input type. The usual scenario is to decode from a known input format, so this limitation is reasonable.
-   **Audio Decoders.** An audio decoder might support a limited, fixed set of output formats. In that case, it may be able to create a list of preferred output formats before the input format is known.
-   **Compressors.** In most cases, a video compressor cannot fully specify its preferred output formats until the application sets the input format, and vice versa. Instead, the DMO should return an incomplete type with no format block. For both audio and video compression, the application usually needs to set various output parameters, such as the bit rate. However, after the input type is set, the compressor should return at least one complete output type, for the reasons mentioned previously.

## Related topics

<dl> <dt>

[Writing a DMO](writing-a-dmo.md)
</dt> </dl>

 

 



