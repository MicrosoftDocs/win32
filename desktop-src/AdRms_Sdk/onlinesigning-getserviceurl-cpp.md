---
Description: The following code example shows how to use the DRMGetServiceLocation function to retrieve the URL of the Active Directory Rights Management Services (AD RMS) certification service in the enterprise or on the Internet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 69cc6ad7-cd5d-445c-9150-a7fcf5562afa
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineSigning\_GetServiceURL.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnlineSigning\_GetServiceURL.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows how to use the [**DRMGetServiceLocation**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetservicelocation?branch=master) function to retrieve the URL of the Active Directory Rights Management Services (AD RMS) certification service in the enterprise or on the Internet. The URL has the form http(s)://*ServerName*/\_wmcs/licensing where *ServerName* identifies the AD RMS server.


```C++
#include "OnlineILSigning.h"

/*===================================================================
File:      OnlineSigning_GetServiceURL.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// The GetServiceURL function uses service discovery to find the URL 
// of a licensing service that can issue a license or certificate.
//
HRESULT GetServiceURL(DRMHSESSION hClient,
                      UINT uiServiceType,
                      UINT uiServiceLocation,
                      PWSTR *ppwszServiceURL)
{
  HRESULT   hr        = S_OK;         // Return value
  UINT      uiURLLgth = 0;            // URL length, characters

  // Call DRMGetServiceLocation once to verify that a 
  // service exists and to retrieve the length of the URL.
  hr = DRMGetServiceLocation( 
          hClient,                    // Client session handle
          uiServiceType,              // Type of service  
          uiServiceLocation,          // Enterprise or Internet
          NULL,                       // Issuance license
          &amp;uiURLLgth,                 // Character length of URL
          NULL);                      // NULL on first call
  if (FAILED(hr)) return hr;

  // Allocate memory for the URL.
  *ppwszServiceURL = new WCHAR[uiURLLgth];
  if (NULL == *ppwszServiceURL)
  {
    hr = E_OUTOFMEMORY;
    return hr;
  }

  // Call DRMGetServiceLocation again to retrieve the URL.
  hr = DRMGetServiceLocation( 
          hClient,                    // Client session handle
          uiServiceType,              // Type of service
          uiServiceLocation,          // Enterprise or Internet
          NULL,                       // Issuance license
          &amp;uiURLLgth,                 // Character length of URL
          *ppwszServiceURL);          // Service URL
 
  return hr;
}
```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



