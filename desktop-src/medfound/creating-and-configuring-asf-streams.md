---
description: Each ASF file contains one or more streams. The ASF Profile object represents a collection of ASF streams. For ASF encoding, you must create and configure the streams that you want to encode.
ms.assetid: cc89e8bc-58ff-48e2-9668-0dcd6cfd25e1
title: Creating and Configuring ASF Streams
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Configuring ASF Streams

Each ASF file contains one or more streams. The [ASF Profile](asf-profile.md) object represents a collection of ASF streams. For ASF encoding, you must create and configure the streams that you want to encode.

An application can perform the following tasks with the ASF profile object:

-   Add or remove a stream.
-   Obtain a stream's configuration settings.
-   Configure payload extensions.
-   Add, remove, or modify an ASF mutual exclusion object.

This topic contains the following sections.

-   [Creating a New Stream](#creating-a-new-stream)
-   [Assigning Stream Numbers](#assigning-stream-numbers)
-   [Setting Leaky Bucket Values](#setting-leaky-bucket-values)
-   [Payload Extensions](#payload-extensions)
-   [Adding a Stream to the Profile](#adding-a-stream-to-the-profile)
-   [Related topics](#related-topics)

## Creating a New Stream

An ASF profile object must contain configuration settings for at least one ASF stream. Each stream is represented by a *stream configuration* object, which exposes the [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) interface. The information in the stream configuration object corresponds to the Stream Properties Object and the Extended Stream Properties Objects in the ASF file header. (See [ASF File Structure](asf-file-structure.md).)

To add a stream to an ASF profile, perform the following steps:

1.  Create an empty stream stream configuration object.
2.  Configure the stream according to the application's requirements.
3.  Add the stream to the profile.

To create a stream for the profile, call [**IMFASFProfile::CreateStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-createstream) to create an empty stream configuration object and receive the pointer in the *ppIStream* parameter. **CreateStream** needs to know the type of the stream to create. The most common types of streams used in ASF files are audio and video streams. In Media Foundation, the stream types are denoted by the media type object that exposes the [**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype) interface. The major type of the media type defines the category of the digital media stream, such as audio or video. The subtype defines the format of the major type. The initial media type set by **CreateStream** can be changed by using the steam configuration object. To retrieve the media type for the stream, call [**IMFASFStreamConfig::GetMediaType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getmediatype) or to retrieve the major type call [**IMFASFStreamConfig::GetStreamType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getstreamtype). The initial media type for a stream can be replaced with a new configured media type by calling [**IMFASFStreamConfig::SetMediaType**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-setmediatype).

If an application creates a profile from a valid presentation descriptor by calling [**MFCreateASFProfileFromPresentationDescriptor**](/windows/desktop/api/wmcontainer/nf-wmcontainer-mfcreateasfprofilefrompresentationdescriptor). The function automatically sets the stream configuration objects for each of the streams and sets them on the profile. The stream media types are set based on the stream descriptors associated with the presentation descriptor.

## Assigning Stream Numbers

Streams of all types must be assigned a stream number. Stream numbers need not be sequential but must be in the range from 1 to 127. To assign stream numbers, call [**IMFASFStreamConfig::SetStreamNumber**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-setstreamnumber). To get the stream number call, [**IMFASFStreamConfig::GetStreamNumber**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getstreamnumber).

> [!Note]  
> A stream number is different from a stream index, which you use when getting streams in a profile by using [**IMFASFProfile::GetStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getstream). The stream index is a number assigned to the stream by the profile object. Stream indexes range between 0 and one less than the number of streams retrieved by [**IMFASFProfile::GetStreamCount**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getstreamcount). You can also get a stream from the profile by stream number by calling [**IMFASFProfile::GetStreamByNumber**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-getstreambynumber).

 

## Setting Leaky Bucket Values

Each stream configuration object that represents a stream must have associated leaky bucket parameters, bit rate and buffer window values.

These values are available to the application through the [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET1**](mf-asfstreamconfig-leakybucket1-attribute.md) attribute and the [**MF\_ASFSTREAMCONFIG\_LEAKYBUCKET2**](mf-asfstreamconfig-leakybucket2-attribute.md) attribute. For file encoding, the actual values depend on the type of encoding and are decided by the encoder. If you already have a configured encoder and the output type is set on the encoder, the application must query the encoder for the leaky bucket parameters and set the values in these attributes.

If you are using the pipeline layer components and configuring the streams for the ASF media sink, most likely, you do not have a configured encoder. In this case, you must query the encoder post-media type negotiations and set the updated value in the [**MFPKEY\_ASFSTREAMSINK\_CORRECTED\_LEAKYBUCKET**](mfpkey-asfstreamsink-corrected-leakybucket-property.md) property of the ASF media sink's property store. The encoding property store is retrieved through the of the ContentInfo object associated with the profile. The updated values are reflected in the stream's leaky bucket attribute values automatically. For general information about leaky buckets and how to get the leaky bucket value from the encoder, see the [The Leaky Bucket Buffer Model](the-leaky-bucket-buffer-model.md).

## Payload Extensions

Media data for the streams are added to the ASF Data Object as [Media Samples](media-samples.md) by the [ASF Multiplexer](asf-multiplexer.md). These media samples can contain payload extension data: SMPTE time code data, non-square pixel aspect ratio, sample duration, and if the sample contains it, a video key frame. For a list of the supported payload extension types, see [ASF Payload Extension GUIDs](asf-payload-extension-guids.md).

A stream must be configured to accept payload extension so that during sample generation the multiplexer can add the supplementary data to each sample for that stream.

To get the total number of payload extensions set on the stream, call [**IMFASFStreamConfig::GetPayloadExtensionCount**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getpayloadextensioncount) and then enumerate the list by calling [**IMFASFStreamConfig::GetPayloadExtension**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-getpayloadextension). To add payload extension for the stream, call [**IMFASFStreamConfig::AddPayloadExtension**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-addpayloadextension). This will add supplementary data to individual media samples generated for the stream.

To remove existing payload extensions associated with the stream, call [**IMFASFStreamConfig::RemoveAllPayloadExtensions**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfstreamconfig-removeallpayloadextensions).

## Adding a Stream to the Profile

After a stream is configured, call [**IMFASFProfile::SetStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-setstream) to add the stream to the profile.

To remove an existing stream in the profile, call [**IMFASFProfile::RemoveStream**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfprofile-removestream).

The configured profile must be set on the ContentInfo object by calling [**IMFASFContentInfo::SetProfile**](/windows/desktop/api/wmcontainer/nf-wmcontainer-imfasfcontentinfo-setprofile). If make changes to an existing stream, you must add it again to the profile and set the profile on the ContentInfo object.

## Related topics

<dl> <dt>

[ASF Profile](asf-profile.md)
</dt> <dt>

[ASF Support in Media Foundation](asf-support-in-media-foundation.md)
</dt> <dt>

[WMContainer ASF Components](wmcontainer-asf-components.md)
</dt> </dl>

 

 



