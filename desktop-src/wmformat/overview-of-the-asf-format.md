---
title: Overview of the ASF Format
description: Overview of the ASF Format
ms.assetid: ef22a493-d6cf-40d2-ab17-d87159066d1d
keywords:
- Windows Media Format SDK,ASF format overview
- Advanced Systems Format (ASF),format overview
- ASF (Advanced Systems Format),format overview
ms.topic: article
ms.date: 05/31/2018
---

# Overview of the ASF Format

The Advanced Systems Format (ASF) is an extensible file format designed primarily for storing and playing synchronized digital media streams and transmitting them over networks. ASF is the container format for Windows Media Audio and Windows Media Video-based content. The extension wma or wmv is used to specify an ASF file that contains content encoded with the Windows Media Audio and/or Windows Media Video codecs. The Windows Media Format SDK can be used to create and read Windows Media files, as well as ASF files that contain other types of compressed or uncompressed data.

This section provides a general description of the ASF format as background information. Because the reader and writer objects handle all low-level file parsing and formatting tasks, it is not necessary to have a detailed understanding of ASF before using this SDK to create ASF files. The complete ASF specification can be found on the [Microsoft Web site](https://download.microsoft.com/download/7/9/0/790fecaa-f64a-4a5e-a430-0bccdab3f1b4/ASF_Specification.doc).

The primary goals of the ASF format are:

-   To support efficient playback from media servers, HTTP servers, and local storage devices.
-   To support scalable media types such as audio and video.
-   To permit a single multimedia composition to be presented over a wide range of bandwidths.
-   To allow authoring control over media stream relationships, especially in constrained-bandwidth scenarios.
-   To be independent of any particular multimedia composition system, computer operating system, or data communications protocol.

An ASF file can contain multiple independent or dependent streams, including multiple audio streams for multichannel audio, or multiple bit rate video streams suitable for transmission over different bandwidths. The streams can be in any compressed or uncompressed format; however, the best compression is achieved with the Microsoft Windows Media Audio and Video 9 Series codecs. In addition to the standard audio and video media stream types, an ASF file can also contain text streams, Web pages and script commands, and any other arbitrary data type. ASF supports live and on-demand multimedia content. It can be used as a vehicle to record or play back H.32X (for example, H.323 and H.324) or MBONE conferences.

An ASF file is organized into sections called "objects." There are three top-level objects, a Header object and a Data object (both required), plus an optional Index object. The Header object contains general information about the file, such as file size, number of streams, error correction methods, and codecs used. Metadata is also stored here. The Header object is the only top level object that can contain other objects. The Data object contains the stream data, organized in packets. The Simple Index object contains a list of associated index/key-frame pairs that enables applications to seek through a file efficiently. The index associated with each key frame can be a presentation time, a video frame number, or a reference time stamp.

Each top-level or lower-level object begins with a globally unique identifier (GUID) and a size value. These numbers allow the file reader to parse the information at appropriate places into identifiable objects. Because of these GUIDs, lower-level objects can be sent in any order and still be recognized. The ASF format is designed to overcome inaccurate data reception. A partially downloaded ASF file can still be read, as long as it contains the Header object and at least one Data object.

Detailed information about ASF in presented in the ASF specification. You can download the specification from the [Microsoft Web site](https://download.microsoft.com/download/7/9/0/790fecaa-f64a-4a5e-a430-0bccdab3f1b4/ASF_Specification.doc).

## Related topics

<dl> <dt>

[**About the Windows Media Format SDK**](about-the-windows-media-format-sdk.md)
</dt> </dl>

 

 




