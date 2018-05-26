---
Description: The header file shown below is included in the following .cpp files that together make up the revocation example
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 9fd5d0f8-d313-4102-99d8-c93feb33b3c2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: RevocationList.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RevocationList.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The header file shown below is included in the following .cpp files that together make up the revocation example:

-   [Revocation\_Main.cpp](revocation-main-cpp.md)
-   [Revocation\_GetRevocationList.cpp](revocation-getrevocationlist-cpp.md)
-   [Revocation\_GetCertificate.cpp](revocation-getcertificate-cpp.md)
-   [Revocation\_GetManifest.cpp](revocation-getmanifest-cpp.md)
-   [Revocation\_GetSecureEnvironment.cpp](revocation-getsecureenvironment-cpp.md)
-   [Revocation\_GetEULChain.cpp](revocation-geteulchain-cpp.md)
-   [Revocation\_ReadEncryptedContent.cpp](revocation-readencryptedcontent-cpp.md)
-   [Revocation\_Callback.cpp](revocation-callback-cpp.md)


```C++
/*===================================================================
File:      RevocationList.h

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
#include <conio.h>        // For _getchar()

// Define _UNICODE for C run-time (CRT) functions (tchar.h)
#ifndef _UNICODE
#define _UNICODE
#endif

// Define UNICODE for Windows UNICODE functions.
#ifndef UNICODE
#define UNICODE
#endif

// Initializes a secure environment and retrieves a handle to it.
HRESULT GetSecureEnvironment(
                 PWSTR          pwszMachineCert,
                 PWSTR          pwszManifest,
                 DRMENVHANDLE*  phEnv,
                 DRMHANDLE*     phLib);

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

// Retrieves a revocation list for the submitted license.
HRESULT GetRevocationList(
                 DRMHSESSION hLicenseStorage,
                 PWSTR pwszEULChain,
                 PWSTR* ppwszRevokeList);

// Retrieves an end user license chain given the appropriate
// issuance license and a license storage session.
HRESULT GetEULChain (
                 DRMHSESSION       hLicenseStorage,
                 DRMENVHANDLE      hEnv,
                 DRMHANDLE         hLib,
                 PWSTR             pwszSignedIL,
                 PWSTR*            ppwszEULChain);

/////////////////////////////////////////////////////////////////////
// The ReadEncryptedContent function reads encrypted content and
// an issuance license from a binary file. The file is created by
// the EncryptingContent example. The format is:
//    Encrypted data length   - 4 bytes
//    Issuance license length - 4 bytes
//    Encrypted data          - variable number of bytes
//    Issuance license        - variable number of bytes
//
HRESULT ReadEncryptedContent(
             PWSTR pwszFileName,
             PWSTR* ppwszIL,
             BYTE** ppbEncrypted);

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

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



