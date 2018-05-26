---
Description: The following code example retrieves a revocation list for an end-user license. The example first tries to retrieve the list from the certificate store. If that fails, the function calls DRMAcquireAdvisories and tries to enumerate the store again.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1c88925c-acf7-4ec1-9207-3a662a1c5d2c
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation\_GetRevocationList.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Revocation\_GetRevocationList.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example retrieves a revocation list for an end-user license. The example first tries to retrieve the list from the certificate store. If that fails, the function calls [**DRMAcquireAdvisories**](/windows/previous-versions/Msdrm/nf-msdrm-drmacquireadvisories?branch=master) and tries to enumerate the store again.


```C++
#include "RevocationList.h"

/*===================================================================
File:      Revocation_GetRevocationList.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetRevocationList function retrieves a revocation list for  
// the specified license.
//
HRESULT GetRevocationList(
            DRMHSESSION hLicenseStorage,
            PWSTR pwszLicense,
            PWSTR* ppwszRevokeList)
{
  HRESULT       hr               = S_OK;   // Return type
  const DWORD   DW_WAIT_TIME     = 60000;  // Maximum signal duration
  DWORD         dwWaitResult     = 0;      // Actual signal duration
  DRM_CONTEXT   context;                   // Callback context

  hr = GetCertificate(
          hLicenseStorage,            // License storage session
          DRM_EL_REVOCATIONLIST,      // Certificate type
          ppwszRevokeList);           // Revocation list
  if(FAILED(hr))
  {
    // Initialize the callback context.
    SecureZeroMemory(&amp;context, sizeof(context));

    // Create an event to signal when the license has been acquired.
    context.hEvent = CreateEvent(
          NULL,                       // No attributes
          FALSE,                      // Automatic reset
          FALSE,                      // Initial state not signaled
          NULL);                      // Event object not named
    if(NULL == context.hEvent) return E_FAIL;

    // Call DRMAcquireAdvisories to retrieve the revocation list(s)
    // required by the license.
    hr = DRMAcquireAdvisories(
          hLicenseStorage,            // License storage session
          pwszLicense,                // Input license
          NULL,                       // Not used
          (void*)&amp;context);           // Callback context
    if(FAILED(hr)) return hr;

    // Wait for the callback to return.
    dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
    if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) return hr;

    // Try to enumerate the revocation list again.
    // Note:
    //   This example assumes that there is only one revocation
    //   list in the store. If others exist, you should increment 
    //   the index of the DRMEnumerateLicense function until you
    //   find the list you want or receive an E_DRM_NO_MORE_DATA
    //   HRESULT return code.
    hr = GetCertificate(
          hLicenseStorage,            // License storage session
          DRM_EL_REVOCATIONLIST,      // Certificate type
          ppwszRevokeList);           // Revocation list
  }

  return hr;
}
```



## Related topics

<dl> <dt>

[Revocation Code Example](revocation-code-example.md)
</dt> <dt>

[Revoking a Certificate](revoking-a-certificate.md)
</dt> </dl>

 

 



