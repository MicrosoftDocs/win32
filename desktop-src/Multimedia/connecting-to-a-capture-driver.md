---
title: Connecting to a Capture Driver
description: Connecting to a Capture Driver
ms.assetid: ce83329f-de5a-4428-bc0d-be5f3d35ff1a
keywords:
- capDriverDisconnect macro
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to a Capture Driver

The following example connects the capture window with the handle *hWndC* to the MSVIDEO driver and then disconnects them using the [**capDriverDisconnect**](/windows/desktop/api/Vfw/nf-vfw-capdriverdisconnect) macro:


```C++
fOK = SendMessage (hWndC, WM_CAP_DRIVER_CONNECT, 0, 0L); 
// 
// Or, use the macro to connect to the MSVIDEO driver: 
// fOK = capDriverConnect(hWndC, 0); 
// 
// Place code to set up and capture video here. 
// 
capDriverDisconnect (hWndC); 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




