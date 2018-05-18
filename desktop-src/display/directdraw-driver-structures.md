---
Description: DirectDraw Driver Structures
ms.assetid: '4fdf0ed7-0a7b-41f7-bbc3-ca694b4a1776'
title: DirectDraw Driver Structures
---

# DirectDraw Driver Structures

## 

This section describes the Microsoft DirectDraw driver structures supported on Microsoft Windows. These structures are used by display drivers that offer DirectDraw support. [DirectDraw](display.directdraw) lists the header files that define the DirectDraw structures described in this section.

Although the DD\_*Xxx* types described in this reference refer to the actual structures in the *ddrawint.h* header file, it is recommended that driver writers use the DDHAL\_*Xxx* types from *ddrawi.h*. In cases where the structure names are different in the headers *ddrawi.h* and *ddrawint.h* use types from the *ddrawi.h* file for cross-platform compatibility. The minor naming differences are aliased with typedefs in the *dx95type.h* header file, which is provided to help port drivers from Windows 98/Me to Windows 2000 and later.

See [DirectDraw Driver Functions](directdraw-driver-functions.md) for function and callback reference information.

Note that the memory for all Microsoft DirectX structures should be initialized to zero before the structures are used. In addition, all structures that contain a **dwSize** member should set this member to the size of the structure, in bytes, before use. The following example performs these tasks on a common structure, [**DDCORECAPS**](ddcorecaps.md):


```
DDCORECAPS ddcorecaps; // Cannot use this yet.

ZeroMemory(&amp;ddcorecaps, sizeof(ddcorecaps));
ddcorecaps.dwSize = sizeof(ddcorecaps);

// Now the structure can be used.
```



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdisplay\display%5D:%20DirectDraw%20Driver%20Structures%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")



