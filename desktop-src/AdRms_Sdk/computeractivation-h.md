---
Description: The following example shows the header file used by the ComputerActivation\_Main.cpp and ComputerActivation\_Callback.cpp files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 806bbc49-b05f-4fc6-8c47-7c9840bab435
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: ComputerActivation.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ComputerActivation.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows the header file used by the [ComputerActivation\_Main.cpp](computeractivation-main-cpp.md) and [ComputerActivation\_Callback.cpp](computeractivation-callback-cpp.md) files.


```C++
/*===================================================================
File:      ComputerActivation.h

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

#include <tchar.h>        // Command line arguments
#include <msdrm.h>        // AD RMS functions
#include <msdrmerror.h>   // Custom AD RMS error codes
#include <conio.h>        // For _getch()

// Define _UNICODE for C run-time (CRT) functions (tchar.h).
#ifndef _UNICODE
#define _UNICODE
#endif

// Define UNICODE for Windows UNICODE functions.
#ifndef UNICODE
#define UNICODE
#endif

// User-defined function called by asynchronous AD RMS
// functions to report operation status. The function must
// have the following signature.
extern HRESULT __stdcall StatusCallback(
                          DRM_STATUS_MSG msg, 
                          HRESULT hr, 
                          void *pvParam, 
                          void *pvContext );

// User-defined structure that can be passed to the pvContext
// parameter of the callback function and used to transmit status
// information to your application.
typedef struct Drm_Context
{
    HANDLE  hEvent;
    HRESULT hr;
} DRM_CONTEXT, *PDRM_CONTEXT;
```



## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[ComputerActivation\_Callback.cpp](computeractivation-callback-cpp.md)
</dt> <dt>

[ComputerActivation\_Main.cpp](computeractivation-main-cpp.md)
</dt> </dl>

 

 



