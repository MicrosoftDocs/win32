---
Description: The following code example retrieves an end-user license chain from the certificate store. The example calls DRMAcquireLicense and then enumerates the store to retrieve the chain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: aeaf04c8-49a8-4531-9b28-ba10eb42a7f7
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Revocation\_GetEULChain.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revocation\_GetEULChain.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example retrieves an end-user license chain from the certificate store. The example calls [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) and then enumerates the store to retrieve the chain.


```C++
#include "RevocationList.h"

/*===================================================================
File:      Revocation_GetEULChain.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetEULChain function retrieves an end user license chain.
//
HRESULT GetEULChain (
          DRMHSESSION       hLicenseStorage,
          DRMENVHANDLE      hEnv,
          DRMHANDLE         hLib,
          PWSTR             pwszSignedIL,
          PWSTR*            ppwszEULChain)
{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //   hr........................Return value
  //   DW_WAIT_TIME..............Maximum time to wait for signal
  //   dwWaitResult..............Actual time of wait for signal
  //   context...................Callback context
  HRESULT       hr               = S_OK;
  const DWORD   DW_WAIT_TIME     = 60000;
  DWORD         dwWaitResult     = 0;
  DRM_CONTEXT   context;

  // Initialize the callback context.
  SecureZeroMemory(&amp;context, sizeof(context));

  // Create an event to signal when the license has been acquired.
  context.hEvent = CreateEvent(
          NULL,                       // No attributes
          FALSE,                      // Automatic reset
          FALSE,                      // Initial state not signaled
          NULL);                      // Event object not named
  if(NULL == context.hEvent) goto e_Exit;

  // Call DRMAcquireLicense, which will put the end-user license 
  // chain into the permanent license store for you by default, or
  // specify DRM_AL_NOPERSIST if you want to put the license into 
  // the temporary store and handle storage and management yourself. 
  hr = DRMAcquireLicense( 
          hLicenseStorage,            // Storage session handle
          0,                          // No flags set
          NULL,                       // No RAC specified
          NULL,                       // Reserved
          NULL,                       // Custom data
          NULL,                       // Optional license URL
          (VOID*)&amp;context);           // Callback context
  if(FAILED(hr)) goto e_Exit;

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
  if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) goto e_Exit;

  // Enumerate the end user license chain from the license store.
  // Note:  This example assumes that there is only one EUL in the 
  //        license  store. If others exist, you should increment 
  //        the index of the DRMEnumerateLicense function until you
  //        find the license you want or receive an 
  //        E_DRM_NO_MORE_DATA HRESULT return code.
  hr = GetCertificate(
          hLicenseStorage,            // Client handle
          DRM_EL_EUL,                 // Certificate type
          ppwszEULChain);             // EUL chain

e_Exit:

  if (NULL != hLicenseStorage)
  {
    hr = DRMCloseSession(hLicenseStorage);
    hLicenseStorage = NULL;
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

 

 



