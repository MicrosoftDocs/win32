---
title: DirectDraw Structures
description: This section contains information about the following structures used with DirectDraw
ms.assetid: 36424B41-B179-414A-ACFF-E63DA7B27043
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DirectDraw Structures

This section contains information about the following structures used with DirectDraw:

-   [**DDBLTBATCH**](/windows/win32/Ddraw/ns-ddraw-_ddbltbatch?branch=master)
-   [**DDBLTFX**](/windows/win32/Ddraw/ns-ddraw-_ddbltfx?branch=master)
-   [**DDCAPS**](/windows/win32/Ddraw/ns-ddraw-_ddcaps_dx3?branch=master)
-   [**DDCOLORCONTROL**](/windows/win32/Ddraw/ns-ddraw-_ddcolorcontrol?branch=master)
-   [**DDCOLORKEY**](/windows/win32/Ddraw/ns-ddraw-_ddcolorkey?branch=master)
-   [**DDDEVICEIDENTIFIER2**](/windows/win32/Ddraw/ns-ddraw-tagdddeviceidentifier2?branch=master)
-   [**DDGAMMARAMP**](/windows/win32/Ddraw/ns-ddraw-_ddgammaramp?branch=master)
-   [**DDOVERLAYFX**](/windows/win32/Ddraw/ns-ddraw-_ddoverlayfx?branch=master)
-   [**DDPIXELFORMAT**](/windows/win32/Ddraw/ns-ddraw-_ddpixelformat?branch=master)
-   [**DDSCAPS**](/windows/win32/Ddraw/ns-ddraw-_ddscaps?branch=master)
-   [**DDSCAPS2**](/windows/win32/Ddraw/ns-ddraw-_ddscaps2?branch=master)
-   [**DDSURFACEDESC**](/windows/win32/Ddraw/ns-ddraw-_ddsurfacedesc?branch=master)
-   [**DDSURFACEDESC2**](/windows/win32/Ddraw/ns-ddraw-_ddsurfacedesc2?branch=master)

> [!Note]  
> You should initialize the memory for each DirectX structure to 0 before you use the structure. In addition, for all structures that contain a **dwSize** member, you should set the member to the size of the structure, in bytes, before the structure is used. The following example performs these tasks on a common structure, [**DDCAPS**](/windows/win32/Ddraw/ns-ddraw-_ddcaps_dx3?branch=master):

 


```
DDCAPS ddcaps; // You cannot use this yet.
 
ZeroMemory(&amp;ddcaps, sizeof(DDCAPS));
ddcaps.dwSize = sizeof(DDCAPS);
 
// Now you can use the structure.
.
.
```



 

 




