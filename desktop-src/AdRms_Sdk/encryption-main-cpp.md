---
Description: The following code example shows the \_tmain function of a console application that encrypts content. In this example, the content to be encrypted is defined in the EncryptingContent.h file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: aa67df48-0716-4646-904a-a2b428749c74
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encryption\_Main.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Encryption\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows the \_tmain function of a console application that encrypts content. In this example, the content to be encrypted is defined in the [EncryptingContent.h](encryptingcontent-h.md) file.


```C++
// Content to encrypt.
#define PLAINTEXT L"This is the content to be encrypted."
```



The Encryption\_Main.cpp function performs the following actions:

-   Creates a client session.
-   Retrieves the machine certificate from the license store.
-   Retrieves the client licensor certificate (used to sign an issuance license offline).
-   Retrieves the rights account certificate for the user specified on the command line.
-   Retrieves the application manifest.
-   Creates a secure environment.
-   Retrieves the signed issuance license.
-   Encrypts the content and writes it to a file.


```C++
#include "EncryptingContent.h"

/*===================================================================
File:      Encryption_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample demonstrates how to use AD RMS to encrypt content.
// You must enter an Active Directory user account and manifest file 
// path on the command line.
//
int _tmain(int argc, _TCHAR* argv[])
{
  HRESULT         hr                = S_OK;   // HRESULT return code
  DRMHSESSION     hClient           = NULL;   // Client handle
  DRMENVHANDLE    hEnv              = NULL;   // Environment handle
  DRMHANDLE       hLib              = NULL;   // Library handle
  DRMPUBHANDLE    hIssuanceLic      = NULL;   // IL handle
  PWSTR           pwszUserID        = NULL;   // User ID
  PWSTR           pwszManFileName   = NULL;   // Manifest file name
  PWSTR           pwszManifest      = NULL;   // Manifest string
  PWSTR           pwszCLC           = NULL;   // Signing certificate
  PWSTR           pwszMachineCert   = NULL;   // Machine certificate
  PWSTR           pwszSignedIL      = NULL;   // Signed license
  PWSTR           pwszGUID          = NULL;   // Content ID GUID
  PWSTR           pwszRAC           = NULL;   // Rights account cert
  BYTE*           pbEncrypted       = NULL;   // Encrypted content
   
  // Validate input. The client must supply a user ID and the 
  // name of the application  manifest file.
  if(NULL==argv[1] || NULL==argv[2]) return hr;
  pwszUserID = argv[1];
  pwszManFileName = argv[2];

  // Create a client session.
  hr = DRMCreateClientSession( 
          &amp;StatusCallback,                    // Callback function
          0,                                  // Reserved
          DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH, // Authentication type
          pwszUserID,                         // User ID
          &amp;hClient );                         // Client handle
  if (FAILED(hr)) return hr;
  wprintf(L"DRMCreateClientSession: hClient = %i \r\n", hClient);

  // Retrieve the machine certificate for the user. This call fails
  // if the computer and the user have not been activated.
  hr = GetCertificate(
          hClient,                            // Client handle
          DRM_EL_MACHINE,                     // Certificate type
          &amp;pwszMachineCert);                  // Machine certificate
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszMachineCert) succeeded.\r\n");

  // Retrieve the client licensor certificate (CLC) from the license
  // store.
  hr = GetCertificate(
          hClient,                            // Client handle
          DRM_EL_SPECIFIED_CLIENTLICENSOR,    // Certificate type
          &amp;pwszCLC);                          // Signing certificate
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszCLC) succeeded.\r\n");

  // Retrieve the rights account certificate (RAC) from the license
  // store.
  hr = GetCertificate(
          hClient,                            // Client handle
          DRM_EL_SPECIFIED_GROUPIDENTITY,     // Certificate type
          &amp;pwszRAC);                          // RAC string
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszRAC) succeeded.\r\n");

  // Read the manifest file into a string.
  hr = GetManifest(
          pwszManFileName,                    // File name 
          &amp;pwszManifest);                     // Application manifest
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetManifest (pwszManifest) succeeded.\r\n");

  // Create a secure environment.
  hr = GetSecureEnvironment(
          pwszMachineCert,                    // Machine certificate
          pwszManifest,                       // Application manifest
          &amp;hEnv,                              // Environment handle
          &amp;hLib);                             // Library handle
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetSecureEnvironment (hEnv and hLib) succeeded.\r\n");


  // Create and sign an issuance license (IL) offline.
  hr = GetOfflineSignedIL(
          hEnv,                               // Environment handle
          hLib,                               // Library handle
          pwszUserID,                         // User account
          pwszMachineCert,                    // Machine certificate
          pwszCLC,                            // CLC string
          pwszManifest,                       // Application manifest
          &amp;pwszGUID,                          // GUID
          &amp;hIssuanceLic,                      // IL handle
          &amp;pwszSignedIL);                     // Signed IL
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetOfflineSignedIL (pwszSignedIL) succeeded.\r\n");


  // Encrypt the content. In this example, the content to be
  // encrypted is in the header file, and the encrypted content
  // is written to a new file.
  hr = EncryptContent(
          hEnv,                               // Environment handle
          hLib,                               // Library handle
          pwszRAC,                            // Rights account cert
          pwszGUID,                           // Content ID from IL
          hIssuanceLic,                       // IL handle
          pwszSignedIL,                       // Signed IL
          &amp;pbEncrypted);                      // Encrypted content
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"EncryptContent (pbEncrypted) succeeded.\r\n");

e_Exit:

  if(NULL != pbEncrypted)
  {
    SecureZeroMemory(pbEncrypted, sizeof(pbEncrypted));
    pbEncrypted = NULL;
  }
  if(NULL != pwszMachineCert)
  {
    delete [] pwszMachineCert;
    pwszMachineCert = NULL;
  }
  if (NULL != pwszCLC)
  {
    delete [] pwszCLC;
    pwszCLC = NULL;
  }
  if (NULL != pwszRAC)
  {
    delete [] pwszRAC;
    pwszRAC = NULL;
  }
  if (NULL != pwszManifest)
  {
    delete [] pwszManifest;
    pwszManifest = NULL;
  }
  if(NULL != pwszSignedIL)
  {
    delete [] pwszSignedIL;
    pwszSignedIL = NULL;
  }
  if(NULL != pwszGUID)
  {
    delete [] pwszGUID;
    pwszGUID = NULL;
  }
  if(NULL != hIssuanceLic)
  {
    hr = DRMClosePubHandle(hIssuanceLic);
    hIssuanceLic = NULL;
  }
  if(NULL != hClient)
  {
    DRMCloseSession(hClient);
    hClient = NULL;
  }
  if(NULL != hLib)
  {
    hr = DRMCloseHandle(hLib);
    hLib = NULL;
  }
  if(NULL != hEnv)
  {
    hr = DRMCloseEnvironmentHandle(hEnv);
    hEnv = NULL;
  }

  return 0;
}
```



## Related topics

<dl> <dt>

[Decrypting Content](decrypting-content.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> <dt>

[Encrypting Content Code Example](encrypting-content-code-example.md)
</dt> </dl>

 

 



