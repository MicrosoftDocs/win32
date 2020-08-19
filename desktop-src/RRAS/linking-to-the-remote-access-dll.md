---
title: Linking to the Remote Access DLL
description: If an application links statically to the RASAPI32 DLL, the application will fail to load if Remote Access Service is not installed.
ms.assetid: a2399406-f73c-40aa-877c-80f2f99ed10a
ms.topic: article
ms.date: 05/31/2018
---

# Linking to the Remote Access DLL

If an application links statically to the RASAPI32 DLL, the application will fail to load if Remote Access Service is not installed. A RAS application can load when RAS is not installed by using [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) to load the DLL, and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to obtain pointers to the RAS functions.

The RAS functions are located in RASAPI32.DLL. The import library for these functions is RASAPI32.LIB. To use the RAS functions, your programs must include the following files:



| File       | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| RAS.H      | Contains the RAS function prototypes, constants, and structure definitions. |
| RASERROR.H | Contains the RAS error codes.                                               |



 

 

 