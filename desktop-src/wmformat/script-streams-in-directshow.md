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
ms.date: 05/31/2018
---

# Script Streams in DirectShow

When the WM ASF Reader filter is given a file that includes a stream of type WMMEDIATYPE\_Script, it creates an output pin for it that can be connected to the DirectShow Internal Script Command Renderer filter. When you call **IGraphBuilder::RenderFile**, that filter is automatically added to the graph and connected. When the Internal Script Command Renderer receives a sample containing a script command, it fires an **EC\_OLE\_EVENT** whose **lParam** contains the script. The application is entirely responsible for handling this event. For more information on **EC\_OLE\_EVENT**, see the DirectShow SDK documentation.

 

 




