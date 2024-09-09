---
description: ASF Script Streams in DirectShow
ms.assetid: afef1b8b-4be2-48a1-b72a-b2e6342a5e84
title: ASF Script Streams in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ASF Script Streams in DirectShow

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the [WM ASF Reader](wm-asf-reader-filter.md) filter is given a file that includes a stream of type WMMEDIATYPE\_Script, it creates an output pin for it that can be connected to the [Internal Script Command Renderer](internal-script-command-renderer-filter.md) filter. When you call [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile), that filter is automatically added to the graph and connected. When the Internal Script Command Renderer receives a sample containing a script command, it fires an [**EC\_OLE\_EVENT**](ec-ole-event.md) event whose *lParam* contains the script. The application is entirely responsible for handling this event.

## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 



