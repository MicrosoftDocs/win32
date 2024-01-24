---
title: File Writing Features
description: File Writing Features
ms.assetid: 4514f463-26cf-48a4-aa0c-c25fc5a1979f
keywords:
- Windows Media Format SDK,file writing features
- Windows Media Format SDK,features
- Advanced Systems Format (ASF),file writing features
- ASF (Advanced Systems Format),file writing features
- Advanced Systems Format (ASF),features
- ASF (Advanced Systems Format),features
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# File Writing Features

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

One of the primary features of the Windows Media Format SDK is the ability to write files in the Advanced Systems Format (ASF). The writer object is used to write ASF files. For more information see, [Writer Object](writer-object.md).

In the most basic file writing scenario, you assign a profile to use and a name of the file to create. You pass samples to the writer one at a time. When you have finished passing samples to the writer, it finishes its operations and completes the ASF file. For more information about basic file writing, see [Writing ASF Files](writing-asf-files.md).

The writer supports several advanced features, which are discussed in the following sections.

-   [Video Resizing](video-resizing.md)
-   [Color Space Conversion](color-space-conversion.md)
-   [Audio Resampling](audio-resampling.md)
-   [Sinks](sinks.md)
-   [Watermarking Support](watermarking-support.md)
-   [Input Formats, Input Settings, and Data Unit Extensions](input-formats-input-settings-and-data-unit-extensions.md)
-   [Input Format Enumeration](input-format-enumeration.md)

## Related topics

<dl> <dt>

[**Features**](features.md)
</dt> </dl>

 

 




