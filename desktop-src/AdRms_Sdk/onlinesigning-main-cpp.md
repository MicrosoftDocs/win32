---
Description: 'The following code example shows the \_tmain function of a console application that creates an issuance license and signs it online by using the certification service of an Active Directory Rights Management Services (AD RMS) server located on the enterprise intranet. The function performs the following actions:'
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3a97917c-9fc7-49cf-be03-bb4c3e5ea7fa
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: OnlineSigning\_Main.cpp
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnlineSigning\_Main.cpp

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following code example shows the \_tmain function of a console application that creates an issuance license and signs it online by using the certification service of an Active Directory Rights Management Services (AD RMS) server located on the enterprise intranet. The function performs the following actions:

-   Creates a client session.
-   Creates an unsigned issuance license for the user specified on the command line.
-   Retrieves the AD RMS certification service URL.
-   Signs the issuance license by using the certification service.


```C++
#include "OnlineILSigning.h"

/*===================================================================
File:      OnlineSigning_Main.cpp

THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF
ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
PARTICULAR PURPOSE.

Copyright (C) Microsoft.  All rights reserved.
===================================================================*/

/////////////////////////////////////////////////////////////////////
// This sample demonstrates how to sign an issuance license online. 
// It acquires the appropriate licenses and certificates,  
// initializes the environment, and signs the publishing license 
// online. 
//
int _tmain(int argc, _TCHAR* argv[])
{
  ///////////////////////////////////////////////////////////////////
  // Declare variables:
  //
  //    hr....................HRESULT return code
  //    hClient...............Client session handle
  //    hIssuanceLicense......Issuance license handle
  //    pwszUserID............User account ID string
  //    pwszLicensingSvr......Licensing server string
  //    DW_WAIT_TIME..........Maximum event signal wait time
  //    dwWaitResult..........Actual event signal wait time
  //    context...............Drm_Context structure instance
  //    
  HRESULT         hr                = S_OK;
  DRMHSESSION     hClient           = NULL;
  DRMPUBHANDLE    hIssuanceLicense  = NULL;
  PWSTR           pwszUserID        = NULL;
  PWSTR           pwszLicensingSvr  = NULL;
  const DWORD     DW_WAIT_TIME      = 60000;
  DWORD           dwWaitResult      = 0;
  DRM_CONTEXT     context;

  // Validate input. Client must supply a user ID.
  if(argc!=2 || NULL== argv[1]) return E_INVALIDARG;
  pwszUserID = argv[1];

  hr = DRMCreateClientSession( 
          &amp;StatusCallback,                    // Callback function
          0,                                  // Reserved
          DRM_DEFAULTGROUPIDTYPE_WINDOWSAUTH, // Authentication type
          pwszUserID,                         // User ID
          &amp;hClient );                         // Client handle
  if (FAILED(hr)) return hr;
  wprintf(L"\r\nDRMCreateClientSession succeeded.\r\n\n");

  // Create an unsigned issuance license for the user specified
  // on the command line. Add the EDIT right to the license.
  hr = GetUnsignedIL(
          pwszUserID,                         // User ID
          &amp;hIssuanceLicense);                 // License handle
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetUnsignedIL succeeded.\r\n\n");

  // Find a service URL.
  hr = GetServiceURL(
          hClient,                            // Client handle
          DRM_SERVICE_TYPE_PUBLISHING,        // Type of service
          DRM_SERVICE_LOCATION_ENTERPRISE,    // Location of service
          &amp;pwszLicensingSvr);                 // Service URL
  if (FAILED(hr)) goto e_Exit;
  wprintf(L"GetServiceURL succeeded.\r\n");
  wprintf(L"pwszLicensingSvr = %s\r\n\n", pwszLicensingSvr);

  // Initialize the callback context.
  SecureZeroMemory(&amp;context, sizeof(context));

  // Create an event for the callback function to signal when
  // the issuance license has been signed.
  context.hEvent = CreateEvent(
          NULL,                               // No attributes
          FALSE,                              // Automatic reset
          FALSE,                              // Not signaled
          NULL);                              // No name
  if(NULL == context.hEvent) goto e_Exit;

  // Sign the issuance license online.
  hr = DRMGetSignedIssuanceLicense( 
          NULL,                               // Environment handle
          hIssuanceLicense,                   // License handle
          DRM_SIGN_ONLINE |                   // Sign online
            DRM_AUTO_GENERATE_KEY,            // Create content key
          NULL,                               // No key specified
          0,                                  // Key size
          L"AES",                             // Key algorithm
          NULL,                               // CLC string
          &amp;StatusCallback,                    // Callback function
          pwszLicensingSvr,                   // Licensing server URL
          (void*)&amp;context);                   // Callback context
  if (FAILED(hr)) goto e_Exit;

  // Wait for the callback to return.
  dwWaitResult = WaitForSingleObject(context.hEvent, DW_WAIT_TIME);
  if(WAIT_TIMEOUT == dwWaitResult || FAILED(context.hr)) goto e_Exit;

  // Print the issuance license to the console. The license is not
  // saved in a store on the local computer. Instead, you typically
  // package the license with the protected content. It is up
  // to the application that consumes the content to know where
  // the license is, retrieve it, and use it to create and bind
  // to an end-user license that can be used to decrypt the
  // protected content.

  wprintf(L"\r\nThe issuance license is:\n\n%s\n", context.pwszData);
  wprintf(L"\r\nEnter any key to continue...\r\n");
  _getch();

e_Exit:

  if(NULL != pwszLicensingSvr)
  {
    delete [] pwszLicensingSvr;
    pwszLicensingSvr = NULL;
  }
  if(NULL != context.pwszData)
  {
    delete [] context.pwszData;
  }
  if(NULL != context.hEvent)
  {
    CloseHandle(context.hEvent);
    SecureZeroMemory(&amp;context, sizeof(context));
  }
  if(NULL != hClient)
  {
    DRMCloseSession(hClient);
    hClient = NULL;
  }

  return hr;
}

```



## Related topics

<dl> <dt>

[Creating and Using Issuance Licenses](creating-and-using-issuance-licenses.md)
</dt> <dt>

[Online Signing Code Example](online-signing-code-example.md)
</dt> </dl>

 

 



