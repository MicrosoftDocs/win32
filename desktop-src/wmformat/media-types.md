---
title: Media Types for Windows Media Format SDK
description: Learn about media types that can be used by the Windows Media Format SDK. Media types are GUID values assigned to constants in the SDK.
ms.assetid: 00dcbb20-09ed-44c5-992c-20f3d17ad47c
keywords:
- Windows Media Format SDK,media types
- Advanced Systems Format (ASF),media types
- ASF (Advanced Systems Format),media types
- media types,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media Types for Windows Media Format SDK

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Media types identify the different types of media that can be used by the Windows Media Format SDK. All media types are GUID values that have been assigned to constants in the SDK. The GUID values represented by the constants listed in this section are listed in the [Media Type Identifiers](media-type-identifiers.md) section of this reference.

The following table lists major media types. These constants define the high level classification of digital media supported by the Windows Media Format SDK.



| Major type                | Description                                                                                             |
|---------------------------|---------------------------------------------------------------------------------------------------------|
| WMMEDIATYPE\_Video        | A video stream.                                                                                         |
| WMMEDIATYPE\_Audio        | An audio stream.                                                                                        |
| WMMEDIATYPE\_Script       | A script stream.                                                                                        |
| WMMEDIATYPE\_FileTransfer | A stream that contains data files. Web streams, which consist of HTML files, also have this major type. |
| WMMEDIATYPE\_Image        | A JPEG image stream for an illustrated audio file (as in a slide show).                                 |
| WMMEDIATYPE\_Text         | A text stream.                                                                                          |



 

In addition to the explicitly supported major media types, you can create your own arbitrary data types. For custom arbitrary data types, you must ensure that the GUID you use does not match an existing major type.

A media stream will often have a subtype in addition to its major type. The following sections list the supported subtypes.



| Section                                                        | Description                                                                                                                                |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [Uncompressed Media Subtypes](uncompressed-media-subtypes.md) | Describes the subtypes available for uncompressed media. These are the types typically associated with input or output media.              |
| [Compressed Media Subtypes](compressed-media-subtypes.md)     | Describes the subtypes available for compressed media. These are the types typically associated with media in a stream within an ASF file. |
| [Video Input Formats](video-input-formats.md)                 | Lists the video formats accepted as inputs for the Windows Media Video 9 codec.                                                            |



 

## Related topics

<dl> <dt>

[**Media Type Identifiers**](media-type-identifiers.md)
</dt> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




