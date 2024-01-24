---
description: Working with Codecs
ms.assetid: c69e0ecf-5f72-4d77-90e6-0f493325c0f4
title: Working with Codecs
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with Codecs

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Microsoft Windows provides several codecs as operating system components. The available codecs always include those that ship with whichever version of the DirectX and Windows Media Player was included in the Windows release. Additional codecs may be installed when newer versions of DirectX or Windows Media Player or the Windows Media SDK runtimes are installed. Third parties may install additional codecs on a host system; these codecs may be designed to work only with a particular application, or they may support general use by any DirectShow application.

Codecs may be implemented in one of three different ways:

-   As a Video for Windows-type audio or video installable codec that is loaded by the Video Compression Manager (VCM) or Audio Compression Manager (ACM). In general, this technology is considered deprecated and its use is not recommended. Installable codecs participate in DirectShow filter graphs through the AVI Decompressor wrapper filter.
-   As a DirectShow filter. Many third party codecs are implemented as native DirectShow filters. One such filter is the Frauenhofer MP3 decompressor filter. In general, these filters may be added to the filter graph in the usual ways. One exception to this rule is that some Windows Media™ Audio or Windows Media Video codecs, and the Microsoft MPEG-4 codec, cannot be added to a filter graph manually. These filters can only be added by the ASF Reader and ASF Writer filters.
-   As DirectX Media Objects (DMOs). DMOs are the recommended way to implement codecs because they can be used either within a DirectShow filter graph using the DMO Wrapper filter, or else independently in any other non-DirectShow-based streaming application. Some Windows Media Audio and Windows Media Video codecs are implemented as DMOs. As with the Windows Media filters, these DMOs cannot be used outside the context of the Windows Media SDK. That means that in DirectShow, they can only be added to a graph through the ASF Reader or ASF Writer filters.

In GraphEdit, all these different types of codecs appear together under the following categories:

-   Audio compressor
-   Video compressor
-   DirectShow filter

Many of these codecs, however, are installed by third parties, or by other Microsoft applications or operating system components, and are not meant for use by other DirectShow applications. The list of codecs visible in GraphEdit also depends on which version of Windows is running on the host system, and which version of the DirectShow SDK is installed.

 

 



