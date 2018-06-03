---
Description: The header file shown below is included in the following .cpp files that together make up the offline signing example:OfflineSigning\_Main.cppOfflineSigning\_GetSignedIL.cppOfflineSigning\_GetServiceURL.cppOfflineSigning\_GetCertificate.cppOfflineSigning\_GetCLC.cppOfflineSigning\_GetManifest.cppOfflineSigning\_Callback.cpp
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: df1d3919-5406-4b33-8702-f04275e01ed5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OfflineILSigning.h
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OfflineILSigning.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The header file shown below is included in the following .cpp files that together make up the offline signing example:

-   [OfflineSigning\_Main.cpp](offlinesigning-main-cpp.md)
-   [OfflineSigning\_GetSignedIL.cpp](offlinesigning-getsignedil-cpp.md)
-   [OfflineSigning\_GetServiceURL.cpp](offlinesigning-getserviceurl-cpp.md)
-   [OfflineSigning\_GetCertificate.cpp](offlinesigning-getcertificate-cpp.md)
-   [OfflineSigning\_GetCLC.cpp](offlinesigning-getclc-cpp.md)
-   [OfflineSigning\_GetManifest.cpp](offlinesigning-getmanifest-cpp.md)
-   [OfflineSigning\_Callback.cpp](offlinesigning-callback-cpp.md)


```C++
/*===================================================================
File:      OfflineSigning.h

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

// Creates an unsigned issuance license, specifies a user and 
// associated right, and signs the license offline by using the 
// client licensor certificate.
HRESULT GetOfflineSignedIL(
                 PWSTR wszUserID, 
                 PWSTR pwszMachineCert,
                 PWSTR pwszCLC,
                 PWSTR pwszManifest,
                 PWSTR *ppwszSignedIL);

// Retrieves a UNICODE string that contains the requested
// certificate. The certificate is retrieved from the local store.
HRESULT GetCertificate(
                 DRMHSESSION hClient, 
                 UINT uFlags, 
                 PWSTR *ppwszCertificate);

// Retrieves a UNICODE string that contains the signed application
// manifest in the file specified by the pwszFileName parameter.
HRESULT GetManifest(
                 PWSTR pwszFileName, 
                 PWSTR *ppwszManifest);

// Retrieves a client licensor certificate (CLC) from an
// AD RMS licensing service in the enterprise.
HRESULT GetCLCFromSvc(
                 DRMHSESSION hClient,
                 PWSTR *ppwszCLC);

// Retrieves the URL of a licensing service that can sign
// the issuance license over a network. In this example,
// the licensing service is in the enterprise and not on
// the Internet.
HRESULT GetServiceURL(
                 DRMHSESSION hClient,
                 UINT uSvcType,
                 UINT uSvcLocation,
                 PWSTR* ppwszLicensingSvr);

// User-defined function called by asynchronous AD RMS
// functions to report operation status. The function must
// have the following signature.
HRESULT __stdcall StatusCallback( 
                 DRM_STATUS_MSG msg, 
                 HRESULT hr, 
                 void* pvParam, 
                 void* pvContext);

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

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> </dl>

 

 



