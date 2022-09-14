---
description: ASF Script Streams in DirectShow
ms.assetid: afef1b8b-4be2-48a1-b72a-b2e6342a5e84
title: ASF Script Streams in DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# ASF Script Streams in DirectShow

When the [WM ASF Reader](wm-asf-reader-filter.md) filter is given a file that includes a stream of type WMMEDIATYPE\_Script, it creates an output pin for it that can be connected to the [Internal Script Command Renderer](internal-script-command-renderer-filter.md) filter. When you call [**IGraphBuilder::RenderFile**](/windows/desktop/api/Strmif/nf-strmif-igraphbuilder-renderfile), that filter is automatically added to the graph and connected. When the Internal Script Command Renderer receives a sample containing a script command, it fires an [**EC\_OLE\_EVENT**](ec-ole-event.md) event whose *lParam* contains the script. The application is entirely responsible for handling this event.

## Related topics

<dl> <dt>

[Reading ASF Files in DirectShow](reading-asf-files-in-directshow.md)
</dt> </dl>

 

 



