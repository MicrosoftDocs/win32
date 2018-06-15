---
title: Linking to the Remote Access DLL
description: If an application links statically to the RASAPI32 DLL, the application will fail to load if Remote Access Service is not installed.
ms.assetid: a2399406-f73c-40aa-877c-80f2f99ed10a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Linking to the Remote Access DLL

If an application links statically to the RASAPI32 DLL, the application will fail to load if Remote Access Service is not installed. A RAS application can load when RAS is not installed by using [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) to load the DLL, and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) to obtain pointers to the RAS functions.

The RAS functions are located in RASAPI32.DLL. The import library for these functions is RASAPI32.LIB. To use the RAS functions, your programs must include the following files:



| File       | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| RAS.H      | Contains the RAS function prototypes, constants, and structure definitions. |
| RASERROR.H | Contains the RAS error codes.                                               |



 

 

 




