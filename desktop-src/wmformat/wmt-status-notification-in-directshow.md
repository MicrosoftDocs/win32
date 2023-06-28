---
title: WMT_STATUS Event Notification in DirectShow
description: WMT\_STATUS Event Notification in DirectShow
ms.assetid: 6b777c7e-2777-445b-88de-a9a28be6da9c
keywords:
- Windows Media Format SDK,WMT_STATUS event notifications in DirectShow
- Windows Media Format SDK,event notifications
- Windows Media Format SDK,DirectShow
- Advanced Systems Format (ASF),WMT_STATUS event notifications in DirectShow
- ASF (Advanced Systems Format),WMT_STATUS event notifications in DirectShow
- Advanced Systems Format (ASF),event notifications
- ASF (Advanced Systems Format),event notifications
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- DirectShow,event notifications
- DirectShow,WMT_STATUS event notifications
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# WMT\_STATUS Event Notification in DirectShow

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Both the ASF Reader and the ASF Writer forward [**WMT\_STATUS**](/previous-versions/windows/desktop/api/Wmsdkidl/ne-wmsdkidl-wmt_status) events to applications. The writer forwards all such events, and the reader forwards only those that pertain to DRM license acquisition. To receive these event notifications in your application, add a case for the **EC\_WMT\_EVENT** in your event-handling function. The *lParam1* parameter associated with the event contains the **WMT\_STATUS** code (which can be **WMT\_ERROR**) and lParam2 contains an [**AM\_WMT\_EVENT\_DATA**](/previous-versions/windows/desktop/api/evcode/ns-evcode-am_wmt_event_data) that includes the **HRESULT**.

 

 