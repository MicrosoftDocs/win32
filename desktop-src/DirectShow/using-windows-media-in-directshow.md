---
description: Using Windows Media in DirectShow
ms.assetid: 2fae0504-d1da-413a-80dd-de7818f506ef
title: Using Windows Media in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using Windows Media in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how to use DirectShow to play and write Advanced Systems Format (ASF) files. ASF files commonly contain audio and video content encoded using the Windows Media Audio and Video codecs. However, ASF can contain any type of data.

The following DirectShow filters support reading and writing ASF files:

-   [WM ASF Reader Filter](wm-asf-reader-filter.md). Reads ASF files.
-   [WM ASF Writer Filter](wm-asf-writer-filter.md). Wrties ASF files.
-   [DMO Wrapper Filter](dmo-wrapper-filter.md). Wraps the Windows Media encoder and decoder DMOs.

### Versions

The WM ASF Reader and WM ASF Writer filters are packaged in the DLL named qasf.dll, and the filters are collectively named "QASF components." These filters are wrappers for the Windows Media Format SDK. The DLL (qasf.dll) was first published in the DirectX SDK but was later updated in the Windows Media Format SDK. Here is the version history of the QASF filters:

-   DirectShow 8.1 supports Windows Media Format SDK version 7.0.
-   DirectShow 9.0 supports Windows Media Format SDK version 7.1.
-   Windows XP Service Pack 2 supports Windows Media Format 9 SDK.
-   Windows Vista supports Windows Media Format 11 SDK.
-   Windows Media Format 9 SDK and later contain corresponding versions of QASF.

To get the latest version of QASF, always download the latest Windows Media Format SDK.

### Legacy Windows Media Source Filter

In Windows XP Service Pack 1 and earlier, the default source filter for ASF files (.asf, .wmv, and .wma file extensions) is the obsolete [Windows Media Source Filter](windows-media-source-filter.md). This behavior was maintained to ensure backward compatibility with applications that used the Windows Media Player 6.4. New applications should use the newer versions of QASF, which make the WM ASF Reader filter the default filter for playing ASF files.

For more information on the Windows Media suite of software development kits, see the [Audio and Video](../audio-and-video.md) section of the MDSN Library.

This article contains the following topics:

-   [Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
-   [Creating ASF Files in DirectShow](creating-asf-files-in-directshow.md)

## Related topics

<dl> <dt>

[Using DirectShow](using-directshow.md)
</dt> </dl>

 

 
