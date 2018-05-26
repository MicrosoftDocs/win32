---
Description: The following example code shows how to retrieve a certificate from the local certificate store. To sign an issuance license offline, you must retrieve the machine and client licensor certificates.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 14fc4d05-83df-4693-8d72-21fc24c6b81e
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OfflineSigning\_GetCertificate.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OfflineSigning\_GetCertificate.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example code shows how to retrieve a certificate from the local certificate store. To sign an issuance license offline, you must retrieve the machine and client licensor certificates.


```C++
#include "OfflineILSigning.h"

/*===================================================================
File:      OfflineSigning_GetCertificate.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetCertificate function retrieves a UNICODE string that
// contains the requested certificate from the local store.
//
HRESULT GetCertificate(DRMHSESSION hSession, 
                       UINT uFlags, 
                       PWSTR *ppwszCertificate)
{
  HRESULT   hr              = S_OK;     // HRESULT return code
  BOOL      fShared         = false;    // Certificate sharing
  UINT      uiCertLength    = 0;        // Length, in characters

  wprintf(L"\r\nEntering GetCertificate.\r\n");

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

  // Allocate memory for the certificate. The caller must delete.
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

  wprintf(L"Leaving GetCertificate: hr = %x \r\n", hr);
  return hr;
}
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> </dl>

 

 



