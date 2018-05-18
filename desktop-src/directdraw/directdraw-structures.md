---
title: DirectDraw Structures
description: This section contains information about the following structures used with DirectDraw
ms.assetid: '36424B41-B179-414A-ACFF-E63DA7B27043'
---

# DirectDraw Structures

This section contains information about the following structures used with DirectDraw:

-   [**DDBLTBATCH**](ddbltbatch.md)
-   [**DDBLTFX**](ddbltfx.md)
-   [**DDCAPS**](ddcaps.md)
-   [**DDCOLORCONTROL**](ddcolorcontrol.md)
-   [**DDCOLORKEY**](ddcolorkey.md)
-   [**DDDEVICEIDENTIFIER2**](dddeviceidentifier2.md)
-   [**DDGAMMARAMP**](ddgammaramp.md)
-   [**DDOVERLAYFX**](ddoverlayfx.md)
-   [**DDPIXELFORMAT**](ddpixelformat.md)
-   [**DDSCAPS**](ddscaps.md)
-   [**DDSCAPS2**](ddscaps2.md)
-   [**DDSURFACEDESC**](ddsurfacedesc.md)
-   [**DDSURFACEDESC2**](ddsurfacedesc2.md)

> [!Note]  
> You should initialize the memory for each DirectX structure to 0 before you use the structure. In addition, for all structures that contain a **dwSize** member, you should set the member to the size of the structure, in bytes, before the structure is used. The following example performs these tasks on a common structure, [**DDCAPS**](ddcaps.md):

 


```
DDCAPS ddcaps; // You cannot use this yet.
 
ZeroMemory(&amp;ddcaps, sizeof(DDCAPS));
ddcaps.dwSize = sizeof(DDCAPS);
 
// Now you can use the structure.
.
.
```



 

 




