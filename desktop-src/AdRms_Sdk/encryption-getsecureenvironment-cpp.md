---
Description: The following example shows how to create a secure environment. The environment handle is used in the Encryption\_GetOfflineSignedIL.cpp file to retrieve a signed issuance license offline.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 19d0aba8-9329-4e5c-a68f-dbcf93762d7d
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Encryption\_GetSecureEnvironment.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Encryption\_GetSecureEnvironment.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows how to create a secure environment. The environment handle is used in the [Encryption\_GetOfflineSignedIL.cpp](encryption-getofflinesignedil-cpp.md) file to retrieve a signed issuance license offline.


```C++
#include "EncryptingContent.h"

/*===================================================================
File:      Encryption_GetSecureEnvironment.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetSecureEnvironment function retrieves a handle to a secure
// environment lockbox.
//
HRESULT GetSecureEnvironment(
          PWSTR          pwszMachineCert,
          PWSTR          pwszManifest,
          DRMENVHANDLE*  phEnv,
          DRMHANDLE*     phLib)
{
  HRESULT       hr = S_OK;                // Return code
  UINT          uiSecProvTypeLgth = 0;    // Provider type length
  UINT          uiSecProvPathLgth = 0;    // Provider path length
  PWSTR         pwszSecProvType   = NULL; // Secure provider type
  PWSTR         pwszSecProvPath   = NULL; // Path to the provider

  wprintf(L"\r\nEntering GetSecureEnvironment.\r\n");

  // Call DRMGetSecurityProvider once to retrieve the number of
  // characters, including the null terminator, needed to allocate
  // memory for the provider type and path strings.
  hr = DRMGetSecurityProvider( 
            0,                      // Reserved
            &amp;uiSecProvTypeLgth,     // Length of the type string
            NULL,                   // Type string - NULL on input
            &amp;uiSecProvPathLgth,     // Length of the path string
            NULL);                  // Path string - NULL on input
  if(FAILED(hr)) return hr;

  // Allocate memory for the type and path strings.
  pwszSecProvType = new WCHAR[uiSecProvTypeLgth];
  pwszSecProvPath = new WCHAR[uiSecProvPathLgth];
  if(NULL==pwszSecProvType || NULL == pwszSecProvPath)
  {
    hr = E_OUTOFMEMORY;
    return hr;
  }

  // Call DRMGetSecurityProvider again to retrieve the secure
  // provider type and path information.
  hr = DRMGetSecurityProvider( 
            0,                      // Reserved
            &amp;uiSecProvTypeLgth,     // Length of the type string
            pwszSecProvType,        // Return type string
            &amp;uiSecProvPathLgth,     // Length of the path string
            pwszSecProvPath );      // Path string
  if(FAILED(hr))goto e_Exit;
  wprintf(L"DRMGetSecurityProvider succeeded.\r\n");
  wprintf(L"pwszSecProvType = %s\r\n", pwszSecProvType);
  wprintf(L"pwszSecProvPath = %s\r\n", pwszSecProvPath);

  // Initialize a secure environment. This requires a lockbox,
  // a signed manifest, and the machine certificate associated
  // with the user.
  hr = DRMInitEnvironment( 
          DRMSECURITYPROVIDERTYPE_SOFTWARESECREP, 
          DRMSPECTYPE_FILENAME,       // Provider is in a file
          pwszSecProvPath,            // Path to the lockbox
          pwszManifest,               // Application manifest
          pwszMachineCert,            // Machine certificate
          phEnv,                      // Return environment handle
          phLib);                     // Return library
  if(FAILED(hr))goto e_Exit;
  wprintf(L"DRMInitEnvironment succeeded.\r\n");
  wprintf(L"Attach a debugger now if desired.\r\n");
  wprintf(L"Then enter any key to continue...");
  _getch();

e_Exit:
  if (NULL != pwszSecProvType)
  {
    delete [] pwszSecProvType;
    pwszSecProvType = NULL;
  }
  if (NULL != pwszSecProvPath)
  {
    delete [] pwszSecProvPath;
    pwszSecProvPath = NULL;
  }

  wprintf(L"Leaving GetSecureEnvironment: hr = %x\r\n", hr);
  return hr;
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

 

 



