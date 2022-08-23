---
title: DirectDraw structures
description: This section contains information about the structures used with DirectDraw.
ms.assetid: 36424B41-B179-414A-ACFF-E63DA7B27043
ms.topic: article
ms.date: 07/12/2022
---

# DirectDraw structures

This section contains information about the following structures used with DirectDraw:

-   [**DDBLTBATCH**](/windows/win32/api/ddraw/ns-ddraw-ddbltbatch)
-   [**DDBLTFX**](/windows/win32/api/ddraw/ns-ddraw-ddbltfx)
-   [**DDCAPS**](/windows/win32/api/ddraw/ns-ddraw-ddcaps_dx3)
-   [**DDCOLORCONTROL**](/windows/win32/api/ddraw/ns-ddraw-ddcolorcontrol)
-   [**DDCOLORKEY**](/windows/win32/api/ddraw/ns-ddraw-ddcolorkey)
-   [**DDDEVICEIDENTIFIER2**](/windows/win32/api/ddraw/ns-ddraw-dddeviceidentifier2)
-   [**DDGAMMARAMP**](/windows/win32/api/ddraw/ns-ddraw-ddgammaramp)
-   [**DDOVERLAYFX**](/windows/win32/api/ddraw/ns-ddraw-ddoverlayfx)
-   [**DDPIXELFORMAT**](/windows/win32/api/ddraw/ns-ddraw-ddpixelformat)
-   [**DDSCAPS**](/windows/win32/api/ddraw/ns-ddraw-ddscaps)
-   [**DDSCAPS2**](/windows/win32/api/ddraw/ns-ddraw-ddscaps2)
-   [**DDSURFACEDESC**](/windows/win32/api/ddraw/ns-ddraw-ddsurfacedesc)
-   [**DDSURFACEDESC2**](/windows/win32/api/ddraw/ns-ddraw-ddsurfacedesc2)

> [!NOTE]  
> You should initialize the memory for each DirectX structure to 0 before you use the structure. In addition, for all structures that contain a *dwSize* member, you should set the member to the size of the structure, in bytes, before you use the structure. The following example performs those tasks on an object of type [**DDCAPS_DX3**](/windows/win32/api/ddraw/ns-ddraw-ddcaps_dx3):

```
DDCAPS_DX3 ddcaps; // You can't use this yet.
 
ZeroMemory(&ddcaps, sizeof(DDCAPS_DX3));
ddcaps.dwSize = sizeof(DDCAPS_DX3);
 
// Now you can use the structure.
...
```
