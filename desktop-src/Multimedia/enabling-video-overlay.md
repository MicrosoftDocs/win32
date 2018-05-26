---
title: Enabling Video Overlay
description: Enabling Video Overlay
ms.assetid: f0b4f24c-3e35-4a18-ac77-8cae7083b0fe
keywords:
- capDriverGetCaps macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enabling Video Overlay

The following example uses the [**capDriverGetCaps**](/windows/win32/Vfw/nf-vfw-capdrivergetcaps?branch=master) macro to determine whether a capture driver has overlay capabilities; if it does, the macro enables the overlay.


```C++
CAPDRIVERCAPS CapDrvCaps; 

capDriverGetCaps(hWndC, &amp;CapDrvCaps, sizeof (CAPDRIVERCAPS)); 

if (CapDrvCaps.fHasOverlay) 
    capOverlay(hWndC, TRUE);
 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




