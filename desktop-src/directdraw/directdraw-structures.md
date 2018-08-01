---
title: DirectDraw Structures
description: This section contains information about the following structures used with DirectDraw
ms.assetid: 36424B41-B179-414A-ACFF-E63DA7B27043
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DirectDraw Structures

This section contains information about the following structures used with DirectDraw:

-   [**DDBLTBATCH**](/windows/desktop/api/Ddraw/ns-ddraw-_ddbltbatch)
-   [**DDBLTFX**](/windows/desktop/api/Ddraw/ns-ddraw-_ddbltfx)
-   [**DDCAPS**](/windows/desktop/api/Ddraw/ns-ddraw-_ddcaps_dx3)
-   [**DDCOLORCONTROL**](/windows/desktop/api/Ddraw/ns-ddraw-_ddcolorcontrol)
-   [**DDCOLORKEY**](/windows/desktop/api/Ddraw/ns-ddraw-_ddcolorkey)
-   [**DDDEVICEIDENTIFIER2**](/windows/desktop/api/Ddraw/ns-ddraw-tagdddeviceidentifier2)
-   [**DDGAMMARAMP**](/windows/desktop/api/Ddraw/ns-ddraw-_ddgammaramp)
-   [**DDOVERLAYFX**](/windows/desktop/api/Ddraw/ns-ddraw-_ddoverlayfx)
-   [**DDPIXELFORMAT**](/windows/desktop/api/Ddraw/ns-ddraw-_ddpixelformat)
-   [**DDSCAPS**](/windows/desktop/api/Ddraw/ns-ddraw-_ddscaps)
-   [**DDSCAPS2**](/windows/desktop/api/Ddraw/ns-ddraw-_ddscaps2)
-   [**DDSURFACEDESC**](/windows/desktop/api/Ddraw/ns-ddraw-_ddsurfacedesc)
-   [**DDSURFACEDESC2**](/windows/desktop/api/Ddraw/ns-ddraw-_ddsurfacedesc2)

> [!Note]  
> You should initialize the memory for each DirectX structure to 0 before you use the structure. In addition, for all structures that contain a **dwSize** member, you should set the member to the size of the structure, in bytes, before the structure is used. The following example performs these tasks on a common structure, [**DDCAPS**](/windows/desktop/api/Ddraw/ns-ddraw-_ddcaps_dx3):

 


```
DDCAPS ddcaps; // You cannot use this yet.
 
ZeroMemory(&ddcaps, sizeof(DDCAPS));
ddcaps.dwSize = sizeof(DDCAPS);
 
// Now you can use the structure.
.
.
```



 

 




