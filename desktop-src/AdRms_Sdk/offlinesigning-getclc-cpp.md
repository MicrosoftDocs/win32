---
Description: If the client licensor certificate has not already been downloaded into the local store, you must retrieve it from the licensing service on an Active Directory Rights Management (AD RMS) server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6f4b4d1f-3a73-4576-9308-afefd90a3599
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OfflineSigning\_GetCLC.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OfflineSigning\_GetCLC.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

If the client licensor certificate has not already been downloaded into the local store, you must retrieve it from the licensing service on an Active Directory Rights Management (AD RMS) server. The following example shows how to:

-   Retrieve the service URL. This has the form http(s)://*ServerName*/\_wmcs/licensing where *ServerName* identifies the AD RMS server.
-   Call [**DRMAcquireLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmacquirelicense) to download the client licensor certificate.
-   Retrieve the downloaded certificate from the store.


```C++
#include "OfflineILSigning.h"

/*===================================================================
File:      OfflineSigning_GetCLC.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetCLCFromSvc function retrieves a client licensor certificate
// (CLC) from an AD RMS licensing service in the enterprise.
//
HRESULT GetCLCFromSvc(DRMHSESSION hClient,
                      PWSTR* ppwszCLC)
{
  HRESULT       hr              = E_FAIL; // HRESULT return code
  UINT          uiURLLength     = 0;      // Licensing URL length
  BOOL          fShared         = false;  // Certificate sharing
  const DWORD   DW_WAIT_TIME    = 60000;  // Maximum wait for signal
  DWORD         dwWaitResult    = 0;      // Actual signal duration
  PWSTR         pwszServiceURL  = NULL;   // Licensing service URL
  DRM_CONTEXT   context;                  // Callback context

  wprintf(L"\r\nEntering GetCLCFromSvc.\r\n");

  // Initialize the callback context.
  SecureZeroMemory(&amp;context, sizeof(context));

  // Use service discovery to find the URL of the licensing service
  // that can issue a client licensor certificate.
  hr = GetServiceURL(
          hClient,                          // Client handle
          DRM_SERVICE_TYPE_CLIENTLICENSOR,  // Type of service
          DRM_SERVICE_LOCATION_ENTERPRISE,  // Location of service
          &amp;pwszServiceURL);                 // Service URL
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetServiceURL: pwszServiceURL = %s \r\n", pwszServiceURL);

  // Create an event to signal when the license has been created.
  context.hEvent = CreateEvent(
          NULL,                       // No attributes
          FALSE,                      // Automatic reset
          FALSE,                      // Initial state not signaled
          NULL);                      // Event object not named
  if(NULL == context.hEvent) goto e_Exit;

  // Create the client licensor certificate.
  hr = DRMAcquireLicense( 
          hClient,                    // Client handle
          0,                          // Flags
          NULL,                       // Rights account certificate
          NULL,                       // Reserved
          NULL,                       // Application specific data
          pwszServiceURL,             // Licensing URL
          (void*)&amp;context);           // Callback context
  if (FAILED(hr)) goto e_Exit;

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
  if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) goto e_Exit;

  // Set any error returned by the callback function.
  if (FAILED(context.hr))
  {
    hr = context.hr;
    goto e_Exit;
  }

  // Retrieve the client licensor certificate from the store.
  hr = GetCertificate(
          hClient,                            // Client handle
          DRM_EL_SPECIFIED_CLIENTLICENSOR,    // Certificate type
          ppwszCLC);                          // Signing certificate

e_Exit:
  if (NULL != context.hEvent)
  {
    CloseHandle(context.hEvent);
    context.hEvent = NULL;
  }
  if (NULL != pwszServiceURL)
  {
    delete [] pwszServiceURL;
    pwszServiceURL = NULL;
  }

  wprintf(L"Leaving GetCLCFromSvc: hr = %x\r\n", hr);
  return hr;
}
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Offline Signing Code Example](offline-signing-code-example.md)
</dt> </dl>

 

 



