---
title: Obtaining the Capabilities of a Capture Driver
description: Obtaining the Capabilities of a Capture Driver
ms.assetid: '17e90ca6-3646-41cb-8d7a-a2102bc16cc5'
keywords: ["WM_CAP_DRIVER_GET_CAPS message", "capDriverGetCaps macro", "CAPDRIVERCAPS structure"]
---

# Obtaining the Capabilities of a Capture Driver

The [**WM\_CAP\_DRIVER\_GET\_CAPS**](wm-cap-driver-get-caps.md) message returns the capabilities of the capture driver and underlying hardware in the [**CAPDRIVERCAPS**](capdrivercaps.md) structure. Each time an application connects a new capture driver to the capture window, it should update the **CAPDRIVERCAPS** structure. The following example uses the [**capDriverGetCaps**](capdrivergetcaps.md) macro to obtain the capture driver capabilities.


```C++
CAPDRIVERCAPS CapDrvCaps; 

SendMessage (hWndC, WM_CAP_DRIVER_GET_CAPS, 
    sizeof (CAPDRIVERCAPS), (LONG) (LPVOID) &amp;CapDrvCaps); 

// Or, use the macro to retrieve the driver capabilities. 
// capDriverGetCaps(hWndC, &amp;CapDrvCaps, sizeof (CAPDRIVERCAPS)); 
```



## Related topics

<dl> <dt>

[Using Video Capture](using-video-capture.md)
</dt> </dl>

 

 




