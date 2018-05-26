---
Description: The header file shown below is included in the following .cpp files that together make up the online signing exampleOnlineSigning\_Main.cppOnlineSigning\_GetServiceURL.cppOnlineSigning\_GetUnsignedIL.cppOnlineSigning\_Callback.cpp
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 57767115-e2d8-4a87-a7c4-c80d62460ab4
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineILSigning.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnlineILSigning.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The header file shown below is included in the following .cpp files that together make up the online signing example:

-   [OnlineSigning\_Main.cpp](onlinesigning-main-cpp.md)
-   [OnlineSigning\_GetServiceURL.cpp](onlinesigning-getserviceurl-cpp.md)
-   [OnlineSigning\_GetUnsignedIL.cpp](onlinesigning-getunsignedil-cpp.md)
-   [OnlineSigning\_Callback.cpp](onlinesigning-callback-cpp.md)


```C++
/*===================================================================
File:      OnlineILSigning.h

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

#include <tchar.h>        // Command line arguments.
#include <windows.h>      // GetSystemTime
#include <strsafe.h>      // StringCchLength and StringCchCopy
#include <msdrm.h>        // AD RMS functions 
#include <msdrmdefs.h>    // AD RMS structures, constants, enums
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

// Creates an issuance license.
extern HRESULT GetUnsignedIL(
                 PWSTR wszUserId, 
                 DRMPUBHANDLE* phIssuanceLic);

// Retrieves the URL of a licensing service that can sign
// the issuance license over a network. In this example,
// the licensing service is in the enterprise and not on
// the Internet.
extern HRESULT GetServiceURL(
                 DRMHSESSION hClient, 
                 UINT uSvcType, 
                 UINT uSvcLocation,
                 PWSTR* ppwszLicensingSvr);

// User-defined function called by asynchronous AD RMS
// functions to report operation status. The function must
// have the following signature.
extern HRESULT __stdcall StatusCallback( 
                 DRM_STATUS_MSG msg, 
                 HRESULT hr, 
                 void *pvParam, 
                 void *pvContext);

// User-defined structure that can be passed to the pvContext
// parameter of the callback function and used to transmit status
// information to your application.
typedef struct Drm_Context
{
  HANDLE  hEvent;
  HRESULT hr;
  PWSTR   pwszData;
} DRM_CONTEXT, *PDRM_CONTEXT;
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



