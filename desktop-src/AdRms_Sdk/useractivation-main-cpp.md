---
Description: The following example shows the main function of a console application that attempts to activate a user account by signing it into an Active Directory Rights Management Services (AD RMS) hierarchy and acquiring a rights account certificate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 5229f939-5ee3-4fe8-bc6a-63e21655a472
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: UserActivation\_Main.cpp
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserActivation\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following example shows the main function of a console application that attempts to activate a user account by signing it into an Active Directory Rights Management Services (AD RMS) hierarchy and acquiring a [*rights account certificate*](r-gly.md#-rm-rights-account-certificate-gly). The function performs the following actions:

-   Creates a client session.
-   Determines whether the user account has already been activated and returns if it has.
-   Uses service discovery to find the certification service URL. The URL has the form http(s)://*ServerName*/\_wmcs/certification where *ServerName* identifies the AD RMS server in the enterprise.
-   Calls [**DRMActivate**](/windows/previous-versions/Msdrm/nf-msdrm-drmactivate?branch=master) to activate the user account. This is an asynchronous function that returns immediately and periodically sends status information to your callback function.

If activation is successful, the rights account certificate is automatically saved in the appropriate [Rights Account Certificate Store](rights-account-certificate-store.md).


```C++
#include "UserActivation.h"

/*===================================================================
File:      UserActivation_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample shows how to activate an Active Directory user 
// account. It uses service discovery to find an available 
// activation server in the enterprise. The command line must
// contain a user name such as someone@example.com.
//
int _tmain(int argc, _TCHAR* argv[])
{

  HRESULT           hr                = S_OK;  // Return value
  DRM_ACTSERV_INFO *pdasi             = NULL;  // Server information
  DRMHSESSION       hClient           = NULL;  // Client handle
  PWSTR             pwszActivationURL = NULL;  // Server URL
  PWSTR             pwszUser          = NULL;  // User account
  DWORD             DW_WAIT_TIME      = 60000; // Time to wait
  DWORD             dwWaitResult      = 0;     // Asynch time
  DRM_CONTEXT       context;                   // Callback context

  // Validate the input.
  if (2 < argc) return E_INVALIDARG;
  pwszUser = argv[1];

  // Create a client session.
  hr = DRMCreateClientSession( 
         &amp;StatusCallback,                     // Callback function
         0,                                   // Reserved 
         DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH,  // Authentication type 
         pwszUser,                            // User ID 
         &amp;hClient );                          // Client handle
  if (FAILED(hr)) return hr;

  // Determine whether the user account has already been activated.
  // If it has, activating it again will add another rights account
  // certificate to the certificate store.
  hr = DRMIsActivated(
          hClient,                          // Client session handle
          DRM_ACTIVATE_GROUPIDENTITY,       // User activation query
          NULL);                            // Reserved.
  if (SUCCEEDED(hr)) goto e_Exit;

  // Use service discovery to find the URL of an activation server in
  // the enterprise.
  hr = GetServiceURL(
          hClient,                          // Client session handle
          DRM_SERVICE_TYPE_ACTIVATION,      // Service type
          DRM_SERVICE_LOCATION_ENTERPRISE,  // Service location
          &amp;pwszActivationURL);              // Service URL
  if (FAILED(hr)) goto e_Exit;

  // Create a DRM_ACTSERV_INFO server information object and assign
  // the URL to the wszURL member.
  pdasi = new DRM_ACTSERV_INFO;
  if (NULL == pdasi)
  {
    hr = E_OUTOFMEMORY;
    goto e_Exit;
  }
  pdasi->wszURL = pwszActivationURL;

  // Create an event for the callback function to signal when
  // the computer has been activated.
  SecureZeroMemory(&amp;context, sizeof(context));
  context.hEvent = CreateEvent(
         NULL,                        // No attributes
         FALSE,                       // Automatic reset
         FALSE,                       // Initial state not signaled
         NULL);                       // Event object not named
  if (NULL == context.hEvent) goto e_Exit;

  // Activate the user account.
  hr = DRMActivate( 
         hClient,                     // Client session handle
         DRM_ACTIVATE_GROUPIDENTITY | // Activate the user
     DRM_ACTIVATE_SILENT,
         0,                           // Default LCID
         pdasi,                       // Server information
         (VOID*)&amp;context,             // Callback context
         NULL);                       // Use the active window
  if (FAILED(hr)) goto e_Exit;

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject( 
         context.hEvent,              // Event handle
         DW_WAIT_TIME);               // Timeout interval
  if (WAIT_TIMEOUT==dwWaitResult || FAILED(context.hr))
  {
    wprintf(L"User activation error.\r\n");
    wprintf(L"Enter any key to continue...");
    _getch();
  }

e_Exit:
  if (NULL != pdasi)
  {
    if (NULL != pdasi->wszURL)
    {
      delete [] pdasi->wszURL;
    }
 pwszActivationURL = NULL;
    delete pdasi;
  }
  if (NULL != context.hEvent)
  {
    CloseHandle(context.hEvent);
  }  
  if (NULL != hClient)
  {
    DRMCloseSession(hClient);
    hClient = NULL;
  }


  return hr;
}
```



## Related topics

<dl> <dt>

[Activating a User](activating-a-user.md)
</dt> <dt>

[UserActivation\_GetServiceURL.cpp](useractivation-getserviceurl-cpp.md)
</dt> <dt>

[UserActivation.h](useractivation-h.md)
</dt> <dt>

[UserActivation\_Callback.cpp](useractivation-callback-cpp.md)
</dt> </dl>

 

 



