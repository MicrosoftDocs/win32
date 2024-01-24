---
description: This topic describes how to work with ASF profiles in Microsoft Media Foundation.
ms.assetid: 03a0981b-29c3-450d-aa58-bc56a76e6cb6
title: ASF Profile
ms.topic: article
ms.date: 05/31/2018
---

# ASF Profile

This topic describes how to work with ASF profiles in Microsoft Media Foundation.

An Advanced Systems Format (ASF) file contains one or more streams. For each stream, the ASF header contains a Stream Properties Header that describes the stream. At the [WMContainer](wmcontainer-asf-components.md) layer, the following objects are used to set or read the properties of the ASF streams:

-   *ASF profile* object: Describes the streams and their relationships with each other. The ASF profile object exposes the [**IMFASFProfile**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfprofile) interface.
-   *Stream configuration* object: Describes one stream. The stream configuration object contains a media type that describes the format of the stream. For audio and video streams, the media type describes exactly how the stream is configured, and is used by codecs that encode or decode the stream. The stream configuration object exposes the [**IMFASFStreamConfig**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfstreamconfig) interface. A valid ASF profile contains at least one stream configuration object.
-   *Mutual exclusion* object: Describes multiple streams that are not intended be read concurrently. A mutual exclusion object exposes the [**IMFASFMutualExclusion**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfmutualexclusion) interface. An ASF profile contains zero or more mutual exclusion objects.

The following diagram shows the relationship between the ASF profile and the objects that are contained in the profile.

![tree diagram of an asf profile node with stream configuration child nodes; the first points to media type, the next two to mutual exclusion](images/asf-components02.png)

For playback, the ASF profile is used to enumerate the streams and find the stream formats. For encoding, the ASF profile is used to configure the streams in the destination file.

The ASF profile is also used to configure the [ASF Media Sink](asf-media-sinks.md). For each stream in the ASF profile, the ASF media sink creates a corresponding stream sink.

## In this section



| Topic                                                                                           | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [Creating an ASF Profile](creating-an-asf-profile.md)<br/>                               | Describes how to create an ASF profile object.<br/>          |
| [Creating and Configuring ASF Streams](creating-and-configuring-asf-streams.md)<br/>     | Describes how to add streams to an ASF profile.<br/>         |
| [Using Mutual Exclusion for ASF Streams](using-mutual-exclusion-for-asf-streams.md)<br/> | Describes how to add mutual exclusions to ASF streams. <br/> |



 

## Related topics

<dl> <dt>

[Media Types](media-types.md)
</dt> <dt>

[Tutorial: 1-Pass Windows Media Encoding](tutorial--1-pass-windows-media-encoding.md)
</dt> <dt>

[Tutorial: Writing a WMA File by Using CBR Encoding](tutorial--writing-a-wma-file-by-using-cbr-encoding.md)
</dt> <dt>

[WMContainer ASF Components](wmcontainer-asf-components.md)
</dt> </dl>

 

 




