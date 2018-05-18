---
title: WMT\_STATUS Event Notification in DirectShow
description: WMT\_STATUS Event Notification in DirectShow
ms.assetid: '6b777c7e-2777-445b-88de-a9a28be6da9c'
keywords: ["Windows Media Format SDK,WMT_STATUS event notifications in DirectShow", "Windows Media Format SDK,event notifications", "Windows Media Format SDK,DirectShow", "Advanced Systems Format (ASF),WMT_STATUS event notifications in DirectShow", "ASF (Advanced Systems Format),WMT_STATUS event notifications in DirectShow", "Advanced Systems Format (ASF),event notifications", "ASF (Advanced Systems Format),event notifications", "Advanced Systems Format (ASF),DirectShow", "ASF (Advanced Systems Format),DirectShow", "DirectShow,event notifications", "DirectShow,WMT_STATUS event notifications"]
---

# WMT\_STATUS Event Notification in DirectShow

Both the ASF Reader and the ASF Writer forward [**WMT\_STATUS**](wmt-status.md) events to applications. The writer forwards all such events, and the reader forwards only those that pertain to DRM license acquisition. To receive these event notifications in your application, add a case for the **EC\_WMT\_EVENT** in your event-handling function. The *lParam1* parameter associated with the event contains the **WMT\_STATUS** code (which can be **WMT\_ERROR**) and lParam2 contains an [**AM\_WMT\_EVENT\_DATA**](am-wmt-event-data.md) that includes the **HRESULT**.

 

 




