---
Description: The following code example shows the \_tmain function of a console application that decrypts content.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ac0b9a94-f946-46ce-a2a1-96b4b7ba5a52
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Decryption\_Main.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Decryption\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows the \_tmain function of a console application that decrypts content. The encrypted content is created by the [Encrypting Content Code Example](encrypting-content-code-example.md) and saved in a custom file. You must specify the name of the file on the command line. The \_tmain function performs the following actions:

-   Creates a client session.
-   Retrieves the machine certificate for the user specified on the command line.
-   Retrieves the application manifest from the file specified on the command line.
-   Creates a secure environment.
-   Retrieves the signed issuance license and encrypted content from the file specified on the command line.
-   Retrieves the rights account certificate (RAC) for the user.
-   Retrieves an end-user license.
-   Decrypts the content.


```C++
#include "DecryptingContent.h"

/*===================================================================
File:      Decryption_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample demonstrates how to use the AD RMS SDK to decrypt 
// previously encrypted content. The content is encrypted to a file 
// by using the EncryptingContent example shown previously in this 
// documentation. The name of the file that includes the encrypted
// content must be specified on the command line.
//
int _tmain(int argc, _TCHAR* argv[])
{
  HRESULT         hr                = S_OK;   // HRESULT return code
  DRMHSESSION     hClient           = NULL;   // Client handle
  DRMENVHANDLE    hEnv              = NULL;   // Environment handle
  DRMHANDLE       hLib              = NULL;   // Library handle
  DRMHANDLE       hBoundLic         = NULL;   // Bound license handle
  PWSTR           pwszUserID        = NULL;   // User ID
  PWSTR           pwszEncryptedFile = NULL;   // Encrypted file
  PWSTR           pwszManifestFile  = NULL;   // Manifest file name
  PWSTR           pwszManifest      = NULL;   // Manifest string
  PWSTR           pwszSignedIL      = NULL;   // Signed IL
  PWSTR           pwszContentID     = NULL;   // Content ID
  PWSTR           pwszMachineCert   = NULL;   // Machine certificate
  PWSTR           pwszRAC           = NULL;   // Rights account cert
  BYTE*           pbEncrypted       = NULL;   // Encrypted content
  BYTE*           pbDecrypted       = NULL;   // Decrypted content
  UINT            uiEncrypted       = 0;      // Encrypted byte count

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
  pwszEncryptedFile = argv[2];
  pwszManifestFile = argv[3];

  // Create a client session.
  hr = DRMCreateClientSession( 
          &amp;StatusCallback,                    // Callback function
          0,                                  // Reserved
          DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH, // Authentication type
          pwszUserID,                         // User ID
          &amp;hClient );                         // Client handle
  if (FAILED(hr)) return hr;
  wprintf(L"DRMCreateClientSession: hClient = %i\r\n", hClient);

  // Retrieve the machine certificate for the user. The machine
  // certificate is used to create a secure environment. This call 
  // fails if the computer and the user have not been activated.
  hr = GetCertificate(
          hClient,                    // Client handle
          DRM_EL_MACHINE,             // Certificate type
          &amp;pwszMachineCert);          // Machine certificate
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszMachineCert) succeeded.\r\n");

  // Read the manifest file into a string. The manifest is used to
  // create a secure environment.
  hr = GetManifest(
          pwszManifestFile,           // File name 
          &amp;pwszManifest);             // Application manifest
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetManifest (pwszManifest) succeeded.\r\n");

  // Create a secure environment.
  hr = GetSecureEnvironment(
          pwszMachineCert,            // Machine certificate
          pwszManifest,               // Application manifest
          &amp;hEnv,                      // Environment handle
          &amp;hLib);                     // Library handle
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetSecureEnvironment succeeded.\r\n");

  // Retrieve the signed issuance license and the previously 
  // encrypted content from the file specified on the command line.
  // The signed issuance license is used to retrieve an end user 
  // license, and the encrypted content will be decrypted by the
  // DecryptContent function later in this example.
  hr = ReadEncryptedContent(
          pwszEncryptedFile,          // File name
          &amp;pwszSignedIL,              // Issuance license
          &amp;uiEncrypted,               // Number of encrypted bytes
          &amp;pbEncrypted);              // Encrypted content
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"ReadEncryptedContent succeeded.\r\n");

  // Retrieve the rights account certificate (RAC) from the license
  // store. The RAC is used to retrieve a bound license.
  hr = GetCertificate(
          hClient,                            // Client handle
          DRM_EL_SPECIFIED_GROUPIDENTITY,     // Certificate type
          &amp;pwszRAC);                          // RAC string
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszRAC) succeeded.\r\n");

  // Retrieve the end user license and use it to create a license
  // that is bound to the EDIT right.
  hr = GetBoundLicense(
          hClient,                    // Client handle
          hEnv,                       // Secure environment
          hLib,                       // Library handle
          pwszRAC,                    // Rights account certificate
          pwszSignedIL,               // Signed issuance license
          &amp;hBoundLic);                // Bound license
  wprintf(L"GetBoundLicense: hBoundLic = %i\r\n", hBoundLic);

  // Decrypt the content.
  hr = DecryptContent(
          hBoundLic,                  // Bound license handle
          uiEncrypted,                // Number of encrypted bytes
          pbEncrypted,                // Encrypted content byte array
          &amp;pbDecrypted);              // Decrypted content byte array
  if (FAILED(hr)) goto e_Exit;

  // Print the decrypted content to the console.
  wprintf(L"DecryptContent succeeded.\r\n\n");
  wprintf(L"Decrypted content = %s \r\n", pbDecrypted);


e_Exit:
  if (NULL != hClient)
  {
    hr = DRMCloseSession(hClient);
    hClient = NULL;
 }
  if (NULL != pwszUserID)
  {
    pwszUserID = NULL;
  }
  if (NULL != pwszEncryptedFile)
  {
    pwszEncryptedFile = NULL;
  }
  if (NULL != pwszManifestFile)
  {
    pwszManifestFile = NULL;
  }
  if (NULL != pwszRAC)
  {
    delete [] pwszRAC;
    pwszRAC = NULL;
  }
  if (NULL != hBoundLic)
  {
    hBoundLic = NULL;
  }
  if (NULL != pbDecrypted)
  {
    delete [] pbDecrypted;
    pbDecrypted = NULL;
  }
  if (NULL != hLib)
  {
    hr = DRMCloseHandle(hLib);
    hLib = NULL;
 }
  if (NULL != hEnv)
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

[Decrypting Content Code Example](decrypting-content-code-example.md)
</dt> <dt>

[Encrypting Content](encrypting-content.md)
</dt> </dl>

 

 



