---
description: About Media Types
ms.assetid: 169cdb00-0c1a-4530-90b7-bc89c71d1d04
title: About Media Types (Microsoft Media Foundation)
ms.topic: article
ms.date: 05/31/2018
---

# About Media Types (Microsoft Media Foundation)

A *media type* describes the format of a media stream. In Microsoft Media Foundation, media types are represented by the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface. This interface inherits the [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes) interface. The details of a media type are specified as attributes.

To create a new media type, call the [**MFCreateMediaType**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatemediatype) function. This function returns a pointer to the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface. The media type initially has no attributes. To set the details of the format, set the relevant attributes.

For a list of media type attributes, see [Media Type Attributes](media-type-attributes.md).

## Major Types and Subtypes

Two important pieces of information for any media type are the major type and the subtype.

-   The *major type* is a GUID that defines the overall category of the data in a media stream. Major types include video and audio. To specify the major type, set the [MF\_MT\_MAJOR\_TYPE](mf-mt-major-type-attribute.md) attribute. The [**IMFMediaType::GetMajorType**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediatype-getmajortype) method returns the value of this attribute.
-   The *subtype* further defines the format. For example, within the video major type, there are subtypes for RGB-24, RGB-32, YUY2, and so forth. Within audio, there are PCM audio, IEEE floating-point audio, and others. The subtype provides more information than the major type, but it does not define everything about the format. For example, video subtypes do not define the image size or the frame rate. To specify the subtype, set the [MF\_MT\_SUBTYPE](mf-mt-subtype-attribute.md) attribute.

All media types should have a major type GUID and a subtype GUID. For a list of major type and subtype GUIDs, see [Media Type GUIDs](media-type-guids.md).

## Why Attributes?

Attributes have several advantages over the format structures that have been used in previous technologies such as DirectShow and the Windows Media Format SDK.

-   It is easier to represent "don't know" or "don't care" values. For example, if you are writing a video transform, you might know in advance which RGB and YUV formats the transform supports, but not the dimensions of the video frame, until you get them from the video source. Similarly, you might not care about certain details, such as the video primaries. With a format structure, every member must be filled with *some* value. As a result, it has become common to use zero to indicate an unknown or default value. This practice can cause errors if another component treats zero as a legitimate value. With attributes, you simply omit the attributes that are unknown or not relevant to your component.

-   As requirements have changed over time, format structures were extended by adding additional data at the end of the structure. For example, **WAVEFORMATEXTENSIBLE** extends the **WAVEFORMATEX** structure. This practice is prone to error, because components must cast structure pointers to other structure types. Attributes can be extended safely.
-   Mutually incompatible format structures have been defined. For example, DirectShow defines the **VIDEOINFOHEADER** and **VIDEOINFOHEADER2** structures. Attributes are set independently of each other, so this problem does not arise.

## Related topics

<dl> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 



