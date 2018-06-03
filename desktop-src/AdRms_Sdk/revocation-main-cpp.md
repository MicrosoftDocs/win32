---
Description: The following code example shows the \_tmain function of a console application that retrieves and registers a revocation list.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0e9cc35d-13a6-427d-bf0e-9fb798b0ee19
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation\_Main.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revocation\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows the \_tmain function of a console application that retrieves and registers a revocation list. The function performs the following actions:

-   Creates a client session.
-   Retrieves the machine certificate from the license store.
-   Retrieves the application manifest.
-   Creates a secure environment.
-   Retrieves a signed issuance license from a custom file.
-   Creates a license storage session.
-   Retrieves the end-user license chain.
-   Retrieves the revocation list from the chain.


```C++
#include "RevocationList.h"

/*===================================================================
File:      Revocation_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample demonstrates how to retrieve and register a revocation
// list associated with an end user license.
//
int _tmain(int argc, _TCHAR* argv[])
{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //    hr.................HRESULT return value
  //    hClient............Handle to the client session
  //    hLicenseStorage....Handle to the license storage session
  //    hEnv...............Handle to the lockbox
  //    hLib...............Handle to the library
  //    pwszUserID.........User account (email address)
  //    pwszEncryptFile....File that contains the issuance license
  //    pwszManifestFile...File that contains the manifest
  //    pwszMachineCert....Computer certificate
  //    pwszSignedIL.......Signed issuance license
  //    pwszEULChain.......End user license chain
  //    pwszRevokeList.....Revocation list string
  //    pbEncrypted........Encrypted content byte array

  HRESULT         hr                = S_OK;
  DRMHSESSION     hClient           = NULL;
  DRMHSESSION     hLicenseStorage   = NULL;
  DRMENVHANDLE    hEnv              = NULL;
  DRMHANDLE       hLib              = NULL;
  PWSTR           pwszUserID        = NULL;
  PWSTR           pwszEncryptFile   = NULL;
  PWSTR           pwszManifestFile  = NULL;
  PWSTR           pwszManifest      = NULL;
  PWSTR           pwszMachineCert   = NULL;
  PWSTR           pwszSignedIL      = NULL;
  PWSTR           pwszEULChain      = NULL;
  PWSTR           pwszRevokeList    = NULL;
  BYTE*           pbEncrypted       = NULL;

  // Validate input. The client must supply a user account ID, the
  // path of a file that contains the application manifest, and the
  // path of a file that contains the encrypted content and the 
  // issuance license used to publish and encrypt that content.
  // In this example, the file that contains the encrypted content
  // has a custom format and is created by the EncryptingContent
  // example.
  if(argc<4 || NULL==argv[1] || NULL==argv[2] || NULL== argv[3])
  {
    return E_FAIL;
  }
  pwszUserID = argv[1];
  pwszEncryptFile = argv[2];
  pwszManifestFile = argv[3];

  // Create a client session.
  hr = DRMCreateClientSession( 
          &amp;StatusCallback,                    // Callback function
          0,                                  // Reserved
          DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH, // Authentication type
          pwszUserID,                         // User ID
          &amp;hClient );                         // Client handle
  if (FAILED(hr)) return hr;

  // Retrieve the machine certificate for the user. The machine
  // certificate is used to create a secure environment. This call 
  // fails if the computer and the user have not been activated.
  hr = GetCertificate(
          hClient,                    // Client handle
          DRM_EL_MACHINE,             // Certificate type
          &amp;pwszMachineCert);          // Machine certificate
  if (FAILED(hr)) goto e_Exit;

  // Read the manifest file into a string. The manifest is used to
  // create a secure environment.
  hr = GetManifest(
          pwszManifestFile,           // File name 
          &amp;pwszManifest);             // Application manifest
  if (FAILED(hr)) goto e_Exit;

  // Create a secure environment.
  hr = GetSecureEnvironment(
          pwszMachineCert,            // Machine certificate
          pwszManifest,               // Application manifest
          &amp;hEnv,                      // Environment handle
          &amp;hLib);                     // Library handle
  if (FAILED(hr)) goto e_Exit;

  // Retrieve the signed issuance license and the previously 
  // encrypted content from the file specified on the command line.
  // The signed issuance license is used to retrieve an end user 
  // license, and the encrypted content will be decrypted by the
  // DecryptContent function later in this example.
  hr = ReadEncryptedContent(
          pwszManifestFile,           // File name
          &amp;pwszSignedIL,              // Issuance license
          &amp;pbEncrypted);              // Encrypted content
  if (FAILED(hr)) goto e_Exit;

  // Create a license storage session.
  hr = DRMCreateLicenseStorageSession( 
          hEnv,                       // Environment handle
          hLib,                       // Library handle
          hClient,                    // Client session handle
          0,                          // Reserved
          pwszSignedIL,               // Signed issuance license
          &amp;hLicenseStorage );         // License storage handle
  if(FAILED(hr)) goto e_Exit;

  // Retrieve the end user license chain.
  hr = GetEULChain(
          hLicenseStorage,
          hEnv,
          hLib,
          pwszSignedIL,
          &amp;pwszEULChain);
  if(FAILED(hr)) goto e_Exit;

  // Retrieve the revocation list.
  hr = GetRevocationList(
          hLicenseStorage,
          pwszEULChain,
          &amp;pwszRevokeList);
  if(FAILED(hr)) goto e_Exit;

  // Register the revocation list.
  hr = DRMRegisterRevocationList(
          hEnv, 
          pwszRevokeList);

  // Print to the console.
  wprintf(L"Revocation list: \r\n");
  wprintf(L"%s\r\n", pwszRevokeList);
  wprintf(L"Enter any key to continue...");
  _getch();

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
  if(NULL != pwszEULChain)
  {
    delete [] pwszEULChain;
    pwszEULChain = NULL;
  }
  if(NULL != pwszRevokeList)
  {
    delete [] pwszRevokeList;
    pwszRevokeList = NULL;
  }
  if(NULL != hLicenseStorage)
  {
    DRMCloseSession(hLicenseStorage);
    hLicenseStorage = NULL;
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

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



