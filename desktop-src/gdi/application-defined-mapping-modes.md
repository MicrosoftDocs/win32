---
description: The two application-defined mapping modes (MM\_ISOTROPIC and MM\_ANISOTROPIC) are provided for application-specific mapping modes.
ms.assetid: c4c4e352-63fc-4e97-a218-a1b7deac02e8
title: Application-Defined Mapping Modes
ms.topic: article
ms.date: 05/31/2018
---

# Application-Defined Mapping Modes

The two application-defined mapping modes (MM\_ISOTROPIC and MM\_ANISOTROPIC) are provided for application-specific mapping modes. The MM\_ISOTROPIC mode guarantees that logical units in the x-direction and in the y-direction are equal, while the MM\_ANISOTROPIC mode allows the units to differ. A CAD or drawing application can benefit from the MM\_ISOTROPIC mapping mode but may need to specify logical units that correspond to the increments on an engineer's scale (1/64 inch). These units would be difficult to obtain with the predefined mapping modes (MM\_HIENGLISH or MM\_HIMETRIC); however, they can easily be obtained by selecting the MM\_ISOTROPIC (or MM\_ANISOTROPIC) mode. The following example shows how to set logical units to 1/64 inch:


```C++
SetMapMode(hDC, MM_ISOTROPIC); 
SetWindowExtEx(hDC, 64, 64, NULL); 
SetViewportExtEx(hDC, GetDeviceCaps(hDC, LOGPIXELSX), 
                      GetDeviceCaps(hDC, LOGPIXELSY), NULL); 
```



 

 



