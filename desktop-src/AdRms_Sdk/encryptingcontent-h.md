---
Description: The header file shown below is included in the following .cpp files that together make up the encryption example:Encryption\_Main.cppEncryption\_EncryptContent.cppEncryption\_GetCertificate.cppEncryption\_GetSecureEnvironment.cppEncryption\_GetManifest.cppEncryption\_GetOfflineSignedIL.cppEncryption\_Callback.cpp
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7e90a7c7-dd08-43cc-8208-81f04561633e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: EncryptingContent.h
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EncryptingContent.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The header file shown below is included in the following .cpp files that together make up the encryption example:

-   [Encryption\_Main.cpp](encryption-main-cpp.md)
-   [Encryption\_EncryptContent.cpp](encryption-encryptcontent-cpp.md)
-   [Encryption\_GetCertificate.cpp](encryption-getcertificate-cpp.md)
-   [Encryption\_GetSecureEnvironment.cpp](encryption-getsecureenvironment-cpp.md)
-   [Encryption\_GetManifest.cpp](encryption-getmanifest-cpp.md)
-   [Encryption\_GetOfflineSignedIL.cpp](encryption-getofflinesignedil-cpp.md)
-   [Encryption\_Callback.cpp](encryption-callback-cpp.md)


```C++
/*===================================================================
File:      EncryptingContent.h

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
#include <msdrmgetinfo.h> // For g_wszQUERY_BLOCKSIZE
#include <conio.h>        // For _getchar()

// Define _UNICODE for C run-time (CRT) functions (tchar.h)
#ifndef _UNICODE
#define _UNICODE
#endif

// Define UNICODE for Windows UNICODE functions.
#ifndef UNICODE
#define UNICODE
#endif

// Content to encrypt.
#define PLAINTEXT L"This is the content to be encrypted."

// Creates an unsigned issuance license, specifies a user and 
// associated right, and signs the license offline by using the 
// client licensor certificate.
HRESULT GetOfflineSignedIL(DRMENVHANDLE hEnv,
                 DRMHANDLE hLib,
                 PWSTR pwszUserID, 
                 PWSTR pwszMachineCert,
                 PWSTR pwszCLC,
                 PWSTR pwszManifest,
                 PWSTR* ppwszGUID,
                 DRMPUBHANDLE* phIssuanceLic,
                 PWSTR *ppwszSignedIL);

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

// Encrypts an item of content. In this example, the content
// to be encrypted is defined by the PLAINTEXT constant value
// in the header file.
HRESULT EncryptContent(
                 DRMENVHANDLE   hEnv,
                 DRMHANDLE      hLib,
                 PWSTR          pwszRAC,
                 PWSTR          pwszGUID,
                 DRMHANDLE      hIssuanceLic,
                 PWSTR          pwszSignedIL,
                 BYTE**         ppbEncrypted);

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

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Encrypting Content Code Example](encrypting-content-code-example.md)
</dt> </dl>

 

 



