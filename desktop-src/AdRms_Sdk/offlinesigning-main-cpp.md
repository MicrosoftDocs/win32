---
Description: The following code example shows the \_tmain function of a console application that creates an issuance license and signs it offline by using the client licensor certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 028c1ced-aefa-42d7-9adb-1d0150902509
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OfflineSigning\_Main.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OfflineSigning\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows the \_tmain function of a console application that creates an issuance license and signs it offline by using the client licensor certificate. The function performs the following actions:

-   Creates a client session.
-   Retrieves the machine certificate.
-   Retrieves the client licensor certificate.
-   Retrieves the application manifest.
-   Creates and signs the issuance license.


```C++
#include "OfflineILSigning.h"

/*===================================================================
File:      OfflineSigning_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample demonstrates how to sign an issuance license offline. 
// It acquires the appropriate licenses and certificates,  
// initializes a secure environment, and signs the publishing  
// license offline. 
//
int _tmain(int argc, _TCHAR* argv[])
{
  HRESULT         hr                = S_OK;   // HRESULT return code
  DRMHSESSION     hClient           = NULL;   // Client handle
  PWSTR           pwszUserID        = NULL;   // User ID
  PWSTR           pwszManFileName   = NULL;   // Manifest file name
  PWSTR           pwszManifest      = NULL;   // Manifest string
  PWSTR           pwszCLC           = NULL;   // Signing certificate
  PWSTR           pwszMachineCert   = NULL;   // Machine certificate
  PWSTR           pwszSignedIL      = NULL;   // Signed license
   
  // Validate input. The client must supply a user ID and the 
  // name of the application  manifest file.
  if(argc>3 || NULL==argv[1] || NULL==argv[2]) return E_INVALIDARG;
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
  wprintf(L"GetCertificate (pwszMachineCert) succeeded. \r\n");

  // Retrieve the client licensor certificate. Try to retrieve it
  // first from the license store. If the attempt is not successful,
  // try to retrieve from an AD RMS licensing service.
  hr = GetCertificate(
          hClient,                            // Client handle
          DRM_EL_SPECIFIED_CLIENTLICENSOR,    // Certificate type
          &amp;pwszCLC);                          // Signing certificate
  if (FAILED(hr))
  {
    hr = GetCLCFromSvc(
          hClient,                            // Client handle
          &amp;pwszCLC);                          // Signing certificate
    if (FAILED(hr)) goto e_Exit;
  }
  wprintf(L"GetCertificate (pwszCLC) succeeded. \r\n");


  // Read the manifest file into a string.
  hr = GetManifest(
          pwszManFileName,                    // File name 
          &amp;pwszManifest);                     // Application manifest
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetCertificate (pwszManifest) succeeded. \r\n");

  // Create an issuance license and sign it.
  hr = GetOfflineSignedIL(
          pwszUserID,                         // User ID
          pwszMachineCert,                    // Machine certificate
          pwszCLC,                            // Signing certificate
          pwszManifest,                       // Application manifest
          &amp;pwszSignedIL);                     // Signed license

  // Print the issuance license to the console. The license is not
  // saved in a store on the local computer. Instead, you typically
  // package the license with the protected content. It is up
  // to the application that consumes the content to know where
  // the license is, retrieve it, and use it to create and bind
  // to an end-user license that can be used to decrypt the
  // protected content.

  wprintf(L"\nThe issuance license is: \n\n%s\n", pwszSignedIL);
  wprintf(L"Enter any key to continue...");
  _getch();

e_Exit:

  // Close the handles created by this function.
  // Delete memory created for use only by this function.
  if (NULL != hClient)
  {
    DRMCloseSession(hClient);
    hClient = NULL;
  }
  if (NULL != pwszManifest)
  {
    delete [] pwszManifest;
    pwszManifest = NULL;
  }
  if (NULL != pwszCLC)
  {
    delete [] pwszCLC;
    pwszCLC = NULL;
  }
  if (NULL != pwszMachineCert)
  {
    delete [] pwszMachineCert;
    pwszMachineCert = NULL;
  }
  if (NULL != pwszSignedIL)
  {
    delete [] pwszSignedIL;
    pwszSignedIL = NULL;
  }
  pwszUserID = NULL;
  pwszManFileName = NULL;

  return hr;
}
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> </dl>

 

 



