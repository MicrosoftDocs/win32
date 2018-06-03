---
Description: DecryptingContent.h
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a0562c71-c97d-4e79-8777-f7fe54c56dcc
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DecryptingContent.h
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DecryptingContent.h

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The header file shown below is included in the following .cpp files that together make up the decryption example:

-   [Decryption\_Main.cpp](decryption-main-cpp.md)
-   [Decryption\_ReadEncryptedContent.cpp](decryption-readencryptedcontent-cpp.md)
-   [Decryption\_GetSecureEnvironment.cpp](decryption-getsecureenvironment-cpp.md)
-   [Decryption\_GetManifest.cpp](decryption-getmanifest-cpp.md)
-   [Decryption\_GetContentID.cpp](decryption-getcontentid-cpp.md)
-   [Decryption\_GetCertificate.cpp](decryption-getcertificate-cpp.md)
-   [Decryption\_GetBoundLicense.cpp](decryption-getboundlicense-cpp.md)
-   [Decryption\_DecryptContent.cpp](decryption-decryptcontent-cpp.md)
-   [Decryption\_Callback.cpp](decryption-callback-cpp.md)


```C++
/*===================================================================
File:      DecryptingContent.h

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

// Encrypted content.
#define PLAINTEXT L"This is the content to be encrypted."

// Initializes a secure environment and retrieves a handle to it.
HRESULT GetSecureEnvironment(
                 PWSTR          pwszMachineCert,
                 PWSTR          pwszManifest,
                 DRMENVHANDLE*  phEnv,
                 DRMHANDLE*     phLib);

// Retrieves a UNICODE string that contains the requested
// certificate. The certificate is retrieved from the local store.
HRESULT GetCertificate(
                 DRMHSESSION    hSession, 
                 UINT           uFlags, 
                 PWSTR          *ppwszCertificate);

// Retrieves a UNICODE string that contains the signed application
// manifest in the file specified by the pwszFileName parameter.
HRESULT GetManifest(
                 PWSTR          pwszFileName, 
                 PWSTR          *ppwszManifest);

// Retrieves an end user license and uses it to create a license
// that is bound to the EDIT right.
HRESULT GetBoundLicense (
                 DRMHSESSION    hClient, 
                 DRMENVHANDLE   hEnv,
                 DRMHANDLE      hLib,
                 PWSTR          pwszRAC,
                 PWSTR          pwszSignedIL,
                 DRMHANDLE*     phBoundLic);

// Retrieves a UNICODE string that contains the content ID
// from the end user license.
HRESULT GetContentID(
                 PWSTR          pwszEUL,
                 PWSTR*         ppwszContentID);

// Reads a binary file to retrieve a signed issuance license
// and a byte array that contains encrypted content. In this
// example, the encrypted content is created by the 
// EncryptingContent example.
HRESULT ReadEncryptedContent(
                 PWSTR          pwszFileName,
                 PWSTR*         ppwszIL,
                 UINT*          uiEncrypted,
                 BYTE**         ppbEncryptedContent);

// Decrypts an item of content. In this example, the content
// to be decrypted is defined by the byte array Encrypted []
// defined in the header file. This value is the encrypted form
// of the PLAINTEXT constant value that is also defined in this
// header file.
HRESULT DecryptContent(
                 DRMHANDLE      hBoundLic,
                 UINT           uiEncrypted,
                 BYTE*          pbEncrypted,
                 BYTE**         ppbDecrypted);

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

[Decrypting Content Code Example](decrypting-content-code-example.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> </dl>

 

 



