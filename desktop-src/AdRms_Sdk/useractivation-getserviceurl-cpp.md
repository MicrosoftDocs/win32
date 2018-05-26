---
Description: The following example shows how to use the DRMGetServiceLocation function to retrieve the URL of the Active Directory Rights Management Services (AD RMS) activation service in the enterprise or on the Internet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: ff75fc2d-10c9-4dab-a0b9-0dd68f37c622
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: UserActivation\_GetServiceURL.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserActivation\_GetServiceURL.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows how to use the [**DRMGetServiceLocation**](/windows/previous-versions/Msdrm/nf-msdrm-drmgetservicelocation?branch=master) function to retrieve the URL of the Active Directory Rights Management Services (AD RMS) activation service in the enterprise or on the Internet. The URL has the form http(s)://*ServerName*/\_wmcs/certification where *ServerName* identifies the AD RMS server.


```C++
#include "UserActivation.h"

/*===================================================================
File:      UserActivation_GetServiceURL.cpp

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

[Activating a User](activating-a-user.md)
</dt> <dt>

[UserActivation.h](useractivation-h.md)
</dt> <dt>

[UserActivation\_GetServiceURL.cpp](useractivation-getserviceurl-cpp.md)
</dt> <dt>

[UserActivation\_Main.cpp](useractivation-main-cpp.md)
</dt> </dl>

 

 



