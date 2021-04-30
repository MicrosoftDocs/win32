---
description: This section describes how to use the transcode API to re-encode media files. The transcode API was introduced in Windows 7.
ms.assetid: '24bf68a8-39bf-4302-b28c-71bb23b63469'
title: Transcode API
ms.topic: article
ms.date: 05/31/2018
---

# Transcode API

This section describes how to use the transcode API to re-encode media files. The transcode API was introduced in Windows 7.

*Transcoding* is the conversion of a digital media file from one format to another. The transcode API is designed to be used with the [Media Session](media-session.md). It simplifies the use of the Media Session for certain types of transcoding applications:

-   Constant bit rate (CBR) encoding, where the target bit rate is known in advance.
-   At most one audio stream and one video stream.
-   Encoding from and to a file.

Transcode API does not support the following:

-   Variable bit rate (VBR) or multi-pass encoding.
-   Multiple audio streams or multiple video streams.
-   DRM-protected content other than ASF files protected with WMDRM.
-   Live streaming, such as live-to-file streaming or live-to-live streaming.

If your encoding application fits within these constraints, the transcode API a simpler programming model than using the Media Session alone.

## In this section



| Topic                                                                                          | Description                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About the Transcode API](about-the-transcode-api.md)<br/>                              | Provides a general overview of the transcode API.<br/>                                                                                                                                                                |
| [Using the Transcode API](fast-transcode-objects.md)<br/>                               | Describes how an application uses the transcode API.<br/>                                                                                                                                                             |
| [Tutorial: Encoding an MP4 File](tutorial--encoding-an-mp4-file-.md)<br/>               | A step-by-step tutorial that shows how to use the transcode API to encode an MP4 file.<br/>                                                                                                                           |
| [Tutorial: Encoding a WMA File](tutorial--converting-an-mp3-file-to-a-wma-file.md)<br/> | Shows how to use the transcode API to encode a WMA file. This tutorial modifies the code shown in [Tutorial: Encoding an MP4 File](tutorial--encoding-an-mp4-file-.md), so you should read that tutorial first.<br/> |



 

## Related topics

<dl> <dt>

[Encoding and File Authoring](encoding-and-file-authoring.md)
</dt> <dt>

[Media Foundation: Essential Concepts](media-foundation-programming--essential-concepts.md)
</dt> <dt>

[Overview of Encoding in Media Foundation](overview-of-encoding-in-media-foundation.md)
</dt> </dl>

 

 




