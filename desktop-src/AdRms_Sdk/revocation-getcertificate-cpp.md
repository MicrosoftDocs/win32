---
Description: The following example code shows how to retrieve a certificate from the local certificate store. This example retrieves the machine certificate and the revocation list from the store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b797909e-1c53-4967-958a-04a9aa93b677
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation\_GetCertificate.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revocation\_GetCertificate.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example code shows how to retrieve a certificate from the local certificate store. This example retrieves the machine certificate and the revocation list from the store.


```C++
#include "RevocationList.h"

/*===================================================================
File:      Revocation_GetCertificate.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetCertificate function retrieves a UNICODE string containing
// the requested certificate or license from the local store.
//
HRESULT GetCertificate(DRMHSESSION hSession, 
                       UINT uFlags, 
                       PWSTR *ppwszCertificate)
{
  HRESULT   hr              = S_OK;     // HRESULT return code
  BOOL      fShared         = false;    // Certificate sharing
  UINT      uiCertLength    = 0;        // Length, in characters

  // Call DRMEnumerateLicense once to determine the number of
  // characters, including the terminating null character, in
  // the certificate.
  hr = DRMEnumerateLicense( 
            hSession,               // Session handle.
            uFlags,                 // Certificate or license type.
            0,                      // Start at index zero.
            &amp;fShared,               // Certificate not shared.
            &amp;uiCertLength,          // Return the length.
            NULL);                  // NULL to obtain length.
  if(FAILED(hr)) return hr;

  // Allocate memory for the certificate. Caller must delete.
  *ppwszCertificate = new WCHAR[uiCertLength];
  if(NULL == *ppwszCertificate)
  {
    hr = E_OUTOFMEMORY;
    return hr;
  }

  // Call DRMEnumerateLicense again to retrieve the certificate.
  hr = DRMEnumerateLicense( 
            hSession,               // Session handle.
            uFlags,                 // Certificate or license type.
            0,                      // Start at index zero.
            &amp;fShared,               // Certificate not shared. 
            &amp;uiCertLength,          // Specify the length. 
            *ppwszCertificate );    // Return the certificate.

  return hr;
}
```



## Related topics

<dl> <dt>

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



