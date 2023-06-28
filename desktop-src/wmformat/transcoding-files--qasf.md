---
title: Transcoding Files (QASF)
description: Transcoding Files (QASF)
ms.assetid: c6dad6cf-4781-4204-883b-cdb33aff5e27
keywords:
- Windows Media Format SDK,transcoding files (QASF)
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),transcoding files (QASF)
- ASF (Advanced Systems Format),transcoding files (QASF)
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- DirectShow,transcoding files (QASF)
- Windows Media Format SDK,QASF
- Advanced Systems Format (ASF),QASF
- ASF (Advanced Systems Format),QASF
- DirectShow,QASF
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Transcoding Files (QASF)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can build a file-transcoding filter graph using the [WM ASF Writer](wm-asf-writer-filter.md) in various ways. The easiest way is to co-create, configure, and add the WM ASF Writer to the filter graph, and then use the **IGraphBuilder::RenderFile** method to build the graph automatically.

An alternative way is to add each filter manually to the graph and connect the pins. After adding the WM ASF Writer, configure it by using the **IConfigAsfWriter** methods if the default profile is not suitable, and connect the WM ASF Writer input pins to the corresponding output pins on the upstream filters.

The following illustration shows typical WM ASF Writer transcoding filter graph configurations.

![typical transcoding filter graphs](images/asf-transcode.png)

 

 




