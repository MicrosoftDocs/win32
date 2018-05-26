---
title: Changing a Video Capture Setting
description: Changing a Video Capture Setting
ms.assetid: a5fe7e1e-084d-4102-91d4-ffe5d1d0e5c8
keywords:
- capCaptureGetSetup macro
- capCaptureSetSetup macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Changing a Video Capture Setting

The following example uses the [**capCaptureGetSetup**](/windows/win32/Vfw/nf-vfw-capcapturegetsetup?branch=master) and [**capCaptureSetSetup**](/windows/win32/Vfw/nf-vfw-capcapturesetsetup?branch=master) macros to change the capture rate from the default value (15 frames per second) to 10 frames per second.


```C++
CAPTUREPARMS CaptureParms;
float FramesPerSec = 10.0;

capCaptureGetSetup(hWndC, &amp;CaptureParms, sizeof(CAPTUREPARMS));

CaptureParms.dwRequestMicroSecPerFrame = (DWORD) (1.0e6 / 
    FramesPerSec);
capCaptureSetSetup(hWndC, &amp;CaptureParms, sizeof (CAPTUREPARMS)); 
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




