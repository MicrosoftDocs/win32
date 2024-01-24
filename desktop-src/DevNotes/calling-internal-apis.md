---
description: The Winternl.h header file exposes prototypes of internal Windows APIs. There is no associated import library, so developers must use run-time dynamic linking to call the functions described in this header file.
ms.assetid: 11f09479-e04b-4e5e-bc46-a2d0daf13785
title: Calling Internal APIs
ms.topic: article
ms.date: 05/31/2018
---

# Calling Internal APIs

The Winternl.h header file exposes prototypes of internal Windows APIs. There is no associated import library, so developers must use run-time dynamic linking to call the functions described in this header file.

The functions and structures in Winternl.h are internal to the operating system and subject to change from one release of Windows to the next, and possibly even between service packs for each release. To maintain the compatibility of your application, you should use the equivalent public functions instead. Further information is available in the header file, Winternl.h, and the documentation for each function.

If you do use these functions, you can access them through run-time dynamic linking using [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress). This gives your code an opportunity to respond gracefully if the function has been changed or removed from the operating system. Signature changes, however, may not be detectable.

 

 
