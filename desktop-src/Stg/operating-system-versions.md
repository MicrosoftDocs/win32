---
title: Operating System Versions
description: This DWORD data type should hold the operating system type in the high-order word and the version number of the operating system in the low-order word. Possible values for the operating system are listed in the following table.
ms.assetid: 318e277b-a797-45a5-87c5-25b91fdf278d
keywords:
- Operating System Versions Structured Storage
ms.topic: article
ms.date: 05/31/2018
---

# Operating System Versions

This **DWORD** data type should hold the operating system type in the high-order word and the version number of the operating system in the low-order word. Possible values for the operating system are listed in the following table.



| Operating system       | Value  |
|------------------------|--------|
| 32-Bit Windows (Win32) | 0x0002 |
| Macintosh              | 0x0001 |
| 16-Bit Windows (Win16) | 0x0000 |



 

For Microsoft Windows operating systems, the operating system version is the low-order word returned by the [**GetVersion**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getversion) function. For Microsoft Windows, the following example code correctly sets the version of the originating operating system.

``` syntax
#ifdef WIN32 
    dwOSVer = (DWORD)MAKELONG( LOWORD(GetVersion()), 2 ) ; 
#else 
    dwOSVer = (DWORD)MAKELONG( LOWORD(GetVersion()), 0 ) ; 
#endif
```

 

 