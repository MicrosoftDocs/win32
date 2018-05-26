---
Description: The header file shown below is included in the following .cpp files that together make up the user account activation exampleUserActivation\_Main.cppUserActivation\_GetServiceURL.cppUserActivation\_Callback.cpp
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a61b1580-e9cf-4933-ab01-7bb63f2eea4b
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: UserActivation.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserActivation.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The header file shown below is included in the following .cpp files that together make up the user account activation example:

-   [UserActivation\_Main.cpp](useractivation-main-cpp.md)
-   [UserActivation\_GetServiceURL.cpp](useractivation-getserviceurl-cpp.md)
-   [UserActivation\_Callback.cpp](useractivation-callback-cpp.md)


```C++
/*===================================================================
File:      UserActivation.h

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

// Define _UNICODE for C run-time (CRT) functions (tchar.h)
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
                          void *pvContext);

// Retrieves the URL of a licensing service that can sign
// the issuance license over a network. In the UserActivation
// example, the licensing service is in the enterprise and 
// not on the Internet.
extern HRESULT GetServiceURL(
                          DRMHSESSION hClient,
                          UINT uiServiceType,
                          UINT uiServiceLocation,
                          PWSTR *ppwszServiceURL);

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

[Activating a User](activating-a-user.md)
</dt> </dl>

 

 



