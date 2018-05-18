---
title: Enabling Video Overlay
description: Enabling Video Overlay
ms.assetid: 'f0b4f24c-3e35-4a18-ac77-8cae7083b0fe'
keywords: ["capDriverGetCaps macro"]
---

# Enabling Video Overlay

The following example uses the [**capDriverGetCaps**](capdrivergetcaps.md) macro to determine whether a capture driver has overlay capabilities; if it does, the macro enables the overlay.


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

 

 




