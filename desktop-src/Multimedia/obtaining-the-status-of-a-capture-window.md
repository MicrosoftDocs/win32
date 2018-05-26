---
title: Obtaining the Status of a Capture Window
description: Obtaining the Status of a Capture Window
ms.assetid: 5095dbd2-7cd4-48b6-bbb4-1f0bddfcfd06
keywords:
- capGetStatus macro
- CAPSTATUS structure
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining the Status of a Capture Window

The following example uses the [SetWindowPos](http://go.microsoft.com/fwlink/p/?linkid=17105) function to set the size of the capture window to the overall dimensions of the incoming video stream based on information returned by the [**capGetStatus**](/windows/win32/Vfw/nf-vfw-capgetstatus?branch=master) macro in the [**CAPSTATUS**](/windows/win32/Vfw/ns-vfw-tagcapstatus?branch=master) structure.


```C++
CAPSTATUS CapStatus;

capGetStatus(hWndC, &amp;CapStatus, sizeof (CAPSTATUS)); 

SetWindowPos(hWndC, NULL, 0, 0, CapStatus.uiImageWidth, 
    CapStatus.uiImageHeight, SWP_NOZORDER | SWP_NOMOVE); 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




