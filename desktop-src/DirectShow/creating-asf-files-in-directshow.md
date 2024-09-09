---
description: Learn about creating ASF files in DirectShow. ASF is a container format that can contain any type of data.
ms.assetid: dffda43a-5831-4889-864f-81351b9e2bb3
title: Creating ASF Files in DirectShow (DirectShow)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating ASF Files in DirectShow (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to use the DirectShow [WM ASF Writer](wm-asf-writer-filter.md) filter to create files in Advanced Systems Format (ASF). ASF is a container format that can contain any type of compressed or uncompressed data. Windows Media Format files are ASF files that use certain codecs as specified in the Windows Media Format Software Development Kit (SDK). These files use the extensions ".wma" for Windows Media Audio files and ".wmv" for Windows Media Video files.

This topic contains the following sections:

-   [The DirectShow SDK and the Windows Media Format SDK](the-directshow-sdk-and-the-windows-media-format-sdk.md)
-   [Configuring the ASF Writer](configuring-the-asf-writer.md)
-   [Building Filter Graphs to Write ASF Files](building-filter-graphs-to-write-asf-files.md)
-   [Configuring Profiles and Other ASF File Properties](configuring-profiles-and-other-asf-file-properties.md)
-   [Unlocking the Windows Media Format SDK](unlocking-the-windows-media-format-sdk.md)

## Related topics

<dl> <dt>

[Using Windows Media in DirectShow](using-windows-media-in-directshow.md)
</dt> </dl>

 

 



