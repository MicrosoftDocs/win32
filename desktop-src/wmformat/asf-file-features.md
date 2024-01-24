---
title: ASF File Features
description: ASF File Features
ms.assetid: 6e180f27-69ef-4fe0-b06c-b2ead7be8a05
keywords:
- Windows Media Format SDK,ASF file features
- Windows Media Format SDK,features
- Advanced Systems Format (ASF),file features
- ASF (Advanced Systems Format),file features
- Advanced Systems Format (ASF),features
- ASF (Advanced Systems Format),features
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ASF File Features

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The primary purpose of the Windows Media Format SDK is to provide support for encapsulating digital media data in Advanced Systems Format (ASF) files and delivering the media to a client application. Delivery scenarios can vary widely from application to application, but all use the ASF file structure between authoring and delivery. ASF files conform to a well defined but very flexible structure. For more information about the ASF file structure, see [Overview of the ASF Format](overview-of-the-asf-format.md).

Detailed information about the data in an ASF file is provided in the ASF specification, which you can download from the [Microsoft Web site](https://download.microsoft.com/download/7/9/0/790fecaa-f64a-4a5e-a430-0bccdab3f1b4/ASF_Specification.doc).

The Windows Media Format SDK provides support for the features of the ASF specification mostly through the profile that is used to create a file. For more information about profiles, see [Profiles](profiles.md).

The following features are discussed in this section.

-   [Audio and Video Streams](audio-and-video-streams.md)
-   [Image Streams](image-streams.md)
-   [Arbitrary Streams](arbitrary-streams.md)
-   [Script Commands](script-commands.md)
-   [Data Unit Extensions](data-unit-extensions.md)
-   [SMPTE Time Code Support](smpte-time-code-support.md)
-   [Mutual Exclusion](mutual-exclusion.md)
-   [Stream Prioritization](stream-prioritization.md)
-   [Bandwidth Sharing](bandwidth-sharing.md)
-   [Indexes](indexes.md)
-   [Markers](markers.md)
-   [Reader Response to ASF Features](reader-response-to-asf-features.md)

## Related topics

<dl> <dt>

[**Features**](features.md)
</dt> </dl>

 

 




