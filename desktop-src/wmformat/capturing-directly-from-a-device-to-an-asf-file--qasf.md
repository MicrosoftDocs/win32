---
title: Capturing Directly from a Device to an ASF File (QASF)
description: Capturing Directly from a Device to an ASF File (QASF)
ms.assetid: 684a11e3-d507-4219-bc0b-6dfe5e85dad1
keywords:
- Windows Media Format SDK,capturing from devices to ASF files (QASF)
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),capturing from devices (QASF)
- ASF (Advanced Systems Format),capturing from devices (QASF)
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- DirectShow,capturing from devices to ASF files (QASF)
- Windows Media Format SDK,QASF
- Advanced Systems Format (ASF),QASF
- ASF (Advanced Systems Format),QASF
- DirectShow,QASF
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Capturing Directly from a Device to an ASF File (QASF)

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

When capturing audio or video directly to an ASF file, the filter graph looks something like the following diagram, depending on the type of capture device being used.

![webcam to wmv capture graph](images/asf-webcam.png)

The DirectShow SDK documentation describes in detail how to create capture graphs, but there is one important point to remember when creating capture graphs using the WM ASF Writer: the WM ASF Writer will not run unless all of its pins are connected. If you configure the WM ASF Writer with the default system profile (not recommended), or any profile with audio and video streams, then it will create an input pin for each stream and each of those pins must be connected. If you do not intend to capture audio, for example, then be sure to configure the filter with a video-only profile so that no audio pin is created.

 

 




