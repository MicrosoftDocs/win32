---
description: Using the Windows Media Video 9.1 Image Category
ms.assetid: b77e955b-767b-4b64-9421-bacac9edf09c
title: Using the Windows Media Video 9.1 Image Category
ms.topic: article
ms.date: 05/31/2018
---

# Using the Windows Media Video 9.1 Image Category

The Windows Media Video 9.1 Image category is different from the other output categories supported by the Windows Media Video 9 encoder and decoder. Instead of processing uncompressed video, it takes special input samples that consist of structured transformation data and, occasionally, RGB bitmap images on which the transformations are performed.

The encoded Windows Media Video 9.1 Image content is virtually identical to regular Windows Media Video 9 encoded content, but it is identified by its own FOURCC ("WMVP").

The encoder output type for video image is set in exactly the same way as standard Windows Media video, except that the subtype and compression values must be set to the video image identifiers. This includes the need to obtain codec private data and append it to the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) structure. For more information, see [Configuring Video Encoding](configuringvideoencoding.md).

The input type configuration for video image is also very similar to input configuration for the other video encoders. You can retrieve a partially completed [**DMO\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/mediaobj/ns-mediaobj-dmo_media_type) from the encoder by calling [**IMediaObject::GetInputType**](/previous-versions/windows/desktop/api/mediaobj/nf-mediaobj-imediaobject-getinputtype), or if you are using the Media Foundation SDK, by calling [**IMFTransform::GetInputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputavailabletype) and retrieving the **DMO\_MEDIA\_TYPE** by using [**MFCreateAMMediaTypeFromMFMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfcreateammediatypefrommfmediatype). You then set the frame size and the [**VIDEOINFOHEADER**](/previous-versions/windows/desktop/api/amvideo/ns-amvideo-videoinfoheader) format structure, just as you would for standard video. As with the output type, you need to ensure that the subtype and compression values are set appropriately.

## Creating Input Samples

The input samples for the video image codec are structured. The definition of the structure and constants used for video image are not included with the Windows Media Audio and Video codec interfaces. These definitions are included in the Windows Media Format SDK, and their use is fully explained in the Windows Media Format SDK documentation.

## Decoding

There are no special requirements for decoding screen capture video. Other than a different subtype (MEDIASUBTYPE\_WMVP) used for decoder input, the compressed video image stream is essentially identical to a standard Windows Media Video stream.

## Related topics

<dl> <dt>

[Working with Video](workingwithvideo.md)
</dt> </dl>

 

 
