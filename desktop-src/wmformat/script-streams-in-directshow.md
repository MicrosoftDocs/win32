---
title: Script Streams in DirectShow
description: Script Streams in DirectShow
ms.assetid: ad467897-1d25-4bb0-a0ec-84560fe7063b
keywords:
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,script streams
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),script streams
- ASF (Advanced Systems Format),script streams
- DirectShow,script streams
- script streams,DirectShow
- streams,script streams in DirectShow
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Script Streams in DirectShow

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When the WM ASF Reader filter is given a file that includes a stream of type WMMEDIATYPE\_Script, it creates an output pin for it that can be connected to the DirectShow Internal Script Command Renderer filter. When you call **IGraphBuilder::RenderFile**, that filter is automatically added to the graph and connected. When the Internal Script Command Renderer receives a sample containing a script command, it fires an **EC\_OLE\_EVENT** whose **lParam** contains the script. The application is entirely responsible for handling this event. For more information on **EC\_OLE\_EVENT**, see the DirectShow SDK documentation.

 

 




